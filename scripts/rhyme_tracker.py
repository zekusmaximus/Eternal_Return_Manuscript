#!/usr/bin/env python3
"""
Rhyme Tracker Script — Movement Two
Tracks sensory rhyme usage with position awareness for braided narrative handoffs.

Movement Two rhymes must:
- OPEN scenes by catching a rhyme from the previous scene
- CLOSE scenes by releasing a rhyme for the next scene to catch
- Stack in Cycle 3 (multiple rhymes per paragraph)

Usage:
    python rhyme_tracker.py <file>
    python rhyme_tracker.py <file> --previous-closing '["bone-frequency"]'
    
Reads movement/cycle from movement_config.json for unified configuration.

Output: JSON report with position-aware rhyme analysis and handoff validation.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Set

# Load configuration
def load_config() -> Dict:
    """Load movement configuration from JSON file."""
    config_path = Path(__file__).parent / "movement_config.json"
    if config_path.exists():
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"movement": "two", "cycle": 1}

CONFIG = load_config()

# Rhyme definitions with markers
RHYME_MARKERS = {
    "blue-white-light": {
        "category": "visual",
        "description": "Holographic/bioluminescent glow",
        "markers": [
            r'\bblue[-\s]?white\b',
            r'\bholographic\s+(?:glow|light|interface)\b',
            r'\bbioluminescent\b',
            r'\bblue\s+(?:glow|light|luminosity)\b',
            r'\bprocessing\s+(?:intensity|glow)\b',
        ]
    },
    "almost-closed-curve": {
        "category": "visual",
        "description": "Geometric form that approaches but doesn't close",
        "markers": [
            r'\balmost[-\s]?closed\s+curve\b',
            r'\btorus(?:[-\s]?spiral)?\b',
            r'\bcurve[sd]?\s+(?:that\s+)?approach(?:es|ed|ing)?\b',
            r'\bspiral(?:ing|s)?\s+(?:inward|toward)\b',
            r'\bform\s+(?:that\s+)?(?:won\'?t|doesn\'?t|cannot)\s+(?:close|complete)\b',
        ]
    },
    "geometric-shadow": {
        "category": "visual",
        "description": "Shape at edge of vision",
        "markers": [
            r'\bgeometric\s+shadow\b',
            r'\bperipheral\s+(?:vision|shape)\b',
            r'\bcorner\s+of\s+(?:my|his|her|the)\s+eye\b',
            r'\bshadow[s]?\s+(?:that\s+)?(?:don\'?t|doesn\'?t)\s+match\b',
        ]
    },
    "bone-frequency": {
        "category": "somatic",
        "description": "Vibration felt in bones, below hearing",
        "markers": [
            r'\bbone[-\s]?frequency\b',
            r'\bfrequency\s+(?:in|below|settl\w+\s+into)\s+(?:my|his|her)?\s*(?:bones?|sternum|chest)\b',
            r'\bbelow\s+hearing\b',
            r'\bresonance\s+(?:in|through)\s+(?:my|his|her)?\s*(?:bones?|chest)\b',
            r'\bvibration\s+(?:below|beneath)\b',
        ]
    },
    "cold-hands": {
        "category": "somatic",
        "description": "Hands/fingers gone cold",
        "markers": [
            r'\bcold\s+hands?\b',
            r'\b(?:hands?|fingers?)\s+(?:are|were|gone|going|too)\s+cold\b',
            r'\bfreezing\s+(?:hands?|fingers?)\b',
            r'\bnumb(?:ness)?\s+(?:in|of)\s+(?:my|his|her)?\s*(?:hands?|fingers?)\b',
        ]
    },
    "falling-backward": {
        "category": "somatic",
        "description": "Vertigo/falling through sensation",
        "markers": [
            r'\bfalling\s+backward\b',
            r'\bvertigo\b',
            r'\blurch(?:ed|es|ing)?\s+(?:in|through)\b',
            r'\bfalling\s+(?:through|into)\b',
            r'\bground\s+(?:gone|vanished|disappeared)\b',
        ]
    },
    "metallic-taste": {
        "category": "somatic",
        "description": "Copper/blood taste",
        "markers": [
            r'\bmetallic\s+taste\b',
            r'\btaste[ds]?\s+(?:like\s+)?(?:copper|metal|blood|pennies)\b',
            r'\bcopper\s+(?:taste|on|in)\b',
            r'\bblood\s+(?:taste|in\s+(?:my|his|her)\s+mouth)\b',
        ]
    },
    "tracing-the-form": {
        "category": "kinesthetic",
        "description": "Unconsciously drawing the geometric form",
        "markers": [
            r'\btracing\s+(?:the\s+)?(?:form|shape|pattern)\b',
            r'\bfinger[s]?\s+(?:on|moving|tracing)\b',
            r'\bdraw(?:n|ing)?\s+(?:in|on)\s+(?:the\s+)?(?:dirt|dust|desk|surface)\b',
            r'\bunconscious(?:ly)?\s+(?:tracing|drawing|sketching)\b',
        ]
    },
    "held-breath": {
        "category": "kinesthetic",
        "description": "Pause between states",
        "markers": [
            r'\bheld?\s+(?:my|his|her)?\s*breath\b',
            r'\bholding\s+(?:my|his|her)?\s*breath\b',
            r'\bpause\s+between\b',
            r'\bsilence\s+before\b',
        ]
    },
    "waking-into-motion": {
        "category": "kinesthetic",
        "description": "Finding yourself already moving",
        "markers": [
            r'\bwak(?:e|ing|ed)\s+(?:into|already|with)\s+(?:motion|moving|walking)\b',
            r'\bfind(?:s)?\s+(?:myself|himself|herself)\s+(?:already\s+)?(?:moving|standing|walking)\b',
            r'\bdon\'?t\s+remember\s+(?:starting|getting|moving)\b',
            r'\bbody\s+(?:already|had been)\s+(?:here|there|moving)\b',
        ]
    },
    "ozone-wet-stone": {
        "category": "olfactory",
        "description": "Server room smell",
        "markers": [
            r'\bozone\s+(?:and|&)\s+wet\s+stone\b',
            r'\bozone\b',
            r'\bwet\s+stone\b',
            r'\bsmell[s]?\s+(?:of|like)\s+(?:ozone|electrical|server)\b',
        ]
    },
    "burning-circuits": {
        "category": "olfactory",
        "description": "Overheating electronics",
        "markers": [
            r'\bburning\s+circuits?\b',
            r'\bfrying\s+electronics?\b',
            r'\bsmell[s]?\s+(?:of|like)\s+(?:burning|fried|overheated)\b',
            r'\bprocessor[s]?\s+(?:overheated|burning)\b',
        ]
    },
    "name-edge-of-memory": {
        "category": "cognitive",
        "description": "Losing words/names",
        "markers": [
            r'\bname\s+(?:on\s+)?(?:the\s+)?edge\s+of\s+(?:my|his|her)?\s*memory\b',
            r'\bforget(?:ting|s)?\s+(?:my|his|her)?\s*(?:own\s+)?name\b',
            r'\blose\s+(?:the\s+)?word[s]?\b',
            r'\bwhat\s+(?:was\s+)?I\s+(?:about\s+)?(?:to\s+)?say\b',
            r'\bArchitect\b',  # The designation at edge of memory
        ]
    },
    "deja-vu-that-isnt": {
        "category": "cognitive",
        "description": "Temporal overlap sensation",
        "markers": [
            r'\bdéjà\s*vu\b',
            r'\bdeja\s*vu\b',
            r'\b(?:been|done|said|seen)\s+(?:this|here|that)\s+before\b',
            r'\bfeeling\s+of\s+(?:repetition|overlap)\b',
        ]
    },
    "sentence-without-origin": {
        "category": "cognitive",
        "description": "Words that arrive unbidden",
        "markers": [
            r'\bsentence\s+(?:without|from|that\s+has\s+no)\s+origin\b',
            r'\bwords?\s+(?:I\s+)?(?:didn\'?t|don\'?t)\s+(?:write|generate|think)\b',
            r'\bhear\s+(?:myself|himself|herself)\s+say(?:ing)?\b',
            r'\bwords?\s+(?:arrived|came)\s+(?:in|to)\s+(?:my|his|her)\s+mouth\b',
        ]
    },
}

# Zone boundaries (in words)
OPENING_ZONE_WORDS = 500
CLOSING_ZONE_WORDS = 500

THREAD_ORDER_CYCLE1 = ["archaeologist", "algorithm", "last_human"]


def load_file(filepath: str) -> str:
    """Load and return file contents."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def infer_thread_from_path(filepath: str) -> str:
    lower = filepath.lower()
    if "archaeologist" in lower:
        return "archaeologist"
    if "algorithm" in lower:
        return "algorithm"
    if "last-human" in lower or "last_human" in lower:
        return "last_human"
    return "unknown"


