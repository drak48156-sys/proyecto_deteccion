from __future__ import annotations

from dataclasses import asdict
from pathlib import Path

from app.features.extractor import extract_features
from app.ingest.loader import load_session
from app.patterns.engine import evaluate_patterns
from app.scoring.reporter import write_outputs
from app.sequence.builder import build_sequences
from app.vision.tracker import run_tracking


def run_pipeline(video_path: str, imu_path: str | None = None, sample_stride: int = 15) -> dict:
    session = load_session(video_path, imu_path)
    vision_summary = run_tracking(session.video_path, sample_stride=sample_stride)
    sequence_summary = build_sequences(vision_summary)
    feature_summary = extract_features(sequence_summary)
    pattern_summary = evaluate_patterns(feature_summary)
    write_outputs(vision_summary, sequence_summary, feature_summary, pattern_summary)

    return {
        "vision": vision_summary.to_dict(),
        "sequences": sequence_summary.to_dict(),
        "features": feature_summary.to_dict(),
        "patterns": pattern_summary.to_dict(),
    }
