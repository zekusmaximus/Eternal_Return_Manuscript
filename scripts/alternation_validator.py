#!/usr/bin/env python3
"""
Alternation Validator Script — Movement Three Phase B
Validates the paragraph→sentence→clause alternation pattern for simultaneous narration.

Phase B requires:
- Opening zone: Alternating paragraphs (~3-4 sentences each)
- Middle zone: Alternating sentences
- End zone: Fragmenting sentences with clause-level shifts

Usage:
    python alternation_validator.py <file>
    python alternation_validator.py <file> --pretty

Output: JSON report with alternation analysis and handoff quality assessment.
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
    return {"movement": "three", "phase": "b"}

CONFIG = load_config()

# Voice signature patterns (for detecting which voice is speaking)
VOICE_SIGNATURES = {
    "archaeologist": {
        "strong": [
            r'\bI\s+(?:find|touch|grab|hold)\b',
            r'\b(?:interface|terminal|server|workstation)\b',
            r'\b(?:cold|weight|pressure)\s+(?:of|in|on)\b',
            r'\b(?:Lena|Marcus)\b',
        ],
        "moderate": [
            r'\b(?:feel|sense|notice)\s+(?:the|my|a)\b',
            r'\b(?:hands?|fingers?)\s+(?:on|touch|move)\b',
        ]
    },
    "algorithm": {
        "strong": [
            r'\b(?:process|calculate|analyze|model|query)\b',
            r'\bif\s+.*then\b',
            r'\b(?:consciousness|awareness)\s+(?:as|of|that)\b',
            r'\b(?:probability|likelihood|variance|optimize)\b',
        ],
        "moderate": [
            r'\b(?:would|could|might|perhaps)\b',
            r'\b(?:recursive|iterate)\b',
        ]
    },
    "last_human": {
        "strong": [
            r'\b(?:ruins?|decay|crumble|hollow)\b',
            r'\b(?:was|were|had been|once)\s+(?:a|the)\b',
            r'\b(?:silence|emptiness|alone)\b',
            r'\b(?:walk|journey|path)\s+(?:through|toward)\b',
        ],
        "moderate": [
            r'\b(?:last|final|only)\b',
            r'(?:^|\.\s+)[A-Z][a-z]{2,8}\.',  # Short fragment sentences
        ]
    }
}

# Rhyme patterns (for cross-voice rhyme detection)
RHYME_PATTERNS = {
    "blue-white-light": r'\bblue[-\s]?white\b',
    "bone-frequency": r'\b(?:frequency|resonance)\s+(?:in|through)?\s*(?:my|his|the)?\s*bones?\b',
    "cold-hands": r'\b(?:cold|freezing)\s+(?:hands?|fingers?)\b',
    "almost-closed-curve": r'\b(?:almost[-\s]?closed|curve\s+(?:that\s+)?approach)\b',
    "falling-backward": r'\bfalling\s+backward\b',
    "metallic-taste": r'\b(?:metallic|copper|metal)\s+taste\b',
}


def load_file(filepath: str) -> str:
    """Load and return file contents."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def count_words(text: str) -> int:
    """Count words in text."""
    return len(text.split())


def split_into_paragraphs(text: str) -> List[str]:
    """Split text into paragraphs."""
    paragraphs = re.split(r'\n\s*\n', text)
    return [p.strip() for p in paragraphs if p.strip()]


def split_into_sentences(text: str) -> List[str]:
    """Split text into sentences."""
    # Handle common abbreviations and edge cases
    text = re.sub(r'(\w)\.(\w)', r'\1. \2', text)  # Add space after periods
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in sentences if s.strip()]


def detect_voice(text: str) -> Dict:
    """Detect which voice(s) are present in a text segment."""
    results = {"primary": None, "scores": {}, "markers": {}}

    for voice, patterns in VOICE_SIGNATURES.items():
        score = 0
        markers = []

        for pattern in patterns.get("strong", []):
            matches = re.findall(pattern, text, re.IGNORECASE)
            score += len(matches) * 2
            markers.extend(matches[:2])

        for pattern in patterns.get("moderate", []):
            matches = re.findall(pattern, text, re.IGNORECASE)
            score += len(matches)

        results["scores"][voice] = score
        results["markers"][voice] = markers[:3]

    # Determine primary voice
    if results["scores"]:
        max_score = max(results["scores"].values())
        if max_score > 0:
            for voice, score in results["scores"].items():
                if score == max_score:
                    results["primary"] = voice
                    break

    # Check for multi-voice (contamination/blend)
    significant_voices = [v for v, s in results["scores"].items() if s >= max_score * 0.5 and s > 0]
    results["is_blended"] = len(significant_voices) > 1
    results["voices_present"] = significant_voices

    return results


