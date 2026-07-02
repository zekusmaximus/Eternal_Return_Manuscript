# Editorial session state

- **Last updated**: 2026-07-02 (R-09 executed; R-05, R-04, R-06 and dev-edit Passes A–C earlier same day)
- **Current item**: none — R-09 complete; next pick per suggested order is R-01 (accommodate "her" in Movement One)
- **Items done**: 4 of 15 roadmap items (R-05, R-04, R-06, R-09)
- **Manuscript baseline**: post-Revision One + R-05/R-04/R-06/R-09, 28 chapters, 84,064 words assembled (`python scripts/assemble.py` verified all chapter endings)
- **Next action**: operator picks the next roadmap item (suggested order continues with R-01, the M1 "her" accommodation — current files 03, 08, 09, 12); session follows `editorial/WORKFLOW.md`. NOTE: all chapter numbers in Pass A-C records are ORIGINAL (pre-R-05) numbers; the cumulative original→current mapping lives in BOOK-MAP.md's renumbering notes.

## Operator decisions

One row per roadmap item (and per R-15 sub-decision). Status ∈ accepted / rejected / deferred / pending.

| Item | Decision | Notes |
|---|---|---|
| R-05 M1 interleave | accepted | option (a) full interleave, approved 2026-07-02 after cold-read prototypes of (a)+(b); executed same day, prose byte-identical |
| R-04 merge 07+08 | accepted | approved 2026-07-02 from full merged draft; title "Stirrings"; gapless renumber; embodiment paragraph restored at operator request |
| R-06 M3 single dismount | accepted | option (a) fold, chosen 2026-07-02 after reading both drafted options; session recommended (a) for reader-facing reasons (single test before M4's three echoes) |
| R-09 compress 16 + 24 | accepted | approved 2026-07-02 from full before/after draft files; ch. 24 passage-numbering ruling = option (a), leave 9/10 headers untouched, log new 8-skip for R-14 |
| R-01 "her" in M1 | pending | premise fix; proposal wording in chapters/10–13 notes |
| R-02 Lena relationship model | pending | recommend option (a): established couple from ch. 01 |
| R-07 genetic-optimization | pending | cut vs seed-and-answer |
| R-08 resisting minds | pending | candidate: Yuki Tanaka as named resister |
| R-11 social threads | pending | Authority beat vs release; Mom; brother Marcus echo; Lena seeds |
| R-12 LH→Arch causality beat | pending | placement: ch. 20 vs 29 |
| R-03 scaffold leaks | pending | includes book-wide register ruling on M3 "Phase" mentions |
| R-10 M4 test differentiation | pending | includes "What returns—continues" triplet reservation |
| R-13 continuity sweep | pending | includes Marcus Chen rename decision |
| R-14 ch. 24 formatting rulings | pending | Passage 2 header; Passage 4 spacing intentional? |
| R-15 small payoffs | pending | date / 847 / Eleanor / Architect line / "her in the pattern" / seven-surfaces |

## Session log

- **2026-07-02** — Phases 0–4 of the reorganization/dev-edit session: inventory (197 files classified), reorg (175 `git mv`, nothing deleted, prose byte-identical), tooling (assemble/stats/continuity/edit_status + CLAUDE.md), full-book Pass A (BOOK-MAP.md), Pass B (DEV-EDIT-REPORT.md), Pass C (30 chapter note files), roadmap + this file + WORKFLOW.md. Manuscript prose untouched throughout. Known conflicts with prior notes stated in DEV-EDIT-REPORT §7 (notably: this session disagrees with phase-g's "ready for polish").
- **2026-07-02** — **R-05 executed (option (a), full M1 interleave).** Operator approved after cold-read prototype builds of options (a) and (b). Seven `git mv` renames (03->04, 04->05, 05->11, 09->12, 10->03, 11->09, 12->10; zero prose edits, files byte-identical). New M1 order: A A L A A G G G L L A G L. Updated: `bible/structure-map.md` (table + braid diagram), `editorial/BOOK-MAP.md` (renumbering note, heading annotations, synthesis line), `editorial/mechanical-issues.md` (numbering-convention note, #6 filename pointer), roadmap (R-05 checked, old->new mapping recorded for later items). `assemble.py` verified all 30 endings, 88,104 words; `stats.py` confirms new order.
- **2026-07-02** — **R-04 executed (merge 07+08 → "Stirrings").** Operator approved the full merged draft (with embodiment paragraph restored) and gapless renumbering. New chapter 3,797 words; five required elements present; kept the phrase ladder, excision seed, bone-frequency and falling-backward rhyme anchors; cut the duplicated pressure/weight escalations, 07's coda scene, and 08's fragments-paragraph (deferred to "The Memory"). Original 08 file archived (`archive/superseded/`); 22 files renumbered down by one (book now 01–29). Updated: structure-map, BOOK-MAP (cumulative mapping + merged-chapter record), rhyme-registry (m1-algo-03 → m1-algo-02), chapter notes 07/08, mechanical-issues, roadmap. Verified: assemble.py 29 chapters / 86,034 words / all endings OK; voice_validator pass, zero contamination.
- **2026-07-02** — **R-09 executed (targeted compressions, original chs. 16 + 24 — current files 15 and 23).** Operator approved from full before/after draft files sent before any repo edit. Ch. 16 "The Archive": 3,242 → 2,483 words (−23.4%), intra-scene compression only — first+second surface scenes folded into one (per report §4 Sag 2); the walk-east seed, Algorithm-preservation insight, cross-time contact, and tracing close all intact verbatim or near-verbatim; chapter note 16 #3 (memory-gap seed) deliberately NOT executed, left open. Ch. 24 "Simultaneous Narration": 5,273 → 4,928 words — passage 5 trimmed −31% (six abstraction-echo lines), passages 7+8 merged under "Passage 7: Fragments" (now 8 headed passages); operator ruled option (a): passages 9/10 headers untouched (passage 9 byte-identical, ch. 01 callback preserved), new header skip at 8 logged in mechanical-issues #1 for R-14; R-14/R-03 defects in the file untouched. Updated: BOOK-MAP (R-09 records under both entries), mechanical-issues #1, roadmap. Verified: assemble.py 28 chapters / 84,064 words / all endings OK; rhyme_tracker --sequence 13/14/15 pass (rhyme set and handoff zones unchanged); voice_validator last_human identical to pre-edit.
- **2026-07-02** — **R-06 executed (option (a), single M3 dismount).** Operator chose the fold after comparing drafted options (a) and (b). The Convergence's test sequence spliced verbatim into Phase C after ¶44 — dissolution → test → separation, the yes preceding the release; collision- and separation-recaps retired with the chapter file to `archive/superseded/25-m3-convergence.md`. Mildred harmonizing clause applied (only new words). M4 renumbered 26–29→25–28 (book now 01–28). Resolves mechanical-issues #2. Updated: structure-map, BOOK-MAP (post-R-06 cumulative mapping + record), archive README, chapter notes 25/26, roadmap. Verified: assemble.py 28 chapters / 85,168 words / all endings OK.
