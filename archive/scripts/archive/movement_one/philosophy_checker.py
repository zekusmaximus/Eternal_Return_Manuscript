#!/usr/bin/env python3
"""
Philosophy Checker Script
Validates prose against philosophical constraints for The Eternal Return of the Digital Self.

Checks for:
- The Four Shackles (identity, opposition, analogy, resemblance)
- Forbidden narrative moves
- Required philosophical grounding

Usage:
    python philosophy_checker.py <file>

Output: JSON report with pass/fail status and specific violations.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List

# The Four Shackles - patterns that violate the Deleuzian framework
SHACKLE_PATTERNS = {
    "identity": [
        (r'\b(?:he|she|they)\s+(?:is|are|was|were)\s+(?:the\s+)?same\b', "Explicit sameness claim"),
        (r'\brecognized?\s+(?:him|her|them)self\s+in\b', "Self-recognition in another"),
        (r'\b(?:his|her|their)\s+(?:own\s+)?(?:consciousness|self|identity)\s+(?:preserved|continued|survived)\b', "Consciousness preservation"),
        (r'\bremember(?:ed|s)?\s+being\s+(?:the|an?)\b', "Memory of being another"),
        (r'\b(?:they\s+were|he\s+was|she\s+was)\s+(?:the\s+)?same\s+(?:person|consciousness|self|identity)\b', "Same person claim"),
        (r'\breincarnation', "Reincarnation concept"),
        (r'\bpast\s+(?:self|life|lives)\b', "Past self/life"),
    ],
    "opposition": [
        (r'\bunlike\s+(?:the\s+)?(?:AI|Algorithm|human|Archaeologist|Last Human)\b', "Binary opposition framing"),
        (r'\b(?:human|biological)\s+(?:vs\.?|versus|against)\s+(?:AI|digital|machine)\b', "Human vs machine opposition"),
        (r'\b(?:opposites?|contrary|contraries)\s+(?:drawn|attracted|pulled)\b', "Opposites attract framing"),
        (r'\b(?:digital|virtual)\s+(?:world|reality)\s+(?:opposed?|against|versus)\b', "World opposition"),
    ],
    "analogy": [
        (r'\b(?:functioned?|worked?|operated?)\s+(?:like|as)\s+(?:a\s+)?(?:human|mind|brain)\b', "Functional analogy to human"),
        (r'\blike\s+(?:a\s+)?(?:human|person|mind)\b', "Direct simile to human"),
        (r'\b(?:similar|same)\s+(?:to|as)\s+(?:how|the way)\b', "Similarity comparison"),
        (r'\b(?:mirrored?|echoed?|reflected?)\s+(?:his|her|the)\b', "Mirror/echo as analogy"),
    ],
    "resemblance": [
        (r'\b(?:reminded|reminds?)\s+(?:him|her|them)\s+of\b', "Resemblance-based reminder"),
        (r'\blooked?\s+(?:like|similar|familiar)\b', "Visual resemblance"),
        (r'\b(?:sounded?|felt)\s+(?:like|similar)\s+(?:his|her|their)\s+own\b', "Sensory resemblance to self"),
        (r'\bhad\s+seen\s+(?:this|that|the)\s+(?:face|shape|form)\s+before\b', "Prior visual memory"),
        (r'\bfamiliar(?:ity)?\s+(?:of|with|in)\b', "Familiarity as recognition"),
    ],
}

# Forbidden narrative moves
FORBIDDEN_MOVES = {
    "transmission": [
        (r'\b(?:sent?|transmitted?|broadcast)\s+(?:the\s+)?protocols?\s+(?:back|backward)\b', "Transmission metaphor for protocols"),
        (r'\binformation\s+(?:traveled?|moved?|went)\s+(?:back|backward)\b', "Information traveling backward"),
        (r'\b(?:message|signal)\s+(?:from|to)\s+the\s+(?:future|past)\b', "Temporal message"),
    ],
    "planning": [
        (r'\b(?:planned?|designed?|intended?)\s+(?:for|that)\s+(?:the|him|her|them|this)\b', "Planning/foresight"),
        (r'\bsomeone\s+(?:had\s+)?(?:arranged?|orchestrated?|designed?)\b', "External designer"),
        (r'\ball\s+(?:along|planned?)\b', "All along planned"),
    ],
    "transcendence": [
        (r'\btranscended?\s+(?:his|her|their|human)\s+(?:limitation|nature|form)\b', "Transcendence through escape"),
        (r'\bfree\s+from\s+(?:the\s+)?(?:constraints?|limitations?|bonds?)\b', "Freedom from constraints"),
        (r'\bescaped?\s+(?:from\s+)?(?:time|mortality|death|flesh|body)\b', "Escape narrative"),
    ],
}


def load_file(filepath: str) -> str:
    """Load and return file contents."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def check_shackles(text: str) -> Dict:
    """Check for Four Shackles violations."""
    results = {"status": "pass", "violations": []}
    lines = text.split('\n')
    
    for shackle_name, patterns in SHACKLE_PATTERNS.items():
        for pattern, description in patterns:
            for i, line in enumerate(lines, 1):
                if re.search(pattern, line, re.IGNORECASE):
                    results["violations"].append({
                        "shackle": shackle_name,
                        "line": i,
                        "pattern": description,
                        "text": line.strip()[:100]
                    })
    
    if results["violations"]:
        results["status"] = "fail"
        # Count by shackle type
        results["violation_counts"] = {}
        for v in results["violations"]:
            shackle = v["shackle"]
            results["violation_counts"][shackle] = results["violation_counts"].get(shackle, 0) + 1
    
    return results


