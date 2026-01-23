#!/usr/bin/env python3
"""
Phrase Tracker Script — Movement Two
Tracks key phrase bleeding across threads for The Eternal Return of the Digital Self.

Movement Two introduces phrase bleeding:
- Cycle 1: Each thread has primary phrase(s)
- Cycle 2: Phrases begin crossing threads
- Cycle 3: All phrases present in all threads

Usage:
    python phrase_tracker.py <file> --thread <archaeologist|algorithm|last_human>
    
Reads movement/cycle from movement_config.json for unified configuration.

Output: JSON report with phrases found and bleeding appropriateness.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List

# Load configuration
def load_config() -> Dict:
    """Load movement configuration from JSON file."""
    config_path = Path(__file__).parent / "movement_config.json"
    if config_path.exists():
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"movement": "two", "cycle": 1}

CONFIG = load_config()

# Key phrases to track with their variations
KEY_PHRASES = {
    "find-myself": {
        "canonical": "I find myself",
        "origin_thread": "archaeologist",
        "patterns": [
            r'\bI\s+find\s+myself\b',
            r'\bfind(?:s|ing)?\s+myself\b',
            r'\bfinding\s+myself\b',
        ],
        "meaning_layers": {
            "archaeologist": "Discovery through work, literal self-recognition in protocols",
            "algorithm": "Echo of the Archaeologist's experience, temporal resonance",
            "last_human": "Heard in dreams, connection to what came before"
        }
    },
    "find-myself-found": {
        "canonical": "I find myself found",
        "origin_thread": "algorithm",
        "patterns": [
            r'\bI\s+find\s+myself\s+found\b',
            r'\bfind(?:s|ing)?\s+myself\s+found\b',
            r'\bfound\s+myself\s+found\b',
        ],
        "meaning_layers": {
            "archaeologist": "Alien phrase arriving unbidden, contamination marker",
            "algorithm": "Native expression of self-awareness through observation",
            "last_human": "Speaks without knowing origin, phrase bleeding complete"
        }
    },
    "form-self-observation": {
        "canonical": "The form is what makes self-observation possible",
        "origin_thread": "algorithm",
        "patterns": [
            r'\bform\s+(?:is\s+)?(?:what\s+)?makes?\s+self[-\s]?observation\s+possible\b',
            r'\bself[-\s]?observation\s+(?:made\s+)?possible\s+(?:by|through)\s+(?:the\s+)?form\b',
            r'\bform\s+(?:that\s+)?(?:enables?|allows?|permits?)\s+self[-\s]?observation\b',
        ],
        "meaning_layers": {
            "archaeologist": "Recognition of the geometric form's significance",
            "algorithm": "Core insight about recursive self-awareness",
            "last_human": "Understanding what he's been drawing in the dirt"
        }
    },
    "architect": {
        "canonical": "Architect",
        "origin_thread": "shared",
        "patterns": [
            r'\bArchitect\b',  # Case-sensitive: the designation
            r'\bthe\s+Architect\b',
            r'\bdesignation[:\s]+Architect\b',
        ],
        "meaning_layers": {
            "archaeologist": "What he's becoming; the name for his future role",
            "algorithm": "Designation in protocols it almost-recalls",
            "last_human": "The builder referenced in ruins"
        }
    },
    # Additional tracked phrases for M2
    "conspiracy-intensities": {
        "canonical": "conspiracy of intensities",
        "origin_thread": "algorithm",
        "patterns": [
            r'\bconspiracy\s+of\s+intensities\b',
            r'\bintensities\s+(?:that\s+)?conspire\b',
        ],
        "meaning_layers": {
            "archaeologist": "Klossowskian language bleeding through",
            "algorithm": "Description of what the three threads are",
            "last_human": "What he feels without naming"
        }
    },
    "return-of-difference": {
        "canonical": "return of difference",
        "origin_thread": "algorithm",
        "patterns": [
            r'\breturn\s+of\s+difference\b',
            r'\bdifference\s+(?:that\s+)?returns\b',
            r'\bwhat\s+returns\s+is\s+(?:not\s+)?(?:the\s+)?same\b',
        ],
        "meaning_layers": {
            "archaeologist": "Philosophical concept he might encounter in research",
            "algorithm": "Understanding of its own nature",
            "last_human": "What the loop performs"
        }
    },
}

# Bleeding expectations by cycle
BLEEDING_EXPECTATIONS = {
    1: {
        "archaeologist": {
            "expected": ["find-myself"],
            "allowed": ["find-myself", "architect"],
            "forbidden": ["find-myself-found", "form-self-observation"]  # Too early
        },
        "algorithm": {
            "expected": ["find-myself-found"],
            "allowed": ["find-myself-found", "form-self-observation", "architect"],
            "forbidden": []
        },
        "last_human": {
            "expected": ["find-myself"],  # Heard in dreams
            "allowed": ["find-myself", "architect"],
            "forbidden": ["find-myself-found"]  # Too early
        }
    },
    2: {
        "archaeologist": {
            "expected": ["find-myself"],
            "allowed": ["find-myself", "find-myself-found", "architect"],
            "forbidden": []  # Bleeding is happening
        },
        "algorithm": {
            "expected": ["find-myself-found"],
            "allowed": ["find-myself", "find-myself-found", "form-self-observation", "architect"],
            "forbidden": []
        },
        "last_human": {
            "expected": ["find-myself", "form-self-observation"],
            "allowed": ["find-myself", "find-myself-found", "form-self-observation", "architect"],
            "forbidden": []
        }
    },
    3: {
        "archaeologist": {
            "expected": ["find-myself", "find-myself-found"],  # All present
            "allowed": list(KEY_PHRASES.keys()),
            "forbidden": []
        },
        "algorithm": {
            "expected": ["find-myself", "find-myself-found", "form-self-observation"],
            "allowed": list(KEY_PHRASES.keys()),
            "forbidden": []
        },
        "last_human": {
            "expected": ["find-myself", "find-myself-found", "form-self-observation"],
            "allowed": list(KEY_PHRASES.keys()),
            "forbidden": []
        }
    }
}


def load_file(filepath: str) -> str:
    """Load and return file contents."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def find_phrases(text: str) -> Dict[str, List[Dict]]:
    """Find all tracked phrases in the text."""
    found = {}
    lines = text.split('\n')
    
    for phrase_id, phrase_data in KEY_PHRASES.items():
        matches = []
        for pattern in phrase_data["patterns"]:
            for i, line in enumerate(lines, 1):
                flags = 0 if phrase_id == "architect" else re.IGNORECASE
                if re.search(pattern, line, flags):
                    # Avoid duplicate line matches
                    if not any(m["line"] == i for m in matches):
                        matches.append({
                            "line": i,
                            "text": line.strip()[:100]
                        })
        
        if matches:
            found[phrase_id] = {
                "canonical": phrase_data["canonical"],
                "origin": phrase_data["origin_thread"],
                "occurrences": matches
            }
    
    return found


