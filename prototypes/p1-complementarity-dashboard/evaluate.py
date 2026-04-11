"""
P1 Evaluation: Run rule-based classifier against 100 benchmark tasks.
Measures accuracy, per-type precision/recall, and per-phase performance.

Usage:
    python evaluate.py
"""

import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

# Inline the classifier to avoid streamlit dependency
TASK_TYPES = {
    "execution": {"label": "Execution (clear input → output)", "allocation": "AI-led, human-reviewed"},
    "creation": {"label": "Creation (aesthetic / creative judgment)", "allocation": "Human+AI collaboration"},
    "decision_data_rich": {"label": "Decision — data-rich", "allocation": "AI recommends, human decides"},
    "decision_uncertain": {"label": "Decision — uncertain / strategic", "allocation": "Human-led, AI-informed"},
    "ethical_political": {"label": "Ethical / political", "allocation": "Human only"},
}

PHASE_DEFAULTS = {
    "Discovery": "decision_uncertain", "Design": "creation", "Development": "execution",
    "Testing": "execution", "Launch": "decision_uncertain", "Growth": "decision_data_rich",
}

KEYWORDS = {
    "execution": [
        "implement", "code", "build", "write tests", "deploy", "migrate",
        "refactor", "fix bug", "create endpoint", "set up", "configure",
        "automate", "script", "documentation", "generate report",
    ],
    "creation": [
        "design", "prototype", "wireframe", "brand", "visual", "layout",
        "illustration", "copy", "content", "creative", "look and feel",
        "color", "typography", "logo", "motion", "animation", "ideate",
    ],
    "decision_data_rich": [
        "analyze", "a/b test", "metrics", "dashboard", "segment",
        "funnel", "conversion", "retention", "cohort", "experiment",
        "personalize", "recommend", "prioritize backlog", "rank features",
    ],
    "decision_uncertain": [
        "strategy", "roadmap", "go/no-go", "pivot", "launch timing",
        "market entry", "positioning", "pricing", "vision", "bet",
        "investment", "kill", "sunset", "partner", "acquire",
    ],
    "ethical_political": [
        "ethics", "bias", "fairness", "privacy", "compliance",
        "regulation", "stakeholder", "legal", "trust", "safety",
        "governance", "responsible", "transparency", "consent",
    ],
}


def classify_task_rule_based(description):
    desc_lower = description.lower()
    scores = {}
    for task_type, keywords in KEYWORDS.items():
        scores[task_type] = sum(1 for kw in keywords if kw in desc_lower)
    best = max(scores, key=scores.get)
    confidence = scores[best] / max(sum(scores.values()), 1)
    if scores[best] == 0:
        return {"type": "unknown", "confidence": 0.0}
    return {"type": best, "confidence": round(min(confidence, 1.0), 2)}


def load_benchmark(path="benchmark_tasks.csv"):
    tasks = []
    with open(Path(__file__).parent / path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            tasks.append(row)
    return tasks


def evaluate():
    tasks = load_benchmark()
    total = len(tasks)
    correct = 0
    type_stats = defaultdict(lambda: {"tp": 0, "fp": 0, "fn": 0})
    phase_stats = defaultdict(lambda: {"correct": 0, "total": 0})
    errors = []

    for task in tasks:
        desc = task["description"]
        phase = task["phase"]
        expected_type = task["expected_type"]

        result = classify_task_rule_based(desc)
        predicted_type = result["type"]

        # Handle "unknown" — fall back to phase default
        if predicted_type == "unknown":
            predicted_type = PHASE_DEFAULTS.get(phase, "decision_uncertain")

        phase_stats[phase]["total"] += 1

        if predicted_type == expected_type:
            correct += 1
            type_stats[expected_type]["tp"] += 1
            phase_stats[phase]["correct"] += 1
        else:
            type_stats[expected_type]["fn"] += 1
            type_stats[predicted_type]["fp"] += 1
            errors.append({
                "description": desc[:80],
                "phase": phase,
                "expected": expected_type,
                "predicted": predicted_type,
                "confidence": result.get("confidence", 0),
            })

    # Overall accuracy
    accuracy = correct / total

    # Per-type precision and recall
    type_metrics = {}
    for t in TASK_TYPES:
        tp = type_stats[t]["tp"]
        fp = type_stats[t]["fp"]
        fn = type_stats[t]["fn"]
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
        type_metrics[t] = {"precision": precision, "recall": recall, "f1": f1, "tp": tp, "fp": fp, "fn": fn}

    # Per-phase accuracy
    phase_metrics = {}
    for phase, stats in sorted(phase_stats.items()):
        phase_metrics[phase] = {
            "accuracy": stats["correct"] / stats["total"] if stats["total"] > 0 else 0,
            "correct": stats["correct"],
            "total": stats["total"],
        }

    # Print report
    print("=" * 70)
    print("P1 EVALUATION REPORT: Rule-Based Classifier vs 100 Benchmark Tasks")
    print("=" * 70)

    print(f"\n## Overall Accuracy: {accuracy:.1%} ({correct}/{total})")

    print(f"\n## Per-Type Metrics")
    print(f"{'Type':<25} {'Prec':>6} {'Recall':>6} {'F1':>6} {'TP':>4} {'FP':>4} {'FN':>4}")
    print("-" * 55)
    for t, m in sorted(type_metrics.items()):
        label = t[:24]
        print(f"{label:<25} {m['precision']:>5.1%} {m['recall']:>5.1%} {m['f1']:>5.1%} {m['tp']:>4} {m['fp']:>4} {m['fn']:>4}")

    print(f"\n## Per-Phase Accuracy")
    print(f"{'Phase':<15} {'Accuracy':>8} {'Correct':>8} {'Total':>6}")
    print("-" * 40)
    for phase, m in phase_metrics.items():
        print(f"{phase:<15} {m['accuracy']:>7.1%} {m['correct']:>8} {m['total']:>6}")

    if errors:
        print(f"\n## Misclassifications ({len(errors)} errors)")
        print(f"{'Description':<50} {'Phase':<12} {'Expected':<22} {'Predicted':<22}")
        print("-" * 106)
        for e in errors[:20]:
            print(f"{e['description']:<50} {e['phase']:<12} {e['expected']:<22} {e['predicted']:<22}")
        if len(errors) > 20:
            print(f"... and {len(errors) - 20} more errors")

    # Save report
    report = {
        "overall_accuracy": round(accuracy, 4),
        "correct": correct,
        "total": total,
        "type_metrics": {t: {k: round(v, 4) if isinstance(v, float) else v for k, v in m.items()} for t, m in type_metrics.items()},
        "phase_metrics": {p: {k: round(v, 4) if isinstance(v, float) else v for k, v in m.items()} for p, m in phase_metrics.items()},
        "error_count": len(errors),
        "errors": errors,
    }

    report_path = Path(__file__).parent / "evaluation_report.json"
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2)
    print(f"\nFull report saved to: {report_path}")

    return report


if __name__ == "__main__":
    evaluate()