def order_sequence(filepaths: List[str], movement: str, cycle: int) -> List[str]:
    if movement == "two" and cycle == 1:
        thread_map = {fp: infer_thread_from_path(fp) for fp in filepaths}
        threads = list(thread_map.values())
        if all(t in THREAD_ORDER_CYCLE1 for t in threads):
            return sorted(filepaths, key=lambda fp: THREAD_ORDER_CYCLE1.index(thread_map[fp]))
    return filepaths


def get_text_zones(text: str) -> Dict[str, str]:
    """Split text into opening, middle, and closing zones."""
    words = text.split()
    total_words = len(words)
    
    if total_words <= OPENING_ZONE_WORDS + CLOSING_ZONE_WORDS:
        # Short text: everything is both opening and closing
        return {
            "opening": text,
            "middle": "",
            "closing": text
        }
    
    opening = ' '.join(words[:OPENING_ZONE_WORDS])
    closing = ' '.join(words[-CLOSING_ZONE_WORDS:])
    middle = ' '.join(words[OPENING_ZONE_WORDS:-CLOSING_ZONE_WORDS])
    
    return {
        "opening": opening,
        "middle": middle,
        "closing": closing
    }


def find_rhymes_in_text(text: str) -> Dict[str, List[Dict]]:
    """Find all rhymes present in the text."""
    found = {}
    lines = text.split('\n')
    
    for rhyme_id, rhyme_data in RHYME_MARKERS.items():
        matches = []
        for marker in rhyme_data["markers"]:
            for i, line in enumerate(lines, 1):
                if re.search(marker, line, re.IGNORECASE):
                    matches.append({
                        "line": i,
                        "text": line.strip()[:80]
                    })
        
        if matches:
            found[rhyme_id] = {
                "category": rhyme_data["category"],
                "description": rhyme_data["description"],
                "occurrences": matches
            }
    
    return found


