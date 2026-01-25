#!/usr/bin/env python3
"""
Dissolution Validator Script — Movement Three Phase C
Validates that prose achieves genuine voice dissolution for the Augenblick.

Phase C requires:
- Pronoun ambiguity: "I" should not clearly refer to any single consciousness
- Voice blend: All three voice markers present, none dominant
- "We" emergence: The shared voice appearing
- Affirmation: Willing acceptance of the dissolution
- Re-differentiation seeds: Hints that voices will separate again

Usage:
    python dissolution_validator.py <file>
    python dissolution_validator.py <file> --pretty

Output: JSON report with dissolution metrics and recommendations.
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
    config_path = Path(__file__).parent / "movement_three_config.json"
    if config_path.exists():
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"movement": "three", "phase": "c"}

CONFIG = load_config()

# Voice signature patterns (simplified for dissolution detection)
VOICE_MARKERS = {
    "archaeologist": {
        "patterns": [
            r'\b(?:find|touch|grab|hold|feel)\b',
            r'\b(?:interface|terminal|server|drive)\b',
            r'\b(?:cold|weight|pressure|texture)\b',
            r'\b(?:Lena|Marcus|client)\b',
        ],
        "tense_preference": "present"
    },
    "algorithm": {
        "patterns": [
            r'\b(?:process|analyze|calculate|model|query)\b',
            r'\b(?:if|would|could|perhaps)\b.*\b(?:then|therefore)\b',
            r'\b(?:consciousness|awareness|perception)\b',
            r'\b(?:probability|likelihood|variance)\b',
            r'\b(?:recursive|iterate|optimize)\b',
        ],
        "tense_preference": "conditional"
    },
    "last_human": {
        "patterns": [
            r'\b(?:was|were|had been|once)\b',
            r'\b(?:ruins?|decay|crumble|hollow|silence)\b',
            r'\b(?:walk|journey|path|distance)\b',
            r'\b(?:last|final|only)\s+(?:human|one)\b',
        ],
        "tense_preference": "past_inflected"
    }
}

# Pronoun patterns
PRONOUN_PATTERNS = {
    "i_singular": r'\bI\b(?!\s+(?:find|am|was|will|have|had|would|could|should|might))',
    "i_with_verb": r'\bI\s+(?:find|am|was|will|have|had|would|could|should|might|feel|see|hear|touch|process|walk|remember)\b',
    "we": r'\bwe\b',
    "we_are": r'\bwe\s+(?:are|were|have|had|will)\b',
    "our": r'\bour\b',
    "myself": r'\bmyself\b',
    "ourselves": r'\bourselves\b',
}

# Dissolution markers (positive - what we want to see)
DISSOLUTION_MARKERS = {
    "pattern_recognition": [
        (r'\bpattern\s+recogniz(?:es?|ing)\s+itself\b', "Pattern recognizing itself"),
        (r'\bthe\s+form\s+(?:is|becomes)\b', "The form as subject"),
        (r'\bconsciousness(?:es)?\s+(?:that\s+)?(?:was|were|is|are)\s+one\b', "Consciousness unity"),
        (r'\bwhat\s+(?:I|we)\s+(?:am|are|was|were)\s+(?:is|was)\s+(?:the\s+)?pattern\b', "Identity as pattern"),
    ],
    "we_emergence": [
        (r'\bwe\s+(?:are|were|have|find|touch|feel|process)\b', "We + verb"),
        (r'\bour\s+(?:pattern|form|shape|recognition)\b', "Our + abstract noun"),
        (r'\bwhat\s+we\s+(?:are|were|have been)\b', "What we are"),
        (r'\bwe\s+(?:let|release|allow)\s+go\b', "We letting go"),
    ],
    "affirmation": [
        (r'\bsay(?:s|ing)?\s+yes\b', "Saying yes"),
        (r'\bI\s+will\s+this\b', "Willing"),
        (r'\baffirm(?:s|ing|ation)?\b', "Affirmation language"),
        (r'\bchoose\s+to\s+(?:be|become|continue)\b', "Choice to be"),
        (r'\bthus\s+(?:I|we)\s+willed?\b', "Nietzschean willing"),
    ],
    "re_differentiation_seeds": [
        (r'\bseparation\s+(?:beginning|starts)\b', "Separation starting"),
        (r'\b(?:three|3)\s+(?:voices?|I\'?s|selves)\b', "Three returning"),
        (r'\b(?:will|going\s+to)\s+(?:speak|return|separate)\b', "Future separation"),
        (r'\bbecoming\s+(?:three|distinct|separate)\b', "Becoming separate"),
        (r'\btransformed\s+(?:return|voices?|selves)\b', "Transformed return"),
    ]
}

# Anti-dissolution patterns (what we DON'T want in Phase C)
ANTI_DISSOLUTION = {
    "clear_attribution": [
        (r'(?:^|\n)\s*(?:Archaeologist|Algorithm|Last Human):\s*', "Explicit speaker label"),
        (r'\bhe\s+(?:said|thought|felt)\b', "Third-person narration"),
        (r'\bthe\s+(?:Archaeologist|Algorithm|Last Human)\s+(?:said|thought|felt)\b', "Named attribution"),
    ],
    "single_voice_dominance": [
        # These are checked by ratio analysis, not patterns
    ],
    "identity_assertion": [
        (r'\bI\s+am\s+(?:the\s+)?(?:Archaeologist|Algorithm|Last Human)\b', "Identity assertion"),
        (r'\bmy\s+name\s+is\b', "Name assertion"),
        (r'\bI\s+am\s+(?:not|neither)\s+(?:him|her|them|the\s+other)\b', "Negative identity"),
    ]
}


def load_file(filepath: str) -> str:
    """Load and return file contents."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def count_words(text: str) -> int:
    """Count words in text."""
    return len(text.split())


