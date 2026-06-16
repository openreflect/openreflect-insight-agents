# Glossary

This glossary defines shared terminology for OpenReflect Insight Agents. The repository is a public-safe framework for provenance-backed insight agents over memory, transcripts, artifacts, and telemetry. It is not the production OpenReflect memory backend, and glossary terms should not imply production readiness.

## Core Terms

### Source

A provenance-bearing input that may contain useful evidence. Sources can include conversation transcripts, memory summaries, semantic memory hits, project notes, voice transcripts, runtime logs, telemetry records, human-authored notes, or artifacts.

Sources are raw inputs to the framework. Downstream assistants should not consume them directly as interpreted truth.

### Source Adapter

A bounded interface that reads a source and converts access to a stable public contract. A source adapter preserves source pointers, avoids secret expansion, exposes observed time and referenced time when known, and can emit public-safe synthetic data for tests.

Public adapters should stay generic. Private adapters that know about local systems, private storage paths, real user profiles, or operational logs belong downstream.

### Source Record

A normalized pointer to a source item or source window. A source record identifies where evidence came from without requiring the public repo to contain the underlying private data.

A source record should describe source type, source system, source reference, observed time, referenced time when known, and privacy handling. It is evidence metadata, not an interpretation.

### Signal Record

A small evidence-backed observation emitted by a capability agent. A signal record captures one bounded observation from one or more source records, such as sentiment, state labels, work-context signals, recommended assistant action, confidence, recency, and privacy tier.

Signal records should stay close to the evidence and avoid broad synthesis. They are inputs to insight records and action briefs.

### Insight Record

A synthesized claim across one or more signals or source records. An insight record includes a claim, evidence refs, confidence, recency scope, uncertainty, recommended use, optional limits on use, and privacy tier.

Insight records interpret evidence with restraint. They should separate present-state claims from historical patterns and should not turn user-state signals into clinical diagnosis.

### Action Brief

A concise downstream instruction for how an assistant should adapt behavior. An action brief includes scope, summary, recommended adjustments, check-ins, stop conditions, evidence refs, and privacy tier.

Action briefs are action surfaces, not evidence stores. They should be short enough to fit live assistant context and clear enough to prevent overconfident behavior.

### Feedback Record

A record of whether an action brief, insight, route, or assistant adjustment helped, missed, caused friction, or requires correction. Feedback records support improvement loops by linking downstream behavior back to the evidence and recommendation that produced it.

Feedback records should capture outcome and correction without rewriting the original evidence.

### Capability Manifest

A public contract describing what a capability agent, skill, or MCP can do. A capability manifest names the capability, status, purpose, inputs, outputs, privacy boundary, evals, and any claims it must not infer.

Manifests should make routing and validation possible without exposing private calibration data.

### Evidence Ref

A stable reference from a signal, insight, action brief, or feedback record back to the supporting source record, signal record, artifact, fixture, or synthetic example.

Evidence refs carry provenance. They should be specific enough to support verification, but public examples must use synthetic or generic references rather than private paths, real transcripts, credentials, chat IDs, or operational logs.

### Privacy Tier

The handling level for a record or artifact. Current schemas use:

- `public`: safe for the public repository.
- `synthetic`: generated or fabricated fixture data that is safe for public evals.
- `private`: real downstream data that must not be committed publicly.
- `restricted`: sensitive downstream data that requires tighter handling than ordinary private records.

Privacy tier travels with derived records. A downstream output should not be assigned a less restrictive tier than its evidence supports.

### Recency Scope

The time relationship between evidence and a claim. Insight records use `present`, `recent`, `near_history`, `medium_history`, `long_history`, `mixed`, and `unknown`. Signal records currently use the same buckets except `mixed`.

Recency scope prevents stale evidence from being treated as current truth. Use `mixed` when an insight combines multiple time windows, and `unknown` when the time basis cannot be established.

### Confidence

A numeric estimate from `0` to `1` for how strongly the evidence supports a signal or insight. Confidence is not a truth guarantee, and it is not a replacement for evidence refs or uncertainty text.

High confidence requires source-backed support. Weak, indirect, stale, or conflicting evidence should lower confidence and be described in uncertainty.

### Uncertainty

Plain-language limits on what the record can safely claim. Uncertainty should identify weak evidence, missing context, ambiguous timing, conflicting signals, stale source material, or assumptions that require human verification.

Use uncertainty to preserve restraint, not as decorative boilerplate.

### Public Downstream

A downstream use that remains safe for public artifacts, examples, docs, schemas, validation scripts, synthetic fixtures, and generic prompts. Public downstream work may demonstrate contracts and behavior, but it must not include real transcripts, private profiles, credentials, local paths, chat IDs, or operational logs.

### Private Downstream

A downstream implementation that connects the public framework to real memory systems, real transcripts, local adapters, private calibration notes, user profiles, credentials, operational logs, or deployment-specific routes.

Private downstream implementations may use the public contracts, but they should keep private data and environment-specific behavior outside this repository.

## Naming Rules

- Use `source` for raw provenance-bearing inputs and `source record` for normalized pointers to those inputs.
- Use `source adapter` for ingestion and normalization boundaries. Do not call an adapter a memory backend.
- Use `signal record` for small evidence-backed observations and `insight record` for synthesized claims across signals or sources.
- Use `action brief` only for concise assistant-facing adaptation guidance.
- Use `feedback record` for downstream outcome/correction data, not for the original claim.
- Use `evidence ref` for provenance pointers. Do not use `citation`, `source`, and `evidence` interchangeably when a schema field expects `evidence_refs`.
- Use `privacy tier` consistently with the schema values: `public`, `synthetic`, `private`, and `restricted`.
- Use `recency scope` for insight-level time framing and `recency bucket` only when referring to the current signal record schema field.
- Name capability agents by bounded job, such as `Evidence Quality Agent` or `Recency/Drift Agent`, not by broad ownership of memory or reflection.
- Avoid terms that imply this repository stores all memory, replaces the core OpenReflect memory backend, contains production adapters, or publishes private calibration data.
