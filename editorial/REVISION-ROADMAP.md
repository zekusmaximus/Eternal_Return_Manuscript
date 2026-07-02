# Revision Roadmap

> Every recommended change from DEV-EDIT-REPORT.md (Pass B) and editorial/chapters/ (Pass C), as dependency-ordered checklist items. One item per revision session, one item per commit (`revise: <ID> <summary>`), per `WORKFLOW.md`. Manuscript prose may be edited **only** inside an approved item, only in that item's affected files.
>
> Status legend: `[ ]` open · `[x]` done · operator decisions (accepted/rejected/deferred) live in `STATE.md`.

## Tier 1 — Structural moves (decide/execute first; they change what every later diff touches)

- [x] **R-05 — Decide the Movement One interleave (chapter reorder only).**
  Scope: reading order of chs. 01–13; zero prose edits. Derives from: DEV-EDIT-REPORT §1.2. Affected: `manuscript/01–13` filenames (renumber via `git mv`), `bible/structure-map.md`, `editorial/BOOK-MAP.md`.
  Hard constraints: 04 before 09; 04 before 13; 18→19→20 untouched (M2); thread-internal order preserved.
  Options: (a) full interleave (Arch 01–02, LH 10, Arch 03–04, Algo 06+07/08, LH 11–12, Arch 05, Algo 09, LH 13); (b) block swap (Arch, LH, Algo); (c) reject — keep as is.
  Done when: operator has read a cold `assemble.py` build of the chosen order and confirmed; files renamed; structure-map and book map updated. *Decision gates R-04's file numbering — decide R-05 before executing R-04.*
  **Done 2026-07-02 — option (a) executed.** Operator approved after receiving cold-read prototype builds of (a) and (b). Renumbering (old → new): 03→04, 04→05, 05→11, 09→12, 10→03, 11→09, 12→10; chs. 01, 02, 06, 07, 08, 13 unchanged. **All chapter numbers in the items below (and in DEV-EDIT-REPORT.md, BOOK-MAP.md, editorial/chapters/) are pre-R-05 numbers** — translate via this mapping. For R-04: old 07/08 now occupy consecutive positions 07/08, so the merge remains local; renumber 09–13 down by one afterwards.

- [ ] **R-04 — Merge chs. 07+08 into one Algorithm chapter (~3,500 words).**
  Derives from: report §1.1; chapters/07, 08 notes (keep/cut lists there). Affected: `manuscript/07-*`, `manuscript/08-*` (one file absorbs the other via git mv + edit), structure-map, book map.
  Done when: merged chapter contains future-pull subroutine, "I miss something I never had," Yuki Tanaka scene, shape-perceives-back resolution, Mildred's *yes*; duplicated pressure/weight escalations removed; `assemble.py` passes; word count 3,200–3,800.

- [ ] **R-06 — Single dismount for Movement Three.**
  Derives from: report §1.3; chapters/25, 26 notes. Affected: `manuscript/25-*`, `manuscript/26-*`, book map.
  Done when: the eternal-return test ("Would you choose this? Again? Infinitely?" + selection principle + gesture-answer) occurs exactly once, either folded into Phase C after its ¶44 or as a ≤600-word rewritten Convergence; the collision-recap prose is gone; M3 still exits on "What returns—"; `assemble.py` passes.

- [ ] **R-09 — Targeted compressions: ch. 16 (−25–30%) and ch. 24 (merge passages 7–8, trim 5).**
  Derives from: report §4 Sags 2–3; chapters/16, 24 notes. Affected: `manuscript/16-*`, `manuscript/24-*`.
  Done when: ch. 16 ≈ 2,300–2,500 words with the "she told me to walk east" seed, Algorithm-preservation insight, cross-time contact, and tracing close intact; ch. 24 has ≤8 passages with passage 9's ch. 01 callback untouched; rhyme handoffs verified (run `scripts/rhyme_tracker.py` on touched files).

## Tier 2 — Arc-level rewrites

- [ ] **R-01 — Accommodate "her" in Movement One (the premise fix; highest-impact prose item).**
  Derives from: report §3-LastHuman; chapters/10–13, 16, 19, 22 notes. Affected: `manuscript/10,11,12,13` (3–6 sentences total + the ch. 13 "not been touched in years" line + ch. 10 "I are" slip + ch. 12 fatalism line "Refusal is not possible" revised to choice-register).
  Done when: a reader of chs. 10–13 can later meet ch. 19's "her" without contradiction (fresh grief, recent grave, a "she" deliberately not thought about); no new backstory exposition added (ch. 19 keeps the reveal); voice check passes (`scripts/voice_validator.py`).

- [ ] **R-02 — Reconcile the Lena relationship across M1→M2.**
  Derives from: report §3-Archaeologist continuity; chapters/03, 05, 14 notes. Affected: `manuscript/03-*`, `manuscript/05-*` (recommended option (a): established couple from ch. 01 — adjust ch. 03's "introduced as" exchange and "essential" beat to be about family/meeting-Mom, not relationship definition; ch. 05's "Love you" then stands).
  Done when: no scene implies the relationship is undefined after the operator's chosen model; ch. 14's cohabitation reads as continuous.

