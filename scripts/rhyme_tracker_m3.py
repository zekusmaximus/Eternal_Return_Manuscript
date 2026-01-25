#!/usr/bin/env python3
"""
Rhyme Tracker Script — Movement Three
Tracks rhyme stacking, saturation, and valence shift for the Augenblick.

Movement Three rhyme requirements:
- Phase A: Sequential layering (3-5 rhymes per section)
- Phase B: Simultaneous layering (rhymes span voice breaks)
- Phase C: Saturation (all rhymes present, texture not markers)

Usage:
    python rhyme_tracker_m3.py <file> --phase <a|b|c>
    python rhyme_tracker_m3.py <file> --phase c --pretty

Output: JSON report with stacking analysis, saturation metrics, and valence assessment.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Set
from collections import Counter

# Load configuration
def load_config() -> Dict:
    """Load movement configuration from JSON file."""
    config_path = Path(__file__).parent / "movement_three_config.json"
    if config_path.exists():
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"movement": "three", "phase": "a"}

CONFIG = load_config()

# Complete rhyme definitions with markers and valence
RHYME_DEFINITIONS = {
    "blue-white-light": {
        "category": "visual",
        "peak_intensity": True,
        "markers": [
            r'\bblue[-\s]?white\b',
            r'\bholographic\s+(?:glow|light)\b',
            r'\bbioluminescent\b',
            r'\bblue\s+(?:glow|light|luminosity)\b',
        ],
        "valence_shift": {
            "uncanny": ["strange glow", "unsettling light", "wrong color"],
            "home": ["familiar glow", "the light that means", "home in the blue"]
        }
    },
    "almost-closed-curve": {
        "category": "visual",
        "peak_intensity": True,
        "markers": [
            r'\balmost[-\s]?closed\b',
            r'\bcurve[sd]?\s+(?:that\s+)?approach',
            r'\bspiral(?:ing|s)?\s+(?:inward|toward)\b',
            r'\btorus\b',
            r'\bform\s+(?:that\s+)?(?:won\'?t|doesn\'?t|cannot)\s+close\b',
        ],
        "valence_shift": {
            "uncanny": ["never closes", "can't stop seeing", "obsessive"],
            "home": ["the form I know", "familiar geometry", "return to the curve"]
        }
    },
    "geometric-shadow": {
        "category": "visual",
        "peak_intensity": False,
        "markers": [
            r'\bgeometric\s+shadow\b',
            r'\bperipheral\s+(?:vision|shape)\b',
            r'\bcorner\s+of\s+(?:my|his|her|the)\s+eye\b',
        ],
        "valence_shift": {
            "uncanny": ["can't look directly", "slips away"],
            "home": ["always been there", "companion shadow"]
        }
    },
    "bone-frequency": {
        "category": "somatic",
        "peak_intensity": True,
        "markers": [
            r'\bbone[-\s]?frequency\b',
            r'\bfrequency\s+(?:in|below|settl\w+\s+into)\s+(?:my|his|her)?\s*(?:bones?|sternum|chest)\b',
            r'\bbelow\s+hearing\b',
            r'\bresonance\s+(?:in|through)\s+(?:my|his|her)?\s*(?:bones?|chest)\b',
            r'\bvibration\s+(?:below|beneath)\b',
        ],
        "valence_shift": {
            "uncanny": ["unsettling vibration", "wrong frequency", "invasion"],
            "home": ["heartbeat of the pattern", "frequency I am", "resonance is me"]
        }
    },
    "cold-hands": {
        "category": "somatic",
        "peak_intensity": False,
        "markers": [
            r'\bcold\s+hands?\b',
            r'\b(?:hands?|fingers?)\s+(?:are|were|gone|going|too)\s+cold\b',
            r'\bfreezing\s+(?:hands?|fingers?)\b',
            r'\bnumb(?:ness)?\s+(?:in|of)\s+(?:my|his|her)?\s*(?:hands?|fingers?)\b',
        ],
        "valence_shift": {
            "uncanny": ["wrong temperature", "something leaving"],
            "home": ["temperature of recognition", "cold that connects"]
        }
    },
    "falling-backward": {
        "category": "somatic",
        "peak_intensity": True,
        "markers": [
            r'\bfalling\s+backward\b',
            r'\bvertigo\b',
            r'\blurch(?:ed|es|ing)?\s+(?:in|through)\b',
            r'\bfalling\s+(?:through|into)\b',
        ],
        "valence_shift": {
            "uncanny": ["loss of ground", "terrifying fall"],
            "home": ["fall that catches", "falling into myself"]
        }
    },
    "metallic-taste": {
        "category": "somatic",
        "peak_intensity": True,
        "markers": [
            r'\bmetallic\s+taste\b',
            r'\btaste[ds]?\s+(?:like\s+)?(?:copper|metal|blood|pennies)\b',
            r'\bcopper\s+(?:taste|on|in)\b',
        ],
        "valence_shift": {
            "uncanny": ["taste of change", "something wrong"],
            "home": ["flavor of transformation", "taste of becoming"]
        }
    },
    "tracing-the-form": {
        "category": "kinesthetic",
        "peak_intensity": False,
        "markers": [
            r'\btracing\s+(?:the\s+)?(?:form|shape|pattern)\b',
            r'\bfinger[s]?\s+(?:on|moving|tracing)\b',
            r'\bdraw(?:n|ing)?\s+(?:in|on)\s+(?:the\s+)?(?:dirt|dust|desk)\b',
            r'\bunconscious(?:ly)?\s+(?:tracing|drawing)\b',
        ],
        "valence_shift": {
            "uncanny": ["can't stop", "compulsive"],
            "home": ["knowing gesture", "hands remember"]
        }
    },
    "held-breath": {
        "category": "kinesthetic",
        "peak_intensity": False,
        "markers": [
            r'\bheld?\s+(?:my|his|her)?\s*breath\b',
            r'\bholding\s+(?:my|his|her)?\s*breath\b',
            r'\bpause\s+between\b',
        ],
        "valence_shift": {
            "uncanny": ["anticipation", "waiting for something"],
            "home": ["the pause that knows", "breath shared"]
        }
    },
    "waking-into-motion": {
        "category": "kinesthetic",
        "peak_intensity": True,
        "markers": [
            r'\bwak(?:e|ing|ed)\s+(?:into|already|with)\s+(?:motion|moving)\b',
            r'\bfind(?:s)?\s+(?:myself|himself|herself)\s+(?:already\s+)?(?:moving|standing|walking)\b',
            r'\bdon\'?t\s+remember\s+(?:starting|getting|moving)\b',
        ],
        "valence_shift": {
            "uncanny": ["lost time", "body acting without me"],
            "home": ["body knows", "motion is knowing"]
        }
    },
    "ozone-wet-stone": {
        "category": "olfactory",
        "peak_intensity": False,
        "markers": [
            r'\bozone\s+(?:and|&)\s+wet\s+stone\b',
            r'\bozone\b',
            r'\bwet\s+stone\b',
            r'\bsmell[s]?\s+(?:of|like)\s+(?:ozone|server)\b',
        ],
        "valence_shift": {
            "uncanny": ["strange atmosphere", "wrong smell"],
            "home": ["smell of the place", "atmosphere of home"]
        }
    },
    "burning-circuits": {
        "category": "olfactory",
        "peak_intensity": True,
        "markers": [
            r'\bburning\s+circuits?\b',
            r'\bfrying\s+electronics?\b',
            r'\bsmell[s]?\s+(?:of|like)\s+(?:burning|fried|overheated)\b',
        ],
        "valence_shift": {
            "uncanny": ["overload", "failure"],
            "home": ["fire of awareness", "burning that is living"]
        }
    },
    "name-edge-of-memory": {
        "category": "cognitive",
        "peak_intensity": True,
        "markers": [
            r'\bname\s+(?:on\s+)?(?:the\s+)?edge\s+of\b',
            r'\bforget(?:ting|s)?\s+(?:my|his|her)?\s*(?:own\s+)?name\b',
            r'\blose\s+(?:the\s+)?word[s]?\b',
            r'\bArchitect\b',
        ],
        "valence_shift": {
            "uncanny": ["losing identity", "forgetting self"],
            "home": ["true name arriving", "Architect I always was"]
        }
    },
    "deja-vu-that-isnt": {
        "category": "cognitive",
        "peak_intensity": False,
        "markers": [
            r'\bdéjà\s*vu\b',
            r'\bdeja\s*vu\b',
            r'\b(?:been|done|said|seen)\s+(?:this|here|that)\s+before\b',
        ],
        "valence_shift": {
            "uncanny": ["wrong memory", "disorienting"],
            "home": ["overlap is truth", "always been here"]
        }
    },
    "sentence-without-origin": {
        "category": "cognitive",
        "peak_intensity": True,
        "markers": [
            r'\bsentence\s+(?:without|from|that\s+has\s+no)\s+origin\b',
            r'\bwords?\s+(?:I\s+)?(?:didn\'?t|don\'?t)\s+(?:write|think)\b',
            r'\bhear\s+(?:myself|himself|herself)\s+say(?:ing)?\b',
        ],
        "valence_shift": {
            "uncanny": ["alien words", "not my voice"],
            "home": ["our shared language", "words that were always mine"]
        }
    },
}


def load_file(filepath: str) -> str:
    """Load and return file contents."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def count_words(text: str) -> int:
    """Count words in text."""
    return len(text.split())