def find_rhymes_with_positions(text: str) -> Dict:
    """Find rhymes and categorize by position (opening/middle/closing)."""
    zones = get_text_zones(text)
    
    opening_rhymes = list(find_rhymes_in_text(zones["opening"]).keys())
    closing_rhymes = list(find_rhymes_in_text(zones["closing"]).keys())
    middle_rhymes = list(find_rhymes_in_text(zones["middle"]).keys()) if zones["middle"] else []
    
    all_rhymes = find_rhymes_in_text(text)
    
    return {
        "all_rhymes": all_rhymes,
        "by_position": {
            "opening": opening_rhymes,
            "middle": middle_rhymes,
            "closing": closing_rhymes
        }
    }


def detect_stacking(text: str) -> List[Dict]:
    """Detect paragraphs with multiple rhymes (stacking)."""
    paragraphs = text.split('\n\n')
    stacked = []
    
    for i, paragraph in enumerate(paragraphs, 1):
        rhymes_in_para = []
        for rhyme_id, rhyme_data in RHYME_MARKERS.items():
            for marker in rhyme_data["markers"]:
                if re.search(marker, paragraph, re.IGNORECASE):
                    rhymes_in_para.append(rhyme_id)
                    break  # Only count each rhyme once per paragraph
        
        if len(rhymes_in_para) >= 3:
            stacked.append({
                "paragraph": i,
                "rhymes": rhymes_in_para,
                "count": len(rhymes_in_para),
                "preview": paragraph[:100].strip()
            })
    
    return stacked


