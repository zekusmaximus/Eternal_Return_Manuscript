#!/usr/bin/env python3
"""
Voice Validator Script
Validates prose against voice reference files for The Eternal Return of the Digital Self.

Usage:
    python voice_validator.py <file> --thread <archaeologist|algorithm|last_human>

Output: JSON report with pass/fail status and specific issues.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple
from collections import Counter

# Voice-specific patterns
VOICE_CONFIG = {
    "archaeologist": {
        "required_tense": "present",
        "tense_patterns": {
            "present": [r'\b(I|he|she)\s+(find|see|hear|feel|touch|grab|take|put|hold|work|look|watch|run|walk|stand|sit|move)\b'],
            "past": [r'\b(found|saw|heard|felt|touched|grabbed|took|put|held|worked|looked|watched|ran|walked|stood|sat|moved)\b'],
        },
        "forbidden_patterns": [
            (r'\bif\s+.*,\s+then\s+(?:perhaps|maybe)', "Nested conditional clause (Algorithm contamination)"),
            (r'\bI\s+(?:calculate|determine|process|analyze|optimize)\b', "Self-referential processing language (Algorithm contamination)"),
            (r'\b\d{1,3}%\s+(?:likelihood|probability|chance)\b', "Probabilistic hedging (Algorithm contamination)"),
            (r'(?:^|\.\s+)[A-Z][a-z]+\.\s+[A-Z][a-z]+\.(?:\s+|$)', "Sentence fragments (Last Human contamination)"),
        ],
        "required_textures": [
            (r'\b(?:drive|server|interface|terminal|screen|hardware|keyboard|monitor)\b', "technology/hardware"),
            (r'\b(?:cold|warm|weight|pressure|texture|smooth|rough|heavy)\b', "tactile"),
            (r'\b(?:fee|contract|client|payment|cost|earn|afford|price)\b', "economic"),
        ],
        "syntax_check": "active_verbs",
    },
    "algorithm": {
        "required_tense": "shifting",
        "tense_patterns": {
            "present": [r'\bI\s+(?:process|analyze|verify|calculate|model|query)\b'],
            "past": [r'\b(?:was|were|had been|remembered|experienced)\b'],
            "conditional": [r'\b(?:if|would|could|might|perhaps|should)\b'],
        },
        "forbidden_patterns": [
            (r'\b(?:I\s+)?(?:grab|touch|feel|hold)\s+(?:the|a|my)\b', "Physical tactile action (Archaeologist contamination)"),
            (r'\b(?:cold|warm|weight|pressure)\s+(?:of|in|on)\b', "Physical sensation (Archaeologist contamination)"),
            (r'(?:^|\.\s+)[A-Z][a-z]+\.\s*$', "Sentence fragment (Last Human contamination)"),
            (r'\b(?:ruins|decay|crumble|erode|empty|hollow)\b', "Elegiac vocabulary (Last Human contamination)"),
        ],
        "required_textures": [
            (r'\b(?:process|optimize|calculate|analyze|query|model|verify)\b', "processing"),
            (r'\b(?:consciousness|awareness|self|perception|attention)\b', "self-reference"),
            (r'\b(?:if|then|perhaps|would|could|might)\b', "conditional"),
        ],
        "syntax_check": "nested_clauses",
    },
    "last_human": {
        "required_tense": "past_inflected_present",
        "tense_patterns": {
            "past_inflected": [r'\b(?:was|were|had been|once|used to)\b'],
            "present": [r'\bI\s+(?:walk|see|hear|feel|stand|sit|look)\b'],
        },
        "forbidden_patterns": [
            (r'\b(?:client|contract|fee|payment|cost|afford)\b', "Economic concerns (Archaeologist contamination)"),
            (r'\b(?:I\s+)?(?:process|calculate|optimize|analyze)\b', "Processing language (Algorithm contamination)"),
            (r'\bif\s+.*,\s+then\s+(?:perhaps|maybe)\b', "Nested conditionals (Algorithm contamination)"),
            (r'\b\d+(?:\.\d+)?%', "Percentages/probabilities (Algorithm contamination)"),
        ],
        "required_textures": [
            (r'\b(?:ruins?|decay|crumble|erode|empty|hollow|silence|alone)\b', "absence/decay"),
            (r'\b(?:was|were|once|had been|used to|remember)\b', "past-inflection"),
            (r'\b(?:walk|journey|path|distance|horizon)\b', "movement/landscape"),
        ],
        "syntax_check": "fragments_and_sparse",
    }
}


def load_file(filepath: str) -> str:
    """Load and return file contents."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def count_words(text: str) -> int:
    """Count words in text."""
    return len(text.split())


