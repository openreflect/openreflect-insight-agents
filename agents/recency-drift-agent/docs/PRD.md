# Recency/Drift Agent PRD

Status: Planned
Created: 2026-06-27
Public posture: generic framework first; private histories, operational timelines, and live system traces stay downstream

## BLUF

Recency/Drift Agent detects when older memories, summaries, preferences, project assumptions, or artifact references may be stale relative to newer evidence. It warns downstream assistants when historical pattern should not be treated as current truth.

## Problem

Long-running assistant systems are vulnerable to stale continuity. A once-true preference, project status, body-state note, tool limitation, or architectural assumption can persist in memory after reality changes. Without drift checks, assistants can sound continuous while acting on outdated context.

The agent must also avoid false drift. A newer source does not always supersede an older one, and absence of recent mention does not prove a change.

## Goals

- Compare timestamped records, summaries, artifact versions, and recent observations for possible staleness.
- Separate current evidence from historical pattern.
- Identify superseded references when newer source evidence exists.
- Recommend refresh, source check, or direct user confirmation.
- Preserve uncertainty when drift is possible but not proven.
- Support synthetic fixtures for stale-state and false-drift cases.

## Non-Goals

- Infer current state from old history.
- Mark a memory superseded without newer source evidence.
- Infer user preference change from silence.
- Claim live system status without a live check.
- Replace direct verification for critical operational state.
- Store private histories or operational timelines in public examples.

## Users

- Assistants preparing to use memory-sensitive context.
- Reflection and synthesis agents checking whether source material is current.
- Operators reviewing stale assumptions in project or behavior records.
- Developers building OpenReflect recency and provenance workflows.

## Core Concept

Recency/Drift Agent is a freshness guard. It should slow down stale assumptions without erasing useful history.

Drift warnings should include:

- stale or possibly stale reference
- newer evidence reference
- drift type
- confidence
- recommended refresh method
- downstream use guidance

## Inputs And Outputs

Initial inputs:

- timestamped insight records
- memory summaries
- artifact versions
- recent observations
- source records
- action briefs

Initial outputs:

- drift warnings
- superseded reference lists
- refresh recommendations
- false-drift abstention notes
- recency guidance for downstream use

## First Milestone

Create a markdown and JSONL scaffold:

1. PRD and README.
2. Prompt for recency and drift review.
3. Synthetic stale-state fixture with newer and older evidence.
4. Example drift warning records.
5. Capability manifest connected to the shared registry.

## Success Criteria

- Old records are not treated as current truth without current evidence.
- Newer contradictory evidence takes precedence when source-backed.
- Silence alone does not create a drift finding.
- The agent recommends live checks for live-state claims.
- Outputs can gate reflection summaries, action briefs, and routing decisions.

