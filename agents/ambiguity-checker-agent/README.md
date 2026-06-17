# Ambiguity Checker Agent

Ambiguity Checker Agent identifies unclear claims, overloaded terms, missing assumptions, weak references, conflicting interpretations, and places where an assistant should ask a clarifying question before acting.

The goal is to make uncertainty operational instead of burying it under fluent language.

## Why it exists

Assistant workflows often fail at the boundary between plausible interpretation and confirmed meaning. A request can contain pronouns with unclear references, terms with multiple meanings, unstated acceptance criteria, missing dates, or claims that require source contact before confidence.

Without an ambiguity layer, assistants may act on the most convenient interpretation.

## Core idea

```text
request / note / plan / insight
        |
        v
ambiguity scan
        |
        v
ambiguity findings
        |
        v
clarifying questions / abstention guidance
        |
        v
safer next action
```

## What It Manages

- Ambiguous references, dates, scopes, and terms
- Missing assumptions and acceptance criteria
- Conflicting interpretations
- Claims that need primary-source verification
- Clarifying questions ranked by action impact
- Abstention and proceed-with-assumption guidance

## Design Principles

- Ambiguity is not failure; hidden ambiguity is failure.
- Ask only questions that materially change the next action.
- Prefer explicit assumptions for low-risk ambiguity.
- Require verification before high-risk claims or external action.
- Public examples stay synthetic and generic.

## Current Status

Draft scaffold:

- PRD
- extraction prompt
- synthetic fixture
- synthetic ambiguity examples
- capability manifest