def validate_handoff(opening_rhymes: List[str], previous_closing: List[str]) -> Dict:
    """Validate that opening rhymes catch from previous scene's closing."""
    if not previous_closing:
        return {
            "status": "skip",
            "message": "No previous scene closing rhymes provided"
        }
    
    caught = [r for r in opening_rhymes if r in previous_closing]
    missed = [r for r in previous_closing if r not in opening_rhymes]
    
    result = {
        "status": "pass" if caught else "warn",
        "caught": caught,
        "missed": missed,
        "handoff_complete": len(caught) > 0
    }
    
    if not caught:
        result["message"] = (
            f"Scene does not catch rhymes from previous scene. "
            f"Previous scene released: {previous_closing}. "
            f"Consider opening with one of these rhymes for continuity."
        )
    
    return result


def assess_intensity(rhyme_data: Dict, cycle: int) -> Dict:
    """Assess if rhyme usage is appropriate for the cycle."""
    rhyme_config = CONFIG.get("rhymes", {}).get("intensity", {})
    cycle_key = f"cycle_{cycle}"
    cycle_config = rhyme_config.get(cycle_key, {"min": 2, "max": 5})
    
    total_rhymes = len(rhyme_data["all_rhymes"])
    positions = rhyme_data["by_position"]
    
    result = {
        "status": "pass",
        "cycle": cycle,
        "expected_range": f"{cycle_config['min']}-{cycle_config['max']}",
        "actual": total_rhymes,
        "issues": [],
        "notes": []
    }
    
    # Check count
    if total_rhymes < cycle_config["min"]:
        result["status"] = "warn"
        result["issues"].append(
            f"Too few rhymes for Cycle {cycle}: found {total_rhymes}, expected ≥{cycle_config['min']}"
        )
    
    if total_rhymes > cycle_config["max"]:
        result["status"] = "warn"
        result["issues"].append(
            f"Too many rhymes for Cycle {cycle}: found {total_rhymes}, expected ≤{cycle_config['max']}"
        )
    
    # Check opening/closing requirements
    if cycle_config.get("opening_required") and not positions.get("opening"):
        result["issues"].append("No rhymes in opening zone (first 500 words)")
    
    if cycle_config.get("closing_required") and not positions.get("closing"):
        result["issues"].append("No rhymes in closing zone (last 500 words)")
    
    return result


def analyze_balance(rhymes_found: Dict) -> Dict:
    """Analyze balance across rhyme categories."""
    categories = {}
    for rhyme_id, rhyme_data in rhymes_found.items():
        cat = rhyme_data["category"]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(rhyme_id)
    
    return {
        "categories_used": list(categories.keys()),
        "category_counts": {k: len(v) for k, v in categories.items()},
        "rhymes_by_category": categories
    }


