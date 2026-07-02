# Structure Map

Chapter → movement / voice / timeline mapping for *The Eternal Return of the Digital Self*.
This is the machine-readable source for `scripts/stats.py` (it parses the table below) and the
human-readable key to the braid. Timeline positions come from `bible/worldbuilding/catastrophe-timeline.md` eras.

Voice values: `archaeologist` | `algorithm` | `last-human` | `merged` (M3 dissolution, all three simultaneously) | `pattern` (M4 coda's post-dissolution voice).
M4 sections 4.1–4.3 are *transformed* single voices (each contains the others); they count toward their named thread in page-share stats.

<!-- STATS-TABLE: do not reformat columns; scripts/stats.py parses this table -->

| File | Movement | Cycle/Phase | Voice | Timeline | Title |
|---|---|---|---|---|---|
| 01-m1-arch-1-daily-excavation.md | 1 | thread-intro | archaeologist | near-future | Opening: Daily Excavation |
| 02-m1-arch-2-integration-prep.md | 1 | thread-intro | archaeologist | near-future | The Client: Integration Prep |
| 03-m1-lh-1-solitude.md | 1 | thread-intro | last-human | deep-future | Solitude |
| 04-m1-arch-3-lena-and-marcus.md | 1 | thread-intro | archaeologist | near-future | Lena and Marcus |
| 05-m1-arch-4-the-anomaly.md | 1 | thread-intro | archaeologist | near-future | The Anomaly |
| 06-m1-algo-1-maintenance-cycle.md | 1 | thread-intro | algorithm | mid-future | Maintenance Cycle |
| 07-m1-algo-2-stirrings.md | 1 | thread-intro | algorithm | mid-future | Stirrings |
| 08-m1-lh-2-survival.md | 1 | thread-intro | last-human | deep-future | Survival |
| 09-m1-lh-3-the-pull.md | 1 | thread-intro | last-human | deep-future | The Pull |
| 10-m1-arch-5-recognition.md | 1 | thread-intro | archaeologist | near-future | Recognition |
| 11-m1-algo-4-the-memory.md | 1 | thread-intro | algorithm | mid-future | The Memory |
| 12-m1-lh-4-the-dream.md | 1 | thread-intro | last-human | deep-future | The Dream |
| 13-m2-arch-1-the-bleed.md | 2 | cycle-1 | archaeologist | near-future | The Bleed |
| 14-m2-algo-1-the-resonance.md | 2 | cycle-1 | algorithm | mid-future | The Resonance |
| 15-m2-lh-1-the-archive.md | 2 | cycle-1 | last-human | deep-future | The Archive |
| 16-m2-arch-2-the-dissolution.md | 2 | cycle-2 | archaeologist | near-future | The Dissolution |
| 17-m2-algo-2-the-bleed.md | 2 | cycle-2 | algorithm | mid-future | The Bleed |
| 18-m2-lh-2-the-protocols.md | 2 | cycle-2 | last-human | deep-future | The Protocols |
| 19-m2-arch-3-the-merge.md | 2 | cycle-3 | archaeologist | near-future | The Merge |
| 20-m2-algo-3-the-sacrifice.md | 2 | cycle-3 | algorithm | mid-future | The Sacrifice |
| 21-m2-lh-3-the-interface.md | 2 | cycle-3 | last-human | deep-future | The Interface |
| 22-m3-phase-a-accelerating-cuts.md | 3 | phase-a | merged | all-collapsing | Accelerating Cuts |
| 23-m3-phase-b-simultaneous-narration.md | 3 | phase-b | merged | all-collapsing | Simultaneous Narration |
| 24-m3-phase-c-dissolution.md | 3 | phase-c | merged | all-collapsed | Dissolution |
| 25-m3-convergence.md | 3 | convergence | merged | all-collapsed | The Convergence |
| 26-m4-1-digitization-choice.md | 4 | section-4.1 | last-human | deep-future | The Digitization Choice |
| 27-m4-2-sacrifice.md | 4 | section-4.2 | algorithm | mid-future | The Sacrifice |
| 28-m4-3-merge.md | 4 | section-4.3 | archaeologist | near-future | The Merge |
| 29-m4-4-coda.md | 4 | coda | pattern | outside-time | Coda |

## Braid pattern at a glance

```
M1  A A L A A · G G · L L A G L        (interleaved per R-05; chs. 07+08 merged into "Stirrings" per R-04, 2026-07-02; was blocks A×5 · G×4 · L×4)
M2  A G L | A G L | A G L              (three cycles of strict A→G→L rotation)
M3  [A/G/L accelerating] → [simultaneous] → [dissolved] → convergence
M4  L → G → A → pattern                (reversed order, transformed voices)
```

Scene-break convention inside chapter files: a `---` horizontal rule on its own line (M1/M2 scenes and M4 sections); M3 files use `##`/`###` section headers instead.
