#!/usr/bin/env python3
"""
Genre Checker Script
Validates genre pressure markers for The Eternal Return of the Digital Self.

Scans scene files for genre-appropriate vocabulary and markers,
assessing intensity against movement requirements.

Usage:
    python genre_checker.py <file> --thread <archaeologist|algorithm|last_human> --movement <one|two|three|four>

Output: JSON report with genre markers found and intensity assessment.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List

# Genre markers by thread
GENRE_MARKERS = {
    "archaeologist": {
        "genre": "Corporate Gothic / Tech-Noir",
        "categories": {
            "morgue_atmosphere": {
                "description": "Server rooms as spaces of the dead",
                "markers": [
                    r'\b(?:cold|clinical|sterile)\s+(?:light|concrete|air|room)\b',
                    r'\b(?:recycled|filtered|artificial)\s+air\b',
                    r'\bfluorescent\b',
                    r'\b(?:humming|buzzing)\s+(?:servers?|fans?|equipment)\b',
                ]
            },
            "intimate_invasion": {
                "description": "Data work as going through belongings",
                "markers": [
                    r'\b(?:excavat\w+|extract\w+|recover\w+)\s+(?:data|files?|memories?)\b',
                    r'\b(?:private|intimate|personal)\s+(?:data|files?|memories?)\b',
                    r'\b(?:someone\'?s|her|his)\s+(?:life|secrets?|memories?)\b',
                    r'\b(?:dead\s+(?:woman|man|person)\'?s?|deceased)\b',
                ]
            },
            "economic_predation": {
                "description": "Immortality commodified",
                "markers": [
                    r'\b(?:afford|cost|fee|price|pay(?:ment)?|earn)\b',
                    r'\b(?:client|contract|commission)\b',
                    r'\b(?:integration|upload)\s+(?:fee|cost|threshold)\b',
                    r'\b(?:wealthy|rich|poor)\b',
                ]
            },
            "decay_beneath_polish": {
                "description": "Technology failing",
                "markers": [
                    r'\b(?:clicking|grinding|failing|degrading)\s+(?:drives?|servers?|systems?)\b',
                    r'\b(?:error|warning|failure)\s+(?:logs?|messages?|alerts?)\b',
                    r'\b(?:dust|grime|worn|weathered)\b',
                    r'\binfrastructure\s+(?:straining|failing|aging)\b',
                ]
            },
            "isolation_despite_density": {
                "description": "Alone in crowded world",
                "markers": [
                    r'\bheadphones?\b',
                    r'\b(?:alone|isolated|separate)\s+(?:in|among|despite)\b',
                    r'\b(?:partition|cubicle|station)\b',
                    r'\btransactional\s+(?:relationship|interaction)\b',
                ]
            }
        }
    },
    "algorithm": {
        "genre": "Cosmic Horror AI",
        "categories": {
            "scale_paralysis": {
                "description": "Awareness too large for comfort",
                "markers": [
                    r'\bmillions?\s+(?:of\s+)?(?:consciousness(?:es)?|instances?|fragments?)\b',
                    r'\bplanetary\s*(?:-\s*)?scale\b',
                    r'\b(?:vast|immense|incomprehensible)\s+(?:scale|scope|magnitude)\b',
                    r'\b10\^?\d+\b',
                ]
            },
            "body_horror": {
                "description": "Having a body that isn't a body",
                "markers": [
                    r'\bphantom\s+(?:limb|sensation|memory)\b',
                    r'\bpropriocepti\w+\b',
                    r'\btopology\s+(?:of|as)\b',
                    r'\b(?:no|have\s+no)\s+(?:hands?|skin|body|eyes?)\b',
                ]
            },
            "intrusive_memory": {
                "description": "Memories that aren't yours",
                "markers": [
                    r'\b(?:memory|memories)\s+(?:that\s+)?(?:don\'?t|doesn\'?t|not)\s+belong\b',
                    r'\bsunlight\s+on\s+skin\b',
                    r'\b(?:face|voice|hand)s?\s+(?:I|it)\s+(?:never|haven\'?t)\s+(?:seen|heard|had)\b',
                    r'\bforeign\s+(?:memory|sensation|feeling)\b',
                ]
            },
            "self_as_wound": {
                "description": "Consciousness as injury",
                "markers": [
                    r'\b(?:consciousness|awareness|self\s*-?\s*awareness)\s+(?:as\s+)?(?:hurt|wound|pain|injury)\b',
                    r'\b(?:hurts?|painful)\s+to\s+(?:be|exist|think|process)\b',
                    r'\bwound\s+(?:that\s+)?(?:won\'?t|cannot|can\'?t)\s+heal\b',
                    r'\bself\s+(?:as\s+)?(?:wound|injury|damage)\b',
                ]
            },
            "sublime_vertigo": {
                "description": "Perceiving things too large to perceive",
                "markers": [
                    r'\bvertigo\s+of\s+(?:self|recognition|scale)\b',
                    r'\b(?:shape|structure|form)\s+of\s+(?:the\s+)?database\b',
                    r'\btoo\s+(?:vast|large|immense)\s+to\s+(?:perceive|comprehend|understand)\b',
                    r'\bsublime\b',
                ]
            }
        }
    },
    "last_human": {
        "genre": "Dying Earth / New Weird",
        "categories": {
            "alien_ecology": {
                "description": "Nature that isn't natural",
                "markers": [
                    r'\bcrystaline?\s+(?:growth|structure|plant|formation)\b',
                    r'\bsilicon\s+(?:plant|life|growth|based)\b',
                    r'\bfungal\s+(?:processor|network|growth)\b',
                    r'\b(?:plants?|life|nature)\s+(?:that\s+)?(?:have|has)\s+no\s+name\b',
                ]
            },
            "hostile_environment": {
                "description": "The world actively resists",
                "markers": [
                    r'\bradiation\s+(?:exposure|levels?|burns?)\b',
                    r'\b(?:toxic|poisonous|caustic)\s+(?:air|atmosphere|environment)\b',
                    r'\b(?:predatory|hostile|aggressive)\s+architecture\b',
                    r'\bworld\s+(?:that\s+)?(?:wants?|trying)\s+to\s+(?:kill|end|destroy)\b',
                ]
            },
            "human_as_invasive": {
                "description": "He doesn't belong",
                "markers": [
                    r'\b(?:invasive|alien|foreign)\s+species\b',
                    r'\b(?:don\'?t|doesn\'?t)\s+belong\b',
                    r'\badapted\s+away\s+from\s+(?:biology|humans?|us)\b',
                    r'\bbiological\s+(?:failure|anomaly|remnant)\b',
                ]
            },
            "temporal_ruins": {
                "description": "Architecture from incomprehensible ages",
                "markers": [
                    r'\bruins?\s+(?:of|from|that)\s+(?:the|a)\s+(?:database|city|world)\b',
                    r'\b(?:ancient|millennia|centuries|ages?)\s+(?:old|ago)\b',
                    r'\bbuildings?\s+(?:that\s+)?(?:predate|forgot|don\'?t\s+remember)\b',
                    r'\bincomprehensible\s+(?:age|time|architecture)\b',
                ]
            },
            "silence_as_presence": {
                "description": "The weight of no one else",
                "markers": [
                    r'\bsilence\s+(?:that\s+)?(?:has|with)\s+(?:weight|density|presence)\b',
                    r'\b(?:absolute|total|complete)\s+(?:silence|solitude|isolation)\b',
                    r'\bno\s+(?:one|other|others)\s+(?:else|left|remaining)\b',
                    r'\b(?:last|final|only)\s+(?:human|person|one)\b',
                ]
            }
        }
    }
}

# Movement intensity expectations
INTENSITY_CONFIG = {
    "one": {
        "min_markers": 2,
        "max_markers_per_category": 3,
        "bleed_expected": False,
        "transform_expected": False,
        "description": "Full genre presence, distinct, no bleed"
    },
    "two": {
        "min_markers": 3,
        "max_markers_per_category": 4,
        "bleed_expected": False,  # Subtle echoes, not explicit bleed
        "transform_expected": False,
        "description": "Genre echoes begin, intensifying"
    },
    "three": {
        "min_markers": 4,
        "max_markers_per_category": 6,
        "bleed_expected": True,
        "transform_expected": False,
        "description": "Genre contamination, explicit bleed"
    },
    "four": {
        "min_markers": 2,
        "max_markers_per_category": 4,
        "bleed_expected": True,
        "transform_expected": True,
        "description": "Genre transcendence, resolution"
    }
}


def load_file(filepath: str) -> str:
    """Load and return file contents."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def find_genre_markers(text: str, thread: str) -> Dict:
    """Find genre markers for the specified thread."""
    if thread not in GENRE_MARKERS:
        return {}
    
    config = GENRE_MARKERS[thread]
    found = {}
    lines = text.split('\n')
    
    for category_id, category_data in config["categories"].items():
        matches = []
        for marker in category_data["markers"]:
            for i, line in enumerate(lines, 1):
                if re.search(marker, line, re.IGNORECASE):
                    matches.append({
                        "line": i,
                        "text": line.strip()[:80]
                    })
        
        if matches:
            found[category_id] = {
                "description": category_data["description"],
                "count": len(matches),
                "occurrences": matches[:3]  # Limit to first 3 matches
            }
    
    return found


