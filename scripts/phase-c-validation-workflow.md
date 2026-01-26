# Phase C Validation Workflow

This document describes how to validate Movement Three, Phase C (Dissolution) using the Phase C tooling.

## Inputs

- Phase C draft: `drafts/movement-three/phase-c-dissolution.md`
- Phase B draft: `drafts/movement-three/phase-b-simultaneous-narration.md`
- Convergence draft: `drafts/movement-three/convergence.md`

## Scripts

- Dissolution validator: `scripts/dissolution_validator.py`
- Phase C review script: `scripts/phase_c_review_script.py`

## Quick Start

Run both tools and store JSON outputs alongside other validation logs:

```bash
python scripts/dissolution_validator.py drafts/movement-three/phase-c-dissolution.md --pretty --output scripts/validation-outputs/phase-c-dissolution.json
python scripts/phase_c_review_script.py drafts/movement-three/phase-c-dissolution.md drafts/movement-three/phase-b-simultaneous-narration.md drafts/movement-three/convergence.md --pretty --output scripts/validation-outputs/phase-c-review.json
```

## Dissolution Validator

Purpose: checks internal Phase C constraints (voice balance, pronoun ambiguity, rhymes, phrases, tense instability, word count).

Command:

```bash
python scripts/dissolution_validator.py drafts/movement-three/phase-c-dissolution.md --pretty --output scripts/validation-outputs/phase-c-dissolution.json
```

Key checks:

- Word count 2,500–3,000
- No dominant voice (>40%)
- Pronoun ambiguity score >=70
- "We" emergence >=5 occurrences
- All 15 rhymes present
- All 6 phrases present
- Tense instability (no dominant tense)

## Phase C Review Script

Purpose: checks continuity from Phase B into Phase C and from Phase C into Convergence.

Command:

```bash
python scripts/phase_c_review_script.py drafts/movement-three/phase-c-dissolution.md drafts/movement-three/phase-b-simultaneous-narration.md drafts/movement-three/convergence.md --pretty --output scripts/validation-outputs/phase-c-review.json
```

Key checks:

- Transition continuity (shared vocabulary and continuity markers)
- Phrase carriage from Phase B into Phase C
- Rhyme continuity/escalation
- Theme continuity across Phase B, Phase C, Convergence
- Voice contamination progression

## Outputs

JSON outputs are written to `scripts/validation-outputs/` for archival and comparison.

## Troubleshooting

- Missing file error: ensure the Phase B / Phase C / Convergence paths exist and are correct.
- Validator failures: revise the draft, then re-run the scripts until PASS.