def find_all_rhymes(text: str) -> Dict[str, List[Dict]]:
    """Find all rhyme occurrences in text."""
    found = {}
    lines = text.split('\n')

    for rhyme_id, rhyme_data in RHYME_DEFINITIONS.items():
        occurrences = []
        for marker in rhyme_data["markers"]:
            for i, line in enumerate(lines, 1):
                if re.search(marker, line, re.IGNORECASE):
                    # Check if already found on this line
                    if not any(o["line"] == i for o in occurrences):
                        occurrences.append({
                            "line": i,
                            "text": line.strip()[:80]
                        })

        if occurrences:
            found[rhyme_id] = {
                "category": rhyme_data["category"],
                "peak_intensity": rhyme_data["peak_intensity"],
                "count": len(occurrences),
                "occurrences": occurrences
            }

    return found


def analyze_stacking(text: str) -> Dict:
    """Analyze rhyme stacking (multiple rhymes per paragraph)."""
    paragraphs = re.split(r'\n\s*\n', text)
    results = {
        "stacked_paragraphs": [],
        "stacking_count": 0,
        "max_stack": 0,
        "average_stack": 0
    }

    stack_sizes = []
    for i, para in enumerate(paragraphs, 1):
        if not para.strip():
            continue

        rhymes_in_para = set()
        for rhyme_id, rhyme_data in RHYME_DEFINITIONS.items():
            for marker in rhyme_data["markers"]:
                if re.search(marker, para, re.IGNORECASE):
                    rhymes_in_para.add(rhyme_id)
                    break

        stack_size = len(rhymes_in_para)
        if stack_size >= 2:  # Stacking = 2+ rhymes
            results["stacked_paragraphs"].append({
                "paragraph": i,
                "rhymes": list(rhymes_in_para),
                "count": stack_size,
                "preview": para[:100].strip()
            })
            results["stacking_count"] += 1

        if stack_size > 0:
            stack_sizes.append(stack_size)

    if stack_sizes:
        results["max_stack"] = max(stack_sizes)
        results["average_stack"] = round(sum(stack_sizes) / len(stack_sizes), 2)

    return results