def analyze_zone(paragraphs: List[str], zone_name: str, expected_type: str) -> Dict:
    """Analyze a zone for alternation patterns."""
    results = {
        "zone": zone_name,
        "expected_type": expected_type,
        "paragraph_count": len(paragraphs),
        "voice_sequence": [],
        "alternation_quality": 0,
        "issues": [],
        "handoff_quality": []
    }

    if not paragraphs:
        return results

    previous_voice = None
    for i, para in enumerate(paragraphs):
        voice_info = detect_voice(para)
        results["voice_sequence"].append({
            "index": i,
            "primary_voice": voice_info["primary"],
            "is_blended": voice_info["is_blended"],
            "word_count": count_words(para)
        })

        # Check for voice alternation
        current_voice = voice_info["primary"]
        if previous_voice and current_voice:
            if current_voice != previous_voice:
                results["handoff_quality"].append({
                    "from": previous_voice,
                    "to": current_voice,
                    "position": i,
                    "quality": "good"
                })
            else:
                results["handoff_quality"].append({
                    "from": previous_voice,
                    "to": current_voice,
                    "position": i,
                    "quality": "same_voice"
                })
                results["issues"].append(f"Paragraph {i}: Same voice as previous ({current_voice})")

        previous_voice = current_voice

    # Calculate alternation quality
    if len(results["handoff_quality"]) > 0:
        good_handoffs = sum(1 for h in results["handoff_quality"] if h["quality"] == "good")
        results["alternation_quality"] = round(good_handoffs / len(results["handoff_quality"]), 2)

    return results


def analyze_sentence_alternation(text: str) -> Dict:
    """Analyze sentence-level alternation."""
    sentences = split_into_sentences(text)
    results = {
        "sentence_count": len(sentences),
        "voice_sequence": [],
        "alternation_rate": 0,
        "handoffs": [],
        "cross_voice_rhymes": []
    }

    previous_voice = None
    alternation_count = 0

    for i, sentence in enumerate(sentences):
        voice_info = detect_voice(sentence)
        results["voice_sequence"].append({
            "index": i,
            "primary_voice": voice_info["primary"],
            "is_blended": voice_info["is_blended"],
            "text_preview": sentence[:50] + "..." if len(sentence) > 50 else sentence
        })

        current_voice = voice_info["primary"]
        if previous_voice and current_voice and current_voice != previous_voice:
            alternation_count += 1
            results["handoffs"].append({
                "position": i,
                "from": previous_voice,
                "to": current_voice
            })

        previous_voice = current_voice

    # Check for rhymes that span voice transitions
    for i, handoff in enumerate(results["handoffs"]):
        if handoff["position"] < len(sentences) - 1:
            combined = sentences[handoff["position"] - 1] + " " + sentences[handoff["position"]]
            for rhyme_id, pattern in RHYME_PATTERNS.items():
                if re.search(pattern, combined, re.IGNORECASE):
                    results["cross_voice_rhymes"].append({
                        "rhyme": rhyme_id,
                        "at_handoff": handoff["position"]
                    })

    if len(sentences) > 1:
        results["alternation_rate"] = round(alternation_count / (len(sentences) - 1), 2)

    return results


def analyze_fragment_zone(text: str) -> Dict:
    """Analyze clause-level fragmentation."""
    results = {
        "has_em_dashes": False,
        "em_dash_count": 0,
        "fragment_count": 0,
        "voice_blur_detected": False,
        "issues": []
    }

    # Count em-dashes (common clause-break marker)
    em_dashes = len(re.findall(r'—', text))
    results["em_dash_count"] = em_dashes
    results["has_em_dashes"] = em_dashes >= 3

    # Count short fragments (under 8 words)
    sentences = split_into_sentences(text)
    fragments = [s for s in sentences if count_words(s) <= 8]
    results["fragment_count"] = len(fragments)

    # Check for voice blur (multiple voice markers in single sentence)
    blur_count = 0
    for sentence in sentences:
        voices_in_sentence = []
        for voice, patterns in VOICE_SIGNATURES.items():
            for pattern in patterns.get("strong", []):
                if re.search(pattern, sentence, re.IGNORECASE):
                    voices_in_sentence.append(voice)
                    break
        if len(set(voices_in_sentence)) >= 2:
            blur_count += 1

    results["voice_blur_detected"] = blur_count >= 2
    results["blur_instances"] = blur_count

    return results