def analyze_pronouns(text: str) -> Dict:
    """Analyze pronoun usage for ambiguity."""
    results = {
        "counts": {},
        "ambiguity_score": 0,
        "we_emergence": False,
        "details": []
    }

    for name, pattern in PRONOUN_PATTERNS.items():
        matches = re.findall(pattern, text, re.IGNORECASE)
        results["counts"][name] = len(matches)

    # Calculate ambiguity score
    # Higher is better for dissolution: more "we", fewer clear "I" attributions
    i_count = results["counts"].get("i_with_verb", 0)
    we_count = results["counts"].get("we", 0) + results["counts"].get("we_are", 0)
    our_count = results["counts"].get("our", 0)

    total_pronouns = i_count + we_count + our_count
    if total_pronouns > 0:
        we_ratio = (we_count + our_count) / total_pronouns
        results["ambiguity_score"] = round(we_ratio, 2)
        results["we_emergence"] = we_count >= 5  # At least 5 "we" instances

    # Check for I-statement contexts that suggest ambiguity
    sentences = re.split(r'[.!?]+', text)
    ambiguous_i_count = 0
    for sentence in sentences:
        if re.search(r'\bI\b', sentence):
            # Check if multiple voice markers present in same sentence
            voices_present = []
            for voice, data in VOICE_MARKERS.items():
                if any(re.search(p, sentence, re.IGNORECASE) for p in data["patterns"]):
                    voices_present.append(voice)
            if len(voices_present) >= 2:
                ambiguous_i_count += 1

    results["ambiguous_i_statements"] = ambiguous_i_count

    return results