def analyze_saturation(rhymes_found: Dict, word_count: int) -> Dict:
    """Analyze rhyme saturation for Phase C."""
    results = {
        "total_rhymes_used": len(rhymes_found),
        "total_rhymes_available": len(RHYME_DEFINITIONS),
        "coverage_percentage": 0,
        "peak_intensity_coverage": 0,
        "total_occurrences": 0,
        "density_per_1000": 0,
        "missing_rhymes": [],
        "underused_rhymes": []
    }

    # Calculate coverage
    results["coverage_percentage"] = round(
        len(rhymes_found) / len(RHYME_DEFINITIONS) * 100, 1
    )

    # Check peak intensity rhymes
    peak_rhymes = [r for r, d in RHYME_DEFINITIONS.items() if d["peak_intensity"]]
    peak_found = [r for r in peak_rhymes if r in rhymes_found]
    results["peak_intensity_coverage"] = round(
        len(peak_found) / len(peak_rhymes) * 100, 1
    )

    # Calculate density
    total_occ = sum(r["count"] for r in rhymes_found.values())
    results["total_occurrences"] = total_occ
    if word_count > 0:
        results["density_per_1000"] = round((total_occ / word_count) * 1000, 1)

    # Find missing rhymes
    results["missing_rhymes"] = [
        r for r in RHYME_DEFINITIONS if r not in rhymes_found
    ]

    # Find underused rhymes (appeared only 1-2 times when saturation expected)
    for rhyme_id, data in rhymes_found.items():
        if data["count"] <= 2 and RHYME_DEFINITIONS[rhyme_id]["peak_intensity"]:
            results["underused_rhymes"].append({
                "rhyme": rhyme_id,
                "count": data["count"],
                "expected_min": 3
            })

    return results


