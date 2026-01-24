#!/usr/bin/env python3
"""
Voice Validator Script — Movement Two
Validates prose with controlled contamination awareness for braided narrative.

Movement Two requires voice bleeding as a feature, not a bug: 
- Cycle 1: Contamination during intensity moments only
- Cycle 2: Traces in normal passages
- Cycle 3: Pervasive but character-distinct

Usage:
    python voice_validator.py <file> --thread <archaeologist|algorithm|last_human>
    
Reads movement/cycle from movement_config.json for unified configuration.

Output: JSON report with voice analysis and contamination assessment.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple
from collections import Counter

# Load configuration
def load_config() -> Dict:
    """Load movement configuration from JSON file."""
    config_path = Path(__file__).parent / "movement_config.json"
    if config_path.exists():
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"movement": "two", "cycle": 1}  # Defaults

CONFIG = load_config()

# Base voice patterns (what defines each voice at its core)
VOICE_CORE = {
    "archaeologist": {
        "signature_tense": "present",
        "signature_patterns": [
            r'\bI\s+(find|see|hear|feel|touch|grab|take|put|hold|work|look|watch)\b',
            r'\b(drive|server|interface|terminal|screen|hardware)\b',
            r'\b(cold|weight|pressure|texture|smooth|rough|heavy)\b',
            r'\b(fee|contract|client|payment|cost|afford)\b',
        ],
        "syntax_expectation": "active_verbs",
        "avg_sentence_length": {"min": 8, "max": 25},
    },
    "algorithm": {
        "signature_tense": "shifting",
        "signature_patterns": [
            r'\bI\s+(?:process|analyze|verify|calculate|model|query)\b',
            r'\b(?:if|would|could|might|perhaps|should)\b.*\b(?:then|therefore)\b',
            r'\b(?:consciousness|awareness|perception|attention)\b',
            r'\b(?:probability|likelihood|percentage|variance)\b',
        ],
        "syntax_expectation": "nested_clauses",
        "avg_sentence_length": {"min": 15, "max": 40},
    },
    "last_human": {
        "signature_tense": "past_inflected_present",
        "signature_patterns": [
            r'\b(?:was|were|had been|once|used to)\b',
            r'\b(?:ruins?|decay|crumble|empty|hollow|silence|alone)\b',
            r'\b(?:walk|journey|path|distance|horizon)\b',
            r'(?:^|\.\s+)[A-Z][a-z]+\.',  # Sentence fragments
        ],
        "syntax_expectation": "fragments_and_sparse",
        "avg_sentence_length": {"min": 3, "max": 15},
    }
}

# Contamination markers: patterns that indicate bleeding FROM another voice
CONTAMINATION_MARKERS = {
    "archaeologist": {
        "from_algorithm": [
            (r'\bif\s+.*,\s+then\s+(?:perhaps|maybe)', "Nested conditional clause"),
            (r'\bI\s+(?:calculate|determine|process|analyze|optimize)\b', "Self-referential processing"),
            (r'\b\d{1,3}%\s+(?:likelihood|probability|chance)\b', "Probabilistic hedging"),
            (r'\b(?:query|recursive|iterate|loop)\b', "Algorithm vocabulary"),
        ],
        "from_last_human": [
            (r'(?:^|\.\s+)[A-Z][a-z]+\.\s+[A-Z][a-z]+\.', "Consecutive fragments"),
            (r'\b(?:once|had been|was a)\s+(?:time|city|world)\b', "Elegiac past-inflection"),
            (r'\b(?:silence|emptiness|hollow|alone)\s+(?:of|in|that)\b', "Absence vocabulary"),
        ],
    },
    "algorithm": {
        "from_archaeologist": [
            (r'\bI\s+(?:grab|touch|feel|hold)\s+(?:the|a|my)\b', "Physical tactile action"),
            (r'\b(?:cold|warm|weight|pressure)\s+(?:of|in|on|against)\b', "Physical sensation"),
            (r'\b(?:Lena|Marcus|client|payment)\b', "Archaeologist's world specifics"),
        ],
        "from_last_human": [
            (r'(?:^|\.\s+)[A-Z][a-z]+\.\s*$', "Sentence fragment ending"),
            (r'\b(?:ruins?|decay|crumble|erode)\b', "Elegiac vocabulary"),
            (r'\b(?:last|only|final)\s+(?:human|person|one)\b', "Last Human identity"),
        ],
    },
    "last_human": {
        "from_archaeologist": [
            (r'\b(?:client|contract|fee|payment|cost|afford)\b', "Economic concerns"),
            (r'\b(?:interface|terminal|server|drive)\b', "Near-future technology"),
            (r'\bI\s+(?:work|take|grab|hold)\s+the\b', "Active present-tense work"),
        ],
        "from_algorithm": [
            (r'\bI\s+(?:process|calculate|optimize|analyze)\b', "Processing language"),
            (r'\bif\s+.*,\s+then\s+(?:perhaps|maybe)\b', "Nested conditionals"),
            (r'\b\d+(?:\.\d+)?%', "Percentages/probabilities"),
            (r'\b(?:consciousness|awareness)\s+(?:as|itself)\b', "Abstract self-reference"),
        ],
    }
}

INTENSITY_PATTERNS = [
    r'\bbleed\b',
    r'\bresonance\b',
    r'\bresonant\b',
    r'\bpanic\b',
    r'\bfrequency\b',
    r'\bintensity\b',
    r'\bvibration\b',
    r'\bdream(?:s|ing|t)?\b',
    r'\bintrusion\b',
    r'\bsurge\b',
    r'\boverload\b',
    r'\bshock\b',
    r'\bstatic\b',
    r'\bsignal\b',
    r'\bthreshold\b',
    r'\boverlap\b',
    r'\bflicker\b',
    r'\bcold\b',
    r'\bhands?\b',
    r'\bweight\b',
    r'\bpressure\b',
    r'\btemperature\b'
]


def load_file(filepath: str) -> str:
    """Load and return file contents."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def count_words(text: str) -> int:
    """Count words in text."""
    return len(text.split())


