# Decision Trace Agent PRD

Status: Draft
Created: 2026-06-17
Public posture: generic framework first; private decision logs and operational traces stay downstream

## BLUF

Decision Trace Agent reconstructs decision provenance from source records. It turns scattered reasoning into inspectable decision traces with evidence, constraints, alternatives, unresolved assumptions, confidence, and revisit triggers.

## Problem

Projects accumulate decisions faster than they accumulate rationale. A repository may show what changed, while conversations and notes explain why. Over time, assistants may remember the conclusion but lose the reason it was defensible.

That creates drift: future work repeats a decision without knowing its constraints, or reverses it without noticing what problem it solved.

## Goals

- Identify decision candidates in provenance-bearing material.
- Reconstruct the decision path using cited evidence.
- Separate inputs, constraints, alternatives, tradeoffs, rationale, and final outcome.
- Preserve unknowns instead of filling gaps.
- Identify revisit triggers when assumptions change.
- Emit concise traces that downstream assistants can inspect before relying on old decisions.

## Non-Goals

- Prove a decision was correct.
- Rewrite history to make a decision look cleaner.
- Infer private motives not present in evidence.
- Replace source review for high-risk decisions.
- Store private operational logs in the public repo.

## Users

- Assistants that need to reuse prior decisions safely.
- Developers maintaining long-horizon agent or memory projects.
- Operators auditing why a plan or architecture moved in a specific direction.

## First Milestone

Create a markdown and JSONL scaffold:

1. PRD and README.
2. Prompt for extracting decision traces.
3. Synthetic fixture with clear and missing rationale.
4. Example insight records.
5. Capability manifest.

## Success Criteria

- Every reconstructed decision cites source references.
- Unknown rationale is marked as unknown rather than inferred.
- Rejected alternatives and constraints are preserved when present.
- The trace includes revisit triggers.
- Outputs can be consumed as shared insight records or converted into a future decision-specific schema.

