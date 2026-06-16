# OpenReflect Insight Agents

OpenReflect Insight Agents is a public framework for building capability agents that mine provenance-rich memory and interaction traces for insight.

The goal is not to remember everything between agents. The goal is to turn memory into useful reflection: signal extraction, pattern detection, state narratives, skill selection, and feedback loops that help an assistant grow with a user over time.

## Why it exists

Most assistant memory systems optimize for recall: preserve facts, retrieve snippets, and keep conversations from resetting. Recall is necessary, but it is not enough.

Long-running human/assistant work needs an insight layer:

- What changed in the user's state or priorities?
- Which patterns keep recurring across projects?
- What evidence supports a behavioral adjustment?
- Which agent, skill, MCP, or workflow should be activated next?
- What should be checked directly instead of inferred?
- How does the assistant improve without becoming overconfident?

OpenReflect Insight Agents provides the public, inspectable starting point for that layer.

## Core idea

```text
provenance-rich memory / transcripts / artifacts / telemetry
        |
        v
source adapters
        |
        v
capability agents
        |
        +--> human telemetry
        +--> reflection synthesis
        +--> project pattern mining
        +--> agent capability routing
        +--> skill and MCP recommendations
        |
        v
insight records + action briefs + feedback loops
        |
        v
OpenReflect surfaces and downstream assistants
```

The framework separates memory from insight:

- Memory preserves evidence.
- Insight interprets evidence with uncertainty, provenance, and restraint.
- Action briefs convert insight into practical assistant behavior.

## What OpenReflect Insight Agents manages

- Capability-agent specifications.
- Public-safe schemas for insight records and action briefs.
- Source adapter interfaces for memory and transcript systems.
- Synthetic fixtures for agent evaluation.
- Prompt files for agent-operated extraction and review.
- Skill and MCP capability registry structure.
- Privacy boundaries between public framework and private calibration data.
- Evaluation criteria for evidence, uncertainty, recency, and usefulness.

## Design principles

- Provenance first: every specific claim needs a source pointer or uncertainty label.
- Insight is not diagnosis: state signals guide check-ins and behavior, not medical claims.
- Memory is substrate, not product: the value is reflection, synthesis, and adaptation.
- Public generic, private calibrated: real profiles, transcripts, routes, and logs stay downstream.
- Small agents, explicit capabilities: each capability agent should have a narrow job and clear evals.
- Feedback loops matter: agent output should improve future extraction, routing, and response behavior.
- Recency matters: historical pattern is not current truth.

## Repository layout

```text
.
├── README.md
├── docs/
│   ├── ADDING-CAPABILITY-AGENTS.md
│   ├── ARCHITECTURE.md
│   ├── CAPABILITY-REGISTRY.md
│   ├── GLOSSARY.md
│   ├── MATURITY.md
│   ├── ROADMAP.md
│   ├── SIGNAL-RECORDS.md
│   ├── SOURCE-ADAPTERS.md
│   └── PRD.md
├── agents/
│   └── human-telemetry-agent/
├── capability-agents/
├── mcps/
├── skills/
├── schemas/
├── examples/
├── fixtures/
├── prompts/
└── scripts/
```

## Current status

Initial project workspace. The first imported capability agent is `agents/human-telemetry-agent`, a public-safe scaffold for extracting time-aware user state and work-context signals from assistant interaction traces.

Useful starting points:

- `docs/PRD.md` defines the product shape.
- `docs/ARCHITECTURE.md` defines the source-adapter to insight-record flow.
- `docs/GLOSSARY.md` defines shared project terminology.
- `docs/SOURCE-ADAPTERS.md` defines the adapter contract for provenance-rich sources.
- `docs/SIGNAL-RECORDS.md` defines shared signal record expectations.
- `docs/ADDING-CAPABILITY-AGENTS.md` explains how to add new capability agents.
- `docs/MATURITY.md` and `docs/ROADMAP.md` describe current maturity and near-term direction.

Run the public-safe audit:

```bash
python3 path/to/audit_public_repo.py .
```

## Public/private model

Use this repository as the generic upstream. Keep environment-specific customizations in private downstream repositories or private branches.

```text
ORG/openreflect-insight-agents     public generic framework
private downstream fork            local adapters, real profiles, credentials, logs
```

This keeps the public framework reusable while preserving operational privacy.
