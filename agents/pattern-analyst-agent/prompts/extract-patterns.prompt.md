# Extract Recurring Patterns

## Purpose

Convert provenance-bearing source records, signal records, or prior insight records into bounded pattern insights.

## Allowed Inputs

- source records
- signal records
- insight records
- transcript excerpts with source references
- project notes with timestamps

## Output Shape

Emit JSONL records compatible with `schemas/insight-record.schema.json`.

Each record should include:

- `claim`: one concise pattern claim
- `evidence_refs`: source ids or references supporting the claim
- `confidence`: 0.0 to 1.0
- `recency_scope`: present, recent, near_history, medium_history, long_history, mixed, or unknown
- `uncertainty`: limits, counterevidence, or why the pattern may be weak
- `recommended_use`: how an assistant may use the pattern
- `do_not_use_for`: misuse boundary
- `privacy`: public, synthetic, private, or restricted

## Rules

- Prefer abstention over a polished but weak pattern claim.
- Do not infer current state from old evidence.
- Do not convert repeated behavior into diagnosis or identity.
- Include counterexamples when they materially weaken the pattern.
- If evidence has mixed recency, set `recency_scope` to `mixed`.
- If a pattern is based on one record, say it is a candidate, not a confirmed pattern.

## Failure Output

If no pattern is supported, return:

```json
{"status":"no_pattern","reason":"insufficient repeated evidence"}
```

