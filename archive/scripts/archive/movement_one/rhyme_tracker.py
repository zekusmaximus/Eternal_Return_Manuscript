#!/usr/bin/env python3
"""
Rhyme Tracker Script
Tracks sensory rhyme usage for The Eternal Return of the Digital Self.

Scans scene files for rhyme markers versus the registry and reports:
- Which rhymes are present
- Intensity appropriateness for the movement
- Usage balance across threads

Usage:
    python rhyme_tracker.py <file> --movement <one|two|three|four>

Output: JSON report with rhymes found and intensity assessment.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Set

# Rhyme definitions - keywords and phrases that indicate rhyme presence
RHYME_MARKERS = {
    "blue-white-light": {
        "category": "visual",
        "intensity_peak": "three",
        "markers": [
            r'\bblue[-\s]?white\b',
            r'\bholographic\s+(?:glow|light|interface)\b',
            r'\bbioluminescent\b',
            r'\bblue\s+(?:glow|light|luminosity)\b',
        ]
    },
    "almost-closed-curve": {
        "category": "visual",
        "intensity_peak": "three",
        "markers": [
            r'\balmost[-\s]?closed\s+curve\b',
            r'\btorus(?:[-\s]?spiral)?\b',
            r'\bcurve[sd]?\s+(?:that\s+)?approach(?:es|ed|ing)?\b',
            r'\bspiral(?:ing|s)?\s+(?:inward|toward)\b',
        ]
    },
    "geometric-shadow": {
        "category": "visual",
        "intensity_peak": "two",
        "markers": [
            r'\bgeometric\s+shadow\b',
            r'\bperipheral\s+(?:vision|shape)\b',
            r'\bcorner\s+of\s+(?:my|his|her|the)\s+eye\b',
            r'\bshadow[s]?\s+(?:that\s+)?(?:don\'?t|doesn\'?t)\s+match\b',
        ]
    },
    "bone-frequency": {
        "category": "somatic",
        "intensity_peak": "three",
        "markers": [
            r'\bbone[-\s]?frequency\b',
            r'\bfrequency\s+(?:in|below|settl\w+\s+into)\s+(?:my|his|her)?\s*(?:bones?|sternum|chest)\b',
            r'\bbelow\s+hearing\b',
            r'\bresonance\s+(?:in|through)\s+(?:my|his|her)?\s*(?:bones?|chest)\b',
        ]
    },
    "cold-hands": {
        "category": "somatic",
        "intensity_peak": "two",
        "markers": [
            r'\bcold\s+hands?\b',
            r'\b(?:hands?|fingers?)\s+(?:are|were|gone|going|too)\s+cold\b',
            r'\bfreezing\s+(?:hands?|fingers?)\b',
            r'\bnumb(?:ness)?\s+(?:in|of)\s+(?:my|his|her)?\s*(?:hands?|fingers?)\b',
        ]
    },
    "falling-backward": {
        "category": "somatic",
        "intensity_peak": "three",
        "markers": [
            r'\bfalling\s+backward\b',
            r'\bvertigo\b',
            r'\blurch(?:ed|es|ing)?\s+(?:in|through)\b',
            r'\bfalling\s+(?:through|into)\b',
        ]
    },
    "metallic-taste": {
        "category": "somatic",
        "intensity_peak": "three",
        "markers": [
            r'\bmetallic\s+taste\b',
            r'\btaste[ds]?\s+(?:like\s+)?(?:copper|metal|blood|pennies)\b',
            r'\bcopper\s+(?:taste|on|in)\b',
            r'\bblood\s+(?:taste|in\s+(?:my|his|her)\s+mouth)\b',
        ]
    },
    "tracing-the-form": {
        "category": "kinesthetic",
        "intensity_peak": "two",
        "markers": [
            r'\btracing\s+(?:the\s+)?(?:form|shape|pattern)\b',
            r'\bfinger[s]?\s+(?:on|moving|tracing)\b',
            r'\bdraw(?:n|ing)?\s+(?:in|on)\s+(?:the\s+)?(?:dirt|dust|desk|surface)\b',
            r'\bunconscious(?:ly)?\s+(?:tracing|drawing|sketching)\b',
        ]
    },
    "held-breath": {
        "category": "kinesthetic",
        "intensity_peak": "two",
        "markers": [
            r'\bheld?\s+(?:my|his|her)?\s*breath\b',
            r'\bholding\s+(?:my|his|her)?\s*breath\b',
            r'\bpause\s+between\b',
            r'\bsilence\s+before\b',
        ]
    },
    "waking-into-motion": {
        "category": "kinesthetic",
        "intensity_peak": "three",
        "markers": [
            r'\bwak(?:e|ing|ed)\s+(?:into|already|with)\s+(?:motion|moving|walking)\b',
            r'\bfind(?:s)?\s+(?:myself|himself|herself)\s+(?:already\s+)?(?:moving|standing|walking)\b',
            r'\bdon\'?t\s+remember\s+(?:starting|getting|moving)\b',
            r'\bbody\s+(?:already|had been)\s+(?:here|there|moving)\b',
        ]
    },
    "ozone-wet-stone": {
        "category": "olfactory",
        "intensity_peak": "two",
        "markers": [
            r'\bozone\s+(?:and|&)\s+wet\s+stone\b',
            r'\bozone\b',
            r'\bwet\s+stone\b',
            r'\bsmell[s]?\s+(?:of|like)\s+(?:ozone|electrical|server)\b',
        ]
    },
    "burning-circuits": {
        "category": "olfactory",
        "intensity_peak": "three",
        "markers": [
            r'\bburning\s+circuits?\b',
            r'\bfrying\s+electronics?\b',
            r'\bsmell[s]?\s+(?:of|like)\s+(?:burning|fried|overheated)\b',
            r'\bprocessor[s]?\s+(?:overheated|burning)\b',
        ]
    },
    "name-edge-of-memory": {
        "category": "cognitive",
        "intensity_peak": "three",
        "markers": [
            r'\bname\s+(?:on\s+)?(?:the\s+)?edge\s+of\s+(?:my|his|her)?\s*memory\b',
            r'\bforget(?:ting|s)?\s+(?:my|his|her)?\s*(?:own\s+)?name\b',
            r'\blose\s+(?:the\s+)?word[s]?\b',
            r'\bwhat\s+(?:was\s+)?I\s+(?:about\s+)?(?:to\s+)?say\b',
        ]
    },
    "deja-vu-that-isnt": {
        "category": "cognitive",
        "intensity_peak": "two",
        "markers": [
            r'\bdéjà\s*vu\b',
            r'\bdeja\s*vu\b',
            r'\b(?:been|done|said|seen)\s+(?:this|here|that)\s+before\b',
            r'\bfeeling\s+of\s+(?:repetition|overlap)\b',
        ]
    },
    "sentence-without-origin": {
        "category": "cognitive",
        "intensity_peak": "three",
        "markers": [
            r'\bsentence\s+(?:without|from|that\s+has\s+no)\s+origin\b',
            r'\bwords?\s+(?:I\s+)?(?:didn\'?t|don\'?t)\s+(?:write|generate|think)\b',
            r'\bhear\s+(?:myself|himself|herself)\s+say(?:ing)?\b',
            r'\bwords?\s+(?:arrived|came)\s+(?:in|to)\s+(?:my|his|her)\s+mouth\b',
        ]
    },
}

# Movement intensity expectations
INTENSITY_LEVELS = {
    "one": {
        "min_rhymes": 1,
        "max_rhymes": 2,
        "intensity": "low",
        "description": "Single occurrence per thread - subtle, dismissable"
    },
    "two": {
        "min_rhymes": 2,
        "max_rhymes": 4,
        "intensity": "medium",
        "description": "Rhymes echo across threads - reader notices"
    },
    "three": {
        "min_rhymes": 3,
        "max_rhymes": 6,
        "intensity": "high",
        "description": "Multiple rhymes per scene - sensory overload"
    },
    "four": {
        "min_rhymes": 1,
        "max_rhymes": 3,
        "intensity": "resolution",
        "description": "Transformed meaning - comfort replaces uncanny"
    }
}


def load_file(filepath: str) -> str:
    """Load and return file contents."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def find_rhymes(text: str) -> Dict[str, List[Dict]]:
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
                        "marker": marker,
                        "text": line.strip()[:80]
                    })
        
        if matches:
            found[rhyme_id] = {
                "category": rhyme_data["category"],
                "intensity_peak": rhyme_data["intensity_peak"],
                "occurrences": matches
            }
    
    return found