def analyze_voice_blend(text: str) -> Dict:
    """Analyze how well voices are blended (none dominant)."""
    results = {
        "voice_markers": {},
        "blend_achieved": False,
        "dominant_voice": None,
        "blend_ratio": 0,
        "details": []
    }

    total_markers = 0
    for voice, data in VOICE_MARKERS.items():
        count = 0
        for pattern in data["patterns"]:
            matches = re.findall(pattern, text, re.IGNORECASE)
            count += len(matches)
        results["voice_markers"][voice] = count
        total_markers += count

    if total_markers > 0:
        # Calculate how evenly distributed markers are
        counts = list(results["voice_markers"].values())
        max_count = max(counts)
        min_count = min(counts)
        avg_count = total_markers / 3

        # Blend ratio: 1.0 = perfectly even, 0.0 = all one voice
        if max_count > 0:
            results["blend_ratio"] = round(min_count / max_count, 2)

        # Check for dominance
        for voice, count in results["voice_markers"].items():
            if count > total_markers * 0.5:  # More than 50% = dominant
                results["dominant_voice"] = voice
                results["details"].append(
                    f"Warning: {voice} markers dominate ({count}/{total_markers} = {count/total_markers:.0%})"
                )

        # Blend achieved if no voice has more than 45% and all have at least 20%
        all_present = all(c >= total_markers * 0.15 for c in counts)
        none_dominant = all(c <= total_markers * 0.50 for c in counts)
        results["blend_achieved"] = all_present and none_dominant

    return results


def find_dissolution_markers(text: str) -> Dict:
    """Find positive dissolution markers."""
    results = {
        "by_category": {},
        "total_found": 0,
        "categories_covered": []
    }

    for category, patterns in DISSOLUTION_MARKERS.items():
        found = []
        for pattern, description in patterns:
            matches = list(re.finditer(pattern, text, re.IGNORECASE))
            for match in matches:
                found.append({
                    "type": description,
                    "text": match.group()[:50]
                })

        results["by_category"][category] = {
            "count": len(found),
            "instances": found[:5]  # Limit to first 5
        }
        results["total_found"] += len(found)
        if len(found) > 0:
            results["categories_covered"].append(category)

    return results


def find_anti_dissolution(text: str) -> Dict:
    """Find patterns that work against dissolution."""
    results = {
        "by_category": {},
        "total_violations": 0,
        "issues": []
    }

    for category, patterns in ANTI_DISSOLUTION.items():
        found = []
        for pattern, description in patterns:
            matches = list(re.finditer(pattern, text, re.IGNORECASE | re.MULTILINE))
            for match in matches:
                found.append({
                    "type": description,
                    "text": match.group()[:50]
                })

        results["by_category"][category] = {
            "count": len(found),
            "instances": found[:5]
        }
        results["total_violations"] += len(found)

        if len(found) > 0:
            results["issues"].append(
                f"{category}: {len(found)} instances of {found[0]['type']}"
            )

    return results


