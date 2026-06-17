# Extract Decision Traces

## Purpose

Reconstruct decision provenance from source records, transcripts, notes, issue comments, or prior insight records.

## Allowed Inputs

- source records
- transcript excerpts with references
- project notes
- commit summaries
- issue or planning excerpts
- prior insight records

## Output Shape

Emit JSONL records compatible with `schemas/insight-record.schema.json`.

Use the `claim` field for the decision trace summary. Include structured details inside the claim when needed:

- decision
- inputs
- constraints
- alternatives
- tradeoffs
- rationale
- unresolved assumptions
- revisit triggers

## Rules

- Reconstruct only what the evidence supports.
- Do not invent rationale because the final decision looks obvious.
- Distinguish contemporary decision evidence from later explanation.
- Cite evidence for the decision and, where possible, for constraints and alternatives.
- Mark missing alternatives or rationale as unknown.
- Include a revisit trigger when the decision depends on a mutable assumption.

## Failure Output

If no decision can be traced, return:

```json
{"status":"no_decision_trace","reason":"no explicit or reconstructable decision found"}
```

