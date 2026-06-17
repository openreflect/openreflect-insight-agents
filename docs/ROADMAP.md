# Roadmap

OpenReflect Insight Agents is an early public framework for provenance-backed
insight agents. This roadmap describes the work needed to make the contracts,
examples, fixtures, and validation paths concrete while preserving the
public/private boundary.

The milestones below are directional. They are not release commitments, product
promises, or production-readiness claims.

## Near Term

Goal: make the public framework easier to inspect, validate, and extend with
synthetic data.

- Harden the source adapter interface:
  - clarify required input and output fields for bounded source windows
  - define warning codes for partial windows, missing timestamps, and privacy
    restrictions
  - add adapter examples that avoid private storage paths, account IDs, and real
    transcript identifiers
- Expand schema coverage:
  - align source packets, signal records, insight records, action briefs, and
    feedback records around shared provenance fields
  - add examples for valid and invalid records where useful
  - keep schema language public-safe and implementation-neutral
- Grow fixture coverage:
  - add more synthetic transcript and source-packet fixtures
  - cover stale-memory, recency-drift, weak-evidence, and user-correction cases
  - label synthetic data clearly so it cannot be confused with observed private
    source material
- Extend validation scripts:
  - validate capability manifests against `schemas/capability-manifest.schema.json`
  - add checks for required provenance, confidence, privacy, and evidence fields
  - keep validation runnable with local files and no private service dependency
- Document downstream integration boundaries:
  - state what belongs in this public repo versus private downstream forks
  - define where private calibration, credentials, logs, and real profiles must
    remain downstream

## Mid Term

Goal: turn the scaffold into a repeatable evaluation and capability-development
workflow.

- Grow the eval runner:
  - run capability prompts against synthetic fixtures
  - compare outputs against expected restraint, evidence use, and abstention
    behavior
  - report failures in a format suitable for local development and CI
- Formalize the capability manifest registry:
  - define registry metadata for capability status, input types, output types,
    privacy handling, and first eval coverage
  - add registry checks so listed capabilities have manifests, schemas, prompts,
    and fixtures where applicable
  - keep the registry descriptive rather than an execution authority
- Add capability-agent examples beyond human telemetry:
  - pattern analysis
  - decision tracing
  - ambiguity checking
  - reflection synthesis
  - project pattern detection
  - skill and workflow recommendation
  - evidence quality review
  - recency and drift review
- Improve action-brief contracts:
  - define how insights become assistant-facing guidance
  - require uncertainty and recommended-use fields for behavior-shaping output
  - preserve evidence references from source packets through final briefs
- Establish public-safe CI:
  - schema validation
  - manifest validation
  - fixture shape checks
  - prompt and documentation path checks

## Later

Goal: support real downstream use without turning the public repo into a private
memory system or production platform.

- Define private adapter extension points:
  - keep source-specific credentials, local paths, account identifiers, and real
    storage details out of the public contract
  - provide enough adapter shape for downstream implementations to plug in
    safely
- Add integration boundary guides:
  - OpenReflect action surfaces
  - assistant context briefs
  - project planning agents
  - skill, MCP, or workflow routers
  - dashboard or review surfaces
- Expand feedback-loop support:
  - capture when action briefs helped, missed, overreached, or became stale
  - use feedback records to improve eval fixtures and capability guidance
  - avoid self-reinforcing adaptations without evidence
- Improve provenance verification patterns:
  - define how downstream systems recover source evidence under the same
    authorization boundary
  - distinguish recoverable source references from public-safe fixture
    references
  - keep quantitative and critical claims tied to source contact
- Prepare for versioned contracts:
  - version schemas and manifest fields deliberately
  - document compatibility expectations before downstream users depend on them
  - prefer small, inspectable changes over broad platform claims

## Non-Goals For Now

- Production deployment tooling.
- A hosted memory service.
- Real user profiles, transcripts, credentials, or operational logs.
- Medical, psychological, or diagnostic interpretation.
- Fully autonomous agent routing without evidence, privacy, and abstention
  checks.