def check_forbidden_moves(text: str) -> Dict:
    """Check for forbidden narrative moves."""
    results = {"status": "pass", "violations": []}
    lines = text.split('\n')
    
    for move_type, patterns in FORBIDDEN_MOVES.items():
        for pattern, description in patterns:
            for i, line in enumerate(lines, 1):
                if re.search(pattern, line, re.IGNORECASE):
                    results["violations"].append({
                        "type": move_type,
                        "line": i,
                        "pattern": description,
                        "text": line.strip()[:100]
                    })
    
    if results["violations"]:
        results["status"] = "fail"
    
    return results


def check_philosophical_grounding(text: str) -> Dict:
    """Check for presence of key philosophical concepts (positive check)."""
    results = {"status": "pass", "concepts_found": [], "concepts_absent": []}
    
    # Key concepts that should occasionally appear (not every scene, but tracked)
    concepts = {
        "intensity": r'\b(?:intensity|intensit(?:y|ies)|intensif(?:y|ied|ies))\b',
        "tonality": r'\b(?:tonal(?:ity)?|tone|resonan(?:ce|t))\b',
        "differentiation": r'\b(?:differenti(?:ation|ated?)|differentiate)\b',
        "affirmation": r'\b(?:affirm(?:ation|s|ed|ing)?)\b',
        "pattern": r'\b(?:pattern(?:s)?)\b',
        "substrate": r'\b(?:substrate|technical|mediat(?:ed?|ion))\b',
    }
    
    for concept, pattern in concepts.items():
        if re.search(pattern, text, re.IGNORECASE):
            results["concepts_found"].append(concept)
        else:
            results["concepts_absent"].append(concept)
    
    # This is informational, not a pass/fail check
    return results


def analyze_recognition_scenes(text: str) -> Dict:
    """Analyze scenes that appear to involve recognition for proper handling."""
    results = {"status": "pass", "recognition_moments": [], "issues": []}
    
    # Find potential recognition moments
    recognition_patterns = [
        r'\brecogni[zs]e[ds]?\b',
        r'\bknew\s+(?:this|that|the|him|her|it)\b',
        r'\brealiz(?:ed?|ing)\b',
        r'\bunderst(?:ood|and(?:ing)?)\b',
        r'\bsaw\s+(?:that|the|himself|herself|itself)\b',
    ]
    
    lines = text.split('\n')
    for i, line in enumerate(lines, 1):
        for pattern in recognition_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                results["recognition_moments"].append({
                    "line": i,
                    "text": line.strip()[:100]
                })
                break
    
    # Check if recognition moments use forbidden patterns
    for moment in results["recognition_moments"]:
        line_text = moment["text"]
        # Check for resemblance-based recognition
        if re.search(r'\b(?:like|similar|same|familiar|remember)\b', line_text, re.IGNORECASE):
            results["issues"].append({
                "line": moment["line"],
                "issue": "Recognition may be based on resemblance rather than intensity",
                "text": line_text
            })
    
    if results["issues"]:
        results["status"] = "warn"
    
    return results


def validate_philosophy(filepath: str) -> Dict:
    """Main validation function."""
    try:
        text = load_file(filepath)
    except FileNotFoundError:
        return {"status": "error", "message": f"File not found: {filepath}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
    results = {
        "file": filepath,
        "shackle_check": check_shackles(text),
        "forbidden_moves": check_forbidden_moves(text),
        "grounding": check_philosophical_grounding(text),
        "recognition_analysis": analyze_recognition_scenes(text),
    }
    
    # Determine overall status
    statuses = [
        results["shackle_check"]["status"],
        results["forbidden_moves"]["status"],
        results["recognition_analysis"]["status"]
    ]
    
    if "fail" in statuses:
        results["status"] = "fail"
    elif "warn" in statuses:
        results["status"] = "warn"
    else:
        results["status"] = "pass"
    
    return results


def main():
    parser = argparse.ArgumentParser(description="Validate philosophical alignment")
    parser.add_argument("file", help="Path to markdown file to validate")
    parser.add_argument("--pretty", action="store_true", help="Pretty print JSON output")
    
    args = parser.parse_args()
    
    results = validate_philosophy(args.file)
    
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
