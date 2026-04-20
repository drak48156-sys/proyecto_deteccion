from __future__ import annotations

import json
from pathlib import Path

from app.features.extractor import FeatureSummary
from app.patterns.engine import PatternSummary
from app.sequence.builder import SequenceSummary
from app.vision.tracker import VisionSummary


OUTPUT_DIR = Path("outputs")


def write_outputs(
    vision_summary: VisionSummary,
    sequence_summary: SequenceSummary,
    feature_summary: FeatureSummary,
    pattern_summary: PatternSummary,
) -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)

    report = {
        "vision": vision_summary.to_dict(),
        "sequences": sequence_summary.to_dict(),
        "features": feature_summary.to_dict(),
        "patterns": pattern_summary.to_dict(),
    }

    (OUTPUT_DIR / "report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    (OUTPUT_DIR / "summary.md").write_text(
        "# PatternSight MVP Summary\n\n"
        f"## Video\n"
        f"- Source: {vision_summary.source}\n"
        f"- FPS: {vision_summary.metadata.fps}\n"
        f"- Resolution: {vision_summary.metadata.width}x{vision_summary.metadata.height}\n"
        f"- Duration (s): {vision_summary.metadata.duration_s}\n"
        f"- Sampled frames: {vision_summary.sampled_frames}\n"
        f"- Motion peaks: {len(vision_summary.estimated_motion_peaks)}\n\n"
        f"## Sequences\n"
        f"- Strategy: {sequence_summary.strategy}\n"
        f"- Total sequences: {feature_summary.total_sequences}\n"
        f"- Mean cycle time (s): {feature_summary.mean_cycle_time_s}\n"
        f"- Variability index: {feature_summary.variability_index}\n"
        f"- Min cycle time (s): {feature_summary.min_cycle_time_s}\n"
        f"- Max cycle time (s): {feature_summary.max_cycle_time_s}\n\n"
        f"## Pattern scores\n"
        f"- Consistency score: {pattern_summary.consistency_score}\n"
        f"- Anomaly score: {pattern_summary.anomaly_score}\n"
        f"- Drift score: {pattern_summary.drift_score}\n",
        encoding="utf-8",
    )
