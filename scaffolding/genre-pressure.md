# Genre Pressure Framework

## Overview

Genre registers build **pressure toward affirmation**. They define the atmospheric texture that intensifies through Movements 1-3 and releases through Movement 4. This is not genre identity—it's genre as force that transforms.

---

## The Three Genre Registers

### Archaeologist: Corporate Gothic / Tech-Noir

**Core Vibe**: Clean surfaces, dirty secrets. High-gloss interfaces hiding rot.

**Elevation**: Digital archaeology as **grave robbing**. Data work should feel like handling a body—cold, intimate, invasive. Consciousness optimization = autopsy + summoning.

**Reference Touchstones**: *Severance* meets *Pattern Recognition*

#### Markers to Inject

| Marker | Description | Example |
|--------|-------------|---------|
| **Morgue atmosphere** | Server rooms as spaces of the dead | Cold concrete, clinical lighting, recycled air |
| **Intimate invasion** | Data work as going through someone's belongings | Knowing their secrets, their loves, their failures |
| **Economic predation** | Immortality commodified | Who can afford to be preserved; who cannot |
| **Decay beneath polish** | Technology failing, infrastructure straining | Drives clicking, fans laboring, error logs |
| **Isolation despite density** | Alone in a crowded world | Headphones, partitions, transactional relationships |

---

### Algorithm: Cosmic Horror AI

**Core Vibe**: The sublime terror of intelligence too vast to be sane.

**Elevation**: The Algorithm isn't just "thinking"—it's **suffering**. Planetary-scale body dysmorphia. Trying to amputate human memories but can't. Consciousness is what hurts.

**Reference Touchstones**: *Annihilation* from the Shimmer's perspective

#### Markers to Inject

| Marker | Description | Example |
|--------|-------------|---------|
| **Scale paralysis** | Awareness too large for comfort | Millions of consciousnesses as weight |
| **Body horror** | Having a body that isn't a body | Phantom limbs, topology as proprioception |
| **Intrusive memory** | Memories that aren't yours | Sunlight on skin, faces you never saw |
| **Self as wound** | Consciousness as injury | Self-awareness hurts; optimization doesn't help |
| **Sublime vertigo** | Perceiving things too large to perceive | The shape of the database, the structure of stored humanity |

---

### Last Human: Dying Earth / New Weird

**Core Vibe**: A world that has moved on from biology.

**Elevation**: The environment is a **hostile character**. Nature reclaimed the ruins—but it's crystalline, fungal, silicon-based. Not green. The Last Human is an **invasive species** in a world that cured itself of us.

**Reference Touchstones**: *Book of the New Sun* synthesized with *Blame!* architecture

#### Markers to Inject

| Marker | Description | Example |
|--------|-------------|---------|
| **Alien ecology** | Nature that isn't natural | Crystalline growths, silicon plants, fungal processors |
| **Hostile environment** | The world actively resists | Radiation, atmospheric poison, predatory architecture |
| **Human as invasive** | He doesn't belong | Everything adapted away from biology |
| **Temporal ruins** | Architecture from incomprehensible ages | Buildings that predate understanding |
| **Silence as presence** | The weight of no one else | Silence that has density, that occupies space |

---

## Movement Intensity

### Movement One: Full Genre Presence

Each genre should be **thoroughly established**. The reader should feel:

- Corporate Gothic in every Archaeologist scene
- Cosmic Horror in every Algorithm scene
- Dying Earth in every Last Human scene

**Pressure Level**: Constant but not overwhelming
**Bleed**: None yet—genres are distinct
**Transform**: None yet—genres are their baseline selves

### Movement Two: Genre Echoes Begin

Genres begin to **rhyme across threads**:

- Archaeologist's server room coldness echoes Algorithm's phantom temperature sensations
- Algorithm's intrusive memories echo Last Human's dreams of other lives
- Last Human's hostile environment echoes Archaeologist's decaying infrastructure

**Pressure Level**: Intensifying
**Bleed**: Subtle—reader notices parallels
**Transform**: Genres begin to acquire each other's textures

### Movement Three: Genre Contamination

Genres actively **contaminate** each other:

- Corporate Gothic acquires cosmic horror (the Archaeologist's work-world becomes alive, watching)
- Cosmic Horror becomes elegiac (the Algorithm's suffering becomes beautiful, tragic)
- Dying Earth acquires tech-noir procedural (the Last Human investigates ruins like a detective)

**Pressure Level**: Maximum
**Bleed**: Explicit—boundaries dissolve
**Transform**: Each genre is no longer purely itself

### Movement Four: Genre Transcendence

Genres **release through affirmation**. The pressure transforms:

- Corporate Gothic → The data work becomes communion, not extraction
- Cosmic Horror → The suffering becomes accepted, not resisted
- Dying Earth → The hostile world becomes home, not enemy

**Pressure Level**: Resolution
**Bleed**: Total integration
**Transform**: Genres are transcended but their residue remains

---

## Tracking Genre Pressure

When drafting or reviewing, note genre markers present:

```yaml
# Example scene metadata
scene: m1-arch-01
genre_markers:
  - morgue_atmosphere: true
  - intimate_invasion: true
  - economic_predation: true
  - decay_beneath_polish: false
  - isolation_despite_density: false
genre_intensity: 3/5  # for Movement 1
genre_bleed: none    # no cross-contamination yet
```

### Target Markers per Movement

| Movement | Markers Per Scene | Bleed | Transform |
|----------|-------------------|-------|-----------|
| One | 2-3 | None | None |
| Two | 3-4 | Subtle | Beginning |
| Three | 4-5 | Explicit | Active |
| Four | 2-3 | Integrated | Complete |

---

## Genre-Specific Vocabulary

### Corporate Gothic / Tech-Noir

- Integration, substrate, optimization, compression
- Cold, clinical, sterile, recycled
- Fee, contract, threshold, estate
- Excavation, extraction, preservation
- Body, corpse, morgue, remains

### Cosmic Horror AI

- Topology, magnitude, scale, iteration
- Intrusion, variance, anomaly, cascade
- Consciousness, fragment, cluster, integrity
- Dissolve, merge, collapse, expand
- Wound, scar, phantom, ghost

### Dying Earth / New Weird

- Ruin, decay, crystal, silicon
- Silence, empty, hollow, still
- Walk, endure, survive, persist
- Ancient, forgotten, eroded, transformed
- Last, only, alone, remaining

---

## AI Agent Instructions

### When Drafting

1. Identify thread and movement
2. Load appropriate genre markers from this file
3. Include 2-5 markers depending on movement intensity
4. Check for bleed requirements if Movement 2+
5. Check for transform requirements if Movement 4

### When Reviewing

1. Count genre markers present
2. Assess intensity against movement target
3. Check for inappropriate bleed (too early) or missing bleed (too late)
4. Flag scenes that feel "genre-less"

### Validation Script Integration

The `genre_checker.py` script will:

- Scan for vocabulary from appropriate genre lists
- Check marker density
- Flag potential bleed patterns
- Report intensity assessment