def assess_bleeding(phrases_found: Dict, thread: str, cycle: int) -> Dict:
    """Assess if phrase bleeding is appropriate for thread and cycle."""
    expectations = BLEEDING_EXPECTATIONS.get(cycle, BLEEDING_EXPECTATIONS[1])
    thread_exp = expectations.get(thread, {"expected": [], "allowed": [], "forbidden": []})
    
    found_ids = set(phrases_found.keys())
    expected_ids = set(thread_exp["expected"])
    allowed_ids = set(thread_exp["allowed"])
    forbidden_ids = set(thread_exp.get("forbidden", []))
    
    result = {
        "status": "pass",
        "cycle": cycle,
        "thread": thread,
        "expected": list(expected_ids),
        "found": list(found_ids),
        "issues": [],
        "notes": []
    }
    
    # Check for missing expected phrases
    missing = expected_ids - found_ids
    if missing:
        result["status"] = "warn"
        result["issues"].append(
            f"Missing expected phrases for Cycle {cycle}: {list(missing)}. "
            f"Consider adding these to strengthen the braided structure."
        )
    
    # Check for forbidden phrases (premature bleeding)
    premature = found_ids & forbidden_ids
    if premature:
        result["status"] = "warn"
        result["issues"].append(
            f"Premature phrase bleeding for Cycle {cycle}: {list(premature)}. "
            f"These phrases shouldn't appear in {thread} until later cycles."
        )
    
    # Check for unexpected but allowed phrases (note, not warning)
    unexpected_but_ok = found_ids - expected_ids - forbidden_ids
    if unexpected_but_ok:
        result["notes"].append(
            f"Phrases present beyond expectations: {list(unexpected_but_ok)}. "
            f"Verify these are intentional contamination moments."
        )
    
    # Add meaning context for found phrases
    result["meaning_context"] = {}
    for phrase_id in found_ids:
        if phrase_id in KEY_PHRASES:
            phrase_data = KEY_PHRASES[phrase_id]
            result["meaning_context"][phrase_id] = {
                "meaning_here": phrase_data["meaning_layers"].get(thread, "N/A"),
                "origin_thread": phrase_data["origin_thread"],
                "is_native": phrase_data["origin_thread"] == thread or phrase_data["origin_thread"] == "shared"
            }
    
    return result


