# Literary releases for Narramorph

`scripts/export_runtime_source.py` creates the non-production, structured editorial artifact used by Narramorph's staged import process. It does not assemble or export the novel.

## Boundary

- Source material is read from immutable Git blobs at the requested commit, not from mutable working-tree files.
- Every canonical manuscript blob is represented only by its path and SHA-256 digest. Manuscript contents are never copied into the artifact.
- Exported context is restricted by `editorial/runtime-release-policy-v1.json` to the structure map, compact voice parameters, philosophy-constraint identifiers, chronology, editorial scene summaries, promise/payoff references, and the approved glossary.
- `approvedExcerptMarkers` is empty. The v1 exporter therefore emits `excerpts: []` and rejects any policy that attempts to approve an unmarked excerpt.
- Ordinary output belongs under git-ignored `build/literary-releases/` and is generated/do-not-edit material. A GitHub literary release may attach a reviewed artifact after its exporter pull request has merged; it is not a product or deployment release.
- Narramorph receives an immutable artifact deliberately. Neither repository fetches the other's default branch during build or runtime, and no exporter writes to Narramorph.

## Commands

Build from an immutable commit (default `HEAD`):

```text
python scripts/export_runtime_source.py --release eternal-return-literary-v1.0.0
```

Validate an artifact and recheck every recorded Git-blob hash when the source repository is available:

```text
python scripts/export_runtime_source.py --validate build/literary-releases/eternal-return-literary-v1.0.0.json
```

The artifact is canonical UTF-8 JSON: NFC strings, lexicographically sorted object keys, compact separators, LF line ending, and exactly one terminal LF. `generatedAt` is the source commit time in UTC and participates in `contentSha256`; no wall-clock or workstation path enters the artifact. Repeating the command for the same release ID and source commit must produce identical bytes.

## Release approval

The exporter does not grant permission by itself. The copyright holder's GitHub release record must identify the immutable source commit, editorial release ID, artifact SHA-256, approved constraint-data scope, allowed Narramorph transformations, target story package, approving identity, and approval date under `INTERACTIVE_USE_PERMISSION.md`.