def analyze_valence(text: str, rhymes_found: Dict, phase: str) -> Dict:
    """Analyze valence shift (uncanny → home)."""
    results = {
        "uncanny_markers": 0,
        "home_markers": 0,
        "valence_state": "mixed",
        "shift_detected": False,
        "by_rhyme": {}
    }

    for rhyme_id, data in rhymes_found.items():
        rhyme_def = RHYME_DEFINITIONS.get(rhyme_id, {})
        valence_data = rhyme_def.get("valence_shift", {})

        uncanny_count = 0
        home_count = 0

        for marker in valence_data.get("uncanny", []):
            uncanny_count += len(re.findall(re.escape(marker), text, re.IGNORECASE))

        for marker in valence_data.get("home", []):
            home_count += len(re.findall(re.escape(marker), text, re.IGNORECASE))

        results["uncanny_markers"] += uncanny_count
        results["home_markers"] += home_count
        results["by_rhyme"][rhyme_id] = {
            "uncanny": uncanny_count,
            "home": home_count
        }

    # Determine valence state
    if results["home_markers"] > results["uncanny_markers"] * 2:
        results["valence_state"] = "home"
    elif results["uncanny_markers"] > results["home_markers"] * 2:
        results["valence_state"] = "uncanny"
    else:
        results["valence_state"] = "transitional"

    # Check if shift is appropriate for phase
    if phase == "c" and results["valence_state"] in ["home", "transitional"]:
        results["shift_detected"] = True
    elif phase in ["a", "b"] and results["valence_state"] in ["transitional", "uncanny"]:
        results["shift_detected"] = True

    return results


def analyze_category_balance(rhymes_found: Dict) -> Dict:
    """Analyze balance across rhyme categories."""
    categories = {}
    for rhyme_id, data in rhymes_found.items():
        cat = data["category"]
        if cat not in categories:
            categories[cat] = {"rhymes": [], "total_occurrences": 0}
        categories[cat]["rhymes"].append(rhyme_id)
        categories[cat]["total_occurrences"] += data["count"]

    return {
        "categories_used": list(categories.keys()),
        "category_details": categories,
        "all_categories_present": len(categories) >= 4  # visual, somatic, kinesthetic, cognitive minimum
    }