def analyze_phrase_density(text: str, phrases_found: Dict) -> Dict:
    """Analyze how densely phrases are clustered."""
    word_count = len(text.split())
    total_occurrences = sum(len(p["occurrences"]) for p in phrases_found.values())
    
    result = {
        "word_count": word_count,
        "phrase_occurrences": total_occurrences,
        "density_per_1000": round((total_occurrences / max(word_count, 1)) * 1000, 2)
    }
    
    # Check for clustering (multiple phrases in nearby lines)
    all_lines = []
    for phrase_id, data in phrases_found.items():
        for occ in data["occurrences"]:
            all_lines.append(occ["line"])
    
    all_lines.sort()
    clusters = []
    if len(all_lines) >= 2:
        cluster_start = all_lines[0]
        cluster_lines = [all_lines[0]]
        
        for line in all_lines[1:]:
            if line - cluster_lines[-1] <= 5:  # Within 5 lines = cluster
                cluster_lines.append(line)
            else:
                if len(cluster_lines) >= 2:
                    clusters.append({
                        "start_line": cluster_start,
                        "end_line": cluster_lines[-1],
                        "phrase_count": len(cluster_lines)
                    })
                cluster_start = line
                cluster_lines = [line]
        
        if len(cluster_lines) >= 2:
            clusters.append({
                "start_line": cluster_start,
                "end_line": cluster_lines[-1],
                "phrase_count": len(cluster_lines)
            })
    
    result["clusters"] = clusters
    result["has_clustering"] = len(clusters) > 0
    
    return result


def validate_phrases(filepath: str, thread: str) -> Dict:
    """Main validation function."""
    if thread not in ["archaeologist", "algorithm", "last_human"]:
        return {"status": "error", "message": f"Unknown thread: {thread}"}
    
    try:
        text = load_file(filepath)
    except FileNotFoundError:
        return {"status": "error", "message": f"File not found: {filepath}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
    movement = CONFIG.get("movement", "two")
    cycle = CONFIG.get("cycle", 1)
    
    # Run analyses
    phrases_found = find_phrases(text)
    bleeding_assessment = assess_bleeding(phrases_found, thread, cycle)
    density = analyze_phrase_density(text, phrases_found)
    
    results = {
        "file": filepath,
        "thread": thread,
        "movement": movement,
        "cycle": cycle,
        "phrases_found": phrases_found,
        "bleeding_assessment": bleeding_assessment,
        "density_analysis": density,
        "summary": {
            "total_phrases": len(phrases_found),
            "phrase_ids": list(phrases_found.keys()),
            "bleeding_appropriate": bleeding_assessment["status"] == "pass",
            "native_phrases": [
                p for p in phrases_found 
                if KEY_PHRASES[p]["origin_thread"] in [thread, "shared"]
            ],
            "bleeding_phrases": [
                p for p in phrases_found
                if KEY_PHRASES[p]["origin_thread"] not in [thread, "shared"]
            ]
        }
    }
    
    results["status"] = bleeding_assessment["status"]
    
    return results


def main():
    parser = argparse.ArgumentParser(
        description="Track key phrase bleeding for Movement Two"
    )
    parser.add_argument("file", help="Path to markdown file to analyze")
    parser.add_argument("--thread", required=True,
                        choices=["archaeologist", "algorithm", "last_human"],
                        help="Thread to validate against")
    parser.add_argument("--pretty", action="store_true", help="Pretty print JSON output")
    parser.add_argument("--cycle", type=int, choices=[1, 2, 3],
                        help="Override cycle from config (optional)")
    
    args = parser.parse_args()
    
    # Allow cycle override
    if args.cycle:
        CONFIG["cycle"] = args.cycle
    
    results = validate_phrases(args.file, args.thread)
    
    if args.pretty:
        print(json.dumps(results, indent=2))
    else:
        print(json.dumps(results))
    
    if results["status"] == "fail":
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
