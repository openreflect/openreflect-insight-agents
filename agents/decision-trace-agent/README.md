# Decision Trace Agent

Decision Trace Agent reconstructs how a decision formed from provenance-bearing records. It identifies inputs, constraints, alternatives, tradeoffs, decision points, final rationale, unresolved assumptions, and follow-up checks.

The goal is not to justify a decision after the fact. The goal is to make decision provenance inspectable.

## Why it exists

Long-running work often contains decisions spread across chats, project notes, commits, plans, and issue comments. The final choice may be visible while the reasoning path is fragmented.

Without a decision trace, assistants can repeat a conclusion without knowing why it was chosen, what alternatives were rejected, or which assumptions remain fragile.

## Core idea

```text
notes / transcripts / artifacts / commits
        |
        v
decision candidates
        |
        v
inputs + constraints + alternatives
        |
        v
trace record
        |
        v
decision brief + revisit triggers
```

## What It Manages

- Decision candidates and final decision statements
- Evidence references for each stage
- Inputs, constraints, tradeoffs, rejected alternatives, and rationale
- Open assumptions and revisit triggers
- Confidence and uncertainty
- Recommended assistant behavior when the decision is reused

## Design Principles

- Reconstruct, do not rationalize.
- Separate decision evidence from later commentary.
- Preserve rejected alternatives when evidence supports them.
- Mark unknown rationale as unknown.
- Private operational decisions stay downstream.

## Current Status

Draft scaffold:

- PRD
- extraction prompt
- synthetic fixture
- synthetic trace examples
- capability manifest

