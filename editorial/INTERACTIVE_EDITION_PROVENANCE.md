# Interactive-edition provenance policy

Status: Active process policy; distribution terms are defined by the root license files and `INTERACTIVE_USE_PERMISSION.md`.

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

The copyright holder's release-specific grant is defined in `INTERACTIVE_USE_PERMISSION.md`. An approval record must satisfy both that grant and the metadata requirements above before Narramorph may distribute new manuscript-derived material.

## Prose protection

Creating schemas, exporters, concordance, summaries, reports, or validation output does not authorize changes to canonical prose. Manuscript edits still require an approved roadmap item and explicit operator approval in the session, followed by the verification steps in `CLAUDE.md`.

## Current transfer status

At the pre-consolidation baseline, no specific release bundle has yet been approved. Existing related content in Narramorph will be classified during the full concordance and provenance audit. The standing permission defines what a future approval may authorize; it does not itself approve any excerpt.