def detect_intensity_lines(lines: List[str]) -> Dict:
    """Identify intensity lines using keyword patterns."""
    flags = [False] * len(lines)

    paragraphs = []
    start = 0
    for i, line in enumerate(lines):
        if line.strip() == "":
            if start <= i - 1:
                paragraphs.append((start, i - 1))
            start = i + 1
    if start < len(lines):
        paragraphs.append((start, len(lines) - 1))

    for start_idx, end_idx in paragraphs:
        paragraph_text = "\n".join(lines[start_idx:end_idx + 1])
        if any(re.search(pattern, paragraph_text, re.IGNORECASE) for pattern in INTENSITY_PATTERNS):
            for j in range(start_idx, end_idx + 1):
                flags[j] = True

    return {
        "flags": flags,
        "count": sum(1 for f in flags if f)
    }


def analyze_voice_signature(text: str, thread: str) -> Dict:
    """Analyze how strongly the text matches the thread's core voice signature."""
    config = VOICE_CORE[thread]
    results = {
        "status": "pass",
        "signature_strength": 0,
        "matches": [],
        "issues": []
    }
    
    total_matches = 0
    for pattern in config["signature_patterns"]:
        matches = re.findall(pattern, text, re.IGNORECASE | re.MULTILINE)
        if matches:
            total_matches += len(matches)
            results["matches"].append({
                "pattern": pattern[:50],
                "count": len(matches)
            })
    
    # Calculate signature strength as matches per 1000 words
    word_count = count_words(text)
    if word_count > 0:
        results["signature_strength"] = round((total_matches / word_count) * 1000, 1)
    
    # Check if signature is strong enough (at least 10 matches per 1000 words)
    if results["signature_strength"] < 10:
        results["status"] = "warn"
        results["issues"].append(
            f"Weak voice signature: {results['signature_strength']} matches/1000 words (target: ≥10)"
        )
    
    return results


