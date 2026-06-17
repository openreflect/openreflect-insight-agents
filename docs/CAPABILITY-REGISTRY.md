# Capability Registry

This registry tracks the initial OpenReflect insight-agent surface.

## Active Agents

### Human Telemetry Agent

- Path: `agents/human-telemetry-agent`
- Status: scaffolded
- Purpose: extract user sentiment, functional state, work-context signals, and assistant action guidance from interaction traces.
- Inputs: transcript excerpts, memory snippets, project notes, voice transcripts.
- Outputs: signal records, state narratives, assistant action briefs.
- Privacy: public framework with private downstream calibration.

### Pattern Analyst Agent

- Path: `agents/pattern-analyst-agent`
- Status: scaffolded
- Purpose: detect recurring structures across provenance-bearing records and emit bounded pattern insights with uncertainty.
- Inputs: source records, signal records, insight records, project notes.
- Outputs: insight records, pattern summaries.
- Privacy: public framework with private downstream traces and calibration.

### Decision Trace Agent

- Path: `agents/decision-trace-agent`
- Status: scaffolded
- Purpose: reconstruct decision provenance from evidence-bearing records without inventing missing rationale.
- Inputs: source records, transcript excerpts, project notes, commit summaries, insight records.
- Outputs: insight records, decision traces, revisit triggers.
- Privacy: public framework with private downstream decision logs and operational traces.

### Ambiguity Checker Agent

- Path: `agents/ambiguity-checker-agent`
- Status: scaffolded
- Purpose: detect action-changing ambiguity and recommend clarification, explicit assumptions, abstention, or source verification.
- Inputs: user requests, project notes, source records, signal records, insight records, action briefs.
- Outputs: insight records, ambiguity findings, clarifying questions.
- Privacy: public framework with private downstream policies and deployment thresholds.

## Planned Capability Agents

### Reflection Synthesis Agent

- Purpose: synthesize multiple signal streams into reflective summaries.
- Key risk: overinterpreting weak signals.
- First eval: synthetic week of mixed signals with expected restrained summary.

### Project Pattern Agent

- Purpose: detect repeated project loops, blockers, context jumps, and momentum shifts.
- Key risk: confusing active project focus with stale history.
- First eval: synthetic project timeline with repeated blocker signals.

### Skill Recommender Agent

- Purpose: map observed needs to available skills, MCPs, and workflows.
- Key risk: recommending tools because they exist rather than because evidence supports them.
- First eval: synthetic task set with expected tool recommendations and abstentions.

### Evidence Quality Agent

- Purpose: score whether an insight is source-backed, inferred, speculative, or stale.
- Key risk: false confidence from polished summaries.
- First eval: mixed-source bundle with planted weak claims.

### Recency/Drift Agent

- Purpose: separate present state from historical pattern and detect stale assumptions.
- Key risk: treating prior user state as current.
- First eval: old pain/fatigue mentions mixed with current clear-state transcript.

### Feedback Loop Agent

- Purpose: record whether assistant adaptations helped, missed, or need correction.
- Key risk: self-reinforcing bad adaptations.
- First eval: synthetic action brief followed by user correction.

### Capability Router Agent

- Purpose: choose which insight agent, skill, or MCP should handle a request.
- Key risk: over-routing simple requests.
- First eval: request set with no-op, single-agent, and multi-agent cases.

## MCP / Skill Surface

Planned categories:

- memory source adapters
- transcript ingestion
- signal extraction
- insight synthesis
- action-brief generation
- provenance verification
- privacy audit
- feedback recording

## Registry Rules

- Each capability gets a bounded purpose.
- Each capability gets at least one synthetic fixture.
- Each capability states what it must not infer.
- Every operational script should have a paired prompt file.
- Private calibration belongs downstream, not in this repo.