def validate_rhymes(filepath: str, previous_closing: List[str] = None) -> Dict:
    """Main validation function."""
    try:
        text = load_file(filepath)
    except FileNotFoundError:
        return {"status": "error", "message": f"File not found: {filepath}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
    movement = CONFIG.get("movement", "two")
    cycle = CONFIG.get("cycle", 1)
    
    # Run analyses
    rhyme_data = find_rhymes_with_positions(text)
    stacking = detect_stacking(text)
    intensity = assess_intensity(rhyme_data, cycle)
    balance = analyze_balance(rhyme_data["all_rhymes"])
    handoff = validate_handoff(
        rhyme_data["by_position"]["opening"],
        previous_closing or []
    )
    
    results = {
        "file": filepath,
        "movement": movement,
        "cycle": cycle,
        "rhymes_found": rhyme_data["all_rhymes"],
        "position_analysis": rhyme_data["by_position"],
        "stacking": stacking,
        "intensity_assessment": intensity,
        "category_balance": balance,
        "handoff_validation": handoff,
        "summary": {
            "total_rhymes": len(rhyme_data["all_rhymes"]),
            "rhyme_ids": list(rhyme_data["all_rhymes"].keys()),
            "opening_rhymes": rhyme_data["by_position"]["opening"],
            "closing_rhymes": rhyme_data["by_position"]["closing"],
            "stacking_detected": len(stacking) > 0
        }
    }
    
    # Determine overall status
    statuses = [intensity["status"]]
    if handoff["status"] == "warn":
        statuses.append("warn")
    
    if "fail" in statuses:
        results["status"] = "fail"
    elif "warn" in statuses:
        results["status"] = "warn"
    else:
        results["status"] = "pass"
    
    return results


def validate_sequence(filepaths: List[str]) -> Dict:
    """Validate a sequence of scenes with automatic handoff chaining."""
    movement = CONFIG.get("movement", "two")
    cycle = CONFIG.get("cycle", 1)
    ordered = order_sequence(filepaths, movement, cycle)

    results = {
        "status": "pass",
        "movement": movement,
        "cycle": cycle,
        "sequence": ordered,
        "scenes": [],
        "handoff_report": {
            "status": "pass",
            "pairs": []
        }
    }

    previous_closing = []
    for index, filepath in enumerate(ordered):
        scene_result = validate_rhymes(filepath, previous_closing)
        results["scenes"].append({
            "file": filepath,
            "status": scene_result.get("status"),
            "summary": scene_result.get("summary", {}),
            "handoff_validation": scene_result.get("handoff_validation", {})
        })

        if scene_result.get("status") == "fail":
            results["status"] = "fail"
        elif scene_result.get("status") == "warn" and results["status"] != "fail":
            results["status"] = "warn"

        if index > 0:
            handoff = scene_result.get("handoff_validation", {})
            results["handoff_report"]["pairs"].append({
                "from": ordered[index - 1],
                "to": filepath,
                "previous_closing": previous_closing,
                "opening": scene_result.get("summary", {}).get("opening_rhymes", []),
                "caught": handoff.get("caught", []),
                "missed": handoff.get("missed", []),
                "status": handoff.get("status", "skip")
            })

            if handoff.get("status") == "warn":
                results["handoff_report"]["status"] = "warn"
                if results["status"] != "fail":
                    results["status"] = "warn"

        previous_closing = scene_result.get("summary", {}).get("closing_rhymes", [])

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Track rhyme usage with position awareness for Movement Two"
    )
    parser.add_argument("file", nargs="?", help="Path to markdown file to analyze")
    parser.add_argument("--pretty", action="store_true", help="Pretty print JSON output")
    parser.add_argument("--cycle", type=int, choices=[1, 2, 3],
                        help="Override cycle from config (optional)")
    parser.add_argument("--previous-closing", type=str,
                        help="JSON array of rhymes from previous scene's closing zone")
    parser.add_argument("--sequence", nargs="+",
                        help="List of scene files (in order) for automatic handoff validation")
    
    args = parser.parse_args()
    
    # Allow cycle override
    if args.cycle:
        CONFIG["cycle"] = args.cycle
    
    # Parse previous closing rhymes if provided
    previous_closing = None
    if args.previous_closing:
        try:
            previous_closing = json.loads(args.previous_closing)
        except json.JSONDecodeError:
            print(json.dumps({"status": "error", "message": "Invalid JSON for --previous-closing"}))
            sys.exit(1)

    if args.sequence:
        results = validate_sequence(args.sequence)
    elif args.file:
        results = validate_rhymes(args.file, previous_closing)
    else:
        print(json.dumps({"status": "error", "message": "Provide a file or use --sequence"}))
        sys.exit(1)
    
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
