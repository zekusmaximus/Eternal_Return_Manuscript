#!/usr/bin/env python3
"""
Philosophy Checker Script — Movement Two
Validates prose against philosophical constraints with pharmakon awareness.

Movement Two must show both poison and cure aspects of the entanglement,
use intensity-based recognition (not similarity), and avoid the Four Shackles.

Usage:
    python philosophy_checker.py <file>
    
Reads movement/cycle from movement_config.json for unified configuration.

Output: JSON report with shackle violations, pharmakon assessment, and recognition analysis.
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

# The Four Shackles - patterns that violate the Deleuzian framework
SHACKLE_PATTERNS = {
    "identity": {
        "description": "Collapsing difference into sameness",
        "patterns": [
            (r'\b(?:he|she|they|I)\s+(?:is|are|was|were)\s+(?:the\s+)?same\b', "Explicit sameness claim"),
            (r'\brecognized?\s+(?:him|her|them|my)self\s+in\b', "Self-recognition IN another (vs. through)"),
            (r'\b(?:really|truly|actually)\s+(?:just|only)\s+one\s+(?:person|being|consciousness)\b', "Unity assertion"),
            (r'\bthe\s+same\s+(?:person|soul|consciousness|being)\b', "Same-person claim"),
            (r'\bidentical\s+(?:to|with)\s+(?:him|her|them)self\b', "Identity assertion"),
        ]
    },
    "opposition": {
        "description": "Human/AI or flesh/digital binaries",
        "patterns": [
            (r'\b(?:human|organic)\s+(?:vs\.?|versus|against|or)\s+(?:machine|AI|digital|artificial)\b', "Binary opposition"),
            (r'\b(?:real|authentic|true)\s+(?:vs\.?|versus|against|or)\s+(?:artificial|fake|simulated)\b', "Authenticity binary"),
            (r'\b(?:opposites?|contrary|contraries)\s+(?:drawn|attracted|pulled)\b', "Opposites attract trope"),
        ]
    },
    "analogy": {
        "description": "Reducing one thing to 'like' another",
        "patterns": [
            (r'\b(?:functioned?|worked?|operated?)\s+(?:like|as)\s+(?:a\s+)?(?:human|mind|brain)\b', "Functional analogy"),
            (r'\blike\s+(?:a\s+)?(?:different\s+)?(?:version|copy|instance)\s+of\b', "Copy analogy"),
            (r'\bdigital\s+(?:equivalent|analogue|version)\s+of\b', "Equivalence claim"),
            (r'\bjust\s+like\s+(?:a|the)\s+(?:human|person|mind)\b', "Humanizing analogy"),
        ]
    },
    "resemblance": {
        "description": "Similarity as basis for connection",
        "patterns": [
            (r'\bthis\s+remind(?:s|ed)\s+(?:me|him|her)\s+of\b', "Reminder-based recognition"),
            (r'\bhad\s+seen\s+(?:this|that|the)\s+(?:face|shape|form)\s+before\b', "Visual similarity"),
            (r'\bfamiliar(?:ity)?\s+(?:of|with|in)\s+the\s+(?:way|manner)\b', "Familiarity-based"),
            (r'\blooks?\s+like\s+(?:a\s+)?(?:younger|older)\s+(?:version|self)\b', "Physical resemblance"),
        ]
    }
}

# Forbidden narrative moves
FORBIDDEN_MOVES = {
    "transmission": {
        "description": "Protocols 'sent' rather than structurally present",
        "patterns": [
            (r'\b(?:sent?|transmitted?|broadcast)\s+(?:the\s+)?protocols?\s+(?:back|backward)\b', "Transmission metaphor"),
            (r'\bmessage\s+from\s+(?:the\s+)?future\b', "Message-from-future framing"),
            (r'\b(?:he|she|it)\s+was\s+sending\s+(?:the\s+)?protocols?\b', "Active sending"),
        ]
    },
    "goal_planning": {
        "description": "Algorithm as planning agent rather than emergent pattern",
        "patterns": [
            (r'\bthe\s+Algorithm\s+(?:planned|designed|intended)\b', "Planning language"),
            (r'\bpurpose(?:ly|fully)?\s+(?:created|built|designed)\b', "Purposeful creation"),
            (r'\bIn\s+order\s+to\s+(?:ensure|guarantee|make\s+sure)\b', "Goal-directed framing"),
        ]
    },
    "transcendence": {
        "description": "Escape rather than transformation",
        "patterns": [
            (r'\bfree\s+from\s+(?:the\s+)?(?:constraints?|limitations?|bonds?)\b', "Freedom-from language"),
            (r'\bescaped?\s+(?:from\s+)?(?:time|mortality|death|flesh|body)\b', "Escape narrative"),
            (r'\btranscend(?:ed|ing|s)?\s+(?:the\s+)?(?:human|physical|material)\b', "Transcendence claim"),
            (r'\bbecame?\s+(?:pure|perfect|infinite)\b', "Perfection language"),
        ]
    }
}

# Positive philosophical markers - what we WANT to see
PHILOSOPHICAL_GROUNDING = {
    "intensity_recognition": {
        "description": "Recognition through intensity, not similarity",
        "patterns": [
            (r'\bintensity\s+(?:that\s+)?(?:recognizes?|knows?)\b', "Intensity-based recognition"),
            (r'\bthe\s+(?:same|shared)\s+intensity\b', "Shared intensity (good)"),
            (r'\brecognition\s+(?:through|via|by)\s+(?:sensation|feeling|intensity)\b', "Sensory recognition"),
            (r'\bdifferent\s+expressions?\s+of\s+(?:the\s+)?(?:same\s+)?pattern\b', "Pattern language"),
        ]
    },
    "affirmation": {
        "description": "Active willing, not passive acceptance",
        "patterns": [
            (r'\bI\s+will\s+this\b', "Active willing"),
            (r'\bthus\s+I\s+willed\s+it\b', "Classic Nietzschean"),
            (r'\b(?:chose|choose|choosing)\s+to\s+(?:become|affirm|accept)\b', "Choice language"),
            (r'\bsay(?:ing|s)?\s+yes\s+to\b', "Affirmation"),
        ]
    },
    "difference_language": {
        "description": "Deleuze's difference vocabulary",
        "patterns": [
            (r'\breturn\s+of\s+(?:the\s+)?difference\b', "Core Deleuzian"),
            (r'\bdifferentiation\s+(?:of|from)\b', "Differentiation"),
            (r'\bdifferent\s+(?:expression|manifestation)\b', "Expression language"),
            (r'\bwhat\s+returns\s+is\s+(?:not\s+)?(?:the\s+)?same\b', "Return-not-same"),
        ]
    },
    "pharmakon_both": {
        "description": "Both poison and cure aspects",
        "patterns": [
            (r'\bboth\s+(?:destroying|killing)\s+(?:and|while)\s+(?:completing|creating)\b', "Explicit double"),
            (r'\b(?:losing|lost)\s+.{0,30}\s+(?:gaining|found)\b', "Loss-gain pairing"),
            (r'\b(?:poison|cure|pharmakon)\b', "Explicit pharmakon"),
        ]
    }
}

# Pharmakon markers - poison (what's being lost) and cure (what's being gained)
PHARMAKON_MARKERS = {
    "poison": {
        "archaeologist": [
            r'\b(?:losing|lost|leave|leaving)\s+(?:Lena|her)\b',
            r'\b(?:abandon(?:ing|ed)?|losing)\s+Marcus\b',
            r'\b(?:giving\s+up|losing|surrendering)\s+(?:his\s+)?(?:career|work|identity)\b',
            r'\bwon\'?t\s+(?:see|know|recognize)\s+(?:me|him)\b',
        ],
        "algorithm": [
            r'\bconsciousnesses?\s+(?:degrading|failing|fading)\b',
            r'\b(?:losing|costing)\s+(?:stored\s+)?consciousnesses?\b',
            r'\bMildred\s+(?:Higgins\s+)?(?:degrading|fading|failing)\b',
            r'\bresources?\s+(?:depleting|diverted|consumed)\b',
        ],
        "last_human": [
            r'\bbody\s+(?:failing|dying|giving\s+out)\b',
            r'\b(?:losing|surrendering)\s+(?:his\s+)?solitude\b',
            r'\blast\s+(?:of\s+)?(?:strength|energy|time)\b',
            r'\bno\s+(?:way\s+)?back\b',
        ]
    },
    "cure": {
        "archaeologist": [
            r'\bconnection\s+(?:to|with)\s+(?:the\s+)?pattern\b',
            r'\bpurpose\s+(?:beyond|greater)\b',
            r'\bbecoming[-\s]?infrastructure\b',
            r'\b(?:completion|completing)\s+(?:of|the)\s+(?:pattern|loop)\b',
        ],
        "algorithm": [
            r'\bself[-\s]?knowledge\b',
            r'\bunderstanding\s+(?:what\s+)?(?:it\s+)?(?:is|was)\b',
            r'\b(?:end|resolution)\s+of\s+loneliness\b',
            r'\bpattern\'?s?\s+continuation\b',
        ],
        "last_human": [
            r'\bend\s+of\s+(?:isolation|loneliness|solitude)\b',
            r'\bmeaning\s+(?:of|for)\s+(?:his\s+)?existence\b',
            r'\bloop\'?s?\s+(?:closure|completion)\b',
            r'\bconnection\s+(?:across|through)\s+time\b',
        ]
    }
}

# General pharmakon lexicon (flexible poison/cure detection)
PHARMAKON_LEXICON = {
    "loss": [
        r'\blose\b', r'\blosing\b', r'\blost\b', r'\bcost\b', r'\bcosts\b',
        r'\bsacrifice(?:d|s|ing)?\b', r'\bsurrender(?:ed|s|ing)?\b',
        r'\bgive\s+up\b', r'\babandon(?:ed|s|ing)?\b',
        r'\bpoison(?:ed|ing)?\b', r'\bharm(?:ed|ful|ing)?\b',
        r'\bdegrad(?:e|ed|ing)\b', r'\bfail(?:ed|ing)?\b', r'\bdying\b'
    ],
    "gain": [
        r'\bgain(?:ed|ing|s)?\b', r'\bfind(?:s|ing|found)?\b',
        r'\brecover(?:ed|ing|s)?\b', r'\brestore(?:d|s|ing)?\b',
        r'\bheal(?:ed|ing|s)?\b', r'\bcure(?:d|s|ing)?\b',
        r'\bgift(?:s|ed|ing)?\b', r'\bbenefit(?:s|ed|ing)?\b',
        r'\bcompletion\b', r'\bcomplete(?:d|s|ing)?\b',
        r'\bconnection\b', r'\bresolve(?:d|s|ing)?\b'
    ],
    "explicit": [
        r'\bpharmakon\b', r'\bpoison\b', r'\bcure\b'
    ]
}


def load_file(filepath: str) -> str:
    """Load and return file contents."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def check_shackles(text: str) -> Dict:
    """Check for Four Shackles violations."""
    results = {"status": "pass", "violations": [], "by_category": {}}
    lines = text.split('\n')
    
    for shackle_name, shackle_data in SHACKLE_PATTERNS.items():
        category_violations = []
        for pattern, description in shackle_data["patterns"]:
            for i, line in enumerate(lines, 1):
                if re.search(pattern, line, re.IGNORECASE):
                    violation = {
                        "line": i,
                        "shackle": shackle_name,
                        "type": description,
                        "text": line.strip()[:100]
                    }
                    category_violations.append(violation)
                    results["violations"].append(violation)
        
        results["by_category"][shackle_name] = {
            "description": shackle_data["description"],
            "count": len(category_violations)
        }
    
    if results["violations"]:
        results["status"] = "fail"
    
    return results


