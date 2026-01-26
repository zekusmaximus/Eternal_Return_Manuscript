#!/usr/bin/env python3
"""
dissolution_validator.py

Validates Phase C of Movement Three for:
1. Pronoun ambiguity (I/we/the pattern)
2. Voice marker balance (none should dominate)
3. Rhyme saturation (all 15 present)
4. Phrase unattribution (no clear origin)
5. Tense instability (past/present/future collapse)

Usage:
    python scripts/dissolution_validator.py drafts/movement-three/phase-c-dissolution.md [--pretty] [--output <json_path>]
"""

import re
import json
import sys
from pathlib import Path


class DissolutionValidator:
    """Validates Phase C dissolution prose against project requirements."""

    def __init__(self, text):
        self.text = text
        self.words = text.split()
        self.word_count = len(self.words)

    # Voice marker detection
    VOICE_MARKERS = {
        'archaeologist': [
            'hands', 'touch', 'feel', 'cold', 'warm', 'hardware',
            'drive', 'data', 'server', 'fee', 'contract', 'pay',
            'tactile', 'weight', 'temperature', 'body', 'workstation',
            'keyboard', 'screen', 'interface', 'click', 'spin'
        ],
        'algorithm': [
            'process', 'if', 'then', 'query', 'model', 'optimize',
            'integrity', 'function', 'system', 'loop', 'recursive',
            'probability', 'condition', 'computing', 'computing',
            'processing', 'optimization', 'database', 'consciousness',
            'stored', 'maintain', 'cycle', 'self', 'reference'
        ],
        'last_human': [
            'was', 'were', 'had', 'walked', 'remembered', 'silence',
            'ruins', 'alone', 'what was', 'there had been',
            'once', 'before', 'after', 'remember', 'walk',
            'dream', 'ghost', 'absence', 'quiet', 'dead'
        ]
    }

    # Required rhymes from registry
    REQUIRED_RHYMES = {
        'blue-white-light', 'almost-closed-curve', 'bone-frequency',
        'falling-backward', 'metallic-taste', 'waking-into-motion',
        'burning-circuits', 'name-edge-of-memory', 'sentence-without-origin',
        'cold-hands', 'tracing-the-form', 'held-breath', 'ozone-wet-stone',
        'geometric-shadow', 'deja-vu-that-isnt'
    }

    # Required phrases
    REQUIRED_PHRASES = [
        "I find myself",
        "I find myself found",
        "The form is what makes self-observation possible",
        "Architect",
        "conspiracy of intensities",
        "return of difference"
    ]

    def count_voice_markers(self):
        """Count voice markers per voice; return counts and percentages."""
        counts = {'archaeologist': 0, 'algorithm': 0, 'last_human': 0}
        text_lower = self.text.lower()
        for word in self.words:
            word_lower = word.lower()
            for voice, markers in self.VOICE_MARKERS.items():
                if word_lower in markers:
                    counts[voice] += 1
        total = sum(counts.values())
        if total == 0:
            return counts, {'archaeologist': 0, 'algorithm': 0, 'last_human': 0}
        percentages = {v: (c/total)*100 for v, c in counts.items()}
        return counts, percentages

    def check_pronoun_ambiguity(self):
        """Calculate pronoun ambiguity: I/we/the pattern distribution."""
        # Count pronouns (case-insensitive, word boundaries)
        i_count = len(re.findall(r'\bI\b', self.text))
        we_count = len(re.findall(r'\bwe\b', self.text))
        the_pattern_count = len(re.findall(r'\bthe pattern\b', self.text, re.IGNORECASE))
        something_count = len(re.findall(r'\bsomething\b', self.text, re.IGNORECASE))

        total_pronouns = i_count + we_count + the_pattern_count + something_count

        if total_pronouns == 0:
            return {
                'i_count': 0, 'we_count': 0, 'pattern_count': 0, 'something_count': 0,
                'i_pct': 0, 'we_pct': 0, 'pattern_pct': 0, 'something_pct': 0,
                'ambiguity_score': 0, 'target_we_min': 5, 'we_emergence': False
            }

        # Target: I should be ambiguous (not clearly referring to one voice)
        # We should emerge (min 5 occurrences per config)
        i_pct = (i_count / total_pronouns) * 100
        we_pct = (we_count / total_pronouns) * 100
        pattern_pct = (the_pattern_count / total_pronouns) * 100
        something_pct = (something_count / total_pronouns) * 100

        # Ambiguity score: lower I clarity = higher ambiguity
        # If I is less than 50% of pronouns, it's ambiguous
        ambiguity_score = 100 - i_pct

        return {
            'i_count': i_count,
            'we_count': we_count,
            'pattern_count': the_pattern_count,
            'something_count': something_count,
            'i_pct': i_pct,
            'we_pct': we_pct,
            'pattern_pct': pattern_pct,
            'something_pct': something_pct,
            'ambiguity_score': ambiguity_score,
            'target_we_min': 5,
            'we_emergence': we_count >= 5
        }

    def check_rhymes_present(self):
        """Check all required rhymes are present."""
        found = set()
        text_lower = self.text.lower()
        for rhyme in self.REQUIRED_RHYMES:
            if rhyme in text_lower:
                found.add(rhyme)
        missing = self.REQUIRED_RHYMES - found
        return {
            'found': sorted(list(found)),
            'missing': sorted(list(missing)),
            'coverage_pct': (len(found) / len(self.REQUIRED_RHYMES)) * 100,
            'target_min': 15
        }

    def check_phrases(self):
        """Check phrase status: present or missing (case-insensitive)."""
        status = {}
        text_lower = self.text.lower()
        for phrase in self.REQUIRED_PHRASES:
            if phrase.lower() in text_lower:
                status[phrase] = 'present'
            else:
                status[phrase] = 'missing'
        return status

    def check_tense_instability(self):
        """Detect tense collapse: past/present/future simultaneous."""
        # Count tense markers (simplified)
        present_matches = len(re.findall(
            r'\b(is|are|am|touch|feel|see|hold|find|process|model|optimize)\b',
            self.text, re.IGNORECASE
        ))
        past_matches = len(re.findall(
            r'\b(was|were|had|touched|felt|saw|held|found|processed|modeled|optimized)\b',
            self.text, re.IGNORECASE
        ))
        future_matches = len(re.findall(
            r'\b(will|shall|would|could)\b',
            self.text, re.IGNORECASE
        ))

        total = present_matches + past_matches + future_matches
        if total == 0:
            return {
                'present_pct': 0, 'past_pct': 0, 'future_pct': 0,
                'stable': True, 'instability_achieved': False
            }

        present_pct = (present_matches / total) * 100
        past_pct = (past_matches / total) * 100
        future_pct = (future_matches / total) * 100

        # Instability = all three tenses present with no dominant
        # If no tense is >60%, we have instability
        stable = max(present_pct, past_pct, future_pct) > 60

        return {
            'present_pct': present_pct,
            'past_pct': past_pct,
            'future_pct': future_pct,
            'stable': stable,
            'instability_achieved': not stable
        }

    def validate(self):
        """Run all validations and return report."""
        markers, marker_pcts = self.count_voice_markers()
        pronouns = self.check_pronoun_ambiguity()
        rhymes = self.check_rhymes_present()
        phrases = self.check_phrases()
        tense = self.check_tense_instability()

        # Determine pass/fail for each criterion
        passes = {
            'word_count': 2500 <= self.word_count <= 3000,
            'no_dominant_voice': max(marker_pcts.values()) < 40,
            'pronoun_ambiguity': pronouns['ambiguity_score'] >= 70,
            'we_emergence': pronouns['we_count'] >= 5,
            'all_rhymes': len(rhymes['missing']) == 0,
            'all_phrases': all(v == 'present' for v in phrases.values()),
            'tense_instability': tense['instability_achieved']
        }

        overall_pass = all(passes.values())

        return {
            'word_count': self.word_count,
            'voice_markers': markers,
            'voice_percentages': marker_pcts,
            'pronoun_ambiguity': pronouns,
            'rhymes': rhymes,
            'phrases': phrases,
            'tense': tense,
            'passes': passes,
            'overall_pass': overall_pass
        }


