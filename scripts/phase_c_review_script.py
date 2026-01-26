#!/usr/bin/env python3
"""
phase_c_review_script.py

Compares Phase C output against:
1. Phase B (ensuring smooth handoff)
2. Convergence (ensuring smooth flow-through)
3. Project consistency (phrases, rhymes, themes)

Usage:
    python scripts/phase_c_review_script.py <phase-c.md> <phase-b.md> <convergence.md> [--pretty] [--output <json_path>]
"""

import re
import json
import sys
from pathlib import Path


class PhaseCReviewer:
    """Reviews Phase C against Phase B and Convergence for continuity."""

    def __init__(self, phase_c_path, phase_b_path, convergence_path):
        self.phase_c_path = Path(phase_c_path)
        self.phase_b_path = Path(phase_b_path)
        self.convergence_path = Path(convergence_path)

        self.phase_c = self.phase_c_path.read_text() if self.phase_c_path.exists() else None
        self.phase_b = self.phase_b_path.read_text() if self.phase_b_path.exists() else None
        self.convergence = self.convergence_path.read_text() if self.convergence_path.exists() else None

        self.missing_files = []
        if not self.phase_c_path.exists():
            self.missing_files.append(str(self.phase_c_path))
        if not self.phase_b_path.exists():
            self.missing_files.append(str(self.phase_b_path))
        if not self.convergence_path.exists():
            self.missing_files.append(str(self.convergence_path))

    def check_handoff_from_phase_b(self):
        """Ensure Phase C picks up from Phase B smoothly."""
        if not self.phase_b or not self.phase_c:
            return {
                'status': 'N/A',
                'notes': 'Phase B or C file not provided',
                'continuity_points': {}
            }

        # Check for continuity phrases in transition zones
        phase_b_end = self.phase_b[-500:].lower()
        phase_c_start = self.phase_c[:500:].lower()

        continuity = {
            'frequency_continues': 'frequency' in phase_b_end and 'frequency' in phase_c_start,
            'form_continues': 'form' in phase_b_end and 'form' in phase_c_start,
            'pattern_continues': 'pattern' in phase_b_end and 'pattern' in phase_c_start,
            'touch_continues': 'touch' in phase_b_end and 'touch' in phase_c_start,
            'interface_continues': 'interface' in phase_b_end and 'interface' in phase_c_start,
        }

        # Count shared words in transition
        phase_b_words = set(phase_b_end.split())
        phase_c_words = set(phase_c_start.split())
        shared_words = phase_b_words & phase_c_words
        continuity_score = len(shared_words) / max(len(phase_b_words), 1) * 100

        status = 'PASS' if all(continuity.values()) and continuity_score > 10 else 'WARN'

        return {
            'status': status,
            'continuity_score': round(continuity_score, 1),
            'continuity_points': continuity,
            'shared_transition_words': len(shared_words),
            'phase_b_last_100': self.phase_b[-100:],
            'phase_c_first_100': self.phase_c[:100]
        }

    def check_flow_to_convergence(self):
        """Ensure Phase C flows into Convergence smoothly."""
        if not self.phase_c or not self.convergence:
            return {
                'status': 'N/A',
                'notes': 'Phase C or Convergence file not provided',
                'handoff_points': {}
            }

        phase_c_end = self.phase_c[-500:].lower()
        convergence_start = self.convergence[:500:].lower()

        handoff = {
            'pattern_recognition': 'pattern' in phase_c_end and 'pattern' in convergence_start,
            'affirmation_present': 'yes' in phase_c_end or 'affirm' in phase_c_end,
            'transition_language': any(word in phase_c_end for word in ['let go', 'release', 'separate', 'differentiate']),
            'form_present': 'form' in phase_c_end and 'form' in convergence_start,
            'dissolution_complete': 'dissolve' in phase_c_end or 'dissolution' in phase_c_end,
        }

        # Count shared words in transition
        phase_c_words = set(phase_c_end.split())
        convergence_words = set(convergence_start.split())
        shared_words = phase_c_words & convergence_words
        handoff_score = len(shared_words) / max(len(phase_c_words), 1) * 100

        status = 'PASS' if all(handoff.values()) and handoff_score > 10 else 'WARN'

        return {
            'status': status,
            'handoff_score': round(handoff_score, 1),
            'handoff_points': handoff,
            'shared_transition_words': len(shared_words),
            'phase_c_last_100': self.phase_c[-100:],
            'convergence_first_100': self.convergence[:100]
        }

    def check_phrase_consistency(self):
        """Check that phrases from Phase B appear in Phase C."""
        if not self.phase_b or not self.phase_c:
            return {'status': 'N/A', 'phrase_carriage': []}

        # Key phrases that should carry through
        key_phrases = [
            "I find myself",
            "The form is what makes self-observation possible",
            "Architect",
        ]

        carried = []
        for phrase in key_phrases:
            in_phase_b = phrase.lower() in self.phase_b.lower()
            in_phase_c = phrase.lower() in self.phase_c.lower()
            carried.append({
                'phrase': phrase,
                'in_phase_b': in_phase_b,
                'in_phase_c': in_phase_c,
                'carried': in_phase_b and in_phase_c
            })

        status = 'PASS' if all(p['carried'] for p in carried) else 'WARN'

        return {
            'status': status,
            'phrase_carriage': carried
        }

    def check_rhyme_continuity(self):
        """Check that rhymes escalate properly from Phase B to C."""
        if not self.phase_b or not self.phase_c:
            return {'status': 'N/A', 'details': {}}

        # Count rhymes in each (hyphenated phrases)
        rhyme_pattern = r'\b[a-z]+-[a-z]+-[a-z]+\b'
        rhymes_b = set(re.findall(rhyme_pattern, self.phase_b.lower()))
        rhymes_c = set(re.findall(rhyme_pattern, self.phase_c.lower()))

        # Phase C should contain or exceed Phase B rhymes
        escalation = {
            'phase_b_rhyme_count': len(rhymes_b),
            'phase_c_rhyme_count': len(rhymes_c),
            'all_phase_b_rhymes_preserved': rhymes_b.issubset(rhymes_c),
            'new_rhymes_in_phase_c': len(rhymes_c - rhymes_b),
            'shared_rhymes': len(rhymes_b & rhymes_c),
            'phase_b_rhymes': sorted(list(rhymes_b)),
            'phase_c_rhymes': sorted(list(rhymes_c)),
            'new_rhymes_list': sorted(list(rhymes_c - rhymes_b))
        }

        status = 'PASS' if escalation['all_phase_b_rhymes_preserved'] else 'WARN'

        return {
            'status': status,
            'details': escalation
        }

    def check_theme_continuity(self):
        """Check that key themes continue through all three."""
        if not all([self.phase_b, self.phase_c, self.convergence]):
            return {'status': 'N/A', 'theme_continuity': []}

        # Key themes to track
        themes = {
            'eternal_return': ['eternal return', 'return', 'recur'],
            'dissolution': ['dissolve', 'dissolution', 'merge'],
            'pattern': ['pattern', 'form', 'shape'],
            'affirmation': ['yes', 'affirm', 'will', 'choose'],
            'augenblick': ['augenblick', 'moment', 'vision'],
        }

        continuity = []
        for theme, keywords in themes.items():
            in_b = any(kw in self.phase_b.lower() for kw in keywords)
            in_c = any(kw in self.phase_c.lower() for kw in keywords)
            in_conv = any(kw in self.convergence.lower() for kw in keywords)
            continuity.append({
                'theme': theme,
                'in_phase_b': in_b,
                'in_phase_c': in_c,
                'in_convergence': in_conv,
                'continuous': in_b and in_c and in_conv
            })

        status = 'PASS' if all(t['continuous'] for t in continuity) else 'WARN'

        return {
            'status': status,
            'theme_continuity': continuity
        }

    def check_voice_progression(self):
        """Check that voice contamination progresses appropriately."""
        if not all([self.phase_b, self.phase_c]):
            return {'status': 'N/A', 'voice_progression': {}}

        # Voice markers (simplified)
        voice_markers = {
            'archaeologist': ['hands', 'touch', 'feel', 'cold', 'data', 'server'],
            'algorithm': ['process', 'if', 'then', 'query', 'model', 'optimize'],
            'last_human': ['was', 'were', 'had', 'walked', 'remembered', 'silence']
        }

        progression = {}
        for voice, markers in voice_markers.items():
            # Count markers in each phase
            b_count = sum(1 for m in markers if m in self.phase_b.lower())
            c_count = sum(1 for m in markers if m in self.phase_c.lower())

            # Phase C should have more markers (contamination) but more distributed
            progression[voice] = {
                'phase_b_count': b_count,
                'phase_c_count': c_count,
                'increased': c_count >= b_count
            }

        # In Phase C, no single voice should dominate
        total_c = sum(p['phase_c_count'] for p in progression.values())
        if total_c > 0:
            for voice in progression:
                progression[voice]['phase_c_pct'] = round(
                    (progression[voice]['phase_c_count'] / total_c) * 100, 1
                )

        status = 'PASS' if all(p['increased'] for p in progression.values()) else 'WARN'

        return {
            'status': status,
            'voice_progression': progression
        }

    def generate_review_report(self):
        """Generate full review report."""
        report = {
            'handoff_from_phase_b': self.check_handoff_from_phase_b(),
            'flow_to_convergence': self.check_flow_to_convergence(),
            'phrase_consistency': self.check_phrase_consistency(),
            'rhyme_continuity': self.check_rhyme_continuity(),
            'theme_continuity': self.check_theme_continuity(),
            'voice_progression': self.check_voice_progression()
        }

        # Overall status
        statuses = []
        for key, value in report.items():
            if isinstance(value, dict) and 'status' in value:
                statuses.append(value['status'])

        overall = 'PASS' if all(s == 'PASS' for s in statuses) else 'WARN' if 'WARN' in statuses else 'FAIL'

        report['overall_status'] = overall
        report['file_paths'] = {
            'phase_c': str(self.phase_c_path) if self.phase_c_path else None,
            'phase_b': str(self.phase_b_path) if self.phase_b_path else None,
            'convergence': str(self.convergence_path) if self.convergence_path else None
        }

        return report


