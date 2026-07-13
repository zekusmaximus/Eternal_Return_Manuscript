# Interactive-edition provenance policy

Status: Active process policy; distribution terms await the Phase 0 owner license decision.

## Separate editions

The consolidation program recognizes three artifacts:

1. the canonical long-form manuscript in this repository;
2. the interactive runtime edition in Narramorph;
3. a reader-specific journey exported by Narramorph.

The artifacts may differ intentionally in order, passage length, second-person framing, unlock structure, choice language, and interactive explanation. They may not silently contradict approved character identity, chronology, causal relationships, philosophical constraints, or ending claims.

## Release requirements

Any future literary release intended for Narramorph must name:

- immutable manuscript commit and release ID;
- approved files/excerpts or machine-readable constraints;
- content owner and distribution permission;
- file/content hashes;
- relevant editorial approvals;
- whether the material is canonical prose, summary, constraint data, or interactive-use excerpt.

Narramorph must record the release ID in its story-package provenance. It must not scrape or fetch this repository's default branch during application build or runtime.

## Prose protection

Creating schemas, exporters, concordance, summaries, reports, or validation output does not authorize changes to canonical prose. Manuscript edits still require an approved roadmap item and explicit operator approval in the session, followed by the verification steps in `CLAUDE.md`.

## Current transfer status

At the pre-consolidation baseline, no new transfer is authorized by this file. Existing related content in Narramorph will be classified during the full concordance and provenance audit.
