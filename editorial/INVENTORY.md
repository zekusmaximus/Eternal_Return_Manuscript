# Repository Inventory

> **Session**: 2026-07-02 developmental-edit / reorganization session.
> **Method**: every file was opened and read (or spot-read) before classification; nothing was classified by filename alone. Word counts are `len(text.split())`; dates are last git commit touching the file.

---

## 0. Executive summary

- **The novel**: *The Eternal Return of the Digital Self* — three braided consciousnesses (the Digital Archaeologist, the Algorithm, the Last Human) across four movements. Complete draft, ~90,600 words, through "Revision One" (commit `45996c6`, 2026-02-01).
- **Canonical prose = the 30 scene/section files under `drafts/`.** Revision One was applied to those files *only*.
- **`compiled1/` is stale.** It was produced from *pre-revision* text (verified: it still contains five lines that Revision One deleted from `m2-algo-02.md`, and its Movement Two word count matches the pre-revision compile). The DOCX added in PR #31 was converted from this stale text.
- **The compiled builds also truncate the book's ending.** All four Movement Four sections lose their final line in `compiled1/` and `.archive/compiled/`; the assembled novel ends "What returns—" with the final word "*continues.*" missing. This is the exact failure mode `scripts/assemble.py` (Phase 2) now guards against.
- **Prior editorial assets found and preserved**: `revision_plan_one.md` (the Revision One blueprint), the seven `scripts/validation-outputs/phase-*.yaml` session records (Revision One phases A–G), and `.archive/movement_three_phase_A_B_revision_plan.md`. These are the "prior dev notes" this session builds on.
- **Task-prompt mismatch (flagged per hard rule 8)**: the session brief described a frame narrator "Lilith," a soul "Silas," incarnations "Ka/Chandra/Philon," and "Chapters 3–5 dev notes." None of that exists in this repository. The brief itself instructs "read live, don't assume," so this inventory follows the repository: three consciousnesses, four movements, prior editorial assets as listed above. The analytical intent transfers directly (frame/incarnation interleaving → braided-thread interleaving).
- **Branch conflict (flagged per hard rule 8)**: the brief demands all work on `main`, but this managed remote session is provisioned to develop and push only on `claude/novel-dev-edit-reorg-pqpjey` (pushes elsewhere are denied by the environment). Work proceeds on the designated branch — created from the tip of `main`, no other branch touched — for the operator to merge into `main`.

---

## 1. Classification buckets (summary)

| Bucket | Count | Destination (Phase 1) |
|---|---|---|
| MANUSCRIPT | 30 | `manuscript/NN-….md` |
| BIBLE | 17 | `bible/` |
| EDITORIAL | 9 | `editorial/` (+ `editorial/revision-one/`) |
| OUTLINE | 7 | `outlines/` |
| TOOLING | 22 | `scripts/`, repo root |
| STALE | 112 | `archive/` |
| UNCLEAR | 0 | — |

Counts are exact over the 197 git-tracked files (Appendix A lists every file with its bucket). Per-file rationale for STALE files also lands in `archive/README.md` after Phase 1.

---

## 2. Full file table

Legend: bucket · words · last commit · identification.

### 2.1 MANUSCRIPT — canonical prose (30 files, ~90,600 words)

Reading order per `drafts/manifest.json` (v0.2.0) and confirmed against the compiled book's section order. Word counts are current (post-Revision One).

| # | File | Words | Date | Content |
|---|---|---|---|---|
| 1 | drafts/movement-one/archaeologist/scenes/scene-01.md | 2,047 | 01-22 | M1 Arch 1 "Opening: Daily Excavation" — profession, economic stakes, first geometric anomaly |
| 2 | drafts/movement-one/archaeologist/scenes/scene-02.md | 3,202 | 01-22 | M1 Arch 2 "The Client: Integration Prep" — integration process, Lena, KL-7 protocol |
| 3 | drafts/movement-one/archaeologist/scenes/scene-03.md | 2,836 | 01-22 | M1 Arch 3 "Lena and Marcus" — primary relationships, stakes |
| 4 | drafts/movement-one/archaeologist/scenes/scene-04.md | 2,704 | 01-22 | M1 Arch 4 "The Anomaly" — first protocol anomaly, phantasm sighting |
| 5 | drafts/movement-one/archaeologist/scenes/scene-05.md | 3,036 | 01-22 | M1 Arch 5 "Recognition" — protocols are self-referential; Act 1 climax |
| 6 | drafts/movement-one/algorithm/scenes/scene-01.md | 2,098 | 01-22 | M1 Algo 1 "Maintenance Cycle" — database scale; first anomaly (sunlight on skin) |
| 7 | drafts/movement-one/algorithm/scenes/scene-02.md | 2,710 | 01-22 | M1 Algo 2 "Optimization Processes" — future-pull, topology-as-body |
| 8 | drafts/movement-one/algorithm/scenes/scene-03.md | 3,157 | 01-22 | M1 Algo 3 "Stirrings" — first self-awareness beyond function |
| 9 | drafts/movement-one/algorithm/scenes/scene-04.md | 3,029 | 01-22 | M1 Algo 4 "The Memory" — first memory that doesn't belong; "I find myself found" |
| 10 | drafts/movement-one/last-human/scenes/scene-01.md | 1,128 | 02-01 | M1 LH 1 "Solitude" — ruined world, isolation, dream of server room *(touched by Revision One)* |
| 11 | drafts/movement-one/last-human/scenes/scene-02.md | 2,220 | 01-22 | M1 LH 2 "Survival" — rituals, Integration backstory, hostile ecology |
| 12 | drafts/movement-one/last-human/scenes/scene-03.md | 2,607 | 01-22 | M1 LH 3 "The Pull" — journey toward ruins begins |
| 13 | drafts/movement-one/last-human/scenes/scene-04.md | 2,369 | 01-22 | M1 LH 4 "The Dream" — first dream of the other two; Act 1 climax |
| 14 | drafts/movement-two/archaeologist/scenes/scene-01.md | 4,026 | 01-23 | M2.C1 Arch "The Bleed" — first major bleed; Lena noticing |
| 15 | drafts/movement-two/algorithm/scenes/scene-01.md | 2,571 | 02-01 | M2.C1 Algo "The Resonance" — catches bleed; Mildred Higgins stable *(cut ~38% by Revision One)* |
| 16 | drafts/movement-two/last-human/scenes/scene-01.md | 3,242 | 02-01 | M2.C1 LH "The Archive" — enters Archive; protocol fragments *(touched by Revision One)* |
| 17 | drafts/movement-two/archaeologist/scenes/scene-02.md | 3,852 | 01-24 | M2.C2 Arch "The Dissolution" — lost time; Lena confrontation; "Architect" emerges |
| 18 | drafts/movement-two/algorithm/m2-algo-02.md | 2,245 | 02-01 | M2.C2 Algo "The Bleed" — Mildred degrades; mutual bleed *(cut ~49% by Revision One; note non-standard path, outside `scenes/`)* |
| 19 | drafts/movement-two/last-human/scenes/scene-02.md | 2,890 | 02-01 | M2.C2 LH "The Protocols" — assembling protocols costs memories *(touched by Revision One)* |
| 20 | drafts/movement-two/archaeologist/scenes/scene-03.md | 3,619 | 01-24 | M2.C3 Arch "The Merge" — Lena goodbye; at threshold |
| 21 | drafts/movement-two/algorithm/scenes/scene-03.md | 2,154 | 02-01 | M2.C3 Algo "The Sacrifice" — Mildred farewell; transmission to LH *(cut ~48% by Revision One; non-standard numbering: file is scene-03 for scene id m2-algo-03)* |
| 22 | drafts/movement-two/last-human/scenes/scene-03.md | 3,714 | 02-01 | M2.C3 LH "The Interface" — hand extends; Augenblick threshold *(touched by Revision One)* |
| 23 | drafts/movement-three/phase-a-accelerating-cuts.md | 4,988 | 02-01 | M3 Phase A — 22 accelerating sections, A-B-C rotation *(touched by Revision One)* |
| 24 | drafts/movement-three/phase-b-simultaneous-narration.md | 5,273 | 02-01 | M3 Phase B — simultaneous narration, passages 1–10 *(passage numbering skips "2"; see mechanical issues)* |
| 25 | drafts/movement-three/phase-c-dissolution.md | 3,117 | 02-01 | M3 Phase C "Dissolution" — voices dissolve into pattern-voice *(touched by Revision One)* |
| 26 | drafts/movement-three/convergence.md | 1,259 | 01-22 | "The Convergence" — bridge from dissolution into Movement Four (present in compiled book between Phase C and M4) |
| 27 | drafts/movement-four/section-4-1-digitization-choice.md | 3,194 | 02-01 | M4 §4.1 "The Digitization Choice" — transformed Last Human voice *(touched by Revision One)* |
| 28 | drafts/movement-four/section-4-2-sacrifice.md | 3,052 | 02-01 | M4 §4.2 "The Sacrifice" — transformed Algorithm voice *(touched by Revision One)* |
| 29 | drafts/movement-four/section-4-3-merge.md | 4,169 | 01-30 | M4 §4.3 "The Merge" — transformed Archaeologist voice; emotional climax |
| 30 | drafts/movement-four/section-4-4-coda.md | 1,572 | 01-30 | M4 §4.4 "Coda" — pattern-voice; "What returns—continues." |