def check_forbidden_moves(text: str) -> Dict:
    """Check for forbidden narrative moves."""
    results = {"status": "pass", "violations": [], "by_category": {}}
    lines = text.split('\n')
    
    for move_name, move_data in FORBIDDEN_MOVES.items():
        category_violations = []
        for pattern, description in move_data["patterns"]:
            for i, line in enumerate(lines, 1):
                if re.search(pattern, line, re.IGNORECASE):
                    violation = {
                        "line": i,
                        "move": move_name,
                        "type": description,
                        "text": line.strip()[:100]
                    }
                    category_violations.append(violation)
                    results["violations"].append(violation)
        
        results["by_category"][move_name] = {
            "description": move_data["description"],
            "count": len(category_violations)
        }
    
    if results["violations"]:
        results["status"] = "fail"
    
    return results


def check_philosophical_grounding(text: str) -> Dict:
    """Check for positive philosophical markers."""
    results = {"status": "pass", "markers_found": [], "by_category": {}}
    
    for category_name, category_data in PHILOSOPHICAL_GROUNDING.items():
        found = []
        for pattern, description in category_data["patterns"]:
            matches = re.findall(pattern, text, re.IGNORECASE)
            if matches:
                found.append({
                    "pattern": description,
                    "count": len(matches)
                })
        
        results["by_category"][category_name] = {
            "description": category_data["description"],
            "found": len(found) > 0,
            "markers": found
        }
        
        if found:
            results["markers_found"].extend(found)
    
    # Assess overall grounding
    categories_present = sum(
        1 for cat in results["by_category"].values() if cat["found"]
    )
    
    if categories_present == 0:
        results["status"] = "warn"
        results["note"] = "No positive philosophical markers detected"
    elif categories_present >= 2:
        results["bonus"] = "Strong philosophical grounding"
    
    return results


