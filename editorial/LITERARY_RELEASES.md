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

## Reproducible vertical slice

`scripts/export_vertical_slice.py` proves a reviewed runtime selection without copying or editing prose. The checked-in selection `editorial/vertical-slices/archaeologist-opening-accept.json` identifies the existing `arch-L1` → `arch-L2-accept` edge by Story Package passage IDs and selects only released chapter/scene-summary, voice, chronology, philosophy, theme-claim, and promise/payoff context. Its rationale favors the product start path with complete metadata and existing desktop/mobile keyboard coverage.

Build the new full literary release and the slice artifact together from the same immutable commit:

```text
python scripts/export_vertical_slice.py --slice archaeologist-opening-accept --release-id eternal-return-literary-v1.0.1
```

Validate both canonical artifacts and recheck the release, selection, and schema Git-blob hashes:

```text
python scripts/export_vertical_slice.py --validate build/literary-releases/eternal-return-literary-slice-archaeologist-opening-accept-v1.0.0.json --base-release build/literary-releases/eternal-return-literary-v1.0.1.json
```

The slice context records must be exact object subsets of the base release. Its two ordered runtime targets must be connected L1→L2 passages, every mapping reference must resolve within the selected canonical context, and output remains under ignored `build/literary-releases/`. A release record may attach both reviewed files after the exporter PR merges; Narramorph then deliberately transfers and independently validates both hashes.

## Release approval

The exporter does not grant permission by itself. The copyright holder's GitHub release record must identify the immutable source commit, editorial release ID, artifact SHA-256, approved constraint-data scope, allowed Narramorph transformations, target story package, approving identity, and approval date under `INTERACTIVE_USE_PERMISSION.md`.