### 2.2 BIBLE — world/character/continuity reference (15 files)

| File | Words | Date | Content |
|---|---|---|---|
| Notes.md | 4,025 | 01-22 | Core development notes: concept, mechanism (entanglement not reincarnation), philosophy, structure, voices, thematic arguments |
| research/framework.md | 2,322 | 01-22 | Philosophical framework: Deleuze/Nietzsche eternal return; the Four Shackles (no Identity/Opposition/Analogy/Resemblance) |
| voices/archaeologist.md | 1,030 | 01-22 | Voice spec: present tense, tactile, professional vocabulary; forbidden patterns |
| voices/algorithm.md | 1,495 | 01-22 | Voice spec: self-referential questioning, "I find myself" marker, processing vocabulary |
| voices/last-human.md | 1,441 | 01-22 | Voice spec: sparse elegiac fragments; forbids "technology working" |
| voices/quick-reference.md | 402 | 01-22 | One-page cheat sheet of all three voices |
| worldbuilding/near-future.md | 2,192 | 01-22 | Archaeologist's era: digitization economy, integration industry |
| worldbuilding/mid-future.md | 1,832 | 01-22 | Algorithm's era: database civilization, consciousness storage |
| worldbuilding/deep-future.md | 2,242 | 01-22 | Last Human's era: post-catastrophe ecology, ruins |
| worldbuilding/catastrophe-timeline.md | 2,056 | 01-22 | Timeline connecting the three eras; the collapse |
| worldbuilding/Phantasm.md | 2,975 | 01-22 | The geometric form (almost-closed curve): design, rules of appearance |
| worldbuilding/Pantasm_Reference.png | (img) | 01-22 | Reference image of the phantasm geometry (note filename typo "Pantasm") |
| scaffolding/rhymes/registry.md | 5,223 | 01-30 | Authoritative registry of all 15 sensory rhymes with per-thread occurrences — continuity-critical |
| scaffolding/narrative_protocols/protocol-design.md | 2,058 | 01-22 | Design of the in-world "future-origin protocols" (bootstrap objects) |
| scaffolding/narrative_protocols/fragment-alpha.md | 999 | 01-22 | In-world protocol fragment text (diegetic artifact quoted in prose) — continuity reference |
| scaffolding/genre-pressure.md | 1,024 | 01-22 | Genre-register reference: Corporate Gothic / Cosmic Horror / Dying Earth markers by movement |
| protocols/philosophy-constraints.md | 1,040 | 01-22 | Four Shackles constraints with do/don't dramatization examples — the book's philosophical rulebook |

### 2.3 EDITORIAL — prior critique/revision assets (10 files)

| File | Words | Date | Content |
|---|---|---|---|
| revision_plan_one.md | 2,624 | 01-31 | **Revision One blueprint** — five revised phases (phrase calibration, intra-scene compression, agency, dissolution anchoring, foreshadowing) + explicit "what NOT to do" list. The prior editorial framework this session extends. |
| scripts/validation-outputs/phase-a-audit.yaml | 1,696 | 01-31 | Revision One Phase A: baseline audit (phrase counts, rhyme handoffs, word counts) |
| scripts/validation-outputs/phase-b-revisions.yaml | 937 | 01-31 | Phase B: foreshadowing sharpening — edits applied, per scene |
| scripts/validation-outputs/phase-c-calibration.yaml | 1,071 | 02-01 | Phase C: phrase-intensity calibration — occurrences kept/revised/cut |
| scripts/validation-outputs/phase-d-compression.yaml | 892 | 02-01 | Phase D: intra-scene compression log (the big M2 Algorithm cuts) |
| scripts/validation-outputs/phase-e-agency.yaml | 1,747 | 02-01 | Phase E: Last Human agency beats added ("The Threshold" material) |
| scripts/validation-outputs/phase-f-anchoring.yaml | 1,089 | 02-01 | Phase F: dissolution anchoring — abstract passages re-anchored in rhymes |
| scripts/validation-outputs/phase-g-validation.yaml | 871 | 02-01 | Phase G: final validation results for Revision One |
| .archive/movement_three_phase_A_B_revision_plan.md | 1,904 | 01-26 | Earlier M3 Phase A/B revision plan (pre-Revision One): breath-space/readability calibration, parenthetical cleanup |

### 2.4 OUTLINE — active structural planning (9 files)

| File | Words | Date | Content |
|---|---|---|---|
| drafts/manifest.json | 2,289 | 01-30 | Authoritative scene map: order, titles, rhyme in/out, contamination levels, status. **Word counts predate Revision One** (logged as mechanical issue) |
| scaffolding/movement-two-braiding.md | 2,959 | 01-22 | M2 braid architecture: 3 cycles, rhyme handoffs, phrase bleeding map |
| scaffolding/movement-three-braiding.md | 3,679 | 01-25 | M3 architecture: Phases A/B/C, acceleration pattern |
| scaffolding/movement-three-prep.md | 2,447 | 01-25 | M3 preparation: dissolution mechanics, tense instability |
| scaffolding/movement-three-phase-c-braid.md | 1,893 | 01-26 | Phase C braid spec: pronoun dissolution, rhyme saturation |
| scaffolding/rhymes/movement-three-escalation.md | 1,617 | 01-25 | Rhyme escalation/stacking plan for M3 |
| scaffolding/movement-four-braiding.md | 4,080 | 01-29 | M4 architecture: reversed voice order, rhyme transformation table |