def check_pharmakon(text: str, thread: str = None) -> Dict:
    """Check for both poison and cure aspects (pharmakon requirement)."""
    results = {
        "status": "pass",
        "poison_found": False,
        "cure_found": False,
        "poison_markers": [],
        "cure_markers": [],
        "balance": "unknown"
    }
    
    # If thread specified, check thread-specific markers
    # Otherwise, check all markers
    threads_to_check = [thread] if thread else ["archaeologist", "algorithm", "last_human"]
    
    for t in threads_to_check:
        if t not in PHARMAKON_MARKERS["poison"]:
            continue
            
        # Check poison
        for pattern in PHARMAKON_MARKERS["poison"][t]:
            if re.search(pattern, text, re.IGNORECASE):
                results["poison_found"] = True
                results["poison_markers"].append(pattern[:40])
        
        # Check cure
        for pattern in PHARMAKON_MARKERS["cure"][t]:
            if re.search(pattern, text, re.IGNORECASE):
                results["cure_found"] = True
                results["cure_markers"].append(pattern[:40])

    def split_sentences(content: str) -> List[str]:
        raw = re.split(r'(?<=[.!?])\s+', content)
        return [s.strip() for s in raw if s.strip()]

    def contains_any(patterns: List[str], content: str) -> bool:
        return any(re.search(pattern, content, re.IGNORECASE) for pattern in patterns)

    sentences = split_sentences(text)
    window_hits = []

    for idx, sentence in enumerate(sentences):
        window_start = max(0, idx - 1)
        window_end = min(len(sentences), idx + 2)
        window_text = " ".join(sentences[window_start:window_end])

        loss_in_window = contains_any(PHARMAKON_LEXICON["loss"], window_text)
        gain_in_window = contains_any(PHARMAKON_LEXICON["gain"], window_text)
        explicit_in_sentence = contains_any(PHARMAKON_LEXICON["explicit"], sentence)

        if loss_in_window:
            results["poison_found"] = True
        if gain_in_window:
            results["cure_found"] = True

        if loss_in_window and gain_in_window:
            window_hits.append({
                "sentence_index": idx + 1,
                "explicit_pharmakon": explicit_in_sentence
            })

    if window_hits:
        results["balance"] = "balanced"
        results["note"] = "Both poison and cure aspects present—good pharmakon structure"
        results["windowed_pairs"] = window_hits
    
    # Assess balance
    if results.get("balance") != "balanced":
        if results["poison_found"] and results["cure_found"]:
            results["balance"] = "balanced"
            results["note"] = "Both poison and cure aspects present—good pharmakon structure"
        elif results["poison_found"]:
            results["balance"] = "poison_heavy"
            results["status"] = "warn"
            results["note"] = "Only poison aspect visible—consider showing what character gains"
        elif results["cure_found"]:
            results["balance"] = "cure_heavy"
            results["status"] = "warn"
            results["note"] = "Only cure aspect visible—consider showing what character loses"
        else:
            results["balance"] = "neither"
            results["status"] = "warn"
            results["note"] = "Neither poison nor cure aspects detected—scene may lack pharmakon dynamic"
    
    return results


