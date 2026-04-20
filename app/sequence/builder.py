from __future__ import annotations

from dataclasses import dataclass

from app.vision.tracker import VisionSummary


@dataclass
class SequenceSummary:
    total_sequences: int
    strategy: str = "placeholder-windowing"


def build_sequences(vision_summary: VisionSummary) -> SequenceSummary:
    estimated_sequences = max(1, vision_summary.tracks_detected)
    return SequenceSummary(total_sequences=estimated_sequences)