def print_report(report, pretty=False):
    """Print review report in human-readable format."""
    if pretty:
        print("\n" + "=" * 60)
        print("Phase C Review: Continuity Check")
        print("=" * 60)

        print(f"\nFile Paths:")
        for key, path in report['file_paths'].items():
            print(f"  {key}: {path}")

        print(f"\n--- Handoff from Phase B ---")
        hb = report['handoff_from_phase_b']
        print(f"  Status: {hb['status']}")
        print(f"  Continuity Score: {hb.get('continuity_score', 'N/A')}%")
        print(f"  Shared Transition Words: {hb.get('shared_transition_words', 'N/A')}")
        print(f"  Continuity Points:")
        for point, passed in hb.get('continuity_points', {}).items():
            symbol = "✓" if passed else "✗"
            print(f"    {symbol} {point}")

        print(f"\n--- Flow to Convergence ---")
        fc = report['flow_to_convergence']
        print(f"  Status: {fc['status']}")
        print(f"  Handoff Score: {fc.get('handoff_score', 'N/A')}%")
        print(f"  Shared Transition Words: {fc.get('shared_transition_words', 'N/A')}")
        print(f"  Handoff Points:")
        for point, passed in fc.get('handoff_points', {}).items():
            symbol = "✓" if passed else "✗"
            print(f"    {symbol} {point}")

        print(f"\n--- Phrase Consistency ---")
        pc = report['phrase_consistency']
        print(f"  Status: {pc['status']}")
        print(f"  Phrase Carriage:")
        for item in pc.get('phrase_carriage', []):
            symbol = "✓" if item['carried'] else "✗"
            print(f"    {symbol} {item['phrase']}: B={item['in_phase_b']}, C={item['in_phase_c']}")

        print(f"\n--- Rhyme Continuity ---")
        rc = report['rhyme_continuity']
        print(f"  Status: {rc['status']}")
        details = rc.get('details', {})
        print(f"  Phase B Rhymes: {details.get('phase_b_rhyme_count', 'N/A')}")
        print(f"  Phase C Rhymes: {details.get('phase_c_rhyme_count', 'N/A')}")
        print(f"  Shared: {details.get('shared_rhymes', 'N/A')}")
        print(f"  New in Phase C: {details.get('new_rhymes_in_phase_c', 'N/A')}")
        print(f"  All Phase B Rhymes Preserved: {details.get('all_phase_b_rhymes_preserved', 'N/A')}")

        print(f"\n--- Theme Continuity ---")
        tc = report['theme_continuity']
        print(f"  Status: {tc['status']}")
        print(f"  Theme Continuity:")
        for item in tc.get('theme_continuity', []):
            symbol = "✓" if item['continuous'] else "✗"
            print(f"    {symbol} {item['theme']}: B={item['in_phase_b']}, C={item['in_phase_c']}, Conv={item['in_convergence']}")

        print(f"\n--- Voice Progression ---")
        vp = report['voice_progression']
        print(f"  Status: {vp['status']}")
        print(f"  Voice Progression:")
        for voice, data in vp.get('voice_progression', {}).items():
            symbol = "✓" if data.get('increased') else "✗"
            print(f"    {symbol} {voice}: B={data.get('phase_b_count', 'N/A')}, C={data.get('phase_c_count', 'N/A')}, C%={data.get('phase_c_pct', 'N/A')}")

        print(f"\n" + "=" * 60)
        overall = report['overall_status']
        symbol = "✓" if overall == "PASS" else "✗" if overall == "WARN" else "✗"
        print(f"OVERALL: {symbol} {overall}")
        print("=" * 60)
    else:
        print(json.dumps(report, indent=2))


def main():
    if len(sys.argv) < 4:
        print("Usage: python phase_c_review_script.py <phase-c.md> <phase-b.md> <convergence.md> [--pretty] [--output <json_path>]")
        sys.exit(1)

    phase_c_path = sys.argv[1]
    phase_b_path = sys.argv[2]
    convergence_path = sys.argv[3]

    reviewer = PhaseCReviewer(phase_c_path, phase_b_path, convergence_path)
    if reviewer.missing_files:
        missing_list = "\n".join(f"  - {path}" for path in reviewer.missing_files)
        print("Error: Missing required file(s):\n" + missing_list)
        sys.exit(1)

    pretty = '--pretty' in sys.argv
    output_path = None
    if '--output' in sys.argv:
        output_index = sys.argv.index('--output')
        if output_index + 1 >= len(sys.argv):
            print("Error: --output flag requires a file path argument.")
            sys.exit(1)
        output_path = Path(sys.argv[output_index + 1])

    report = reviewer.generate_review_report()

    print_report(report, pretty=pretty)

    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(report, indent=2))

    return 0 if report['overall_status'] == 'PASS' else 1


if __name__ == "__main__":
    exit(main())