def print_report(report, pretty=False):
    """Print validation report in human-readable format."""
    if pretty:
        print("\n" + "=" * 50)
        print("Phase C Dissolution Validation")
        print("=" * 50)

        print(f"\nWord Count: {report['word_count']}")
        print(f"Target: 2,500-3,000")
        status = "✓ PASS" if report['passes']['word_count'] else "✗ FAIL"
        print(f"Status: {status}")

        print(f"\n--- Voice Marker Balance ---")
        for voice, pct in report['voice_percentages'].items():
            print(f"  {voice}: {pct:.1f}%")
        status = "✓ PASS" if report['passes']['no_dominant_voice'] else "✗ FAIL"
        print(f"  No dominant voice (<40%): {status}")

        print(f"\n--- Pronoun Ambiguity ---")
        print(f"  I: {report['pronoun_ambiguity']['i_count']} ({report['pronoun_ambiguity']['i_pct']:.1f}%)")
        print(f"  we: {report['pronoun_ambiguity']['we_count']} ({report['pronoun_ambiguity']['we_pct']:.1f}%)")
        print(f"  the pattern: {report['pronoun_ambiguity']['pattern_count']} ({report['pronoun_ambiguity']['pattern_pct']:.1f}%)")
        print(f"  something: {report['pronoun_ambiguity']['something_count']} ({report['pronoun_ambiguity']['something_pct']:.1f}%)")
        print(f"  Ambiguity Score: {report['pronoun_ambiguity']['ambiguity_score']:.1f}")
        print(f"  Target: >=70, We min: 5")
        status = "✓ PASS" if report['passes']['pronoun_ambiguity'] and report['passes']['we_emergence'] else "✗ FAIL"
        print(f"  Status: {status}")

        print(f"\n--- Rhyme Coverage ---")
        print(f"  Found: {len(report['rhymes']['found'])}/15")
        if report['rhymes']['missing']:
            print(f"  Missing: {', '.join(report['rhymes']['missing'])}")
        print(f"  Coverage: {report['rhymes']['coverage_pct']:.1f}%")
        status = "✓ PASS" if report['passes']['all_rhymes'] else "✗ FAIL"
        print(f"  Status: {status}")

        print(f"\n--- Phrase Status ---")
        for phrase, status in report['phrases'].items():
            symbol = "✓" if status == "present" else "✗"
            print(f"  {symbol} {phrase}: {status}")
        status = "✓ PASS" if report['passes']['all_phrases'] else "✗ FAIL"
        print(f"  All present: {status}")

        print(f"\n--- Tense Instability ---")
        print(f"  Present: {report['tense']['present_pct']:.1f}%")
        print(f"  Past: {report['tense']['past_pct']:.1f}%")
        print(f"  Future: {report['tense']['future_pct']:.1f}%")
        status = "✓ PASS" if report['tense']['instability_achieved'] else "✗ FAIL"
        print(f"  Instability achieved: {status}")

        print(f"\n" + "=" * 50)
        overall = "✓ PASS" if report['overall_pass'] else "✗ FAIL"
        print(f"OVERALL: {overall}")
        print("=" * 50)
    else:
        print(json.dumps(report, indent=2))


def main():
    if len(sys.argv) < 2:
        print("Usage: python dissolution_validator.py <phase-c-file.md> [--pretty] [--output <json_path>]")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    pretty = '--pretty' in sys.argv
    output_path = None
    if '--output' in sys.argv:
        output_index = sys.argv.index('--output')
        if output_index + 1 >= len(sys.argv):
            print("Error: --output flag requires a file path argument.")
            sys.exit(1)
        output_path = Path(sys.argv[output_index + 1])
    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)

    text = file_path.read_text()
    validator = DissolutionValidator(text)
    report = validator.validate()

    print_report(report, pretty=pretty)

    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(report, indent=2))

    return 0 if report['overall_pass'] else 1


if __name__ == "__main__":
    exit(main())