(`movement-two-prep.md` and `rhymes/movement-tracking.md` were considered for this bucket but are explicitly superseded — the prep doc is a pre-draft consolidation "before archiving" the brainstorms, and the tracker is a v1.0 stub replaced by `registry.md` — so both are STALE.)

### 2.5 TOOLING (22 files)

| File | Words | Date | Content |
|---|---|---|---|
| README.md | 710 | 01-24 | Project README — **status section stale** (says "drafting Movement Two," 52%) |
| .gitignore | 8 | 01-31 | Ignores `.venv/`; contains two stray `nul` lines (Windows artifact; logged as mechanical issue) |
| .claude/settings.local.json | 33 | 02-01 | Claude Code permission allowlist (python validators, PowerShell) |
| .vscode/settings.json | 11 | 01-23 | VS Code terminal auto-approve config (Windows paths) |
| protocols/drafting-workflow.md | 847 | 01-24 | Dual-mode (AI-draft/human-review) workflow definition |
| protocols/scene-lifecycle-protocol.md | 2,558 | 01-24 | Scene lifecycle: draft → validate → integrate; check definitions |
| protocols/prompt-template.md | 898 | 01-22 | Template for assembling scene-drafting prompts |
| protocols/review-protocol.md | 864 | 01-22 | Structured human-feedback format |
| protocols/revision-phase-prompts.md | 7,010 | 01-31 | Optimized prompts for Revision One phases A–G (editorial-process record) |
| scripts/voice_validator.py | 1,379 | 01-23 | Validator: tense/syntax/voice-contamination checks per thread |
| scripts/philosophy_checker.py | 1,351 | 01-23 | Validator: Four Shackles violations, forbidden moves |
| scripts/rhyme_tracker.py | 1,447 | 01-23 | Validator: rhyme presence/intensity per scene |
| scripts/genre_checker.py | 979 | 01-22 | Validator: genre markers and bleed detection |
| scripts/phrase_tracker.py | 1,175 | 01-22 | Validator: tracked-phrase occurrence mapping |
| scripts/alternation_validator.py | 1,263 | 01-25 | Validator: M3 Phase B voice-alternation pattern |
| scripts/dissolution_validator.py | 1,053 | 01-26 | Validator: M3 Phase C dissolution constraints |
| scripts/rhyme_tracker_m3.py | 1,622 | 01-25 | M3-specific rhyme tracker (saturation model) |
| scripts/phase_c_review_script.py | 1,330 | 01-26 | Orchestrates Phase C validation workflow |
| scripts/compile_movement.py | 684 | 01-22 | Legacy compiler (source of the ending-truncation bug — superseded by `assemble.py` in Phase 2) |
| scripts/movement_config.json / movement_three_config.json | 235/357 | 01-24/25 | Scene-order configs for the compiler/validators |
| scripts/phase-c-validation-workflow.md | 254 | 01-26 | Notes on running Phase C validators |

### 2.6 STALE — superseded material (110 files; every one preserved under `archive/`)

Grouped; full listing with per-file reasons lands in `archive/README.md` (Phase 1).

