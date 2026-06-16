# Adding Capability Agents

This guide describes how to add a new OpenReflect insight capability agent to the public framework.

Capability agents consume provenance-bearing source or signal records and emit bounded insight, signal, or action artifacts. They are not production runtime services in this repository. Treat this repo as the public contract layer: manifests, schemas, prompts, synthetic fixtures, examples, and validation expectations.

## 1. Define Purpose And Boundaries

Start by writing the smallest useful job the agent can do.

Define:

- the evidence the agent is allowed to consume;
- the artifact it should emit;
- the decisions or assistant behavior its output can inform;
- what it must not infer;
- what belongs in private downstream calibration instead of this public repo.

Good capability boundaries are narrow. A recency/drift agent should separate stale history from present state; it should not also perform project planning, human telemetry, and action routing.

Every capability should preserve the framework's core constraints:

- provenance before interpretation;
- uncertainty before overclaiming;
- synthetic examples instead of real transcripts;
- public generic contracts instead of private local paths, profiles, credentials, or logs;
- recency-aware interpretation when historical evidence is involved.

## 2. Create A Capability Manifest

Add a public-safe manifest under `examples/` while the capability is planned or scaffolded. Use `schemas/capability-manifest.schema.json` as the contract.

Required fields:

- `id`: stable machine-readable capability id.
- `name`: human-readable name.
- `status`: one of `planned`, `scaffolded`, `active`, or `deprecated`.
- `purpose`: one-sentence bounded purpose.
- `inputs`: source, signal, or artifact types the agent can consume.
- `outputs`: records or briefs the agent emits.
- `privacy_boundary`: what stays public here and what belongs downstream.
- `evals`: synthetic fixture or validation expectations.

Use `must_not_infer` whenever the capability could overreach. This field is optional in the schema, but it should be present for agents that reason about people, state, intent, identity, safety, privacy, quality, or recommended action.

Validate the manifest:

```bash
python3 scripts/validate_capability_manifest.py examples/<agent-id>.capability.json
```

The validator checks the manifest shape. It does not prove that the capability is safe, useful, or complete.

## 3. Add Schemas And Examples When Needed

Add a schema only when the capability emits a record shape that is not already covered by shared contracts.

Prefer shared schemas first:

- `schemas/source-record.schema.json` for provenance-bearing inputs.
- `schemas/signal-record.schema.json` for bounded observations.
- `schemas/insight-record.schema.json` for synthesized claims.
- `schemas/action-brief.schema.json` for recommended assistant behavior.
- `schemas/feedback-record.schema.json` for correction and outcome tracking.

Capability-specific fields should usually live under an extension field or in a local capability schema. Promote a field to a shared schema only when multiple capabilities need it.

Examples must be public-safe:

- use synthetic people, projects, timestamps, and source references;
- keep evidence excerpts short and generic;
- avoid real chat ids, local filesystem paths, credentials, private profile facts, and operational logs;
- mark uncertainty explicitly when the example depends on interpretation.

## 4. Write Prompts As Contracts

Prompts in this repo should describe repeatable behavior, not private deployment details.

For each capability prompt, define:

- purpose;
- allowed inputs;
- expected output shape;
- provenance requirements;
- uncertainty and abstention rules;
- privacy handling;
- failure cases or "do not" rules.

Pair operational scripts with prompt files when possible. A prompt should make it clear what the agent may infer, what it must cite, and when it should return no finding.

Do not include:

- real user profiles;
- private calibration instructions;
- production credentials;
- local adapter paths;
- claims that a production runtime exists in this repository.

## 5. Add Synthetic Fixtures

Every capability should have at least one synthetic fixture before it is treated as more than an idea.

Fixtures should test the risky part of the capability, not only the happy path. Examples:

- weak evidence that should produce abstention;
- old evidence that should not be treated as current;
- conflicting records with explicit uncertainty;
- private-looking input that should be rejected or redacted;
- clear evidence with expected bounded output.

Keep fixtures small enough to review by hand. Store them near the capability when the fixture is agent-specific, or in a shared fixtures area when it tests a cross-agent contract.

## 6. Define Eval Expectations

Evals should state what a reviewer or validator expects from the agent.

At minimum, document:

- required source or evidence references;
- confidence or uncertainty behavior;
- recency handling;
- privacy tier handling;
- expected abstentions;
- output fields that must be present;
- cases where the agent must not recommend action.

Evaluation can be manual, prompt-based, or script-backed. The public framework should make the expected behavior inspectable even before deterministic validators exist.

## 7. Run Public Safety Checks

Before committing a new capability agent, check that the public repo still contains only generic contracts and synthetic material.

Review for:

- real names, chat ids, message ids, account ids, source paths, or private project paths;
- credentials, tokens, environment values, or secret references;
- real transcripts, private memory excerpts, operational logs, or calibration notes;
- medical, psychological, identity, or intent claims presented as fact;
- examples that imply access to a live production runtime.

Recommended validation:

```bash
python3 scripts/validate_capability_manifest.py examples/<agent-id>.capability.json
```

If available in your environment, also run the public-safe audit referenced by the README.

## Contribution Checklist

Before opening a change, confirm:

- the agent has a bounded purpose and explicit non-goals;
- the capability manifest validates;
- new schemas or examples are synthetic and public-safe;
- prompts include provenance, uncertainty, privacy, and abstention rules;
- fixtures cover at least one risk or failure mode;
- eval expectations are documented;
- the change does not claim this repository provides a production runtime.
