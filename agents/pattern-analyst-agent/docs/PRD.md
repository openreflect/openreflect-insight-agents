# Pattern Analyst Agent PRD

Status: Draft
Created: 2026-06-17
Public posture: generic framework first; private source adapters and real datasets stay downstream

## BLUF

Pattern Analyst Agent finds recurring structures across provenance-bearing memory and interaction records. It emits bounded pattern insights that include evidence references, confidence, recency scope, uncertainty, and recommended use.

## Problem

Assistant memory often contains repeated signals that are meaningful only in aggregate. A user may repeatedly return to a blocker, ask for the same grounding behavior, correct the same failure mode, or show the same project loop. Individual records are easy to retrieve, but the repeated structure can remain invisible.

The opposite risk is also real: an assistant may see one old event and convert it into an overconfident trait claim.

## Goals

- Detect recurring structures across source, signal, and insight records.
- Separate current patterns from historical patterns.
- Require evidence references for every pattern claim.
- Preserve uncertainty, counterevidence, and recency.
- Produce concise recommendations for how the pattern may inform assistant behavior.
- Abstain when the evidence is too thin or too stale.

## Non-Goals

- Diagnose personality, medical, or psychological conditions.
- Treat old repeated history as present state.
- Produce identity claims from weak evidence.
- Replace direct user confirmation for sensitive interpretations.
- Build production memory retrieval in this repository.

## Users

- Assistants that need pattern-aware context.
- Developers building OpenReflect-compatible insight agents.
- Operators reviewing repeated project, communication, or workflow signals.

## First Milestone

Create a markdown and JSONL scaffold:

1. PRD and README.
2. Prompt for extracting pattern insights.
3. Synthetic fixture with repeated and countervailing evidence.
4. Example insight records.
5. Capability manifest.

## Success Criteria

- Pattern claims cite multiple source references when available.
- The agent marks weak or emerging patterns as uncertain.
- Stale patterns do not become current-state claims.
- Counterevidence is represented in the uncertainty field.
- Outputs can be consumed as shared insight records.

