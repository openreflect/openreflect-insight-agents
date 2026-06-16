# Signal Records

Signal records are provenance-backed observations emitted by capability agents. They sit between source adapters and higher-level insight records: a signal captures a bounded observation, while an insight may synthesize multiple signals into a broader claim.

The shared schema lives at `schemas/signal-record.schema.json`. Capability agents can keep local schemas for their own records, but those schemas should map onto the shared fields when the records need to be exchanged across agents.

## Base Schema

The base schema defines fields every portable signal should expose:

- `id`: stable signal identifier.
- `created_at` or `observed_at`: when the record was created or when the signal was observed.
- `source_refs` or `evidence_refs`: provenance pointers to source material, artifacts, telemetry, or derived evidence.
- `signal_type`: broad class of signal, such as `human_telemetry`, `artifact_quality`, or `workflow_risk`.
- `signal_labels`: normalized labels for filtering and aggregation.
- `confidence`: numeric confidence from `0` to `1`.
- `recency_scope`: coarse freshness bucket.
- `interpretation`: short explanation of what the signal means.
- `recommended_use`: how downstream systems may use the signal.
- `privacy`: privacy tier for routing and display.

Optional shared fields include `referenced_at`, `evidence_excerpt`, `uncertainty`, `do_not_use_for`, and `extensions`.

The shared schema is intentionally not a production memory backend. It is a public-safe interchange contract for synthetic fixtures, prompts, validation, and capability-agent outputs.

## Capability Extensions

Capability-specific fields belong under `extensions` unless they are broadly reusable enough to promote into the base schema.

For example, a human-telemetry capability may keep fields such as sentiment, state labels, check-in guidance, or subject references in its local schema. An artifact-review capability might instead extend records with artifact kind, parser version, review dimensions, or quality gates.

Extension schemas should:

- keep provenance in the shared `source_refs` or `evidence_refs` fields;
- keep privacy routing in the shared `privacy` field;
- avoid real transcripts, local paths, credentials, chat identifiers, and operational logs in committed examples;
- document any additional required extension fields in the capability directory;
- preserve compatibility with the shared schema when records are intended for cross-agent exchange.

## Relationship To Insight Records

Signal records are evidence-bearing intermediate outputs. Insight records are synthesized claims built from one or more signals or source records. A downstream insight should cite the relevant signal IDs or evidence references instead of depending on private source expansion.

This separation lets capability agents evolve independently while keeping a common public contract for provenance, confidence, recency, recommended use, and privacy.
