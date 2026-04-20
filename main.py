from __future__ import annotations

import argparse

from app.pipeline import run_pipeline


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="PatternSight MVP pipeline")
    parser.add_argument("video", help="Ruta del video a procesar")
    parser.add_argument("--imu", help="Ruta opcional del archivo IMU", default=None)
    parser.add_argument(
        "--sample-stride",
        type=int,
        default=15,
        help="Tomar un frame cada N frames para estimar señal de movimiento",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    run_pipeline(args.video, args.imu, sample_stride=args.sample_stride)
    print("PatternSight MVP ejecutado. Revisa outputs/report.json y outputs/summary.md")


if __name__ == "__main__":
    main()
