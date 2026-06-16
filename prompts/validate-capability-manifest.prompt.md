# Validate Capability Manifest Prompt

## Purpose

Validate that a capability manifest describes a bounded OpenReflect insight agent with clear inputs, outputs, privacy boundaries, and evals.

## Inputs

- Path to a JSON capability manifest.

## Preconditions

- Manifest is public-safe.
- Manifest uses synthetic or generic examples only.
- Real transcripts, profile data, local paths, credentials, and private logs are excluded.

## Validation

- Required fields are present.
- Status is one of `planned`, `scaffolded`, `active`, or `deprecated`.
- Inputs, outputs, and evals are non-empty.
- `must_not_infer` is explicit when the capability could overreach.

## Do Not

- Add private source paths.
- Add real user identifiers.
- Treat weak inferred state as fact.
- Expand the agent scope to cover unrelated capabilities.
