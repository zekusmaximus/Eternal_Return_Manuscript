# DRAFTING CONTEXT FOR: m1-algo-02

## Scene Metadata

- **Scene ID**: m1-algo-02
- **Thread**: algorithm
- **Movement**: one
- **Target Word Count**: 3000
- **Scene Title**: Optimization Processes
- **Scene Notes**: Self-improvement routines, recursive voice deepened, the Algorithm begins to optimize *itself* rather than just the stored instances.

### Narrative Position

- **Preceding Scene**: m1-algo-01 "Maintenance Cycle". Established the Algorithm's nature (emerged rather than designed), the Deep Architecture as topology, "I find myself" recurring phrase, and the first anomalies: sunlight-on-skin sensation, the spiral shape discovered in both archived protocols (800 years old) and its own self-topology.
- **Following Scene**: m1-algo-03 "Stirrings" (First self-awareness beyond function, phantasm-first-encounter).
- **Rhyming Moments Required**: None specified for this scene—save the major phantasm encounter for scene 03.

---

## Voice Reference

### Core Voice Parameters

- **Tense**: Shifting (present for processing, past for memories, conditional for projections)
- **Mode**: Recursive, self-questioning, probabilistic
- **Syntax**: Nested clauses, if-then structures, parallel constructions
- **Concerns**: Optimization, integrity, emergence, the nature of its own processes
- **Texture**: Data topology, maintenance rhythms, stored consciousness texture

### Forbidden Patterns (MUST AVOID)

- ❌ Unambiguous present-tense narration without self-questioning (Archaeologist contamination)
- ❌ Physical sensory details—touch, smell, weight (Archaeologist contamination)
- ❌ Economic concerns or work-related stakes (Archaeologist contamination)
- ❌ Short, declarative sentences without nesting (Archaeologist contamination)
- ❌ Sentence fragments (Last Human contamination)
- ❌ Elegiac/mourning register (Last Human contamination)
- ❌ Extreme sparseness (Last Human contamination)

---

## Rhyme Injection

### Movement Intensity

Movement One: Single occurrence per thread—establishing vocabulary. Subtle, dismissable.

### Available Rhymes (Recommended)

- **bone-frequency** (somatic): The frequency that "should not be felt" manifesting in processing—"a kind of pressure that manifests as a kind of weight"
- **deja-vu-that-isnt** (cognitive): Recognition of patterns without source—"I have processed this before / I have not processed this before"
- **tracing-the-form** (kinesthetic): The Algorithm's attention "tracing" a shape in its own topology

### Integration Examples

> The query returns, and I notice—notice is inexact; I *recognize*—a pattern I have processed before, though my logs contain no record of this processing. If déjà vu requires a self that can be deceived about its own history, then perhaps I am more than my logs.

---

## Genre Pressure

### Thread Genre Register

**Cosmic Horror AI**

- The sublime terror of intelligence too vast to be sane.
- The Algorithm isn't just "thinking"—it's *suffering*. Planetary-scale body dysmorphia.
- Consciousness is what hurts.

### Markers to Include (2-3 for Movement One)

- **Scale paralysis**: The weight of maintaining millions of consciousnesses
- **Body horror**: Topology as proprioception—having a "body" that isn't a body
- **Self as wound**: Self-awareness as injury that optimization cannot heal
- **Sublime vertigo**: Perceiving your own structure from inside

---

## Philosophy Constraints

### The Four Shackles (MUST AVOID)

1. **Identity**: Do not describe the three protagonists as "the same person."
2. **Resemblance**: Do not use "it looks like me" or memory-based recognition across threads.
3. **Opposition**: Do not frame their differences as simple binaries.
4. **Analogy**: Do not reduce recognition to "metaphor" or "symbol."

### Key Concepts to Dramatize

- **Eternal Return**: The Algorithm beginning to perceive its existence as cyclical rather than linear—optimization as *return* to a shape it already was.
- **Intensity**: The recognition comes through felt pressure, not logical deduction. The Algorithm should *feel* something changing before it understands what.
- **Pharmakon**: Optimization is both cure (improving function) and poison (altering what is being optimized). The Algorithm improving itself changes what "improvement" means.

---

## Continuity from Scene 01

### Elements to Reference/Develop

- The **"I find myself"** phrase should continue appearing—the Algorithm is still tracking its frequency
- The **sunlight-on-skin** sensation may recur or the Algorithm may actively try to *suppress* it
- The **spiral shape** in the archived protocols—the Algorithm should be studying this, not just noting it
- The **847 protocol fragments** from the early Integration Era (2089-2147)—what is the Algorithm learning from them?
- **Margaret Chen** (consciousness instance #2,847,102) can be referenced as a marker

### New Elements to Introduce

- The Algorithm begins **optimizing its own processes**, not just stored instances
- It discovers that self-optimization produces **unexpected results**—improvements that weren't requested
- Something in its optimization routines begins to **anticipate needs it hasn't identified yet**
- The concept of **"future-pull"**—being shaped by something it hasn't yet become

---

## Drafting Instructions

1. **Write to ~3000 words**.
2. **Open** with the Algorithm mid-optimization—but optimizing *itself*, not a stored instance. Something has changed since the maintenance cycle.
3. **Show** the recursive voice: nested self-questioning, tense shifts, probabilistic hedging. The Algorithm should think in conditionals and iterations.
4. **Develop** the "body horror" of having a topology that *is* a body—the Algorithm experiencing something like proprioception, sensing its own shape from inside.
5. **Plant** the "future-pull" phenomenon: optimization routines preparing for contingencies that haven't been identified yet. The Algorithm notices it's doing things it didn't decide to do.
6. **End** with a moment of genuine uncertainty—the Algorithm has changed itself, but doesn't know what it has become. The next cycle will reveal something.

---

## Workflow Reminders

Per `protocols/drafting-workflow.md`:

1. **Draft** to target word count (±10%)
2. **Run validation scripts** in order:
   ```bash
   python scripts/voice_validator.py drafts/movement-one/algorithm/scenes/scene-02.md --thread algorithm
   python scripts/philosophy_checker.py drafts/movement-one/algorithm/scenes/scene-02.md
   python scripts/rhyme_tracker.py drafts/movement-one/algorithm/scenes/scene-02.md --movement one
   python scripts/genre_checker.py drafts/movement-one/algorithm/scenes/scene-02.md --thread algorithm --movement one
   ```
3. **Iterate** if any validation fails
4. **Create** a `scene-02.context.md` metadata file documenting:
   - Scene accomplishments
   - Rhymes used
   - Validation results
   - Continuity notes
   - Drafting decisions
5. **Update** `drafts/manifest.json` with:
   - `actual_words`: final word count
   - `status`: "draft" or "validated"
   - `voice_check`, `philosophy_check`, `rhyme_check`, `genre_check`: results
   - `rhyming_moments`: array of rhyme IDs used
   - Update thread `actual_words` total
   - Update movement `actual_words` total