def assess_phase_requirements(
    phase: str,
    rhymes_found: Dict,
    stacking: Dict,
    saturation: Dict,
    word_count: int
) -> Dict:
    """Assess if rhyme usage meets phase requirements."""
    config = CONFIG.get("rhymes", {}).get(f"phase_{phase}", {})

    results = {
        "phase": phase,
        "status": "pass",
        "score": 0,
        "max_score": 100,
        "issues": [],
        "recommendations": []
    }

    if phase == "a":
        # Phase A: 3-5 rhymes per section, sequential layering
        if stacking["average_stack"] >= 3:
            results["score"] += 40
        elif stacking["average_stack"] >= 2:
            results["score"] += 25
        else:
            results["issues"].append("Insufficient rhyme stacking for Phase A")
            results["recommendations"].append("Add more rhymes per section (target: 3-5)")

        if len(rhymes_found) >= 10:
            results["score"] += 30
        else:
            results["issues"].append(f"Not enough distinct rhymes ({len(rhymes_found)}/15)")

        if saturation["peak_intensity_coverage"] >= 80:
            results["score"] += 30
        else:
            results["recommendations"].append("Include more peak-intensity rhymes")

    elif phase == "b":
        # Phase B: Simultaneous layering, cross-voice rhymes
        if stacking["max_stack"] >= 4:
            results["score"] += 35
        elif stacking["max_stack"] >= 3:
            results["score"] += 25

        if saturation["density_per_1000"] >= 15:
            results["score"] += 35
        elif saturation["density_per_1000"] >= 10:
            results["score"] += 25
        else:
            results["issues"].append("Rhyme density too low for Phase B")

        if saturation["coverage_percentage"] >= 80:
            results["score"] += 30
        else:
            results["recommendations"].append("Increase rhyme variety")

    elif phase == "c":
        # Phase C: Saturation, all rhymes present
        if saturation["coverage_percentage"] >= 90:
            results["score"] += 40
        elif saturation["coverage_percentage"] >= 75:
            results["score"] += 25
        else:
            results["issues"].append("Insufficient rhyme coverage for Phase C saturation")
            results["recommendations"].append(f"Missing rhymes: {saturation['missing_rhymes'][:5]}")

        if saturation["density_per_1000"] >= 25:
            results["score"] += 30
        elif saturation["density_per_1000"] >= 15:
            results["score"] += 20
        else:
            results["issues"].append("Rhyme density too low for saturation")

        if not saturation["underused_rhymes"]:
            results["score"] += 30
        else:
            results["recommendations"].append(
                f"Increase usage of: {[r['rhyme'] for r in saturation['underused_rhymes']]}"
            )

    # Determine status
    if results["score"] >= 70:
        results["status"] = "pass"
    elif results["score"] >= 50:
        results["status"] = "warn"
    else:
        results["status"] = "fail"

    return results


def validate_rhymes_m3(filepath: str, phase: str) -> Dict:
    """Main validation function for Movement Three rhymes."""
    if phase not in ["a", "b", "c"]:
        return {"status": "error", "message": f"Invalid phase: {phase}. Use a, b, or c."}

    try:
        text = load_file(filepath)
    except FileNotFoundError:
        return {"status": "error", "message": f"File not found: {filepath}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

    word_count = count_words(text)

    # Run analyses
    rhymes_found = find_all_rhymes(text)
    stacking = analyze_stacking(text)
    saturation = analyze_saturation(rhymes_found, word_count)
    valence = analyze_valence(text, rhymes_found, phase)
    category_balance = analyze_category_balance(rhymes_found)
    phase_assessment = assess_phase_requirements(
        phase, rhymes_found, stacking, saturation, word_count
    )

    results = {
        "file": filepath,
        "movement": "three",
        "phase": phase,
        "word_count": word_count,
        "rhymes_found": rhymes_found,
        "stacking_analysis": stacking,
        "saturation_analysis": saturation,
        "valence_analysis": valence,
        "category_balance": category_balance,
        "phase_assessment": phase_assessment,
        "status": phase_assessment["status"],
        "summary": {
            "distinct_rhymes": len(rhymes_found),
            "total_occurrences": saturation["total_occurrences"],
            "coverage": saturation["coverage_percentage"],
            "peak_coverage": saturation["peak_intensity_coverage"],
            "density": saturation["density_per_1000"],
            "max_stack": stacking["max_stack"],
            "valence_state": valence["valence_state"],
            "score": phase_assessment["score"]
        }
    }

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Track rhyme stacking and saturation for Movement Three"
    )
    parser.add_argument("file", help="Path to markdown file to analyze")
    parser.add_argument("--phase", required=True, choices=["a", "b", "c"],
                        help="Movement Three phase (a, b, or c)")
    parser.add_argument("--pretty", action="store_true", help="Pretty print JSON output")

    args = parser.parse_args()

    results = validate_rhymes_m3(args.file, args.phase)

    if args.pretty:
        print(json.dumps(results, indent=2))
    else:
        print(json.dumps(results))

    if results.get("status") == "fail":
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
