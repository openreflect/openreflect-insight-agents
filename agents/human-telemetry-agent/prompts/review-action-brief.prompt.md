# Review Human Telemetry Signals

## Purpose

Turn recent human telemetry signal records into a short assistant action brief.

## Input

- JSONL signal records
- Current task or work block
- Optional known user preference profile

## Output

Return a concise brief:

```text
Current state read:
Evidence:
Present vs historical:
Recommended response mode:
Check-in:
Stop condition:
```

## Rules

- Do not overstate confidence.
- Separate current state from historical pattern.
- Prefer action guidance over abstract description.
- If evidence is thin, say so.
- If the next action depends on state, include one short check-in question.
