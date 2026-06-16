# Architecture

## Layers

OpenReflect Insight Agents is organized around five layers.

```text
sources -> adapters -> capability agents -> insight records -> action surfaces
```

## Sources

Sources are provenance-bearing inputs:

- conversation transcripts
- memory summaries
- semantic memory hits
- project notes
- voice transcripts
- runtime logs
- telemetry records
- human-authored notes

Sources are not interpreted directly by downstream assistants. They are converted into records with evidence, confidence, and privacy policy.

## Adapters

Adapters normalize source access while preserving source pointers. A public adapter interface should avoid hard-coding any private memory system.

Adapter responsibilities:

- read a bounded source window
- preserve source reference
- avoid secret expansion
- expose observed time and referenced time when known
- emit public-safe synthetic data for tests

## Capability Agents

Capability agents perform bounded interpretation. Each agent should define:

- input record types
- output record types
- prompt contract
- deterministic validation where possible
- uncertainty rules
- privacy tier handling
- synthetic eval fixtures

Human Telemetry Agent is the first capability agent.

## Insight Records

Insight records are synthesized outputs that may combine multiple signals. They should include:

- claim
- evidence references
- confidence
- recency
- scope
- uncertainty
- recommended use
- privacy tier

## Action Surfaces

Action surfaces consume insight:

- assistant context briefs
- OpenReflect records
- dashboards
- project planning agents
- skill/MCP routers
- follow-up check-ins

The first action surface should be a concise assistant action brief.

## Privacy Boundary

Public repo:

- schemas
- synthetic fixtures
- generic prompts
- adapter contracts
- validation scripts

Private downstream:

- real transcripts
- local memory paths
- user profiles
- private calibration notes
- credentials
- operational logs

## Design Constraint

The framework should not centralize all memory into one database before proving the insight loops. Start with Markdown, JSONL, schemas, prompts, and fixture evals.