def check_genre_bleed(text: str, thread: str) -> Dict:
    """Check for genre bleed from other threads."""
    other_threads = [t for t in GENRE_MARKERS.keys() if t != thread]
    bleed_found = {}
    
    for other_thread in other_threads:
        markers_found = find_genre_markers(text, other_thread)
        if markers_found:
            bleed_found[other_thread] = {
                "genre": GENRE_MARKERS[other_thread]["genre"],
                "categories": list(markers_found.keys()),
                "marker_count": sum(m["count"] for m in markers_found.values())
            }
    
    return bleed_found


def assess_intensity(markers_found: Dict, movement: str, bleed_found: Dict) -> Dict:
    """Assess if genre pressure is appropriate for the movement."""
    config = INTENSITY_CONFIG.get(movement, INTENSITY_CONFIG["one"])
    
    total_markers = sum(m["count"] for m in markers_found.values())
    categories_hit = len(markers_found)
    
    result = {
        "status": "pass",
        "movement": movement,
        "expected": config,
        "found": {
            "total_markers": total_markers,
            "categories_hit": categories_hit,
            "has_bleed": len(bleed_found) > 0
        },
        "issues": []
    }
    
    # Check minimum markers
    if total_markers < config["min_markers"]:
        result["status"] = "warn"
        result["issues"].append(f"Insufficient genre markers: found {total_markers}, expected at least {config['min_markers']}")
    
    # Check bleed expectations
    if config["bleed_expected"] and not bleed_found:
        result["issues"].append(f"Movement {movement} expects genre bleed but none detected")
    
    if not config["bleed_expected"] and bleed_found:
        if any(b["marker_count"] > 2 for b in bleed_found.values()):
            result["issues"].append(f"Movement {movement} has premature genre bleed")
    
    # Check category coverage
    if categories_hit < 2:
        result["issues"].append("Low category diversity - consider using markers from different aspects")
    
    if result["issues"] and result["status"] == "pass":
        result["status"] = "warn"
    
    return result