def detect_contamination(text: str, thread: str) -> Dict:
    """Detect contamination from other voices."""
    markers = CONTAMINATION_MARKERS[thread]
    lines = text.split('\n')
    intensity = detect_intensity_lines(lines)
    
    results = {
        "total_contamination": 0,
        "by_source": {},
        "by_segment": {"base": 0, "intensity": 0},
        "by_source_segment": {},
        "instances": [],
        "intensity_segments": {
            "lines_flagged": intensity["count"],
            "total_lines": len(lines)
        }
    }
    
    for source, patterns in markers.items():
        source_thread = source.replace("from_", "")
        results["by_source"][source_thread] = 0
        results["by_source_segment"][source_thread] = {"base": 0, "intensity": 0}
        
        for pattern, description in patterns:
            for i, line in enumerate(lines, 1):
                if re.search(pattern, line, re.IGNORECASE):
                    segment = "intensity" if intensity["flags"][i - 1] else "base"
                    results["instances"].append({
                        "line": i,
                        "source": source_thread,
                        "type": description,
                        "text": line.strip()[:80]
                    })
                    results["by_source"][source_thread] += 1
                    results["total_contamination"] += 1
                    results["by_segment"][segment] += 1
                    results["by_source_segment"][source_thread][segment] += 1
    
    return results


def assess_contamination(contamination: Dict, cycle: int) -> Dict:
    """Assess if contamination level is appropriate for the cycle."""
    budget = CONFIG.get("contamination", {}).get("budget", {})
    cycle_key = f"cycle_{cycle}"
    cycle_budget = budget.get(cycle_key, {"min": 0, "max": 10})
    
    total = contamination["total_contamination"]
    base_total = contamination["by_segment"].get("base", 0)
    intensity_total = contamination["by_segment"].get("intensity", 0)
    
    result = {
        "status": "pass",
        "cycle": cycle,
        "expected_range": f"{cycle_budget['min']}-{cycle_budget['max']}",
        "actual": {
            "total": total,
            "base": base_total,
            "intensity": intensity_total
        },
        "issues": [],
        "notes": []
    }

    if cycle == 1:
        base_max = max(2, int(cycle_budget["max"] * 0.25))
        result["expected_range"] = f"base ≤{base_max} (intensity allowed)"

        if base_total > base_max:
            result["status"] = "warn"
            result["issues"].append(
                f"Too much contamination outside intensity segments for Cycle 1: found {base_total}, expected ≤{base_max}."
            )

        if intensity_total > 0:
            result["notes"].append(
                f"Intensity-segment contamination detected ({intensity_total}) and allowed for Cycle 1."
            )
    else:
        if total < cycle_budget["min"]:
            result["status"] = "warn"
            result["issues"].append(
                f"Too little contamination for Cycle {cycle}: found {total}, expected ≥{cycle_budget['min']}. "
                f"Scene may be too 'pure' for Movement Two's braided structure."
            )
        
        if total > cycle_budget["max"]:
            result["status"] = "warn"
            result["issues"].append(
                f"Too much contamination for Cycle {cycle}: found {total}, expected ≤{cycle_budget['max']}. "
                f"Voice may be dissolving prematurely (save for Movement Three)."
            )
    
    # Check for mutual contamination
    sources = contamination["by_source"]
    contaminated_from = [s for s, count in sources.items() if count > 0]
    if len(contaminated_from) == 1:
        result["notes"].append(
            f"One-directional contamination (from {contaminated_from[0]} only). "
            f"Consider: is reciprocal contamination present in the other thread's scene?"
        )
    
    return result


