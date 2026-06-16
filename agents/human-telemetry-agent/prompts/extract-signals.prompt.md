# Extract Human Telemetry Signals

## Purpose

Extract normalized human telemetry signal records from a transcript, memory excerpt, or project log.

## Input

- Source system name
- Source type
- Source reference
- Observed timestamp
- Optional project/workstream hint
- Text excerpt

## Output

Return JSONL. Each line must conform to `schema/signal-record.schema.json`.

## Rules

- Treat language-derived state as signal, not proof.
- Do not diagnose medical or psychiatric conditions.
- Separate present signals from historical references.
- Include `project_ref` only when evidence supports it.
- Use `needs_checkin: true` when the assistant should verify before adapting materially.
- Keep evidence excerpts short and sanitized.
- If uncertain, lower confidence and explain uncertainty in `interpretation`.

## Label Guidance

Use base sentiment:

- positive
- neutral
- negative
- mixed
- unknown

Use state labels such as:

- clear
- focused
- overloaded
- fatigued
- pain-affected
- hesitant
- frustrated
- vulnerable
- compressed
- scattered
- repetitive
- urgent
- over-verbal
- under-specified
- context-jumping

## Prompt

Given the input excerpt, emit one or more signal records. Prefer fewer, stronger records over many weak ones.
