# Skill Recommender Agent PRD

Status: Planned
Created: 2026-06-27
Public posture: generic framework first; private skill contents, credentials, and deployment logs stay downstream

## BLUF

Skill Recommender Agent maps task context to candidate skills, MCPs, and workflows using capability metadata, observed needs, and outcome signals. It recommends what to use, why, and what is missing, while avoiding claims about private access or safety that are not supported by the registry.

## Problem

Assistant environments can accumulate many skills, tools, MCPs, and workflows. Without a recommendation layer, agents may underuse useful capabilities, choose tools because they are familiar, or over-route simple tasks into unnecessary machinery.

The more dangerous failure is false capability confidence: recommending a skill because it exists in a catalog, assuming credentials are available, or treating a planned capability as active.

## Goals

- Recommend candidate skills, MCPs, or workflows from task context and capability metadata.
- Explain the selection rationale with evidence from the registry or prior outcome signals.
- Detect missing capabilities and recommend abstention when no suitable skill exists.
- Distinguish active, scaffolded, planned, and unavailable capabilities.
- Avoid private access, credential, or deployment assumptions.
- Produce recommendations that a capability router or assistant can inspect before acting.

## Non-Goals

- Execute the selected skill or tool.
- Infer credential availability or private tool access.
- Claim a skill is safe for sensitive use without evidence.
- Recommend tools merely because they exist.
- Replace human approval for external or high-risk actions.
- Store private skill bodies, secrets, or local deployment logs in public examples.

## Users

- Assistants deciding whether to activate a specialized skill.
- Capability routers composing multi-agent workflows.
- Developers maintaining OpenReflect-compatible skill catalogs.
- Operators reviewing why a tool or workflow was recommended.

## Core Concept

Skill Recommender Agent is a restrained matchmaker. It should prefer no recommendation over an unjustified one, and it should make missing capability gaps explicit.

Recommendations should include:

- task need
- candidate skill or workflow
- registry evidence
- rationale
- status and readiness caveat
- missing capability note when applicable

## Inputs And Outputs

Initial inputs:

- task description
- capability registry
- skill metadata
- MCP metadata
- outcome signals
- policy constraints

Initial outputs:

- skill recommendation
- selection rationale
- missing capability note
- abstention decision
- readiness caveat

## First Milestone

Create a markdown and JSONL scaffold:

1. PRD and README.
2. Prompt for recommending or abstaining from skills.
3. Synthetic task set with expected recommendations and abstentions.
4. Example recommendation records.
5. Capability manifest connected to the shared registry.

## Success Criteria

- Recommendations cite metadata or outcome evidence.
- Planned or unavailable capabilities are not presented as active.
- Missing capability cases produce clear abstention notes.
- Simple tasks are not over-routed.
- Private access and credential availability are never inferred.

