# Reflection Synthesis Agent PRD

Status: Planned
Created: 2026-06-27
Public posture: generic framework first; private transcripts, identities, and operational logs stay downstream

## BLUF

Reflection Synthesis Agent turns multiple provenance-backed observations into concise reflective summaries for later human or agent review. It does not discover every fact itself; it composes source-linked insight records, signal records, artifact references, transcript excerpts, and operator notes into bounded summaries with open questions and uncertainty.

## Problem

Insight systems can collect many small observations without producing a usable reflection. A user or downstream assistant may have signal records, pattern notes, decision traces, and feedback records, but still lack a short answer to "what does this body of evidence suggest, and what should be reviewed next?"

The risk runs both ways. Without synthesis, evidence remains fragmented. With careless synthesis, an assistant may turn weak signals into overconfident narrative, infer private motives, or smooth over contradictions that should remain visible.

## Goals

- Summarize multiple source-backed records into short reflective notes.
- Preserve source references and uncertainty in the summary.
- Separate observed evidence from interpretation.
- Surface contradictions, missing evidence, and open questions.
- Produce reflection summaries that are useful for later human review, assistant context, or downstream action-brief generation.
- Abstain or narrow scope when evidence is thin, stale, or outside the requested window.

## Non-Goals

- Infer private motive without evidence.
- Diagnose psychological, medical, or personality traits.
- Treat a single observation as durable intent.
- Claim production readiness from synthetic or partial evidence.
- Replace source review for high-stakes operational decisions.
- Store private transcripts, identities, local paths, or operational logs in the public repository.

## Users

- Assistants that need compact reflective context before responding.
- Human operators reviewing recent activity, state, or project flow.
- Developers building OpenReflect-compatible synthesis capabilities.
- Downstream evaluators checking whether insights remain evidence-backed after summarization.

## Core Concept

Reflection Synthesis Agent is the note-taker for the insight layer. It should make a body of evidence easier to understand without pretending the evidence is stronger than it is.

The output should answer:

- What evidence-backed themes are present?
- Which sources support each theme?
- What remains uncertain?
- What should be checked directly?
- How should this reflection be used, and how should it not be used?

## Inputs And Outputs

Initial inputs:

- insight records
- signal records
- artifact references
- transcript excerpts
- operator notes
- prior reflection summaries

Initial outputs:

- reflection summary
- source reference list
- open questions
- uncertainty notes
- recommended use and non-use guidance

## First Milestone

Create a markdown and JSONL scaffold:

1. PRD and README.
2. Prompt for synthesizing reflection summaries from mixed records.
3. Synthetic fixture with mixed, weak, and contradictory signals.
4. Example reflection summary with source references and open questions.
5. Capability manifest connected to the shared registry.

## Success Criteria

- Summary claims cite source references or carry uncertainty labels.
- Contradictions and missing evidence are preserved instead of hidden.
- The output remains concise enough to fit in an assistant review loop.
- Sensitive interpretations are marked for direct user confirmation.
- The agent abstains from broad narrative when evidence is too thin.

