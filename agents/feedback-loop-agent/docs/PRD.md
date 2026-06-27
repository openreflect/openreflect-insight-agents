# Feedback Loop Agent PRD

Status: Planned
Created: 2026-06-27
Public posture: generic framework first; private feedback, chat identifiers, and deployment telemetry stay downstream

## BLUF

Feedback Loop Agent records whether assistant adaptations, recommendations, routes, and insight outputs helped, missed, overreached, or required correction. It turns feedback events into behavior-adjustment notes and eval-update recommendations without overfitting from a single event.

## Problem

Insight agents can make the same mistake repeatedly if feedback remains trapped in chat history or informal notes. A user correction, failed route, useful action brief, or stale recommendation should influence future behavior and eval coverage.

The risk is self-reinforcement. If the system treats one positive or negative event as durable truth, it may lock in a bad adaptation, exaggerate a preference, or optimize for a local success at the expense of broader usefulness.

## Goals

- Capture feedback events tied to prior recommendations, action briefs, routes, or outputs.
- Distinguish helped, missed, overreached, stale, unclear, and corrected outcomes.
- Produce behavior-adjustment notes for downstream assistants.
- Recommend eval updates when feedback exposes a repeatable failure mode.
- Preserve source references and avoid satisfaction claims without explicit feedback.
- Support public-safe synthetic feedback fixtures.

## Non-Goals

- Infer user satisfaction without feedback.
- Convert a single event into a durable preference without corroboration.
- Judge model quality without eval evidence.
- Claim deployment health without telemetry.
- Replace human review for sensitive behavior changes.
- Store private user feedback, chat identifiers, or deployment telemetry in public examples.

## Users

- Assistants improving behavior from user or system feedback.
- Developers maintaining eval suites for insight agents.
- Operators auditing whether recommendations actually helped.
- Capability routers using prior outcomes to choose or avoid agents.

## Core Concept

Feedback Loop Agent is the learning ledger for the insight layer. It should preserve corrections and outcomes in a form that can improve future behavior without creating brittle rules from isolated events.

Feedback records should include:

- feedback event
- prior recommendation or action brief reference
- outcome category
- evidence
- behavior-adjustment note
- eval-update recommendation

## Inputs And Outputs

Initial inputs:

- feedback events
- prior recommendations
- action briefs
- routing decisions
- outcome records
- eval results

Initial outputs:

- feedback summaries
- behavior-adjustment notes
- eval-update recommendations
- overfit warnings
- unresolved feedback questions

## First Milestone

Create a markdown and JSONL scaffold:

1. PRD and README.
2. Prompt for converting feedback events into feedback records.
3. Synthetic fixture with helped, missed, corrected, and ambiguous outcomes.
4. Example feedback records.
5. Capability manifest connected to the shared registry.

## Success Criteria

- Feedback records cite the event and the prior output being evaluated.
- Corrections are preserved as behavior guidance.
- Single events are marked as limited evidence unless corroborated.
- Eval-update recommendations are traceable to observed failures.
- Outputs can feed future synthesis, routing, and skill recommendation.

