from __future__ import annotations

import argparse

from app.features.extractor import extract_features
from app.ingest.loader import load_session
from app.patterns.engine import evaluate_patterns
from app.scoring.reporter import write_outputs
from app.sequence.builder import build_sequences
from app.vision.tracker import run_tracking


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="PatternSight MVP pipeline")
    parser.add_argument("video", help="Ruta del video a procesar")
    parser.add_argument("--imu", help="Ruta opcional del archivo IMU", default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    session = load_session(args.video, args.imu)
    vision_summary = run_tracking(session.video_path)
    sequence_summary = build_sequences(vision_summary)
    feature_summary = extract_features(sequence_summary)
    pattern_summary = evaluate_patterns(feature_summary)
    write_outputs(feature_summary, pattern_summary)
    print("PatternSight MVP ejecutado. Revisa outputs/report.json y outputs/summary.md")


if __name__ == "__main__":
    main()
