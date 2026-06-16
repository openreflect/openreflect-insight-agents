# Maturity and Status

Status: scaffold / framework draft
Public posture: generic contracts and synthetic examples only

OpenReflect Insight Agents is an early public framework for provenance-backed insight agents. It defines the shape of the system: schemas, capability manifests, public-safe examples, prompt contracts, and evaluation scaffolding for agents that turn evidence-bearing sources into restrained insight records and action briefs.

This repository should not be read as a production implementation. It does not currently provide a live backend, deployed service, persistent OpenReflect feed, private adapter bridge, or operational calibration layer.

## What Is Defined

The repository currently defines:

- Top-level product and architecture direction in `README.md`, `docs/PRD.md`, and `docs/ARCHITECTURE.md`.
- Public schema contracts for source records, signal records, insight records, action briefs, feedback records, and capability manifests.
- A capability registry describing active and planned insight-agent roles.
- Public-safe capability examples under `examples/`.
- A scaffolded Human Telemetry Agent under `agents/human-telemetry-agent/`.
- Synthetic fixtures and prompt files for early extraction, review, and validation workflows.
- A validation script for capability manifests.

These artifacts are intended to make the framework inspectable and discussable before runtime behavior is built out.

## What Is Draft

The following areas are draft-level and subject to change:

- Schema fields, enum values, and validation requirements.
- Capability-agent boundaries and registry entries.
- Prompt contracts and expected output formats.
- Evaluation criteria and fixture coverage.
- Source adapter responsibilities and privacy-tier handling.
- The exact format of action briefs consumed by downstream assistants.

Consumers should treat these contracts as design-stage interfaces, not stable APIs.

## What Is Not Implemented

This repository does not currently implement:

- A production backend or hosted OpenReflect service.
- Live ingestion from real memory systems, transcripts, logs, or telemetry stores.
- A persistent database, queue, scheduler, or action-brief delivery pipeline.
- Runtime agent orchestration.
- Private downstream calibration against real users, projects, or operational data.
- Security hardening for deployment.
- Production-grade monitoring, migrations, authentication, or authorization.

Any examples that look executable are framework examples unless explicitly documented otherwise.

## Appropriate Use

Appropriate current uses:

- Reviewing the public framework direction.
- Iterating on provenance, uncertainty, privacy, and action-brief contracts.
- Building synthetic fixtures and eval cases.
- Prototyping compatible capability agents against public schemas.
- Discussing what downstream private adapters should provide without publishing private data.

Inappropriate current uses:

- Claiming production readiness.
- Treating generated insight as verified operational truth without source review.
- Running this repository against private transcripts or real user data in public.
- Advertising live OpenReflect backend behavior from this scaffold.
- Depending on the current schemas as stable integration contracts.

## Public Safety Boundary

This repository is the public, generic upstream. It may contain:

- Generic contracts.
- Public-safe schemas.
- Synthetic examples.
- Synthetic fixtures.
- Prompt and validation scaffolding.
- High-level architecture and product documentation.

Private downstream repositories, branches, or deployments must contain:

- Real transcripts.
- Real operational logs.
- User profiles or calibration notes.
- Environment-specific source adapters.
- Credentials, tokens, keys, and secrets.
- Private evaluation data.
- Deployment configuration.

The public repo should preserve the pattern of the system without exposing the people, operations, or data that would calibrate it.

## Current Interpretation Rule

When in doubt, interpret this repository as a public design scaffold for a provenance-backed insight-agent framework. Do not infer production behavior, live backend availability, real-data readiness, or stable API guarantees from the presence of schemas, examples, prompts, or validation scripts.
