# Human Telemetry Agent PRD

Status: Draft
Created: 2026-06-14
Public posture: generic framework first; private adapters and real datasets stay private

## BLUF

Human Telemetry Agent is a time-aware insight agent that mines assistant interaction traces for user sentiment, state, and work-context signals. It turns scattered transcripts, memory records, and project logs into evidence-backed state narratives that an assistant can use to adapt its behavior.

The first live calibration case is private. The productizable version must remain generic: it should support any human using an assistant stack with provenance-bearing memory.

## Problem

Assistants can miss important human state changes because signals are spread across long-running sessions, memory stores, audio transcripts, project notes, and runtime logs. The result is context drift: the assistant may answer the local prompt correctly while missing the user's fatigue, pain, overload, frustration, confidence, hesitation, or project-specific cognitive load.

This creates a practical risk in long-horizon work. A human may carry heavier context weight than the assistant, move between projects quickly, or fail to notice how physical state, fatigue, caffeine, context-jumping, or overload is affecting the work. The assistant needs a durable, evidence-backed way to notice and check these patterns without becoming clinically overconfident.

For OpenReflect, this is a market-relevant capability: insight agents over provenance-rich memory can turn assistant interaction history into useful personal-state intelligence.

## Goals

- Extract sentiment and state signals from transcript-like and memory-like sources.
- Align every signal with time, source, confidence, and supporting evidence.
- Separate present-state interpretation from historical trend mining.
- Link state signals to projects, tasks, and work modes when evidence supports it.
- Produce concise narratives that explain what the signal suggests and how the assistant should adapt.
- Support private calibration adapters while keeping the public framework generic and reusable.
- Provide an inspectable markdown and JSONL-first prototype before heavier infrastructure.

## Non-Goals

- Diagnose medical or psychiatric conditions.
- Replace direct user check-ins.
- Treat language-derived state as proof.
- Build a full OpenReflect backend in the first version.
- Publicly expose private transcripts, local paths, personal names, chat IDs, runtime IDs, or private operational details.

## Users

- Primary operator: an assistant or agent that needs to adapt to a human's current state.
- Primary human: a person whose interaction traces contain state signals.
- Developer/operator: someone configuring data-source adapters and private calibration profiles.
- Future OpenReflect user: a person who wants personal insight from assistant memory with provenance.

## Core Concept

Human Telemetry Agent works like a mood ring for assistant-mediated work, but with provenance and restraint.

It should not merely label text as positive, negative, or neutral. That base sentiment layer is useful, but the value is the higher-level interpretation:

- What state might this indicate?
- What evidence supports that reading?
- How recent is it?
- Is it tied to a project, task, or body-state flag?
- How should the assistant change behavior now?
- What should be checked directly with the user?

## Data Sources

Initial source adapters:

- OpenReflect memory exports or APIs.
- Assistant conversation summaries and recall tools.
- Local semantic memory files.
- Workspace markdown notes and task files.
- Agent memory, logs, and artifacts.
- Audio transcripts produced by messaging or voice interfaces.

The adapter interface should make it possible to add other memory systems later without changing the signal schema.

## Signal Codecs

Signal codecs are modular extractors that convert raw traces into normalized signal records.

Initial codecs:

- sentiment codec: positive, neutral, negative, mixed, unknown
- state-label codec: overload, hesitation, repetition, context-jump, clarity, urgency
- temporal codec: observed time, referenced time, recency bucket
- project codec: project or workstream association
- body-state codec: pain, sleep, caffeine, medication, food, energy when explicitly mentioned or strongly implied
- assistant-response codec: recommended behavioral adjustment
- provenance codec: source pointers, confidence, excerpt policy, privacy tier

## Time Model

Every query and signal must distinguish:

- present: current session or active work block
- recent: last 24-72 hours
- near history: last 7-30 days
- medium history: last 30-90 days
- long history: older than 90 days

Historical similarity should never be treated as current truth.

## Project Alignment

The agent should infer project or workstream only when evidence supports it. When project alignment is uncertain, the record should use `project_ref: null` and include the ambiguity in `interpretation`.

## First Milestone

Create a markdown and JSONL prototype:

1. PRD and schema document.
2. `examples/signals.example.jsonl` with synthetic examples.
3. `private/signals.private.jsonl` ignored by git for live calibration.
4. One extractor prompt that takes a transcript excerpt and emits normalized signal records.
5. One review prompt that turns recent signals into a short assistant action brief.

## Success Criteria

- The assistant can answer "what state signals are present right now?" with evidence and timestamps.
- The assistant can distinguish current state from historical pattern.
- The assistant can adapt response length, scope, and check-in behavior based on the signal brief.
- Private calibration records stay out of the public framework.
- The schema supports multiple assistant memory systems through adapters.
- The public repo can be audited cleanly for private-data leakage.
