from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass
class VisionSummary:
    source: Path
    detector: str = "placeholder"
    tracks_detected: int = 0


def run_tracking(video_path: Path) -> VisionSummary:
    return VisionSummary(source=video_path)