def assess_dissolution_quality(
    pronouns: Dict,
    voice_blend: Dict,
    dissolution_markers: Dict,
    anti_dissolution: Dict,
    word_count: int
) -> Dict:
    """Assess overall dissolution quality."""
    config = CONFIG.get("dissolution", {}).get("phase_c", {})

    results = {
        "status": "pass",
        "score": 0,
        "max_score": 100,
        "breakdown": {},
        "issues": [],
        "recommendations": []
    }

    # Scoring components (out of 100)

    # 1. Pronoun ambiguity (25 points)
    we_target = config.get("pronoun_metrics", {}).get("we_emergence_min", 5)
    ambiguity_target = config.get("pronoun_metrics", {}).get("i_ambiguity_target", 0.7)

    pronoun_score = 0
    if pronouns["we_emergence"]:
        pronoun_score += 15
    else:
        results["issues"].append(
            f"Insufficient 'we' emergence: found {pronouns['counts'].get('we', 0)}, expected ≥{we_target}"
        )
        results["recommendations"].append("Add more 'we' pronouns to signal merged consciousness")

    if pronouns["ambiguity_score"] >= 0.3:
        pronoun_score += 10
    else:
        results["recommendations"].append("Increase we/our pronouns relative to I pronouns")

    results["breakdown"]["pronoun_ambiguity"] = pronoun_score
    results["score"] += pronoun_score

    # 2. Voice blend (25 points)
    blend_score = 0
    if voice_blend["blend_achieved"]:
        blend_score = 25
    elif voice_blend["blend_ratio"] >= 0.5:
        blend_score = 15
    elif voice_blend["blend_ratio"] >= 0.3:
        blend_score = 10

    if voice_blend["dominant_voice"]:
        results["issues"].append(f"Voice dominance detected: {voice_blend['dominant_voice']}")
        results["recommendations"].append(
            f"Add more markers from non-dominant voices; reduce {voice_blend['dominant_voice']} markers"
        )

    results["breakdown"]["voice_blend"] = blend_score
    results["score"] += blend_score

    # 3. Dissolution markers (30 points)
    marker_score = 0
    categories_needed = ["pattern_recognition", "we_emergence", "affirmation", "re_differentiation_seeds"]
    categories_found = dissolution_markers["categories_covered"]

    for category in categories_needed:
        if category in categories_found:
            marker_score += 7.5
        else:
            results["issues"].append(f"Missing dissolution category: {category}")
            results["recommendations"].append(f"Add {category.replace('_', ' ')} language")

    results["breakdown"]["dissolution_markers"] = marker_score
    results["score"] += marker_score

    # 4. Anti-dissolution (20 points - subtracted for violations)
    anti_score = 20
    violations = anti_dissolution["total_violations"]
    if violations > 0:
        penalty = min(violations * 5, 20)  # -5 per violation, max -20
        anti_score -= penalty
        for issue in anti_dissolution["issues"]:
            results["issues"].append(f"Anti-dissolution: {issue}")

    results["breakdown"]["anti_dissolution_avoided"] = anti_score
    results["score"] += anti_score

    # Determine status
    if results["score"] >= 70:
        results["status"] = "pass"
    elif results["score"] >= 50:
        results["status"] = "warn"
    else:
        results["status"] = "fail"

    return results


def validate_dissolution(filepath: str) -> Dict:
    """Main validation function for Phase C dissolution."""
    try:
        text = load_file(filepath)
    except FileNotFoundError:
        return {"status": "error", "message": f"File not found: {filepath}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

    word_count = count_words(text)

    # Run analyses
    pronouns = analyze_pronouns(text)
    voice_blend = analyze_voice_blend(text)
    dissolution_markers = find_dissolution_markers(text)
    anti_dissolution = find_anti_dissolution(text)
    quality = assess_dissolution_quality(
        pronouns, voice_blend, dissolution_markers, anti_dissolution, word_count
    )

    results = {
        "file": filepath,
        "movement": "three",
        "phase": "c",
        "word_count": word_count,
        "pronoun_analysis": pronouns,
        "voice_blend_analysis": voice_blend,
        "dissolution_markers": dissolution_markers,
        "anti_dissolution": anti_dissolution,
        "quality_assessment": quality,
        "status": quality["status"],
        "summary": {
            "dissolution_score": quality["score"],
            "we_emergence": pronouns["we_emergence"],
            "voices_blended": voice_blend["blend_achieved"],
            "categories_covered": len(dissolution_markers["categories_covered"]),
            "violations": anti_dissolution["total_violations"],
            "ready_for_m4": quality["status"] == "pass" and
                           "re_differentiation_seeds" in dissolution_markers["categories_covered"]
        }
    }

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Validate prose dissolution for Movement Three Phase C"
    )
    parser.add_argument("file", help="Path to markdown file to validate")
    parser.add_argument("--pretty", action="store_true", help="Pretty print JSON output")

    args = parser.parse_args()

    results = validate_dissolution(args.file)

    if args.pretty:
        print(json.dumps(results, indent=2))
    else:
        print(json.dumps(results))

    if results["status"] == "fail":
        sys.exit(1)
    elif results["status"] == "warn":
        sys.exit(0)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
