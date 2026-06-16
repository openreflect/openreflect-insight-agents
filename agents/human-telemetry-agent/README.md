# Human Telemetry Agent

Human Telemetry Agent is a provenance-aware signal miner for assistant interaction traces. It extracts time-aligned user sentiment, functional state, and work-context signals from memory systems so assistants can adapt with evidence instead of guessing.

The goal is a reusable OpenReflect-aligned framework for personal insight agents. Private calibration profiles and real interaction data live outside the public repository.

## Why it exists

Assistant conversations contain useful state signals: fatigue, overload, frustration, clarity, context switching, pain mentions, hesitation, urgency, and requests for grounding. Those signals are often scattered across transcripts, summaries, memory stores, project logs, and voice transcripts.

Without a durable signal layer, assistants can answer a prompt correctly while missing the human state that should change the response.

## Core idea

```text
memory systems / transcripts / logs
        |
        v
source adapters
        |
        v
signal codecs
        |
        v
time-aligned signal records
        |
        v
state narrative + assistant action brief
```

The agent is a "mood ring" for assistant-mediated work, but with provenance: timestamp, source pointer, confidence, evidence, privacy tier, and recommended assistant behavior.

## What It Manages

- Base sentiment: positive, neutral, negative, mixed, unknown
- Functional state labels: overloaded, fatigued, pain-affected, hesitant, frustrated, clear, scattered, repetitive, urgent, context-jumping
- Work-context links: project, task, workstream, active mode
- Time semantics: present, recent, near history, medium history, long history
- Provenance: source system, source reference, evidence excerpt policy, confidence
- Assistant action briefs: how the assistant should adjust response length, scope, check-ins, and stop conditions

## Design principles

- Signals are evidence, not diagnosis.
- Present-state inference and historical trend mining are separate modes.
- Every specific claim needs a source pointer or an explicit uncertainty label.
- Public framework stays generic; private calibration data stays private.
- Markdown, JSONL, and prompt files come before heavy infrastructure.
- Adapters should make memory systems interchangeable.

## Repository layout

```text
docs/       Product requirements and design notes
schema/     JSON schema and taxonomy definitions
examples/   Public-safe example records
fixtures/   Synthetic test inputs
prompts/    Agent prompts paired with future scripts
scripts/    Deterministic extraction/eval scripts
private/    Ignored local-only calibration workspace
```

## Current status

Draft scaffold. The first milestone is a markdown and JSONL prototype:

- product requirements document
- normalized signal schema
- synthetic examples
- extractor prompt
- review/action-brief prompt

## Public/private model

Public repo:

- generic schema
- synthetic fixtures
- adapter interfaces
- sanitized examples
- public-safe tests and evals
- script/prompt pairs
- privacy and provenance rules

Private local workspace:

- real profiles
- real transcripts
- live adapter configuration
- local memory paths
- operational calibration logs

Never commit secrets, private transcripts, real chat IDs, local system paths, credential references, or live operational logs.
