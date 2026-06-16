#!/usr/bin/env python3
"""Run deterministic repository evals without LLM or third-party dependencies."""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]

CAPABILITY_REQUIRED = {
    "id": str,
    "name": str,
    "status": str,
    "purpose": str,
    "inputs": list,
    "outputs": list,
    "privacy_boundary": str,
    "evals": list,
}
VALID_STATUS = {"planned", "scaffolded", "active", "deprecated"}

SCHEMA_EXAMPLE_PAIRS = (
    (
        ROOT / "schemas" / "feedback-record.schema.json",
        ROOT / "examples" / "feedback-record.example.json",
    ),
    (
        ROOT / "schemas" / "source-record.schema.json",
        ROOT / "examples" / "source-record.example.json",
    ),
    (
        ROOT / "agents" / "human-telemetry-agent" / "schema" / "signal-record.schema.json",
        ROOT / "agents" / "human-telemetry-agent" / "examples" / "signals.example.jsonl",
    ),
)


@dataclass(frozen=True)
class EvalResult:
    name: str
    passed: bool
    detail: str


class ValidationError(ValueError):
    """Raised when an instance does not satisfy the supported schema subset."""


def repo_path(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - eval output should preserve parse errors.
        raise ValidationError(f"{repo_path(path)}: could not read JSON: {exc}") from exc


def json_type_name(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, int):
        return "integer"
    if isinstance(value, float):
        return "number"
    if isinstance(value, str):
        return "string"
    if isinstance(value, list):
        return "array"
    if isinstance(value, dict):
        return "object"
    return type(value).__name__


def matches_type(value: Any, expected_type: str) -> bool:
    if expected_type == "null":
        return value is None
    if expected_type == "boolean":
        return isinstance(value, bool)
    if expected_type == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected_type == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected_type == "string":
        return isinstance(value, str)
    if expected_type == "array":
        return isinstance(value, list)
    if expected_type == "object":
        return isinstance(value, dict)
    raise ValidationError(f"unsupported schema type: {expected_type}")


def validate_type(instance: Any, expected: Any, pointer: str) -> None:
    expected_types = expected if isinstance(expected, list) else [expected]
    if not any(matches_type(instance, expected_type) for expected_type in expected_types):
        allowed = " or ".join(expected_types)
        raise ValidationError(f"{pointer}: expected {allowed}, got {json_type_name(instance)}")


def validate_date_time(value: Any, pointer: str) -> None:
    if value is None:
        return
    if not isinstance(value, str):
        raise ValidationError(f"{pointer}: date-time value must be a string")
    normalized = value.replace("Z", "+00:00")
    try:
        datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise ValidationError(f"{pointer}: invalid date-time") from exc


def validate_schema(instance: Any, schema: dict[str, Any], pointer: str = "$") -> None:
    if "allOf" in schema:
        for subschema in schema["allOf"]:
            validate_schema(instance, subschema, pointer)

    if "anyOf" in schema:
        errors = collect_branch_errors(instance, schema["anyOf"], pointer)
        if len(errors) == len(schema["anyOf"]):
            raise ValidationError(f"{pointer}: did not match anyOf ({'; '.join(errors)})")

    if "oneOf" in schema:
        errors = collect_branch_errors(instance, schema["oneOf"], pointer)
        matches = len(schema["oneOf"]) - len(errors)
        if matches != 1:
            raise ValidationError(f"{pointer}: expected exactly one oneOf match, got {matches}")

    if "type" in schema:
        validate_type(instance, schema["type"], pointer)

    if "enum" in schema and instance not in schema["enum"]:
        allowed = ", ".join(repr(item) for item in schema["enum"])
        raise ValidationError(f"{pointer}: expected one of {allowed}")

    if schema.get("format") == "date-time":
        validate_date_time(instance, pointer)

    if isinstance(instance, (int, float)) and not isinstance(instance, bool):
        if "minimum" in schema and instance < schema["minimum"]:
            raise ValidationError(f"{pointer}: value is below minimum {schema['minimum']}")
        if "maximum" in schema and instance > schema["maximum"]:
            raise ValidationError(f"{pointer}: value is above maximum {schema['maximum']}")

    if isinstance(instance, list):
        validate_array(instance, schema, pointer)

    if isinstance(instance, dict):
        validate_object(instance, schema, pointer)


def collect_branch_errors(instance: Any, schemas: list[dict[str, Any]], pointer: str) -> list[str]:
    errors = []
    for subschema in schemas:
        try:
            validate_schema(instance, subschema, pointer)
        except ValidationError as exc:
            errors.append(str(exc))
    return errors


def validate_array(instance: list[Any], schema: dict[str, Any], pointer: str) -> None:
    if "minItems" in schema and len(instance) < schema["minItems"]:
        raise ValidationError(f"{pointer}: expected at least {schema['minItems']} item(s)")

    if schema.get("uniqueItems"):
        seen = set()
        for item in instance:
            key = json.dumps(item, sort_keys=True, separators=(",", ":"))
            if key in seen:
                raise ValidationError(f"{pointer}: duplicate array item")
            seen.add(key)

    if "items" in schema:
        for index, item in enumerate(instance):
            validate_schema(item, schema["items"], f"{pointer}/{index}")


def validate_object(instance: dict[str, Any], schema: dict[str, Any], pointer: str) -> None:
    for field in schema.get("required", []):
        if field not in instance:
            raise ValidationError(f"{pointer}: missing required field {field}")

    properties = schema.get("properties", {})
    for field, subschema in properties.items():
        if field in instance:
            validate_schema(instance[field], subschema, f"{pointer}/{field}")

    additional = schema.get("additionalProperties", True)
    extra_fields = sorted(set(instance) - set(properties))
    if additional is False and extra_fields:
        raise ValidationError(f"{pointer}: unexpected field(s): {', '.join(extra_fields)}")
    if isinstance(additional, dict):
        for field in extra_fields:
            validate_schema(instance[field], additional, f"{pointer}/{field}")


def validate_capability_manifest(path: Path) -> None:
    data = load_json(path)
    if not isinstance(data, dict):
        raise ValidationError(f"{repo_path(path)}: manifest root must be an object")

    for field, expected_type in CAPABILITY_REQUIRED.items():
        if field not in data:
            raise ValidationError(f"{repo_path(path)}: missing required field: {field}")
        if not isinstance(data[field], expected_type):
            raise ValidationError(f"{repo_path(path)}: field {field} must be {expected_type.__name__}")

    if data["status"] not in VALID_STATUS:
        allowed = ", ".join(sorted(VALID_STATUS))
        raise ValidationError(f"{repo_path(path)}: status must be one of: {allowed}")

    for list_field in ("inputs", "outputs", "evals"):
        if not data[list_field]:
            raise ValidationError(f"{repo_path(path)}: {list_field} must not be empty")
        if not all(isinstance(item, str) and item.strip() for item in data[list_field]):
            raise ValidationError(f"{repo_path(path)}: {list_field} must contain non-empty strings")

    if "must_not_infer" in data:
        if not isinstance(data["must_not_infer"], list):
            raise ValidationError(f"{repo_path(path)}: must_not_infer must be a list when provided")
        if not all(isinstance(item, str) and item.strip() for item in data["must_not_infer"]):
            raise ValidationError(f"{repo_path(path)}: must_not_infer must contain non-empty strings")


def run_capability_manifest_evals() -> list[EvalResult]:
    results = []
    paths = sorted((ROOT / "examples").glob("*.capability.json"))
    for path in paths:
        name = f"capability manifest: {repo_path(path)}"
        try:
            validate_capability_manifest(path)
        except ValidationError as exc:
            results.append(EvalResult(name, False, str(exc)))
        else:
            results.append(EvalResult(name, True, "OK"))
    return results


def load_examples(path: Path) -> list[Any]:
    if path.suffix == ".jsonl":
        examples = []
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if not line.strip():
                continue
            try:
                examples.append(json.loads(line))
            except Exception as exc:  # noqa: BLE001 - eval output should preserve parse errors.
                raise ValidationError(f"{repo_path(path)}:{line_number}: could not read JSON: {exc}") from exc
        if not examples:
            raise ValidationError(f"{repo_path(path)}: JSONL example file is empty")
        return examples
    return [load_json(path)]


def run_schema_example_evals() -> list[EvalResult]:
    results = []
    for schema_path, example_path in SCHEMA_EXAMPLE_PAIRS:
        name = f"schema example: {repo_path(example_path)} -> {repo_path(schema_path)}"
        try:
            schema = load_json(schema_path)
            for index, example in enumerate(load_examples(example_path), start=1):
                pointer = "$" if example_path.suffix != ".jsonl" else f"${index}"
                validate_schema(example, schema, pointer)
        except ValidationError as exc:
            results.append(EvalResult(name, False, str(exc)))
        else:
            results.append(EvalResult(name, True, "OK"))
    return results


def main() -> int:
    results = run_capability_manifest_evals() + run_schema_example_evals()
    failures = [result for result in results if not result.passed]

    for result in results:
        status = "OK" if result.passed else "FAIL"
        print(f"{status}  {result.name}")
        if not result.passed:
            print(f"      {result.detail}")

    print()
    if failures:
        print(f"EVALS_FAILED: {len(failures)} failed, {len(results) - len(failures)} passed")
        return 1

    print(f"EVALS_OK: {len(results)} passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
