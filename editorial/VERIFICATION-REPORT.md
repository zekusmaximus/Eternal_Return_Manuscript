# Full-book verification report (post-roadmap)

- **Date**: 2026-07-03
- **Session type**: verification pass — manuscript read-only, zero prose edits made
- **Baseline verified**: 28 chapters, 85,139 words (`python scripts/assemble.py`), git HEAD `ee8c67b` (roadmap complete, 15/15)
- **Chapter numbers**: findings cite **current file names with line numbers**; where an original chapter number matters it is given per the cumulative mapping in BOOK-MAP.md (01→01, 02→02, 03→04, 04→05, 05→10, 06→06, 07+08→07, 09→11, 10→03, 11→08, 12→09, 13→12, 14→13, 15→14, 16→15, 17→16, 18→17, 19→18, 20→19, 21→20, 22→21, 23→22, 24→23, 25→24, 26→retired, 27→25, 28→26, 29→27, 30→28)

## Summary of results

| Check | Result |
|---|---|
| A. Build + ending integrity | **PASS** |
| B. Invariant grep sweep | **PASS with 2 findings** (F1, F2) + 1 note (N1) |
| C. Voice validation (all single-voice files) | **PASS** — all 15 listed baselines match exactly; 9 fresh values recorded |
| D. Rhyme architecture | **PASS** — cycles 1–2 pass; cycle-3 warns and Phase C 14/15 verified byte-identical to pre-roadmap state (N2) |
| E. Continuity index | **PASS with 1 finding** (F6 — index was stale; regenerated and committed) |
| F. Phrase + philosophy sweeps | **PASS** — minimums exceeded; the two checker "fail"s are pre-existing false positives (N3); no roadmap insertion violates the Four Shackles |
| G. Promise-ledger audit | **FAIL (records, not prose)** — ledger rows lag the executed roadmap (F5) |
| H. Cold read (full build, end to end) | **PASS with 2 findings** (F3 shared with B-adjacent sweep; I1 impression) |
| I. Export survivability (DOCX + EPUB via pandoc 3.9) | **PASS with 1 finding** (F4) — ending, italics, em-dashes, all nine M3 headers survive |

**Manuscript verdict in one line: the prose verifies clean against every roadmap done-condition; the defects found are three small missed-site/grammar slips (F1–F3), one formatting defect visible only in export (F4), and record-keeping lag (F5, F6).**

---

## Check A — Build + ending integrity: PASS

- `python scripts/assemble.py`: **28 chapters, 85,139 words, all chapter endings verified OK** — exactly the roadmap-close baseline; zero delta from git HEAD.
- Built file's final line is `*continues.*` — the legacy truncation failure mode is absent.
- Per-file last-prose-line check: file 25 ends "The pattern—", file 26 "The spiral—", file 27 "*continues.*", coda ends the book "*continues.*" — the R-10 ending map is intact. (Files 15/18/19/21/22/23/25/26 carry a trailing `---` scene-rule after the last prose line; assemble.py and both exports handle it correctly.)

## Check B — Invariant grep sweep: PASS with findings

All zero-hit assertions hold: no `Marcus Chen`, `Sarah Chen`, `3,102,458`, `#847,293`, `7,847,293`, bare `#847,102`, `forty-seven years`, `billions of preserved humans`, `You already know what you are`, jammed `[a-z]\.[A-Z]` joins, in-prose Movement labels, or "the entire novel". (The `4,847,102` in file 06:91 is a range endpoint — "instances 4,847,102 through 4,847,293" — not the forbidden bare form.)

