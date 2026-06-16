#!/usr/bin/env python3
"""Validate an OpenReflect Insight Agents capability manifest."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REQUIRED = {
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


def fail(message: str) -> int:
    print(f"MANIFEST_INVALID: {message}", file=sys.stderr)
    return 1


def main() -> int:
    if len(sys.argv) != 2:
        return fail("usage: validate_capability_manifest.py path/to/manifest.json")

    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - command-line validator should report parse errors plainly.
        return fail(f"could not read JSON: {exc}")

    for field, expected_type in REQUIRED.items():
        if field not in data:
            return fail(f"missing required field: {field}")
        if not isinstance(data[field], expected_type):
            return fail(f"field {field} must be {expected_type.__name__}")

    if data["status"] not in VALID_STATUS:
        return fail(f"status must be one of: {', '.join(sorted(VALID_STATUS))}")

    for list_field in ("inputs", "outputs", "evals"):
        if not data[list_field]:
            return fail(f"{list_field} must not be empty")
        if not all(isinstance(item, str) and item.strip() for item in data[list_field]):
            return fail(f"{list_field} must contain non-empty strings")

    if "must_not_infer" in data:
        if not isinstance(data["must_not_infer"], list):
            return fail("must_not_infer must be a list when provided")
        if not all(isinstance(item, str) and item.strip() for item in data["must_not_infer"]):
            return fail("must_not_infer must contain non-empty strings")

    print("CAPABILITY_MANIFEST_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