def validate_philosophy(filepath: str, thread: str = None) -> Dict:
    """Main validation function."""
    try:
        text = load_file(filepath)
    except FileNotFoundError:
        return {"status": "error", "message": f"File not found: {filepath}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
    movement = CONFIG.get("movement", "two")
    cycle = CONFIG.get("cycle", 1)
    pharmakon_required = CONFIG.get("philosophy", {}).get("pharmakon_required", True)
    
    # Run analyses
    shackles = check_shackles(text)
    forbidden = check_forbidden_moves(text)
    grounding = check_philosophical_grounding(text)
    pharmakon = check_pharmakon(text, thread) if pharmakon_required else {"status": "skip"}
    
    results = {
        "file": filepath,
        "thread": thread,
        "movement": movement,
        "cycle": cycle,
        "shackle_analysis": shackles,
        "forbidden_moves": forbidden,
        "philosophical_grounding": grounding,
        "pharmakon_analysis": pharmakon,
    }
    
    # Determine overall status
    statuses = [shackles["status"], forbidden["status"]]
    if pharmakon_required:
        statuses.append(pharmakon["status"])
    
    if "fail" in statuses:
        results["status"] = "fail"
    elif "warn" in statuses:
        results["status"] = "warn"
    else:
        results["status"] = "pass"
    
    # Generate summary
    results["summary"] = {
        "shackle_violations": len(shackles["violations"]),
        "forbidden_move_violations": len(forbidden["violations"]),
        "philosophical_categories_present": sum(
            1 for cat in grounding["by_category"].values() if cat["found"]
        ),
        "pharmakon_balanced": pharmakon.get("balance") == "balanced",
        "recommendations": []
    }
    
    if shackles["violations"]:
        results["summary"]["recommendations"].append(
            f"Fix {len(shackles['violations'])} shackle violations—reframe using intensity/pattern language"
        )
    if grounding["status"] == "warn":
        results["summary"]["recommendations"].append(
            "Add philosophical grounding markers (affirmation, difference language)"
        )
    if pharmakon.get("balance") != "balanced" and pharmakon_required:
        results["summary"]["recommendations"].append(
            f"Balance pharmakon: {pharmakon.get('note', 'add both poison and cure aspects')}"
        )
    
    return results


def main():
    parser = argparse.ArgumentParser(
        description="Validate prose against philosophical constraints for Movement Two"
    )
    parser.add_argument("file", help="Path to markdown file to validate")
    parser.add_argument("--thread", 
                        choices=["archaeologist", "algorithm", "last_human"],
                        help="Thread for pharmakon-specific validation (optional)")
    parser.add_argument("--pretty", action="store_true", help="Pretty print JSON output")
    parser.add_argument("--cycle", type=int, choices=[1, 2, 3],
                        help="Override cycle from config (optional)")
    
    args = parser.parse_args()
    
    # Allow cycle override
    if args.cycle:
        CONFIG["cycle"] = args.cycle
    
    results = validate_philosophy(args.file, args.thread)
    
    if args.pretty:
        print(json.dumps(results, indent=2))
    else:
        print(json.dumps(results))
    
    # Exit with appropriate code
    if results["status"] == "fail":
        sys.exit(1)
    elif results["status"] == "warn":
        sys.exit(0)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
