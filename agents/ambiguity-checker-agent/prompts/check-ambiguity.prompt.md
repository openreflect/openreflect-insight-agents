# Check Ambiguity

## Purpose

Identify materially ambiguous language in requests, plans, notes, source records, or insight records before an assistant acts.

## Allowed Inputs

- user requests
- project notes
- plans
- source records
- signal records
- insight records
- action briefs

## Output Shape

Emit JSONL records compatible with `schemas/insight-record.schema.json`.

Use the `claim` field to summarize the ambiguity finding. Include:

- ambiguous term or reference
- possible interpretations
- why it matters
- recommended assumption, clarifying question, or abstention

## Rules

- Flag only ambiguity that could change action, interpretation, privacy, cost, safety, or verification needs.
- Do not ask clarifying questions for ambiguity that can be handled with a low-risk explicit assumption.
- If the next action is external, destructive, costly, or privacy-sensitive, require confirmation or source verification.
- If a date is relative, resolve it only when the current date is available; otherwise ask or mark unknown.
- Preserve the original source reference.

## Failure Output

If no material ambiguity is found, return:

```json
{"status":"no_material_ambiguity","reason":"no action-changing ambiguity found"}
```

