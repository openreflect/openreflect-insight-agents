# Project Pattern Agent PRD

Status: Planned
Created: 2026-06-27
Public posture: generic framework first; private repository paths, customer data, and internal planning records stay downstream

## BLUF

Project Pattern Agent identifies recurring project-level loops across provenance-backed notes, artifacts, decisions, and insight records. It emits bounded pattern records that describe repeated blockers, context jumps, momentum shifts, revisit loops, or execution rhythms without inventing unstated ownership, priority, or causality.

## Problem

Projects often repeat the same failure modes before anyone names them. A team may cycle through unclear ownership, stale assumptions, blocked integration points, scope churn, or inconsistent verification. Individual notes show incidents; project health depends on seeing recurrence.

The opposite risk is overreach. A repeated phrase, an old blocker, or a single delayed task can become an exaggerated project diagnosis if the agent does not preserve recency, counterevidence, and source boundaries.

## Goals

- Detect recurring project patterns across notes, decision records, artifact metadata, and insight records.
- Separate active project-state signals from stale historical loops.
- Identify blockers, momentum changes, revisit cycles, context jumps, and verification gaps.
- Preserve supporting evidence and counterevidence.
- Recommend bounded follow-up, such as source verification, planning review, owner clarification, or fixture creation.
- Keep public fixtures generic and synthetic.

## Non-Goals

- Infer unstated project owner, roadmap, priority, or business strategy.
- Claim causality without evidence.
- Replace project management systems or human planning judgment.
- Audit private repositories or customer data inside the public repo.
- Treat all repeated activity as a problem.

## Users

- Assistants helping operators keep long-running projects coherent.
- Developers building project-aware OpenReflect insight agents.
- Human project owners looking for recurring execution loops.
- Capability routers deciding whether project-pattern analysis should run before action.

## Core Concept

Project Pattern Agent is a recurrence detector for project work. It should answer "what keeps happening in this project?" while keeping old patterns, current blockers, and speculative explanations separate.

Pattern records should include:

- project or artifact reference
- pattern description
- supporting evidence
- recency scope
- counterevidence or uncertainty
- recommended follow-up

## Inputs And Outputs

Initial inputs:

- project notes
- decision records
- artifact metadata
- insight records
- source records
- action briefs

Initial outputs:

- pattern records
- supporting evidence lists
- recency and drift notes
- recommended follow-up
- abstention notes when evidence is insufficient

## First Milestone

Create a markdown and JSONL scaffold:

1. PRD and README.
2. Prompt for extracting project pattern records.
3. Synthetic project timeline fixture with repeated blockers and counterevidence.
4. Example pattern records.
5. Capability manifest connected to the shared registry.

## Success Criteria

- Pattern records cite multiple source references when recurrence is claimed.
- Active patterns are separated from stale or resolved patterns.
- Recommended follow-up is practical and bounded.
- The agent avoids confidential roadmap, owner, or priority inference.
- Outputs can feed shared insight records or planning review surfaces.