def validate_alternation(filepath: str) -> Dict:
    """Main validation function for Phase B alternation."""
    try:
        text = load_file(filepath)
    except FileNotFoundError:
        return {"status": "error", "message": f"File not found: {filepath}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

    word_count = count_words(text)
    paragraphs = split_into_paragraphs(text)

    # Determine zone boundaries (based on config or defaults)
    config = CONFIG.get("alternation", {}).get("phase_b", {})
    para_zone_words = config.get("paragraph_zone_words", 1800)
    sent_zone_words = config.get("sentence_zone_words", 2400)

    # Calculate cumulative word counts to find zone boundaries
    cumulative = 0
    para_zone_end = 0
    sent_zone_end = 0

    for i, para in enumerate(paragraphs):
        cumulative += count_words(para)
        if cumulative <= para_zone_words:
            para_zone_end = i + 1
        if cumulative <= para_zone_words + sent_zone_words:
            sent_zone_end = i + 1

    # Split into zones
    paragraph_zone = paragraphs[:para_zone_end]
    sentence_zone = paragraphs[para_zone_end:sent_zone_end]
    fragment_zone = paragraphs[sent_zone_end:]

    # Analyze each zone
    para_analysis = analyze_zone(paragraph_zone, "paragraph", "paragraph_alternation")
    sent_analysis = analyze_sentence_alternation("\n\n".join(sentence_zone))
    frag_analysis = analyze_fragment_zone("\n\n".join(fragment_zone))

    # Calculate overall score
    score = 0
    issues = []
    recommendations = []

    # Paragraph zone scoring (30 points)
    if para_analysis["alternation_quality"] >= 0.7:
        score += 30
    elif para_analysis["alternation_quality"] >= 0.5:
        score += 20
    else:
        score += 10
        issues.append("Low paragraph alternation quality")
        recommendations.append("Ensure paragraphs alternate between voices more consistently")

    # Sentence zone scoring (40 points)
    if sent_analysis["alternation_rate"] >= 0.5:
        score += 30
    elif sent_analysis["alternation_rate"] >= 0.3:
        score += 20
    else:
        score += 10
        issues.append("Low sentence alternation rate")
        recommendations.append("Increase sentence-level voice switching")

    if sent_analysis["cross_voice_rhymes"]:
        score += 10
    else:
        recommendations.append("Add rhymes that span voice transitions")

    # Fragment zone scoring (30 points)
    if frag_analysis["has_em_dashes"] and frag_analysis["fragment_count"] >= 5:
        score += 20
    elif frag_analysis["fragment_count"] >= 3:
        score += 15
    else:
        score += 5
        issues.append("Insufficient fragmentation in end zone")
        recommendations.append("Add more em-dash clause breaks and short fragments")

    if frag_analysis["voice_blur_detected"]:
        score += 10
    else:
        recommendations.append("Increase voice blurring with multiple voice markers per sentence")

    # Determine status
    if score >= 70:
        status = "pass"
    elif score >= 50:
        status = "warn"
    else:
        status = "fail"

    results = {
        "file": filepath,
        "movement": "three",
        "phase": "b",
        "word_count": word_count,
        "paragraph_count": len(paragraphs),
        "zones": {
            "paragraph": {
                "paragraphs": len(paragraph_zone),
                "words": sum(count_words(p) for p in paragraph_zone),
                "analysis": para_analysis
            },
            "sentence": {
                "paragraphs": len(sentence_zone),
                "words": sum(count_words(p) for p in sentence_zone),
                "analysis": sent_analysis
            },
            "fragment": {
                "paragraphs": len(fragment_zone),
                "words": sum(count_words(p) for p in fragment_zone),
                "analysis": frag_analysis
            }
        },
        "quality_assessment": {
            "score": score,
            "max_score": 100,
            "status": status,
            "issues": issues,
            "recommendations": recommendations
        },
        "status": status,
        "summary": {
            "alternation_score": score,
            "paragraph_alternation": para_analysis["alternation_quality"],
            "sentence_alternation": sent_analysis["alternation_rate"],
            "fragmentation_achieved": frag_analysis["has_em_dashes"],
            "voice_blur_achieved": frag_analysis["voice_blur_detected"],
            "cross_voice_rhymes": len(sent_analysis.get("cross_voice_rhymes", []))
        }
    }

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Validate alternation patterns for Movement Three Phase B"
    )
    parser.add_argument("file", help="Path to markdown file to validate")
    parser.add_argument("--pretty", action="store_true", help="Pretty print JSON output")

    args = parser.parse_args()

    results = validate_alternation(args.file)

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