- [ ] **R-07 — Fix the unseeded genetic-optimization claim (ch. 27).**
  Derives from: report §5 unearned-payoff (a), §6.2(b); chapters/27 note 1. Affected: `manuscript/27-*` (+ `manuscript/21-*` if seeding option chosen).
  Done when: either both clauses cut, or seeded in ch. 21's transmission AND answered in ch. 27 ("the breeding does not say yes. I say yes.").

- [ ] **R-08 — Dramatize the selection principle: give the resisting minds a face and an outcome.**
  Derives from: report §3-Algorithm, §6.1; chapters/21 note 3, 28 note 5, 26 note 3. Affected: `manuscript/21-*` or `manuscript/28-*` (one scene-beat, ~150–300 words; candidate: repurpose Yuki Tanaka as the named resister).
  Done when: one named instance refuses affirmation and the text shows what "what cannot affirm does not return" means for them; placed adjacent to the surviving selection-principle statement.

- [ ] **R-11 — Pay or release the social threads (economy, Mom, brother Marcus, Lena seeds).**
  Derives from: report §3-Archaeologist (P5), §5 items 1–3/5, §6.3; chapters/20 note 2, 29 notes 3–4/6. Affected: `manuscript/17-*` or `20-*` (Authority beat or explicit release + Mom line + Lena's lost-person clause + Lena integration seed), `manuscript/29-*` (economic payoff sentence + brother-Marcus echo).
  Done when: the concealment thread has either a consequence or an on-page release; ch. 29 names the money/months when declining integration; brother Marcus's position is echoed once; each addition ≤2 sentences.

- [ ] **R-12 — Close the cross-life causality triangle (one LH→Arch beat).**
  Derives from: report §2.1. Affected: `manuscript/20-*` or `manuscript/29-*` (~200–400 words).
  Done when: one concrete Last Human choice (e.g. sparing the crystals, ch. 19 §8) is legible in the Archaeologist's world as consequence, in the register of ch. 09 §7.

## Tier 3 — Chapter-level fixes

- [ ] **R-03 — Excise/normalize the scaffold leaks.**
  Derives from: mechanical-issues #3; report priority 2; chapters/20 n.1, 22 n.1, 23 nn.1–2, 24 n.2, 28 n.1, 29 n.2. Affected: `manuscript/20,22,23,24,28,29`.
  Done when: no bare "Movement One/Two/Three/Four" labels or reader-addressed sentences remain in prose; M3 in-text "Phase" references either systematized or removed (one register decision applied book-wide); the coda's title echo untouched.

- [ ] **R-10 — Differentiate the three M4 tests; de-duplicate 28/29.**
  Derives from: report §4 Sag 4; chapters/27 n.4, 28 n.5, 30 n.3. Affected: `manuscript/28-*` (primary), `27/29` (light).
  Done when: "the yes is what enabling looks like when enabling has become love" appears once; ch. 28's test is reframed as consent-on-behalf; decision recorded on reserving the "What returns—continues" triplet for the coda.

- [ ] **R-13 — Continuity-numbers-and-names sweep (single commit).**
  Derives from: mechanical-issues #7–12; chapters/01 n.3, 03 n.1, 05 nn.1/3/4, 06 nn.2–3, 09 n.2, 15 nn.2–3, 17 nn.1–2, 20 n.3, 21 n.2, 25 n.3, 28 nn.2–4, 29 n.5. Affected: many manuscript files, small diffs; also `bible/name-index.md` regeneration.
  Contents: one canonical Marcus Wei number; rename colleague Marcus Chen (and decide Sarah Chen/Yuki Tanaka echoes); Mildred instance number + matrix unified; "dead woman"→Martinez fix; months ledger reconciled (63→55→57→…); protocol dating canonized (recommend birth−15); "twenty years excavating"; ch. 28 Mildred quote + "billions"; ch. 29 coffee-dynamic line; stored-consciousness capability line (ch. 06 vs 28).
  Done when: `python scripts/continuity.py` regenerated and spot-checked; every mechanical-issues #7–12 entry marked resolved in that file.

- [ ] **R-14 — Formatting/numbering defects (operator rulings required).**
  Derives from: mechanical-issues #1/#4/#5. Affected: `manuscript/24-*`.
  Done when: Passage 2 header restored or passages renumbered; Passage 4 spacing ruled (intentional → documented in structure-map; defect → spaces restored); manifest note updated.

- [ ] **R-15 — Small payoffs and unifications.**
  Derives from: report §5 items 4/7, §2.2; chapters/01 n.2, 02 nn.1/3, 19 n.3, 20 n.3, 22 n.3. Affected: `manuscript/02, 19, 20, 21, 22, 29` (one-line diffs).
  Contents: the 2047.03.14 date (cut or anchor); 847 motif (one anchoring sentence or thinning); Eleanor Vasquez echo; "Architect" ch. 19 line unified to function-reading; "her in the pattern" (ch. 22) softened-to-belief or seeded in ch. 19; "seven surfaces" rhyme decision.
  Done when: each sub-decision recorded in STATE.md and applied or explicitly rejected.

## Suggested execution order

R-05 (decision) → R-04 → R-06 → R-09 → R-01 → R-02 → R-07 → R-08 → R-11 → R-12 → R-03 → R-10 → R-13 → R-14 → R-15.
Rationale: reorders/merges first (they renumber files and shift context), then the premise fixes that other diffs cite, then additive arc beats, then mechanical sweeps last so they run over final text.