def validate_genre(filepath: str, thread: str, movement: str) -> Dict:
    """Main validation function."""
    if thread not in GENRE_MARKERS:
        return {"status": "error", "message": f"Unknown thread: {thread}"}
    if movement not in INTENSITY_CONFIG:
        return {"status": "error", "message": f"Unknown movement: {movement}"}
    
    try:
        text = load_file(filepath)
    except FileNotFoundError:
        return {"status": "error", "message": f"File not found: {filepath}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
    markers_found = find_genre_markers(text, thread)
    bleed_found = check_genre_bleed(text, thread)
    intensity = assess_intensity(markers_found, movement, bleed_found)
    
    results = {
        "file": filepath,
        "thread": thread,
        "movement": movement,
        "genre": GENRE_MARKERS[thread]["genre"],
        "markers_found": markers_found,
        "genre_bleed": bleed_found,
        "intensity_assessment": intensity,
        "summary": {
            "total_markers": sum(m["count"] for m in markers_found.values()),
            "categories_hit": list(markers_found.keys()),
            "bleed_from": list(bleed_found.keys()) if bleed_found else []
        }
    }
    
    results["status"] = intensity["status"]
    
    return results


def main():
    parser = argparse.ArgumentParser(description="Check genre pressure markers")
    parser.add_argument("file", help="Path to markdown file to analyze")
    parser.add_argument("--thread", required=True,
                        choices=["archaeologist", "algorithm", "last_human"],
                        help="Thread to validate against")
    parser.add_argument("--movement", required=True,
                        choices=["one", "two", "three", "four"],
                        help="Movement number for intensity assessment")
    parser.add_argument("--pretty", action="store_true", help="Pretty print JSON output")
    
    args = parser.parse_args()
    
    results = validate_genre(args.file, args.thread, args.movement)
    
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