def assess_intensity(rhymes_found: Dict, movement: str) -> Dict:
    """Assess if rhyme usage is appropriate for the movement."""
    level = INTENSITY_LEVELS.get(movement, INTENSITY_LEVELS["one"])
    
    rhyme_count = len(rhymes_found)
    
    result = {
        "status": "pass",
        "movement": movement,
        "expected": level,
        "found_count": rhyme_count,
        "issues": []
    }
    
    if rhyme_count < level["min_rhymes"]:
        result["status"] = "warn"
        result["issues"].append(f"Too few rhymes for Movement {movement.upper()}: found {rhyme_count}, expected at least {level['min_rhymes']}")
    
    if rhyme_count > level["max_rhymes"]:
        result["status"] = "warn"
        result["issues"].append(f"Too many rhymes for Movement {movement.upper()}: found {rhyme_count}, expected at most {level['max_rhymes']}")
    
    # Check if rhymes are appropriate for movement
    for rhyme_id, rhyme_data in rhymes_found.items():
        peak = rhyme_data["intensity_peak"]
        movement_order = {"one": 1, "two": 2, "three": 3, "four": 4}
        
        # Rhymes can appear before their peak but shouldn't be intense
        if movement_order.get(movement, 1) < movement_order.get(peak, 1):
            if len(rhyme_data["occurrences"]) > 1:
                result["issues"].append(f"Rhyme '{rhyme_id}' (peak: Movement {peak}) used multiple times before its peak in Movement {movement}")
    
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


def validate_rhymes(filepath: str, movement: str) -> Dict:
    """Main validation function."""
    if movement not in INTENSITY_LEVELS:
        return {"status": "error", "message": f"Unknown movement: {movement}"}
    
    try:
        text = load_file(filepath)
    except FileNotFoundError:
        return {"status": "error", "message": f"File not found: {filepath}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
    rhymes_found = find_rhymes(text)
    intensity_assessment = assess_intensity(rhymes_found, movement)
    balance = analyze_balance(rhymes_found)
    
    results = {
        "file": filepath,
        "movement": movement,
        "rhymes_found": rhymes_found,
        "intensity_assessment": intensity_assessment,
        "category_balance": balance,
        "summary": {
            "total_rhymes": len(rhymes_found),
            "rhyme_ids": list(rhymes_found.keys()),
            "categories": list(balance["categories_used"])
        }
    }
    
    results["status"] = intensity_assessment["status"]
    
    return results


def main():
    parser = argparse.ArgumentParser(description="Track rhyme usage in scenes")
    parser.add_argument("file", help="Path to markdown file to analyze")
    parser.add_argument("--movement", required=True,
                        choices=["one", "two", "three", "four"],
                        help="Movement number for intensity assessment")
    parser.add_argument("--pretty", action="store_true", help="Pretty print JSON output")
    
    args = parser.parse_args()
    
    results = validate_rhymes(args.file, args.movement)
    
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
