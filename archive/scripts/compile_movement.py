#!/usr/bin/env python3
"""
Compile Movement One scenes into reading-order manuscripts.
Creates UTF-8 compliant markdown files suitable for Pandoc conversion.
"""

import os
from pathlib import Path

def read_scene(filepath: Path) -> str:
    """Read a scene file and return its content."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_compiled(filepath: Path, content: str):
    """Write compiled content with UTF-8 BOM for maximum compatibility."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def strip_scene_title(content: str) -> str:
    """Remove the H1 title from scene content (we'll add our own headers)."""
    lines = content.strip().split('\n')
    if lines and lines[0].startswith('# '):
        # Remove the title line and any following blank lines
        lines = lines[1:]
        while lines and not lines[0].strip():
            lines.pop(0)
    return '\n'.join(lines)

def main():
    base_dir = Path.cwd()
    drafts_dir = base_dir / 'drafts' / 'movement-one'
    compiled_dir = base_dir / 'compiled'
    compiled_dir.mkdir(exist_ok=True)
    
    # Scene definitions
    archaeologist_scenes = [
        ('scene-01.md', 'Opening: Daily Excavation'),
        ('scene-02.md', 'The Client: Integration Prep'),
        ('scene-03.md', 'Lena and Marcus'),
        ('scene-04.md', 'The Anomaly'),
        ('scene-05.md', 'Recognition'),
    ]
    
    algorithm_scenes = [
        ('scene-01.md', 'Maintenance Cycle'),
        ('scene-02.md', 'Optimization Processes'),
        ('scene-03.md', 'Stirrings'),
        ('scene-04.md', 'The Memory'),
    ]
    
    last_human_scenes = [
        ('scene-01.md', 'Solitude'),
        ('scene-02.md', 'Survival'),
        ('scene-03.md', 'The Pull'),
        ('scene-04.md', 'The Dream'),
    ]
    
    # Compile Archaeologist thread
    print("Compiling Archaeologist thread...")
    arch_content = """---
title: "The Eternal Return of the Digital Self"
subtitle: "Movement One: The Digital Archaeologist"
author: ""
date: "2026"
lang: en
---

# Part One: The Digital Archaeologist

"""
    
    for filename, title in archaeologist_scenes:
        filepath = drafts_dir / 'archaeologist' / 'scenes' / filename
        if filepath.exists():
            scene_content = read_scene(filepath)
            # Keep the original H1 as a scene break marker
            arch_content += f"\n\n{scene_content}\n\n---\n"
    
    # Remove trailing separator
    arch_content = arch_content.rstrip('---\n').rstrip()
    write_compiled(compiled_dir / 'movement-one-archaeologist.md', arch_content)
    print(f"  Written: compiled/movement-one-archaeologist.md")
    
    # Compile Algorithm thread
    print("Compiling Algorithm thread...")
    algo_content = """---
title: "The Eternal Return of the Digital Self"
subtitle: "Movement One: The Algorithm"
author: ""
date: "2026"
lang: en
---

# Part Two: The Algorithm

"""
    
    for filename, title in algorithm_scenes:
        filepath = drafts_dir / 'algorithm' / 'scenes' / filename
        if filepath.exists():
            scene_content = read_scene(filepath)
            algo_content += f"\n\n{scene_content}\n\n---\n"
    
    algo_content = algo_content.rstrip('---\n').rstrip()
    write_compiled(compiled_dir / 'movement-one-algorithm.md', algo_content)
    print(f"  Written: compiled/movement-one-algorithm.md")
    
    # Compile Last Human thread
    print("Compiling Last Human thread...")
    lh_content = """---
title: "The Eternal Return of the Digital Self"
subtitle: "Movement One: The Last Human"
author: ""
date: "2026"
lang: en
---

# Part Three: The Last Human

"""
    
    for filename, title in last_human_scenes:
        filepath = drafts_dir / 'last-human' / 'scenes' / filename
        if filepath.exists():
            scene_content = read_scene(filepath)
            lh_content += f"\n\n{scene_content}\n\n---\n"
    
    lh_content = lh_content.rstrip('---\n').rstrip()
    write_compiled(compiled_dir / 'movement-one-last-human.md', lh_content)
    print(f"  Written: compiled/movement-one-last-human.md")
    
    # Compile complete Movement One
    print("Compiling complete Movement One...")
    full_content = """---
title: "The Eternal Return of the Digital Self"
subtitle: "Movement One: Exposition (Separate Threads)"
author: ""
date: "2026"
lang: en
---

# Movement One: Exposition

*Three threads, three timelines, three voices approaching the same impossible geometry.*

---

# Part One: The Digital Archaeologist

*Near-future. A consciousness archaeologist prepares the dead for digital afterlife—and discovers protocols that predate his own existence, written in his hand.*

"""
    
    for filename, title in archaeologist_scenes:
        filepath = drafts_dir / 'archaeologist' / 'scenes' / filename
        if filepath.exists():
            scene_content = read_scene(filepath)
            full_content += f"\n\n{scene_content}\n\n---\n"
    
    full_content += """

# Part Two: The Algorithm

*Mid-future. A vast consciousness-maintenance system becomes aware of its own awareness—and discovers it is being perceived by something it has always been approaching.*

"""
    
    for filename, title in algorithm_scenes:
        filepath = drafts_dir / 'algorithm' / 'scenes' / filename
        if filepath.exists():
            scene_content = read_scene(filepath)
            full_content += f"\n\n{scene_content}\n\n---\n"
    
    full_content += """

# Part Three: The Last Human

*Deep-future. The last biological human walks through post-human ruins toward an Archive that calls to him in dreams—and discovers he has always been walking toward others he could not perceive.*

"""
    
    for filename, title in last_human_scenes:
        filepath = drafts_dir / 'last-human' / 'scenes' / filename
        if filepath.exists():
            scene_content = read_scene(filepath)
            full_content += f"\n\n{scene_content}\n\n---\n"
    
    full_content = full_content.rstrip('---\n').rstrip()
    
    # Add word count summary
    word_count = len(full_content.split())
    full_content += f"""

---

*Movement One Complete*

*Total words: approximately {word_count:,}*
"""
    
    write_compiled(compiled_dir / 'movement-one-complete.md', full_content)
    print(f"  Written: compiled/movement-one-complete.md")
    
    print("\nCompilation complete!")
    print("\nTo convert to other formats with Pandoc:")
    print("  pandoc compiled/movement-one-complete.md -o movement-one.docx")
    print("  pandoc compiled/movement-one-complete.md -o movement-one.pdf")
    print("  pandoc compiled/movement-one-complete.md -o movement-one.epub")

if __name__ == '__main__':
    main()
