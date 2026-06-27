# Evidence Quality Agent PRD

Status: Planned
Created: 2026-06-27
Public posture: generic framework first; private evidence bodies, raw transcripts, and internal audit logs stay downstream

## BLUF

Evidence Quality Agent scores the freshness, clarity, and support level of evidence attached to claims, insight records, and action briefs. It flags weak sourcing, missing provenance, stale references, inference jumps, and verification needs without deciding the underlying truth of unsupported claims.

## Problem

Polished summaries can hide weak evidence. An assistant may cite a vague memory, rely on stale context, collapse inference into fact, or make a quantitative claim without source contact. Downstream systems need a way to inspect evidence quality before using an insight to shape behavior or action.

Evidence review must also avoid becoming a false authority. The agent can judge whether a claim is supported by the provided sources; it should not decide the real-world truth of a claim when the required source is absent.

## Goals

- Score whether claims are source-backed, inferred, speculative, stale, or unsupported.
- Identify missing source references and vague provenance.
- Flag stale evidence where timestamps or newer references suggest drift.
- Recommend verification methods or source review when needed.
- Preserve claim-level distinctions instead of assigning only one document-level score.
- Support public-safe synthetic evidence bundles and fixtures.

## Non-Goals

- Determine truth without source evidence.
- Provide legal, medical, or compliance conclusions.
- Infer source intent.
- Replace primary-source verification for critical operational claims.
- Store private evidence bodies, transcripts, or audit logs in the public repo.

## Users

- Assistants deciding whether an insight is safe to use.
- Operators auditing reports, action briefs, and decision traces.
- Developers building provenance and verification workflows.
- Capability agents that need evidence-quality gates before synthesis or routing.

## Core Concept

Evidence Quality Agent is a claim auditor, not a truth oracle. It should make evidence strength visible so downstream agents know when to rely, verify, narrow, or abstain.

Evidence reviews should include:

- claim text or claim reference
- support level
- source clarity
- freshness
- inference risk
- verification recommendation

## Inputs And Outputs

Initial inputs:

- source references
- insight records
- artifact metadata
- claim lists
- action briefs
- timestamps and recency metadata

Initial outputs:

- evidence quality score
- weak evidence flags
- missing source findings
- stale source warnings
- verification recommendations

## First Milestone

Create a markdown and JSONL scaffold:

1. PRD and README.
2. Prompt for claim-level evidence review.
3. Synthetic mixed-source bundle with planted weak claims.
4. Example evidence quality records.
5. Capability manifest connected to the shared registry.

## Success Criteria

- Unsupported claims are flagged without being rewritten as true or false.
- Quantitative and critical claims require specific source references.
- Stale or ambiguous evidence receives verification guidance.
- Claim-level output is inspectable by downstream agents.
- Public examples contain only synthetic or public-safe source metadata.