All exact counts hold: `#3,847,102` ×3 (files 11/14/17, all Marcus Wei); `#2,847,102` = Mildred at every site; `Daniel Park` ×2 with `Daniel` only in 16/19/22/23/27; `Sarah Moreau` ×2 (17/20) and no other Sarah; `Nakamura` ×1 (19); `Tanaka` only 07/26 (Yuki, #4,399,847, integrated 2847, both sites consistent); `2047.03.14` ×2 (02:227 comment + 19:209 threshold anchor); `enabling has become love` ×1 (26:159); `Eleanor Vasquez` in 27:137 (plus her established 01/04 sites); `forty-nine years` ×3 (file 10); `fifty-three` (13:198 + the transitional 16:19), `fifty-two` (16:19), Lena forty-one (01/02).

- **F1 (finding)** — `manuscript/11-m1-algo-4-the-memory.md:77` (original ch. 09): the received-memory fragment "*The timeline number sits in the corner of my awareness like a splinter. Fifty-five months.*" contradicts line 83 of the **same memory episode** ("fifty-seven months to a threshold"). This is a missed site of R-13.5 / mechanical #11 (the ruling changed cur 11's received-memory line at 83 but not the italic fragment at 77). **Recommendation**: one-word fix (Fifty-five → Fifty-seven) as an operator one-off or R-13 erratum; the memory depicts the post-price-rise Archaeologist, so 57 is the only consistent value.
- **F2 (finding)** — `manuscript/05-m1-arch-4-the-anomaly.md:69` (original ch. 04): "The timestamp predates my career by twenty years. The timestamp predates my birth by five." This is the exact wording class R-13.6 / mechanical #9 canonized away (canon **birth−15**: cur 02:197 "by decades… my *birth* by fifteen", cur 10 "forty-nine years ago" ×3, cur 27:39 "fifteen years before I was born", Phase C "fifteen years before I was born"). The original ch. 04 site was not in R-13.6's list and survived. It is also internally strained on its own terms (career−20 would put his career start at age ~15 against ch. 01's "saving for eleven years"). **Recommendation**: operator ruling — align to canon (e.g. "…predates my career by decades. The timestamp predates my birth by fifteen.") as an R-13 erratum, or rule it a distinct fragment timestamp (not recommended; both scenes describe the same anomalous Martinez-archive code).
- **N1 (note, not a defect)** — `fifty-seven` also occurs once in file 04:59, which the sweep's expected-location list (05/10/11) omits: it is the price-rise transition sentence itself ("fifty-five months becomes fifty-seven"), which necessarily contains both numbers. Consistent with the BOOK-MAP entry-04 ledger.

## Check C — Voice validation: PASS

All 15 files with recorded baselines reproduce them **exactly** (signature to the decimal, contamination to the instance count). The 9 fresh files agree with every prior partial record (R-01's 03/08/09/12 = 1/1/3/12; R-02's 04 = 9.9/0). File 24 is merged voice per structure-map — no validator thread exists; recorded n/a (same precedent as file 23 in R-14). Overall "warn" statuses are the validator's global movement-two/cycle-3 contamination-band expectation applied to every file — the warn-band statuses below are ACCEPTED per the roadmap-close baseline, not defects.

**Canonical post-roadmap baseline table** (signature strength / signature status / contamination instances / overall):

| File | Thread | Signature | Sig status | Contam | Overall | Baseline check |
|---|---|---|---|---|---|---|
| 01 | archaeologist | 17.6 | pass | 0 | warn | fresh |
| 02 | archaeologist | 7.5 | warn | 1 | warn | matches |
| 03 | last_human | 21.6 | pass | 1 | warn | fresh (matches R-01 log) |
| 04 | archaeologist | 9.9 | warn | 0 | warn | fresh (matches R-02 log) |
| 05 | archaeologist | 11.8 | pass | 2 | warn | matches |
| 06 | algorithm | 19.0 | pass | 0 | warn | matches |
| 07 | algorithm | 14.2 | pass | 0 | warn | fresh |
| 08 | last_human | 17.0 | pass | 1 | warn | fresh (matches R-01 log) |
| 09 | last_human | 20.4 | pass | 3 | warn | fresh (matches R-01 log) |
| 10 | archaeologist | 8.2 | warn | 6 | warn | matches |
| 11 | algorithm | 14.5 | pass | 3 | warn | matches |
| 12 | last_human | 15.5 | pass | 12 | warn | fresh (matches R-01 log) |
| 13 | archaeologist | 11.4 | pass | 3 | warn | fresh |
| 14 | algorithm | 15.6 | pass | 12 | warn | matches |
| 15 | last_human | 11.7 | pass | 1 | warn | fresh |
| 16 | archaeologist | 10.8 | pass | 2 | warn | matches |
| 17 | algorithm | 19.6 | pass | 2 | warn | matches |
| 18 | last_human | 13.7 | pass | 3 | warn | matches (post-R-15 value) |
| 19 | archaeologist | 11.3 | pass | 5 | pass | matches |
| 20 | algorithm | 12.4 | pass | 14 | warn | matches |
| 21 | last_human | 15.3 | pass | 18 | warn | matches |
| 22–23 | merged | — | — | — | n/a | skipped per instructions |
| 24 | merged | — | — | — | n/a | no validator thread (structure-map: merged) |
| 25 | last_human | 25.9 | pass | 16 | warn | matches (contam per R-10 log) |
| 26 | algorithm | 9.6 | warn | 19 | warn | matches |
| 27 | archaeologist | 11.0 | pass | 4 | pass | matches |
| 28 | pattern | — | — | — | n/a | skipped per instructions |

## Check D — Rhyme architecture: PASS

- **Cycle 1 (13/14/15)**: sequence PASS; handoffs pass (bone-frequency caught 13→14; almost-closed-curve + cold-hands caught 14→15).
- **Cycle 2 (16/17/18)**: sequence PASS; handoffs pass (metallic-taste 16→17; name-edge-of-memory 17→18).
- **Cycle 3 (19/20/21)**: sequence **warn** — files 19 (10 rhymes) and 21 (12 rhymes) exceed the cycle-3 count band, and the 19→20 handoff-zone check reports name-edge-of-memory released-but-not-caught-in-opening (the rhyme IS present in file 20's body and closing zones — a zone-width artifact). **Verified byte-identical to the pre-R-12 (pre-roadmap-insertion) state** by running the tracker on the git versions at commit `1c9f29b`: same statuses, counts, and handoff results. Pre-existing designed state (cycle 3 = pervasive), not a regression. Recorded here as the accepted baseline.
- **M3 (22/23/24)**: files 22/23 show all 15 rhymes (the accepted "15 > cycle-3 ≤7" design warn). File 24 shows **14/15** — the tracker's `tracing-the-form` regex does not match Phase C's inverted phrasings ("I trace the form", "The form traces itself", "the tracing that traced it"), though the vocabulary is abundantly present in the prose. Verified byte-identical pre-R-06: a tracker-regex limitation, not a manuscript defect. `rhyme_tracker_m3.py`: 22 warn / 23 pass (score 90) / 24 "fail" (coverage 93.3, score 40) — the phase-C "fail" is the same pre-existing regex artifact (confirmed on the pre-R-06 file: identical result).
- **R-12 handoff chain intact** (original 19→20→21 = current 18→19→20): 18:207 "If dissolution is coming, I will walk into it. I will not be dragged." → 19:171 "He will walk into it. He will not be dragged." → 20:147 "the arrival at that node can be dragged or willed." The echo also lands forward at 21:171 ("I know what it means to be dragged. This is not that.") and 22:327 ("I walk into it.").

## Check E — Continuity index: PASS with finding

- `python scripts/continuity.py` regenerated `bible/name-index.md`: **222 terms, 13 variant groups**.
- **F6 (finding, records)** — the checked-in index was **stale**: it predated R-14/R-15 (deltas are exactly those items' edits — Passage count 8→9 in file 23, Eleanor Vasquez gaining her file-27 site, "Architecture" entering at 18/27, Architect 72→73, Lena 27(8)→27(9)). R-13's regeneration was the last one run. The regenerated index is committed with this report. **Recommendation**: add "run continuity.py" to the per-item verify list even for items believed name-neutral.
- All 13 near-miss variant groups reviewed: every one is a trivial possessive/plural/contraction pair (Algorithm/Algorithm's, Mildred Higgins/Higgins's, He's/She's…) or the Waking/Walking edit-distance artifact (both are registered rhyme vocabulary). No name inconsistencies. The known-accepted Wei #3,847,102 / Mildred #2,847,102 cluster-adjacency stands as recorded (mechanical #8); the index's capitalized-term generator does not surface numbers, and no new number near-misses exist (Check B counts).

## Check F — Phrase + philosophy sweeps: PASS

- Phrase minimums (revision-plan Phase 1): "I find myself" **×108** book-wide (min 8–12) ✓; "I find myself found" **×54** (min 5–7) ✓; "almost-closed curve" **×71** (min 10) ✓. `phrase_tracker.py` run per-file on all 24 single-voice files: pass/warn statuses only (warns are the M1-files-under-movement-two-config artifact; no errors, no missing-phrase failures on M2 files).
- `philosophy_checker.py` run on all 28 files: 26 pass/warn with zero shackle violations. Two "fail"s, **both pre-existing verbatim in the pre-roadmap text (verified via git) and both false positives**:
  - 10:119 "they ARE my work" — the Archaeologist recognizing his own protocols across the bootstrap loop (self-identity across his own timeline, canonical to the premise), not a protagonist-flattening claim. **N3.**
  - 28:33 (coda) "These are not separate places. They are the same architecture perceived from positions that time arranged" — a claim about *places* in the licensed post-dissolution pattern voice, which itself preserves positional difference; the identity shackle targets "the three protagonists are the same person" claims. **N3.**
- **No roadmap insertion triggers any shackle or forbidden-move pattern.** The Four Shackles hold: the M4 chapters and coda consistently use differentiation language ("We are not the same… expressions of a single virtual pattern", "What returns is not the Same").

## Check G — Promise-ledger audit: FAIL (records lag; no prose defect)

Walking BOOK-MAP §Synthesis's consolidated ledger row by row:

- Marked paid and verified in prose: P1, P2 (R-11; 27:§3 economy passage present), P3/P33/P40, P4, P5 (R-11; 16:139–141 audit-archived-unread present), P6/P16/P22, P7 (R-11; 19:115 present), P8 (implicitly paid; the R-15.6 seven-surfaces marker rejection is recorded under BOOK-MAP entry 02), P11 (R-11; 19:111 present), P12/P41, P14, P15, P17, P18-chain, P25/26/30/32/37/38/44, P31, P39, P43 (R-08; Yuki beat present 26:141–147), P45.
- **F5 (finding — every sub-item is a ledger-text defect, not a manuscript one):**
  1. **P9 row still reads "UNPAID — the date never recurs"** — but R-15.1 paid it (19:209 anchors 2047.03.14; BOOK-MAP entry-02/19 R-15 records say "P9 paid"). Row never updated.
  2. **P20 row still reads "UNPAID — structural numerology with no revealed meaning"** — but R-15.2 anchored it (20's "847 fragments. 847 storage clusters…" paragraph; BOOK-MAP entry-20 R-15 record says "P20 (847) anchored once"). Row never updated.
  3. **No Eleanor row exists** — R-15.3 closed the Eleanor Vasquez loop (27:137); the ruling lives only in the entry-29 record. The consolidated ledger should carry it.
  4. **P23 row still reads "Orphaned single-use"** — stale since R-08 made Yuki Tanaka the named resister in file 26.
  5. **P10** ("WEAK — happens off-page"), **P28** ("ORPHANED" male dream-voice — verified still true: the speaker exists only in LH dreams at 08:93, 09:117–127, 12:47/147; no scene contains him, and no roadmap item addressed it), **P29** ("Inconsistent… overtaken by events") and **P35** ("Partially paid") carry Pass-B assessments but no explicit paid/released **ruling**.
- **Recommendation**: a small records-maintenance commit (editorial files only, extend-don't-overwrite) adding "→ PAID by R-15 (2026-07-03)" to P9/P20, "→ dramatized by R-08" to P23, an Eleanor row, and explicit operator rulings (pay/release) for P10/P28/P29/P35 — P28 being the only one with a live fix path left open (dev-note option (a): the colleague-warning beat, now Daniel Park, ch. 17 scene 2).

## Check H — Cold read (assembled build, end to end): PASS with findings

Read `build/full-manuscript.md` in full, in reading order. Overall: the book reads continuously and the roadmap insertions are seamless at every seam I checked against STATE's session log — the R-01 seeds sit quietly in the M1 LH chapters; R-02's family-stakes exchange reads native; the R-11 goodbye insertions (Mom, the lost person, the integration seed) ride the scene's rhythm without bump; R-12's vigil beat lands "I find myself found" as an earned capstone; R-15's date anchor, 847 anchor, and Eleanor return all read as if drafted in place; R-08's Yuki refusal is one of the strongest beats in M4; R-10's differentiated test-closes give the three M4 chapters distinct arguments. The M3 Phase register (licensed) reads consistently; no Movement labels, reader-address, or register breaks surfaced beyond the item below. Timeline, names, and numbers cohere throughout except as already noted (F1, F2).

- **F3 (finding)** — `manuscript/13-m2-arch-1-the-bleed.md:99`: "The **accusations sits** between us, patient as the protocols, waiting for me to decide what to do with **it**." Number-agreement slip (subject/verb and the trailing pronoun). **Recommendation**: "The accusation sits… what to do with it" (or pluralize throughout); one-word operator one-off. Pre-existing (not roadmap-introduced).
- **I1 (impression, operator ruling requested; low priority)** — `manuscript/24-m3-phase-c-dissolution.md:21` "the sublime edge where **Corporate Gothic** meets something older" and 24:29 "the elegiac tone of a dying earth meets the **tech-noir** investigation". These are genre/register *labels* in Phase C's merged voice. R-03.5's ruling licenses M3's structure-self-perception ("the sections shorten" etc.), and the R-03 sweep left these standing — but genre-taxonomy vocabulary is arguably closer to the unlicensed scaffold class than to structure-perception. Flagged for an explicit ruling either way; no change made or presumed.
- Cold-read confirmations worth recording: the file 05 "fifty-seven … instead of sixty-five" math checks (63+2−8=57); 16:19's "fifty-three months … Fifty-two months now" transition matches the BOOK-MAP entry-04 ledger; Phase C and file 27 both carry the birth−15 canon ("fifteen years before I was born" / "predates my birth by fifteen years"), which isolates F2 as the single surviving off-canon site.

## Check I — Export survivability: PASS with finding

No system pandoc; installed `pypandoc-binary` (pandoc 3.9) in the session sandbox and exported `build/full-manuscript.md` to **DOCX and EPUB**. Results:

- **Final word survives both formats**: DOCX document text ends "…We are what returns.What returns—continues." and the EPUB contains the final `<em>continues.</em>` — the archive/compiled1 truncation failure mode does **not** reproduce.
- **Italics survive**: 395 italic runs in DOCX, 393 `<em>` spans in EPUB (including the closing "*continues.*").
- **Em-dashes survive**: 1,922 in both exports vs 1,920 in source — the +2 traced to **F4** below, not a conversion loss.
- **All nine M3 passage headers survive in both formats**, including "Passage 2: Two More Positions".
- **F4 (finding)** — `manuscript/23-m3-phase-b-simultaneous-narration.md:191 and :222`: the `---` scene rules closing Passages 5 and 6 sit **directly against the preceding prose line with no blank line**. Strict-Markdown converters therefore do not read them as horizontal rules: pandoc absorbed each into the preceding paragraph as a smart-dash (the +2 em-dashes); other converters would render the preceding line as a setext heading. Everywhere else in the book the rule is correctly blank-line-separated. Verified pre-existing before R-09 (git `237c9df^`). **Recommendation**: insert one blank line before each of the two rules (formatting-only, zero prose change) as an operator one-off; until then, any exporter should be checked at these two boundaries. Logged as mechanical #23.
- Operator re-check greps for their own export pipeline: (1) the final word — `tail -c 100 <export-as-text>` must end `continues.`; (2) the two Phase B boundaries — the paragraphs ending "the almost is—everything—" and "—are becoming—" must be followed by a scene break, not fused into a heading or a longer dash-run.

---

## Consolidated findings

| # | Where | What | Class | Recommendation |
|---|---|---|---|---|
| F1 | manuscript/11-m1-algo-4-the-memory.md:77 | "Fifty-five months." vs same memory's "fifty-seven months" (line 83) | missed R-13.5 site | one word, 55→57 (operator one-off / R-13 erratum) |
| F2 | manuscript/05-m1-arch-4-the-anomaly.md:69 | "career by twenty years… birth by five" vs birth−15 canon | missed R-13.6 site | align to canon (operator ruling; erratum) |
| F3 | manuscript/13-m2-arch-1-the-bleed.md:99 | "The accusations sits… with it" | grammar (pre-existing) | "The accusation sits" (operator one-off) |
| F4 | manuscript/23-m3-phase-b-simultaneous-narration.md:191, 222 | `---` rules lacking preceding blank line; exports misparse | formatting (pre-existing) | insert blank lines (formatting-only one-off) |
| F5 | editorial/BOOK-MAP.md §Synthesis ledger | P9/P20/P23 rows stale; Eleanor row missing; P10/P28/P29/P35 unruled | records lag | records-maintenance commit; P28 needs a real pay/release decision |
| F6 | bible/name-index.md | index was stale (pre-R-14/R-15) | records lag | regenerated + committed this session |
| I1 | manuscript/24-m3-phase-c-dissolution.md:21, 29 | "Corporate Gothic" / "tech-noir" genre labels in Phase C | register question | operator ruling under R-03.5's license (low priority) |

New mechanical-issues entries: #20 (F2), #21 (F1), #22 (F3), #23 (F4), #24 (I1).

## Verdict

The book is ready for line-level polish. Every structural, arc-level, and chapter-level roadmap outcome verifies in the assembled text: the build is complete and correctly terminated, every continuity invariant from the R-13 sweep holds under grep, the voice and rhyme architecture reproduce their recorded baselines to the decimal, the Four Shackles are intact, the roadmap insertions read seamlessly in a cold front-to-back read, and the text survives DOCX/EPUB conversion with its ending, italics, and M3 apparatus intact. What remains is genuinely line-level: two one-word continuity errata the R-13 sweep's site lists missed (F1, F2), one grammar slip (F3), two missing blank lines that only matter to converters (F4), and editorial bookkeeping (F5, F6) — none of which touches structure, voice, or design. The one open judgment call (I1) is a register question the operator can rule on in minutes. I recommend clearing F1–F4 as a single small erratum batch (with the usual per-item approval) before or alongside the first polish pass, and doing the F5 ledger maintenance so the records enter polish clean.
