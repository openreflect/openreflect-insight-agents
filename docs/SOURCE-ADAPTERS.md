# Source Adapter Contract

Source adapters are the boundary between provenance-bearing sources and insight
capabilities.

The architecture flow is:

```text
sources -> adapters -> capability agents -> insight records -> action surfaces
```

Adapters do not produce insights. They read bounded source windows, normalize the
minimum metadata needed for provenance and privacy, and emit records that
capability agents can interpret safely.

This repository defines the public-safe contract only. It does not define a
production memory backend, private transcript store, credential model, or
deployment interface.

## Responsibilities

Every adapter must:

- Read a bounded source window requested by the caller.
- Preserve stable source references without exposing private storage details.
- Distinguish observed time from referenced time when either is known.
- Carry privacy tier metadata forward without weakening it.
- Provide evidence excerpts that are short, necessary, and policy-compliant.
- Support synthetic fixture mode for tests and examples.
- Avoid secret expansion, credential lookup, or private context enrichment.
- Report uncertainty when source metadata is missing, ambiguous, or partial.

## Bounded Source Window

An adapter accepts an explicit source window and must not silently widen it.
Window bounds may be expressed by cursor, item count, timestamp range, artifact
range, or source-native locator.

If a source cannot satisfy the requested window exactly, the adapter should emit
the closest bounded result and include a warning. It must not perform unbounded
search, whole-account export, or opportunistic backfill.

Example input:

```json
{
  "adapter_id": "generic-transcript-adapter",
  "source": {
    "type": "transcript",
    "locator": "source://conversation/example-thread"
  },
  "window": {
    "start_ref": "turn-0100",
    "end_ref": "turn-0125",
    "max_items": 25
  },
  "privacy_floor": "private",
  "synthetic": false,
  "request_purpose": "capability-agent-input"
}
```

## Source References

Source references are provenance pointers, not raw data dumps. They should be
stable enough for a downstream verifier to recover the source under the same
authorization boundary, but generic enough for this public framework.

Recommended fields:

```json
{
  "source_ref": {
    "source_type": "transcript",
    "source_id": "example-thread",
    "item_ref": "turn-0108",
    "span_ref": "chars:120-240",
    "version_ref": "artifact-version-example"
  }
}
```

Adapters must not emit local filesystem paths, private chat identifiers,
credentials, account IDs, or internal operational logs as source references in
public fixtures or committed examples.

## Time Semantics

Adapters should separate:

- `observed_at`: when the source item was observed, recorded, received, or
  created.
- `referenced_at`: the time discussed by the source content, if the content
  clearly references one.

These fields answer different questions. A transcript observed today may
reference an event from last month. A project note written last week may describe
future intent. Capability agents need both to avoid treating historical or
referenced states as current.

If either value is unknown, omit it or set it to `null` and include uncertainty.
Do not infer precise timestamps from vague language.

## Privacy Tiers

Adapters must preserve or raise privacy restrictions. They must not downgrade
privacy.

Public framework tiers:

- `public`: safe to publish in repository examples.
- `synthetic`: generated fixture data that resembles structure but not real
  source content.
- `private`: user, organization, or project data that should stay downstream.
- `restricted`: sensitive data requiring stricter handling than normal private
  content.

Adapter output privacy is the maximum of the request privacy floor, source
privacy, excerpt privacy, and any adapter-specific policy.

## Evidence Excerpts

Evidence excerpts are optional, minimal snippets that help capability agents
reason without receiving an entire source object.

Excerpt policy:

- Include only what is needed for the requested capability.
- Keep excerpts short and bounded.
- Prefer redacted or synthetic text for public fixtures.
- Preserve enough context to avoid misleading fragments.
- Attach every excerpt to a source reference.
- Mark omissions, redactions, or transformations.

Adapters must not use excerpts to smuggle full transcripts, complete documents,
credentials, private identifiers, or unrelated context.

## Synthetic Fixture Mode

Each adapter should support a synthetic mode for tests and public examples. In
synthetic mode, the adapter emits structurally realistic records with invented
content and stable fixture references.

Synthetic mode must:

- Use `privacy: "synthetic"`.
- Avoid real transcripts, real people, real chat IDs, real local paths, and
  operational logs.
- Make fixture generation deterministic when possible.
- Preserve the same shape as non-synthetic adapter output.
- Label generated content so downstream tests do not confuse it with observed
  source material.

## Generic Output Shape

Adapter output is a source packet: a bounded set of source items plus provenance,
time, privacy, and warnings.

```json
{
  "adapter_id": "generic-transcript-adapter",
  "adapter_version": "0.1.0",
  "source_packet_id": "source-packet-example-001",
  "source_window": {
    "source_type": "transcript",
    "locator": "source://conversation/example-thread",
    "start_ref": "turn-0100",
    "end_ref": "turn-0125",
    "item_count": 2,
    "bounded": true
  },
  "privacy": "private",
  "items": [
    {
      "source_ref": {
        "source_type": "transcript",
        "source_id": "example-thread",
        "item_ref": "turn-0108",
        "span_ref": "chars:120-240"
      },
      "observed_at": "2026-01-15T10:20:00Z",
      "referenced_at": null,
      "privacy": "private",
      "excerpt": {
        "text": "Synthetic-style placeholder excerpt for capability evaluation.",
        "policy": "minimal",
        "redactions": []
      },
      "metadata": {
        "content_type": "text/plain",
        "source_role": "human-authored"
      }
    }
  ],
  "warnings": [
    {
      "code": "referenced_time_unknown",
      "message": "No explicit referenced time was present in the bounded window."
    }
  ]
}
```

Capability agents consume source packets and may produce insight records with
`evidence_refs` pointing back to adapter `source_ref` values. Action surfaces
consume insight records; they should not call private sources directly.

## What Adapters Must Not Do

Adapters must not:

- Produce claims, diagnoses, recommendations, or action briefs.
- Treat source access as permission to expose private content.
- Expand secrets, credentials, tokens, or hidden environment values.
- Follow links into unrelated private systems unless explicitly requested by the
  bounded source window and allowed by policy.
- Perform unbounded account, workspace, repository, or transcript scans.
- Downgrade privacy tiers to satisfy a caller.
- Replace source references with unverifiable summaries.
- Invent timestamps, authorship, confidence, or provenance.
- Store or commit real private source content in this public repository.
- Claim production readiness for this framework.

## Contract Boundary

Adapters are allowed to normalize, redact, filter, and point. They are not
allowed to interpret beyond the minimum needed to preserve source semantics.

Interpretation belongs in capability agents. Durable claims belong in insight
records. Delivery and user-facing behavior belong in action surfaces.