def analyze_syntax(text: str, thread: str, cycle: int) -> Dict:
    """Analyze syntax patterns with cycle-aware expectations."""
    config = VOICE_CORE[thread]
    results = {"status": "pass", "issues": [], "metrics": {}}
    
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    if not sentences:
        return {"status": "error", "issues": ["No sentences found"]}
    
    # Calculate metrics
    avg_length = sum(len(s.split()) for s in sentences) / len(sentences)
    short_sentences = sum(1 for s in sentences if len(s.split()) <= 5)
    long_sentences = sum(1 for s in sentences if len(s.split()) > 20)
    
    results["metrics"] = {
        "total_sentences": len(sentences),
        "avg_words_per_sentence": round(avg_length, 1),
        "short_sentences_pct": round(short_sentences / len(sentences) * 100, 1),
        "long_sentences_pct": round(long_sentences / len(sentences) * 100, 1)
    }
    
    # Check syntax with cycle-aware thresholds
    # In later cycles, syntax expectations loosen due to contamination
    tolerance = 1 + (cycle * 0.2)  # 20% more tolerance per cycle
    
    expected = config["avg_sentence_length"]
    if avg_length < expected["min"] / tolerance:
        results["issues"].append(
            f"Sentences shorter than expected for {thread} (avg: {avg_length:.1f}, expected: ≥{expected['min']})"
        )
    if avg_length > expected["max"] * tolerance:
        results["issues"].append(
            f"Sentences longer than expected for {thread} (avg: {avg_length:.1f}, expected: ≤{expected['max']})"
        )
    
    if results["issues"]:
        results["status"] = "warn"
    
    return results


def validate_voice(filepath: str, thread: str) -> Dict:
    """Main validation function."""
    if thread not in VOICE_CORE:
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
    signature = analyze_voice_signature(text, thread)
    contamination = detect_contamination(text, thread)
    contamination_assessment = assess_contamination(contamination, cycle)
    syntax = analyze_syntax(text, thread, cycle)
    
    results = {
        "file": filepath,
        "thread": thread,
        "movement": movement,
        "cycle": cycle,
        "word_count": count_words(text),
        "voice_signature": signature,
        "contamination_detected": contamination,
        "contamination_assessment": contamination_assessment,
        "syntax_analysis": syntax,
    }
    
    # Determine overall status
    statuses = [
        signature["status"],
        contamination_assessment["status"],
        syntax["status"]
    ]
    
    if "fail" in statuses:
        results["status"] = "fail"
    elif "warn" in statuses:
        results["status"] = "warn"
    else:
        results["status"] = "pass"
    
    # Generate summary
    results["summary"] = {
        "voice_identifiable": signature["signature_strength"] >= 10,
        "contamination_appropriate": contamination_assessment["status"] == "pass",
        "contamination_sources": [s for s, c in contamination["by_source"].items() if c > 0],
        "contamination_by_segment": contamination.get("by_segment", {}),
        "recommendations": []
    }
    
    # Add recommendations
    if signature["status"] != "pass":
        results["summary"]["recommendations"].append(
            "Strengthen core voice signature with more thread-specific vocabulary and syntax"
        )
    if contamination_assessment["status"] != "pass":
        for issue in contamination_assessment["issues"]:
            results["summary"]["recommendations"].append(issue)
    
    return results


def main():
    parser = argparse.ArgumentParser(
        description="Validate prose voice with Movement Two contamination awareness"
    )
    parser.add_argument("file", help="Path to markdown file to validate")
    parser.add_argument("--thread", required=True, 
                        choices=["archaeologist", "algorithm", "last_human"],
                        help="Voice thread to validate against")
    parser.add_argument("--pretty", action="store_true", help="Pretty print JSON output")
    parser.add_argument("--cycle", type=int, choices=[1, 2, 3],
                        help="Override cycle from config (optional)")
    
    args = parser.parse_args()
    
    # Allow cycle override
    if args.cycle:
        CONFIG["cycle"] = args.cycle
    
    results = validate_voice(args.file, args.thread)
    
    if args.pretty:
        print(json.dumps(results, indent=2))
    else:
        print(json.dumps(results))
    
    # Exit with appropriate code
    if results["status"] == "fail":
        sys.exit(1)
    elif results["status"] == "warn":
        sys.exit(0)  # Warnings don't fail the build
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