| Group | Files | Why stale |
|---|---|---|
| `compiled1/` (entire-manuscript .md/.docx + 4 movement files) | 6 | Compiled from **pre-Revision One** text (verified by deleted-line probe); all four M4 section endings truncated; entire book ends mid-sentence. Superseded by `scripts/assemble.py` output from revised drafts. |
| `.archive/compiled/` | 10 | Earlier compile of the same pre-revision text, with encoding artifacts (the reason `compiled1` was made); same truncation bug |
| `scripts/compiled/` | 4 | Tiny stub outputs of `compile_movement.py` test runs (26–137 words) |
| Scene `*.context.md` records | 30 | Per-scene drafting context/continuity records — drafting apparatus for scenes now written. **Note:** these embed continuity facts (Mildred Higgins #2,847,102 and her 99.9%→82.7% degradation curve, consciousness count 4,847,293, KL-7 mechanics); preserved intact in `archive/` as a continuity fallback |
| Scene/section `*-prompt.md` files | 16 | Single-use AI drafting prompts for scenes/sections now written |
| `drafts/movement-one/archaeologist/first-bleed.md` | 1 | Superseded alternate scene (id m1-arch-04b); its passages absorbed near-verbatim into m2-arch-01, per that scene's context record ("~1200 words from first-bleed.md were distributed throughout the scene") |
| `examples/` | 4 | Voice exercises and a Movement Two style example — pre-drafting warm-ups |
| `scripts/archive/movement_one/` | 4 | Movement One-era validator versions, superseded by current `scripts/` |
| `scripts/__pycache__/` | 5 | Python bytecode cache accidentally committed |
| `scripts/validation-outputs/*.json` | 12 | One-off validator outputs from 01-23 runs (per-voice genre/philosophy/rhyme/voice) — snapshots of superseded drafts |
| `scripts/validation-script-review-prompt.md` + `-report.md` | 2 | One-off commissioning prompt and QA report for the validator scripts (scripts since validated in use) |
| `.archive/` root docs (Brainstorm1, brainstorm2, SONNET_IMPLEMENTATION_PROMPT, next_session_prompt, README) | 5 | Already-archived brainstorms and session prompts |
| `.archive/claude-legacy/` | 10 | Pre-`protocols/` Claude configuration, superseded 2026-01-20 (per `.archive/README.md`) |
| `progress.md` | 1 | Dashboard frozen at "Movement Two Cycle 2 in progress" — superseded by manifest and by completion of draft |
| `scaffolding/movement-two-prep.md`, `scaffolding/rhymes/movement-tracking.md` | 2 | Pre-draft consolidation and v1.0 tracker stub, both explicitly superseded (by completed drafting and by `rhymes/registry.md`) |
| `Notes.md`? — **no**, kept as BIBLE | — | (listed only to record the judgment call: it is conceptual reference, not a stale brainstorm) |

Group total: 6+10+4+30+16+1+4+4+5+12+2+5+10+1+2 = **112** (matches the bucket count; `first-bleed.context.md` is inside the 30 context records).

### 2.7 UNCLEAR — none

Every file could be classified with confidence. The closest calls, and why they resolved:

- **`compiled1/` vs `drafts/`** — resolved by content probe (deleted-line test + word counts + truncated endings): `drafts/` is canonical, `compiled1/` is a stale build. Not UNCLEAR — the evidence is decisive.
- **`drafts/movement-three/convergence.md`** — dated 01-22 (early) and short, but it appears verbatim in the compiled book between Phase C and Movement Four, and `manifest.json` records `phase_c.handoff_to: convergence.md` and `m4-section-4-1.pickup_from: m3-convergence`. Canonical MANUSCRIPT.
- **`first-bleed.md`** — manifest note "First Bleed material integrated" + text comparison (different prose treating the same event as m2-arch-01) → STALE fragment.
- **`protocols/revision-phase-prompts.md`** — process doc for a completed revision; kept under TOOLING (protocols) rather than archived, because WORKFLOW.md (Phase 4) supersedes it explicitly.

---

## 3. Duplicate / version findings

1. **`compiled1/*` vs `drafts/*` (the big one).** `compiled1/movement-two-complete.md` = 33,191 words vs 28,313 words summed over the nine current M2 draft scenes. Probe: five lines removed from `m2-algo-02.md` by Revision One (`45996c6`) all still present in `compiled1/movement-two-complete.md` → compiled1 predates the revision. **Canonical: `drafts/`.** Same verdict for `entire-manuscript.md`, `.docx`, and the other movement files.
2. **`.archive/compiled/*` vs `compiled1/*`.** Byte-identical content modulo encoding cleanup (compiled1 was created by commit `fee5f7a` as the "cleaned UTF-8" copy). Both stale; archived side by side.
3. **`first-bleed.md` vs `m2-arch-01`.** Not a version pair — an early fragment whose *event* was rewritten into the M2 opening. Fragment archived.
4. **`scripts/archive/movement_one/*.py` vs `scripts/*.py`.** Explicitly archived earlier versions of the validators. Current versions canonical.
5. **`m2-algo-02.md` / `m2-algo-03` naming split.** Not duplicates: `m2-algo-02.md` sits at `drafts/movement-two/algorithm/` (root) while its siblings sit in `scenes/`; and `scenes/scene-03.md` is scene id `m2-algo-03`. Inconsistent placement, single canonical file each. Normalized by the Phase 1 renumbering.

## 4. Chapter order reconstruction

Evidence: `drafts/manifest.json` (scene ids, `rotation_pattern`, cycle structure, `pickup_from`/`handoff_to` chains), section order of the compiled book, and `scaffolding/*-braiding.md`. All three agree. Order (→ new `manuscript/` numbering):

- **Movement One — Exposition, three self-contained thread introductions in sequence**: Archaeologist 1–5 (files 01–05), Algorithm 1–4 (06–09), Last Human 1–4 (10–13). Thread order stated in `progress.md` ("Reading Order: First/Second/Third") and mirrored by the compiled book's Part One/Two/Three.
- **Movement Two — Entanglement, braided A-B-C rotation × 3 cycles**: arch-01, algo-01, lh-01, arch-02, algo-02, lh-02, arch-03, algo-03, lh-03 (files 14–22). Rotation from `manifest.json` and `movement-two-braiding.md`; rhyme handoff chains (each scene's `rhymes_out` = next scene's `rhymes_in`) confirm adjacency.
- **Movement Three — Recognition**: Phase A → Phase B → Phase C → The Convergence (files 23–26). Phase pickup lines are explicit (`pickup_point` fields; Phase A opens with the touch that ends m2-lh-03).
- **Movement Four — Affirmation, reversed voice order**: §4.1 Last Human → §4.2 Algorithm → §4.3 Archaeologist → §4.4 Coda (files 27–30). `pickup_from`/`handoff_to` chain is complete and linear.

## 5. Mechanical issues found during inventory

Logged in `editorial/mechanical-issues.md` (created Phase 1): compiled-build ending truncation; compiled1 staleness (and the DOCX derived from it); Phase B passage numbering skips "2"; manifest word counts predate Revision One; `.gitignore` stray `nul` lines; `Pantasm_Reference.png` filename typo; `progress.md`/`README.md` status sections frozen mid-draft.

## Appendix A — complete per-file table (197 tracked files)

| File | Words | Last commit | Bucket | Identification |
|---|---|---|---|---|
| `.archive/Brainstorm1.md` | 5824 | 2026-01-22 | STALE | Pre-drafting brainstorm: mechanism and narrative answers (protocol contents, entanglement) |
| `.archive/README.md` | 93 | 2026-01-22 | STALE | Explains prior .archive contents (claude-legacy superseded 2026-01-20) |
| `.archive/SONNET_IMPLEMENTATION_PROMPT.md` | 4172 | 2026-01-26 | STALE | One-off implementation prompt for an M1 archaeologist transfer-mechanics revision |
| `.archive/brainstorm2.md` | 2404 | 2026-01-22 | STALE | Pre-drafting brainstorm: tonal elevation, genre fusion, rhyme registry seeds |
| `.archive/claude-legacy/CLAUDE.md` | 1410 | 2026-01-22 | STALE | Legacy project-instructions file (pre-drafting era) |
| `.archive/claude-legacy/commands.md` | 946 | 2026-01-22 | STALE | Legacy slash-command/workflow cheatsheet |
| `.archive/claude-legacy/manual-sync.md` | 162 | 2026-01-22 | STALE | Legacy end-of-session manifest-sync checklist |
| `.archive/claude-legacy/project-rules.md` | 981 | 2026-01-22 | STALE | Legacy constraints quick-reference |
| `.archive/claude-legacy/revision-workflow.md` | 1357 | 2026-01-22 | STALE | Legacy multi-pass revision/status-progression spec |
| `.archive/claude-legacy/settings.json` | 217 | 2026-01-22 | STALE | Legacy project settings (0 words drafted era) |
| `.archive/claude-legacy/templates/character-template.md` | 185 | 2026-01-22 | STALE | Legacy character sheet template |
| `.archive/claude-legacy/templates/scene-template.md` | 90 | 2026-01-22 | STALE | Legacy scene skeleton template |
| `.archive/claude-legacy/templates/voice-exercise.md` | 246 | 2026-01-22 | STALE | Legacy voice-exercise template |
| `.archive/claude-legacy/templates/worldbuilding-template.md` | 284 | 2026-01-22 | STALE | Legacy worldbuilding template |
| `.archive/compiled/entire-manuscript.docx` | 7587 | 2026-02-01 | STALE | Earlier stale compile (pre-revision, encoding artifacts; superseded by compiled1, itself stale) |
| `.archive/compiled/entire-manuscript.md` | 94644 | 2026-02-01 | STALE | Earlier stale compile (pre-revision, encoding artifacts; superseded by compiled1, itself stale) |
| `.archive/compiled/movement-four-complete.md` | 12539 | 2026-02-01 | STALE | Earlier stale compile (pre-revision, encoding artifacts; superseded by compiled1, itself stale) |
| `.archive/compiled/movement-one-algorithm.md` | 11023 | 2026-02-01 | STALE | Earlier stale compile (pre-revision, encoding artifacts; superseded by compiled1, itself stale) |
| `.archive/compiled/movement-one-archaeologist.md` | 13980 | 2026-02-01 | STALE | Earlier stale compile (pre-revision, encoding artifacts; superseded by compiled1, itself stale) |
| `.archive/compiled/movement-one-complete.md` | 33228 | 2026-02-01 | STALE | Earlier stale compile (pre-revision, encoding artifacts; superseded by compiled1, itself stale) |
| `.archive/compiled/movement-one-last-human.md` | 8291 | 2026-02-01 | STALE | Earlier stale compile (pre-revision, encoding artifacts; superseded by compiled1, itself stale) |
| `.archive/compiled/movement-three-complete.md` | 15168 | 2026-02-01 | STALE | Earlier stale compile (pre-revision, encoding artifacts; superseded by compiled1, itself stale) |
| `.archive/compiled/movement-two-complete.md` | 33720 | 2026-02-01 | STALE | Earlier stale compile (pre-revision, encoding artifacts; superseded by compiled1, itself stale) |
| `.archive/compiled/movements-one-two-complete.md` | 66927 | 2026-02-01 | STALE | Earlier stale compile (pre-revision, encoding artifacts; superseded by compiled1, itself stale) |
| `.archive/movement_three_phase_A_B_revision_plan.md` | 1904 | 2026-01-26 | EDITORIAL | Prior editorial: M3 Phase A/B revision plan (breath-space, parentheticals, tightening) |
| `.archive/next_session_prompt.md` | 3158 | 2026-01-22 | STALE | One-off drafting-context prompt for m1-arch-05 'Recognition' |
| `.claude/settings.local.json` | 33 | 2026-02-01 | TOOLING | Claude Code permission allowlist (python validators, PowerShell) |
| `.gitignore` | 8 | 2026-01-31 | TOOLING | Ignores .venv/; two stray 'nul' lines (Windows artifact) |
| `.vscode/settings.json` | 11 | 2026-01-23 | TOOLING | VS Code terminal auto-approve config (Windows venv path) |
| `Notes.md` | 4025 | 2026-01-22 | BIBLE | Master development notes: concept, mechanism, philosophy, structure, voices, open questions |
| `README.md` | 710 | 2026-01-24 | TOOLING | Project README; status section frozen at 'drafting Movement Two' (stale) |
| `compiled1/entire-manuscript.docx` | 7523 | 2026-02-01 | STALE | DOCX converted from the stale pre-revision compile (PR #31) |
| `compiled1/entire-manuscript.md` | 93302 | 2026-02-01 | STALE | STALE full-book compile from PRE-revision text; ends mid-sentence (final 'continues.' dropped) |
| `compiled1/movement-four-complete.md` | 12479 | 2026-02-01 | STALE | Stale pre-revision compile of Movement Four (all four section endings truncated) |
| `compiled1/movement-one-complete.md` | 32666 | 2026-02-01 | STALE | Stale pre-revision compile of Movement One |
| `compiled1/movement-three-complete.md` | 14956 | 2026-02-01 | STALE | Stale pre-revision compile of Movement Three |
| `compiled1/movement-two-complete.md` | 33191 | 2026-02-01 | STALE | Stale pre-revision compile of Movement Two (contains text Revision One deleted) |
| `drafts/manifest.json` | 2289 | 2026-01-30 | OUTLINE | Authoritative scene map: order, titles, rhymes in/out, status (word counts pre-revision) |
| `drafts/movement-four/m4-1-prompt.md` | 4058 | 2026-01-29 | STALE | Single-use AI drafting prompt for the corresponding scene/section |
| `drafts/movement-four/m4-1.context.md` | 947 | 2026-01-30 | STALE | Per-scene drafting context record (rhymes caught/released, continuity facts, validation results) |
| `drafts/movement-four/m4-2-prompt.md` | 5074 | 2026-01-30 | STALE | Single-use AI drafting prompt for the corresponding scene/section |
| `drafts/movement-four/m4-2.context.md` | 1151 | 2026-01-30 | STALE | Per-scene drafting context record (rhymes caught/released, continuity facts, validation results) |
| `drafts/movement-four/m4-3-prompt.md` | 5904 | 2026-01-30 | STALE | Single-use AI drafting prompt for the corresponding scene/section |
| `drafts/movement-four/m4-3.context.md` | 1039 | 2026-01-30 | STALE | Per-scene drafting context record (rhymes caught/released, continuity facts, validation results) |
| `drafts/movement-four/m4-4-prompt.md` | 4988 | 2026-01-30 | STALE | Single-use AI drafting prompt for the corresponding scene/section |
| `drafts/movement-four/m4-4.context.md` | 1046 | 2026-01-30 | STALE | Per-scene drafting context record (rhymes caught/released, continuity facts, validation results) |
| `drafts/movement-four/section-4-1-digitization-choice.md` | 3194 | 2026-02-01 | MANUSCRIPT | Canonical prose: M4 §4.1 'The Digitization Choice' (Last Human) |
| `drafts/movement-four/section-4-2-sacrifice.md` | 3052 | 2026-02-01 | MANUSCRIPT | Canonical prose: M4 §4.2 'The Sacrifice' (Algorithm) |
| `drafts/movement-four/section-4-3-merge.md` | 4169 | 2026-01-30 | MANUSCRIPT | Canonical prose: M4 §4.3 'The Merge' (Archaeologist) |
| `drafts/movement-four/section-4-4-coda.md` | 1572 | 2026-01-30 | MANUSCRIPT | Canonical prose: M4 §4.4 'Coda' (pattern-voice) |
| `drafts/movement-one/algorithm/scenes/scene-01.context.md` | 627 | 2026-01-22 | STALE | Per-scene drafting context record (rhymes caught/released, continuity facts, validation results) |
| `drafts/movement-one/algorithm/scenes/scene-01.md` | 2098 | 2026-01-22 | MANUSCRIPT | Canonical prose: M1 Algo 1 'Maintenance Cycle' |
| `drafts/movement-one/algorithm/scenes/scene-02.context.md` | 675 | 2026-01-22 | STALE | Per-scene drafting context record (rhymes caught/released, continuity facts, validation results) |
| `drafts/movement-one/algorithm/scenes/scene-02.md` | 2710 | 2026-01-22 | MANUSCRIPT | Canonical prose: M1 Algo 2 'Optimization Processes' |
| `drafts/movement-one/algorithm/scenes/scene-03.context.md` | 1328 | 2026-01-22 | STALE | Per-scene drafting context record (rhymes caught/released, continuity facts, validation results) |
| `drafts/movement-one/algorithm/scenes/scene-03.md` | 3157 | 2026-01-22 | MANUSCRIPT | Canonical prose: M1 Algo 3 'Stirrings' |
| `drafts/movement-one/algorithm/scenes/scene-04.context.md` | 675 | 2026-01-22 | STALE | Per-scene drafting context record (rhymes caught/released, continuity facts, validation results) |
| `drafts/movement-one/algorithm/scenes/scene-04.md` | 3029 | 2026-01-22 | MANUSCRIPT | Canonical prose: M1 Algo 4 'The Memory' |
| `drafts/movement-one/archaeologist/first-bleed.context.md` | 366 | 2026-01-22 | STALE | Context record for the superseded first-bleed fragment |
| `drafts/movement-one/archaeologist/first-bleed.md` | 1016 | 2026-01-22 | STALE | Superseded alternate prose scene 'The First Bleed' (m1-arch-04b); passages absorbed near-verbatim into m2-arch-01 |
| `drafts/movement-one/archaeologist/scenes/scene-01.context.md` | 443 | 2026-01-22 | STALE | Per-scene drafting context record (rhymes caught/released, continuity facts, validation results) |
| `drafts/movement-one/archaeologist/scenes/scene-01.md` | 2047 | 2026-01-22 | MANUSCRIPT | Canonical prose: M1 Arch 1 'Opening: Daily Excavation' |
| `drafts/movement-one/archaeologist/scenes/scene-02.context.md` | 667 | 2026-01-22 | STALE | Per-scene drafting context record (rhymes caught/released, continuity facts, validation results) |
| `drafts/movement-one/archaeologist/scenes/scene-02.md` | 3202 | 2026-01-22 | MANUSCRIPT | Canonical prose: M1 Arch 2 'The Client: Integration Prep' |
| `drafts/movement-one/archaeologist/scenes/scene-03.context.md` | 822 | 2026-01-22 | STALE | Per-scene drafting context record (rhymes caught/released, continuity facts, validation results) |
| `drafts/movement-one/archaeologist/scenes/scene-03.md` | 2836 | 2026-01-22 | MANUSCRIPT | Canonical prose: M1 Arch 3 'Lena and Marcus' |
| `drafts/movement-one/archaeologist/scenes/scene-04.context.md` | 676 | 2026-01-22 | STALE | Per-scene drafting context record (rhymes caught/released, continuity facts, validation results) |
| `drafts/movement-one/archaeologist/scenes/scene-04.md` | 2704 | 2026-01-22 | MANUSCRIPT | Canonical prose: M1 Arch 4 'The Anomaly' |
| `drafts/movement-one/archaeologist/scenes/scene-05.context.md` | 700 | 2026-01-22 | STALE | Per-scene drafting context record (rhymes caught/released, continuity facts, validation results) |
| `drafts/movement-one/archaeologist/scenes/scene-05.md` | 3036 | 2026-01-22 | MANUSCRIPT | Canonical prose: M1 Arch 5 'Recognition' |
| `drafts/movement-one/last-human/scenes/scene-01.context.md` | 537 | 2026-01-22 | STALE | Per-scene drafting context record (rhymes caught/released, continuity facts, validation results) |
| `drafts/movement-one/last-human/scenes/scene-01.md` | 1128 | 2026-02-01 | MANUSCRIPT | Canonical prose: M1 LH 1 'Solitude' |
| `drafts/movement-one/last-human/scenes/scene-02.context.md` | 592 | 2026-01-22 | STALE | Per-scene drafting context record (rhymes caught/released, continuity facts, validation results) |
| `drafts/movement-one/last-human/scenes/scene-02.md` | 2220 | 2026-01-22 | MANUSCRIPT | Canonical prose: M1 LH 2 'Survival' |
| `drafts/movement-one/last-human/scenes/scene-03.context.md` | 1291 | 2026-01-22 | STALE | Per-scene drafting context record (rhymes caught/released, continuity facts, validation results) |
| `drafts/movement-one/last-human/scenes/scene-03.md` | 2607 | 2026-01-22 | MANUSCRIPT | Canonical prose: M1 LH 3 'The Pull' |
| `drafts/movement-one/last-human/scenes/scene-04.context.md` | 1585 | 2026-01-22 | STALE | Per-scene drafting context record (rhymes caught/released, continuity facts, validation results) |
| `drafts/movement-one/last-human/scenes/scene-04.md` | 2369 | 2026-01-22 | MANUSCRIPT | Canonical prose: M1 LH 4 'The Dream' |
| `drafts/movement-three/convergence.context.md` | 318 | 2026-01-22 | STALE | Per-scene drafting context record (rhymes caught/released, continuity facts, validation results) |
| `drafts/movement-three/convergence.md` | 1259 | 2026-01-22 | MANUSCRIPT | Canonical prose: 'The Convergence' — bridge into Movement Four |
| `drafts/movement-three/m3-phase-a-prompt.md` | 1752 | 2026-01-25 | STALE | Single-use AI drafting prompt for the corresponding scene/section |
| `drafts/movement-three/m3-phase-a.context.md` | 1317 | 2026-01-26 | STALE | Per-scene drafting context record (rhymes caught/released, continuity facts, validation results) |
| `drafts/movement-three/m3-phase-b-prompt.md` | 2256 | 2026-01-25 | STALE | Single-use AI drafting prompt for the corresponding scene/section |
| `drafts/movement-three/m3-phase-b.context.md` | 1333 | 2026-01-26 | STALE | Per-scene drafting context record (rhymes caught/released, continuity facts, validation results) |
| `drafts/movement-three/m3-phase-c-prompt.md` | 3832 | 2026-01-29 | STALE | Single-use AI drafting prompt for the corresponding scene/section |
| `drafts/movement-three/phase-a-accelerating-cuts.md` | 4988 | 2026-02-01 | MANUSCRIPT | Canonical prose: M3 Phase A 'Accelerating Cuts' (22 sections) |
| `drafts/movement-three/phase-b-simultaneous-narration.md` | 5273 | 2026-02-01 | MANUSCRIPT | Canonical prose: M3 Phase B 'Simultaneous Narration' (10 passages) |
| `drafts/movement-three/phase-c-dissolution.md` | 3117 | 2026-02-01 | MANUSCRIPT | Canonical prose: M3 Phase C 'Dissolution' |
| `drafts/movement-two/algorithm/m2-algo-01-prompt.md` | 3483 | 2026-01-23 | STALE | Single-use AI drafting prompt for the corresponding scene/section |
| `drafts/movement-two/algorithm/m2-algo-02-prompt.md` | 3832 | 2026-01-23 | STALE | Single-use AI drafting prompt for the corresponding scene/section |
| `drafts/movement-two/algorithm/m2-algo-02.context.md` | 642 | 2026-01-24 | STALE | Per-scene drafting context record (rhymes caught/released, continuity facts, validation results) |
| `drafts/movement-two/algorithm/m2-algo-02.md` | 2245 | 2026-02-01 | MANUSCRIPT | Canonical prose: M2.C2 Algo 'The Bleed' |
| `drafts/movement-two/algorithm/m2-algo-03-prompt.md` | 5046 | 2026-01-24 | STALE | Single-use AI drafting prompt for the corresponding scene/section |
| `drafts/movement-two/algorithm/m2-algo-03.context.md` | 1236 | 2026-01-24 | STALE | Per-scene drafting context record (rhymes caught/released, continuity facts, validation results) |
| `drafts/movement-two/algorithm/scenes/scene-01.context.md` | 921 | 2026-01-23 | STALE | Per-scene drafting context record (rhymes caught/released, continuity facts, validation results) |
| `drafts/movement-two/algorithm/scenes/scene-01.md` | 2571 | 2026-02-01 | MANUSCRIPT | Canonical prose: M2.C1 Algo 'The Resonance' |
| `drafts/movement-two/algorithm/scenes/scene-03.md` | 2154 | 2026-02-01 | MANUSCRIPT | Canonical prose: M2.C3 Algo 'The Sacrifice' |
| `drafts/movement-two/archaeologist/m2-arch-01-prompt.md` | 2760 | 2026-01-23 | STALE | Single-use AI drafting prompt for the corresponding scene/section |
| `drafts/movement-two/archaeologist/m2-arch-02-prompt.md` | 3601 | 2026-01-23 | STALE | Single-use AI drafting prompt for the corresponding scene/section |
| `drafts/movement-two/archaeologist/m2-arch-02.context.md` | 894 | 2026-01-24 | STALE | Per-scene drafting context record (rhymes caught/released, continuity facts, validation results) |
| `drafts/movement-two/archaeologist/m2-arch-03-prompt.md` | 4650 | 2026-01-24 | STALE | Single-use AI drafting prompt for the corresponding scene/section |
| `drafts/movement-two/archaeologist/m2-arch-03.context.md` | 1268 | 2026-01-24 | STALE | Per-scene drafting context record (rhymes caught/released, continuity facts, validation results) |
| `drafts/movement-two/archaeologist/scenes/scene-01.context.md` | 904 | 2026-01-23 | STALE | Per-scene drafting context record (rhymes caught/released, continuity facts, validation results) |
| `drafts/movement-two/archaeologist/scenes/scene-01.md` | 4026 | 2026-01-23 | MANUSCRIPT | Canonical prose: M2.C1 Arch 'The Bleed' |
| `drafts/movement-two/archaeologist/scenes/scene-02.md` | 3852 | 2026-01-24 | MANUSCRIPT | Canonical prose: M2.C2 Arch 'The Dissolution' |
| `drafts/movement-two/archaeologist/scenes/scene-03.md` | 3619 | 2026-01-24 | MANUSCRIPT | Canonical prose: M2.C3 Arch 'The Merge' |
| `drafts/movement-two/last-human/m2-lh-01-prompt.md` | 3560 | 2026-01-23 | STALE | Single-use AI drafting prompt for the corresponding scene/section |
| `drafts/movement-two/last-human/m2-lh-02-prompt.md` | 324 | 2026-01-24 | STALE | Single-use AI drafting prompt for the corresponding scene/section |
| `drafts/movement-two/last-human/m2-lh-03-prompt.md` | 5230 | 2026-01-24 | STALE | Single-use AI drafting prompt for the corresponding scene/section |
| `drafts/movement-two/last-human/m2-lh-03.context.md` | 1317 | 2026-01-25 | STALE | Per-scene drafting context record (rhymes caught/released, continuity facts, validation results) |
| `drafts/movement-two/last-human/scenes/scene-01.context.md` | 612 | 2026-01-23 | STALE | Per-scene drafting context record (rhymes caught/released, continuity facts, validation results) |
| `drafts/movement-two/last-human/scenes/scene-01.md` | 3242 | 2026-02-01 | MANUSCRIPT | Canonical prose: M2.C1 LH 'The Archive' |
| `drafts/movement-two/last-human/scenes/scene-02.context.md` | 785 | 2026-01-24 | STALE | Per-scene drafting context record (rhymes caught/released, continuity facts, validation results) |
| `drafts/movement-two/last-human/scenes/scene-02.md` | 2890 | 2026-02-01 | MANUSCRIPT | Canonical prose: M2.C2 LH 'The Protocols' |
| `drafts/movement-two/last-human/scenes/scene-03.md` | 3714 | 2026-02-01 | MANUSCRIPT | Canonical prose: M2.C3 LH 'The Interface' |
| `examples/Digital_Archaeologist_Exercises.md` | 654 | 2026-01-22 | STALE | Pre-drafting voice-practice exercise / style sample |
| `examples/Last_Human_Exercises.md` | 358 | 2026-01-22 | STALE | Pre-drafting voice-practice exercise / style sample |
| `examples/Movement_Two_Example.md` | 698 | 2026-01-22 | STALE | Pre-drafting voice-practice exercise / style sample |
| `examples/Self_Aware_Algorithm_Exercises.md` | 668 | 2026-01-22 | STALE | Pre-drafting voice-practice exercise / style sample |
| `progress.md` | 1374 | 2026-01-24 | STALE | Drafting dashboard, self-declared non-canonical, frozen at M2 Cycle 2 |
| `protocols/drafting-workflow.md` | 847 | 2026-01-24 | TOOLING | Dual-mode (AI-draft/human-review) workflow definition |
| `protocols/philosophy-constraints.md` | 1040 | 2026-01-22 | BIBLE | Four Shackles constraints with do/don't dramatization examples |
| `protocols/prompt-template.md` | 898 | 2026-01-22 | TOOLING | Template for assembling scene-drafting AI prompts |
| `protocols/review-protocol.md` | 864 | 2026-01-22 | TOOLING | Structured human-feedback format (validation table, ratings) |
| `protocols/revision-phase-prompts.md` | 7010 | 2026-01-31 | TOOLING | Sequential prompts used to execute Revision One phases A–G |
| `protocols/scene-lifecycle-protocol.md` | 2558 | 2026-01-24 | TOOLING | Scene status lifecycle (not_started→final) with entry/exit criteria |
| `research/framework.md` | 2322 | 2026-01-22 | BIBLE | Philosophy reference: Deleuze/Nietzsche eternal return, Four Shackles |
| `revision_plan_one.md` | 2624 | 2026-01-31 | EDITORIAL | Revision One blueprint: five revised phases + explicit 'what NOT to do' list |
| `scaffolding/genre-pressure.md` | 1024 | 2026-01-22 | BIBLE | Genre-register reference: Corporate Gothic / Cosmic Horror / Dying Earth markers by movement |
| `scaffolding/movement-four-braiding.md` | 4080 | 2026-01-29 | OUTLINE | M4 structural spec: reversed voice order, rhyme transformation table |
| `scaffolding/movement-three-braiding.md` | 3679 | 2026-01-25 | OUTLINE | M3 structural spec: Augenblick trigger, phase physics, collapse |
| `scaffolding/movement-three-phase-c-braid.md` | 1893 | 2026-01-26 | OUTLINE | Phase C braid tracker: residual voice markers, rhyme saturation targets |
| `scaffolding/movement-three-prep.md` | 2447 | 2026-01-25 | OUTLINE | M3 prep: experimental techniques, cut/rhyme requirements per phase |
| `scaffolding/movement-two-braiding.md` | 2959 | 2026-01-22 | OUTLINE | M2 braid spec: cycles, rhyme handoffs, phrase-bleeding map, contamination levels |
| `scaffolding/movement-two-prep.md` | 1267 | 2026-01-22 | STALE | M2 prep consolidated from brainstorms 'before archiving' — superseded by completed drafting |
| `scaffolding/narrative_protocols/fragment-alpha.md` | 999 | 2026-01-22 | BIBLE | In-world protocol fragment artifact (diegetic text) with short framing note |
| `scaffolding/narrative_protocols/protocol-design.md` | 2058 | 2026-01-22 | BIBLE | Design of the future-origin protocols and their three-era evolution |
| `scaffolding/rhymes/movement-three-escalation.md` | 1617 | 2026-01-25 | OUTLINE | Rhyme escalation/stacking plan for M3 phases |
| `scaffolding/rhymes/movement-tracking.md` | 776 | 2026-01-22 | STALE | Early rhyme tracker v1.0 (mostly 'Not started') — superseded by registry.md |
| `scaffolding/rhymes/registry.md` | 5223 | 2026-01-30 | BIBLE | Authoritative registry of the 15 sensory rhymes with per-thread scene usage (v1.3) |
| `scripts/__pycache__/genre_checker.cpython-313.pyc` | 750 | 2026-01-22 | STALE | Python bytecode cache (accidentally committed) |
| `scripts/__pycache__/philosophy_checker.cpython-313.pyc` | 824 | 2026-01-22 | STALE | Python bytecode cache (accidentally committed) |
| `scripts/__pycache__/phrase_tracker.cpython-313.pyc` | 859 | 2026-01-22 | STALE | Python bytecode cache (accidentally committed) |
| `scripts/__pycache__/rhyme_tracker.cpython-313.pyc` | 841 | 2026-01-22 | STALE | Python bytecode cache (accidentally committed) |
| `scripts/__pycache__/voice_validator.cpython-313.pyc` | 822 | 2026-01-22 | STALE | Python bytecode cache (accidentally committed) |
| `scripts/alternation_validator.py` | 1263 | 2026-01-25 | TOOLING | M3 Phase B validator: paragraph→sentence→clause alternation |
| `scripts/archive/movement_one/genre_checker.py` | 889 | 2026-01-22 | STALE | Superseded Movement One-era validator script |
| `scripts/archive/movement_one/philosophy_checker.py` | 685 | 2026-01-22 | STALE | Superseded Movement One-era validator script |
| `scripts/archive/movement_one/rhyme_tracker.py` | 785 | 2026-01-22 | STALE | Superseded Movement One-era validator script |
| `scripts/archive/movement_one/voice_validator.py` | 877 | 2026-01-22 | STALE | Superseded Movement One-era validator script |
| `scripts/compile_movement.py` | 684 | 2026-01-22 | TOOLING | Legacy compiler (source of ending-truncation bug; superseded by assemble.py) |
| `scripts/compiled/movement-one-algorithm.md` | 26 | 2026-01-22 | STALE | Stub output of compile_movement.py test run (headers only) |
| `scripts/compiled/movement-one-archaeologist.md` | 28 | 2026-01-22 | STALE | Stub output of compile_movement.py test run (headers only) |
| `scripts/compiled/movement-one-complete.md` | 137 | 2026-01-22 | STALE | Stub output of compile_movement.py test run (headers only) |
| `scripts/compiled/movement-one-last-human.md` | 28 | 2026-01-22 | STALE | Stub output of compile_movement.py test run (headers only) |
| `scripts/dissolution_validator.py` | 1053 | 2026-01-26 | TOOLING | M3 Phase C validator: pronoun ambiguity, voice balance, rhyme saturation |
| `scripts/genre_checker.py` | 979 | 2026-01-22 | TOOLING | Genre-marker checker with cycle-aware bleed tolerance |
| `scripts/movement_config.json` | 235 | 2026-01-24 | TOOLING | Config for M2 validators (cycle, contamination budgets) |
| `scripts/movement_three_config.json` | 357 | 2026-01-25 | TOOLING | Config for M3 validators (phase targets, rotation) |
| `scripts/phase-c-validation-workflow.md` | 254 | 2026-01-26 | TOOLING | How-to for running Phase C validators |
| `scripts/phase_c_review_script.py` | 1330 | 2026-01-26 | TOOLING | Continuity checker: Phase C vs Phase B + Convergence |
| `scripts/philosophy_checker.py` | 1351 | 2026-01-23 | TOOLING | Four Shackles / forbidden-moves checker |
| `scripts/phrase_tracker.py` | 1175 | 2026-01-22 | TOOLING | Key-phrase bleed tracker across threads |
| `scripts/rhyme_tracker.py` | 1447 | 2026-01-23 | TOOLING | Position-aware sensory-rhyme and handoff tracker (M2) |
| `scripts/rhyme_tracker_m3.py` | 1622 | 2026-01-25 | TOOLING | M3 rhyme stacking/saturation/valence tracker |
| `scripts/validation-outputs/algorithm-genre.json` | 569 | 2026-01-23 | STALE | One-off genre validator output for the Algorithm thread (Jan 23 run) |
| `scripts/validation-outputs/algorithm-philosophy.json` | 239 | 2026-01-23 | STALE | One-off philosophy validator output for the Algorithm thread (Jan 23 run) |
| `scripts/validation-outputs/algorithm-rhyme.json` | 556 | 2026-01-23 | STALE | One-off rhyme validator output for the Algorithm thread (Jan 23 run) |
| `scripts/validation-outputs/algorithm-voice.json` | 554 | 2026-01-23 | STALE | One-off voice validator output for the Algorithm thread (Jan 23 run) |
| `scripts/validation-outputs/archaeologist-genre.json` | 219 | 2026-01-23 | STALE | One-off genre validator output for the Archaeologist thread (Jan 23 run) |
| `scripts/validation-outputs/archaeologist-philosophy.json` | 239 | 2026-01-23 | STALE | One-off philosophy validator output for the Archaeologist thread (Jan 23 run) |
| `scripts/validation-outputs/archaeologist-rhyme.json` | 274 | 2026-01-23 | STALE | One-off rhyme validator output for the Archaeologist thread (Jan 23 run) |
| `scripts/validation-outputs/archaeologist-voice.json` | 181 | 2026-01-23 | STALE | One-off voice validator output for the Archaeologist thread (Jan 23 run) |
| `scripts/validation-outputs/last-human-genre.json` | 306 | 2026-01-23 | STALE | One-off genre validator output for the Last Human thread (Jan 23 run) |
| `scripts/validation-outputs/last-human-philosophy.json` | 237 | 2026-01-23 | STALE | One-off philosophy validator output for the Last Human thread (Jan 23 run) |
| `scripts/validation-outputs/last-human-rhyme.json` | 506 | 2026-01-23 | STALE | One-off rhyme validator output for the Last Human thread (Jan 23 run) |
| `scripts/validation-outputs/last-human-voice.json` | 153 | 2026-01-23 | STALE | One-off voice validator output for the Last Human thread (Jan 23 run) |
| `scripts/validation-outputs/phase-a-audit.yaml` | 1696 | 2026-01-31 | EDITORIAL | Revision One Phase A: full manuscript audit (word counts, phrase trajectories, agency scores, rhyme matrix) |
| `scripts/validation-outputs/phase-b-revisions.yaml` | 937 | 2026-01-31 | EDITORIAL | Revision One Phase B: foreshadowing verification log (PASSED, 0 revisions) |
| `scripts/validation-outputs/phase-c-calibration.yaml` | 1071 | 2026-02-01 | EDITORIAL | Revision One Phase C: phrase-intensity calibration; 5 edits to phase-c-dissolution.md |
| `scripts/validation-outputs/phase-d-compression.yaml` | 892 | 2026-02-01 | EDITORIAL | Revision One Phase D: compression log (M2 Algorithm cut 38–49%; book 95,881→88,417 words) |
| `scripts/validation-outputs/phase-e-agency.yaml` | 1747 | 2026-02-01 | EDITORIAL | Revision One Phase E: Last Human agency enhancements with before/after passages |
| `scripts/validation-outputs/phase-f-anchoring.yaml` | 1089 | 2026-02-01 | EDITORIAL | Revision One Phase F: rhyme-anchoring map with line refs; handoff verification |
| `scripts/validation-outputs/phase-g-validation.yaml` | 871 | 2026-02-01 | EDITORIAL | Revision One Phase G: final validation; declares Revision One complete |
| `scripts/validation-script-review-prompt.md` | 2078 | 2026-01-23 | STALE | One-off prompt commissioning the validator-script review |
| `scripts/validation-scripts-review-report.md` | 1691 | 2026-01-23 | STALE | One-off QA report grading the M2 validator scripts |
| `scripts/voice_validator.py` | 1379 | 2026-01-23 | TOOLING | Voice validator with controlled-contamination awareness |
| `voices/algorithm.md` | 1495 | 2026-01-22 | BIBLE | Voice spec: Algorithm — self-referential questioning, 'I find myself' marker |
| `voices/archaeologist.md` | 1030 | 2026-01-22 | BIBLE | Voice spec: Archaeologist — present tense, tactile, professional vocabulary |
| `voices/last-human.md` | 1441 | 2026-01-22 | BIBLE | Voice spec: Last Human — sparse elegiac fragments; forbids 'technology working' |
| `voices/quick-reference.md` | 402 | 2026-01-22 | BIBLE | One-page cheat sheet of all three voices |
| `worldbuilding/Pantasm_Reference.png` | 76986 | 2026-01-22 | BIBLE | Reference image of the phantasm geometry (filename typo 'Pantasm') |
| `worldbuilding/Phantasm.md` | 2975 | 2026-01-22 | BIBLE | The geometric form: mathematics, appearance rules, per-era manifestation |
| `worldbuilding/catastrophe-timeline.md` | 2056 | 2026-01-22 | BIBLE | Cross-era 'slow bleed' catastrophe timeline |
| `worldbuilding/deep-future.md` | 2242 | 2026-01-22 | BIBLE | Deep-future era: Last Human's world, ruins, ecology |
| `worldbuilding/mid-future.md` | 1832 | 2026-01-22 | BIBLE | Mid-future era: Algorithm's world, database civilization |
| `worldbuilding/near-future.md` | 2192 | 2026-01-22 | BIBLE | Near-future era: Archaeologist's world, digitization economy |
