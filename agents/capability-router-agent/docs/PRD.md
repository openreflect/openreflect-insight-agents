# Capability Router Agent PRD

Status: Planned
Created: 2026-06-27
Public posture: generic framework first; private policy details, local environment data, and operational routing logs stay downstream

## BLUF

Capability Router Agent chooses which insight agent, skill, MCP, or workflow should handle a request based on capability manifests, input requirements, status, policy constraints, and task scope. It routes only when routing adds value, and it marks unsupported or overbroad requests clearly.

## Problem

As the capability catalog grows, assistants need help deciding where work should go. A request may need human telemetry, ambiguity checking, evidence review, recency drift review, skill recommendation, or no specialized agent at all.

Routing can also become its own failure mode. Over-routing simple work wastes time, planned capabilities may be treated as available, and private access or policy exceptions may be assumed without evidence.

## Goals

- Match task requests to available or planned capabilities using manifest metadata.
- Distinguish no-op, single-capability, and multi-capability routing cases.
- Check input availability before recommending a route.
- Respect capability status, privacy boundaries, and policy constraints.
- Emit unsupported request notes when no suitable capability exists.
- Avoid over-routing simple requests that do not need specialized handling.

## Non-Goals

- Execute routed work.
- Treat planned capabilities as active.
- Infer private data access or policy exceptions.
- Claim production readiness from a manifest.
- Replace human approval for sensitive external actions.
- Store private routing logs or environment-specific policies in the public repo.

## Users

- Assistants orchestrating OpenReflect insight capabilities.
- Developers validating capability manifest coverage.
- Operators reviewing why a task was routed or not routed.
- Downstream systems composing multi-agent workflows.

## Core Concept

Capability Router Agent is the dispatcher for the insight layer. It should choose the smallest adequate route, explain why, and refuse unsupported requests without pretending the catalog can do more than it can.

Routing decisions should include:

- task request
- selected capability or no-op
- match rationale
- required inputs
- missing inputs
- status and privacy caveats
- unsupported request note when applicable

## Inputs And Outputs

Initial inputs:

- task request
- capability manifests
- input inventory
- policy constraints
- prior routing outcomes
- skill and MCP metadata

Initial outputs:

- routing decisions
- capability match rationales
- unsupported request notes
- missing input warnings
- over-routing abstention notes

## First Milestone

Create a markdown and JSONL scaffold:

1. PRD and README.
2. Prompt for routing or abstaining from routing.
3. Synthetic request set covering no-op, single-agent, multi-agent, planned-only, and unsupported cases.
4. Example routing decision records.
5. Capability manifest connected to the shared registry.

## Success Criteria

- Planned capabilities are not represented as active.
- Simple requests can receive no-op routing.
- Routes cite manifest metadata and available inputs.
- Unsupported requests produce explicit notes rather than forced matches.
- Privacy and policy constraints are visible in routing rationale.

