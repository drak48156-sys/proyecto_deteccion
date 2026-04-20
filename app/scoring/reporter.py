from __future__ import annotations

import json
from pathlib import Path

from app.features.extractor import FeatureSummary
from app.patterns.engine import PatternSummary


OUTPUT_DIR = Path("outputs")


def write_outputs(feature_summary: FeatureSummary, pattern_summary: PatternSummary) -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)

    report = {
        "features": feature_summary.to_dict(),
        "patterns": pattern_summary.to_dict(),
    }

    (OUTPUT_DIR / "report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    (OUTPUT_DIR / "summary.md").write_text(
        "# PatternSight MVP Summary\n\n"
        f"- Total sequences: {feature_summary.total_sequences}\n"
        f"- Mean cycle time (s): {feature_summary.mean_cycle_time_s}\n"
        f"- Variability index: {feature_summary.variability_index}\n"
        f"- Consistency score: {pattern_summary.consistency_score}\n"
        f"- Anomaly score: {pattern_summary.anomaly_score}\n"
        f"- Drift score: {pattern_summary.drift_score}\n",
        encoding="utf-8",
    )