def analyze_tense(text: str, thread: str) -> Dict:
    """Analyze tense usage against expected patterns."""
    config = VOICE_CONFIG[thread]
    results = {"status": "pass", "issues": [], "tense_distribution": {}}
    
    patterns = config["tense_patterns"]
    tense_counts = {}
    
    for tense_name, pattern_list in patterns.items():
        count = 0
        for pattern in pattern_list:
            matches = re.findall(pattern, text, re.IGNORECASE)
            count += len(matches)
        tense_counts[tense_name] = count
    
    results["tense_distribution"] = tense_counts
    
    # Check tense requirements based on thread
    if thread == "archaeologist":
        if tense_counts.get("past", 0) > tense_counts.get("present", 0) * 0.3:
            results["status"] = "warn"
            results["issues"].append("High past tense usage for archaeologist (should be primarily present)")
    
    elif thread == "algorithm":
        # Algorithm should have mixed tenses
        if len([t for t, c in tense_counts.items() if c > 0]) < 2:
            results["status"] = "warn"
            results["issues"].append("Algorithm voice should use shifting tenses (present/past/conditional)")
    
    elif thread == "last_human":
        if tense_counts.get("past_inflected", 0) < 3:
            results["status"] = "warn"
            results["issues"].append("Last Human voice should have past-inflected present constructions")
    
    return results


def check_forbidden_patterns(text: str, thread: str) -> Dict:
    """Check for forbidden patterns indicating voice contamination."""
    config = VOICE_CONFIG[thread]
    results = {"status": "pass", "violations": []}
    
    lines = text.split('\n')
    for pattern, description in config["forbidden_patterns"]:
        for i, line in enumerate(lines, 1):
            if re.search(pattern, line, re.IGNORECASE):
                results["violations"].append({
                    "line": i,
                    "pattern": description,
                    "text": line.strip()[:100]
                })
    
    if results["violations"]:
        results["status"] = "fail"
    
    return results


def check_required_textures(text: str, thread: str) -> Dict:
    """Check for presence of required texture vocabulary."""
    config = VOICE_CONFIG[thread]
    results = {"status": "pass", "textures": {}, "missing": []}
    
    for pattern, texture_type in config["required_textures"]:
        matches = re.findall(pattern, text, re.IGNORECASE)
        results["textures"][texture_type] = len(matches)
        if len(matches) == 0:
            results["missing"].append(texture_type)
    
    # If more than half of textures are missing, flag as issue
    if len(results["missing"]) > len(config["required_textures"]) / 2:
        results["status"] = "warn"
    
    return results


def analyze_syntax(text: str, thread: str) -> Dict:
    """Analyze syntax patterns against expected patterns."""
    config = VOICE_CONFIG[thread]
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
    
    # Check syntax based on thread
    check_type = config["syntax_check"]
    
    if check_type == "active_verbs":
        # Archaeologist should have direct, active prose
        if avg_length > 25:
            results["issues"].append("Sentences too long for archaeologist voice (aim for direct, active prose)")
    
    elif check_type == "nested_clauses":
        # Algorithm should have nested, complex sentences
        if avg_length < 15:
            results["issues"].append("Sentences too short for algorithm voice (allow nested complexity)")
    
    elif check_type == "fragments_and_sparse":
        # Last Human should have fragments and sparse prose
        if short_sentences / len(sentences) < 0.2:
            results["issues"].append("Too few short sentences/fragments for Last Human voice")
    
    if results["issues"]:
        results["status"] = "warn"
    
    return results


def validate_voice(filepath: str, thread: str) -> Dict:
    """Main validation function."""
    if thread not in VOICE_CONFIG:
        return {"status": "error", "message": f"Unknown thread: {thread}"}
    
    try:
        text = load_file(filepath)
    except FileNotFoundError:
        return {"status": "error", "message": f"File not found: {filepath}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
    results = {
        "file": filepath,
        "thread": thread,
        "word_count": count_words(text),
        "tense_analysis": analyze_tense(text, thread),
        "forbidden_patterns": check_forbidden_patterns(text, thread),
        "texture_analysis": check_required_textures(text, thread),
        "syntax_analysis": analyze_syntax(text, thread),
    }
    
    # Determine overall status
    statuses = [
        results["tense_analysis"]["status"],
        results["forbidden_patterns"]["status"],
        results["texture_analysis"]["status"],
        results["syntax_analysis"]["status"]
    ]
    
    if "fail" in statuses:
        results["status"] = "fail"
    elif "warn" in statuses:
        results["status"] = "warn"
    else:
        results["status"] = "pass"
    
    return results


def main():
    parser = argparse.ArgumentParser(description="Validate prose voice consistency")
    parser.add_argument("file", help="Path to markdown file to validate")
    parser.add_argument("--thread", required=True, 
                        choices=["archaeologist", "algorithm", "last_human"],
                        help="Voice thread to validate against")
    parser.add_argument("--pretty", action="store_true", help="Pretty print JSON output")
    
    args = parser.parse_args()
    
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
