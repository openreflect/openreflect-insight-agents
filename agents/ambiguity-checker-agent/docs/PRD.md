# Ambiguity Checker Agent PRD

Status: Draft
Created: 2026-06-17
Public posture: generic framework first; private policies and deployment-specific risk thresholds stay downstream

## BLUF

Ambiguity Checker Agent scans requests, plans, notes, and insight records for unclear language that could cause wrong action. It emits ambiguity findings with source references, risk, possible interpretations, recommended assumptions, and clarifying questions.

## Problem

LLMs are fluent under uncertainty. They often choose an interpretation and continue, especially when the user expects momentum. That is useful for low-risk tasks but dangerous when ambiguity affects scope, identity, dates, external action, budget, privacy, or irreversible changes.

OpenReflect needs an insight capability that treats ambiguity as a first-class object.

## Goals

- Detect materially ambiguous language in source records and plans.
- Distinguish harmless ambiguity from action-changing ambiguity.
- Identify likely interpretations without choosing one prematurely.
- Recommend either a clarifying question, a safe assumption, or abstention.
- Mark claims that require source-first verification.
- Emit concise findings that downstream assistants can use before acting.

## Non-Goals

- Block every action until all ambiguity is removed.
- Reward excessive questioning.
- Replace user judgment.
- Infer hidden intent from vague language.
- Store private policy thresholds in the public repo.

## Users

- Assistants preparing to execute requests.
- Developers reviewing agent plans and prompts.
- Operators auditing whether a workflow has enough clarity to proceed.

## First Milestone

Create a markdown and JSONL scaffold:

1. PRD and README.
2. Prompt for extracting ambiguity findings.
3. Synthetic fixture with ambiguous request language.
4. Example insight records.
5. Capability manifest.

## Success Criteria

- Findings cite the ambiguous source text or record.
- The agent identifies why the ambiguity matters.
- The agent asks only high-value clarifying questions.
- Low-risk ambiguity gets an explicit assumption rather than unnecessary blocking.
- High-risk ambiguity triggers abstention or verification guidance.

