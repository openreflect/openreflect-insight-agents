# OpenReflect Insight Agents PRD

Status: Draft
Created: 2026-06-14
Public posture: generic framework first; private memory adapters and calibration data stay downstream

## Summary

OpenReflect Insight Agents is a framework for building agents that enrich memory with evidence-backed insight. It provides schemas, prompts, fixtures, and capability-agent patterns for mining assistant interaction history, project artifacts, and telemetry into actionable reflection.

The repo starts with a small capability-agent catalog: Human Telemetry Agent, Pattern Analyst Agent, Decision Trace Agent, and Ambiguity Checker Agent. The broader direction is a library of skill, MCP, and capability agents that can mine and feed OpenReflect.

## Problem

Memory frameworks usually answer "what happened?" or "what should be recalled?" They rarely answer the higher-value questions:

- What does this pattern mean?
- What should the assistant do differently now?
- Which evidence supports that adjustment?
- What is current state versus historical tendency?
- Which tool, skill, agent, or workflow should be activated?
- What should be verified with the human?

Without an insight layer, agents can share memory and still fail to grow with the user.

## Product Thesis

OpenReflect should not be a shared scratchpad for agents. It should be a reflection system: provenance-rich memory plus capability agents that extract patterns, produce restrained interpretations, and feed better behavior back into the assistant loop.

## Goals

- Define a public-safe capability-agent framework for OpenReflect.
- Import Human Telemetry Agent as the first capability agent.
- Add Pattern Analyst, Decision Trace Agent, and Ambiguity Checker as scaffolded catalog agents.
- Provide schemas for signal records, insight records, and assistant action briefs.
- Provide prompt patterns for extraction, review, and synthesis agents.
- Maintain a registry of skills, MCPs, and capability agents.
- Support source adapters for transcripts, memory systems, project notes, logs, and telemetry.
- Keep private calibration profiles and real datasets out of the public repository.
- Build toward agents that improve user-specific insight over time.

## Non-Goals

- Replacing OpenReflect's core memory/provenance backend.
- Building a monolithic all-purpose agent.
- Publishing private transcripts or local operational details.
- Treating inferred state as clinical diagnosis.
- Making agent-to-agent memory sharing the main product.

## Users

- Developers building OpenReflect-compatible insight agents.
- Assistant operators who need evidence-backed state and project insight.
- Human users who want memory to become useful self-reflection.
- Agent runtimes that need action briefs, routing recommendations, and skill suggestions.

## First Capability Agent

### Human Telemetry Agent

Purpose: extract time-aligned user sentiment, functional state, work-context signals, and assistant action guidance from provenance-bearing interaction traces.

Initial outputs:

- normalized signal records
- state narratives
- assistant action briefs
- check-in recommendations
- privacy tier and evidence policy

## Scaffolded Catalog Agents

### Pattern Analyst Agent

Purpose: detect recurring structures across provenance-bearing records and emit bounded pattern insights with uncertainty.

### Decision Trace Agent

Purpose: reconstruct decision provenance from evidence-bearing records without inventing missing rationale.

### Ambiguity Checker Agent

Purpose: detect action-changing ambiguity and recommend clarification, explicit assumptions, abstention, or source verification.

## Future Capability Agents

Candidate agents:

- Reflection Synthesis Agent: turns multiple signal streams into short reflective summaries.
- Project Pattern Agent: detects repeated project-context loops, blockers, and momentum changes.
- Skill Recommender Agent: maps observed needs to available skills, MCPs, and workflows.
- Evidence Quality Agent: scores whether an insight is well-supported or speculative.
- Recency/Drift Agent: separates present state from stale historical pattern.
- Feedback Loop Agent: records whether assistant adaptations helped or missed.
- Capability Router Agent: selects the right downstream agent or MCP for a given insight task.

## Core Data Objects

- Source record: pointer to transcript, log, note, memory item, artifact, or telemetry.
- Signal record: small evidence-backed observation.
- Insight record: synthesis across one or more signals.
- Action brief: concise instruction for how an assistant should adapt.
- Capability manifest: what an agent/skill/MCP can do, required inputs, outputs, evals.
- Feedback record: whether an action brief produced useful behavior.

## Evaluation Criteria

- Every specific claim has provenance or an uncertainty label.
- Present-state claims are separated from historical pattern.
- Private data is excluded from public fixtures and examples.
- Action briefs are short enough to be used in live assistant context.
- Capability agents have bounded scope and synthetic eval fixtures.
- Agent output improves behavior without overclaiming certainty.

## Milestones

### M0: Monorepo Scaffold

- top-level README and PRD
- capability registry
- Human Telemetry Agent imported under `agents/`
- Pattern Analyst, Decision Trace, and Ambiguity Checker scaffolded under `agents/`
- public audit passes

### M1: Shared Schemas

- signal record schema
- insight record schema
- action brief schema
- capability manifest schema

### M2: Agent Evals

- synthetic fixtures for each capability agent
- deterministic validation scripts
- paired prompts for agent-operated scripts

### M3: Private Adapter Bridge

- downstream private adapter examples
- public adapter interface docs
- no real transcripts in public repo

### M4: OpenReflect Feed

- generic export format for feeding OpenReflect
- action brief format for downstream assistants
- feedback record format for improvement loops
