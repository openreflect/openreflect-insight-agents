# Pattern Analyst Agent

Pattern Analyst Agent is a provenance-aware capability agent for finding recurring structures across memory records, transcripts, project notes, and prior insight records. It turns repeated evidence into bounded pattern claims with source references, recency scope, confidence, and explicit uncertainty.

The goal is to help assistants notice recurring loops without treating repetition as proof.

## Why it exists

Long-running assistant work accumulates fragments: repeated blockers, recurring phrasing, project loops, recurring user needs, similar failure modes, and repeated corrections. Those patterns are useful only when they stay attached to evidence and time.

Without a bounded pattern layer, assistants either miss repeated structure or overfit to stale history.

## Core idea

```text
source records / signal records / insight records
        |
        v
candidate repetitions
        |
        v
evidence clustering
        |
        v
pattern claims with uncertainty
        |
        v
recommended use / do-not-use guidance
```

## What It Manages

- Recurring behaviors, themes, blockers, priorities, and workflow loops
- Evidence clusters across multiple source records
- Recency scope: present, recent, near history, medium history, long history, mixed, unknown
- Pattern strength: weak, emerging, recurring, strong
- Counterevidence and exceptions
- Recommended assistant use and misuse boundaries

## Design Principles

- A pattern requires multiple evidence points or one evidence point plus explicit uncertainty.
- Historical recurrence is not current truth.
- Pattern claims should preserve counterexamples.
- Pattern labels should be descriptive, not diagnostic.
- Private calibration data stays downstream.

## Current Status

Draft scaffold:

- PRD
- extraction prompt
- synthetic fixture
- synthetic insight examples
- capability manifest

