from __future__ import annotations

from dataclasses import dataclass, asdict

from app.vision.tracker import VisionSummary


@dataclass
class SequenceSummary:
    total_sequences: int
    strategy: str
    estimated_cycle_times_s: list[float]
    peak_timestamps_s: list[float]

    def to_dict(self) -> dict:
        return asdict(self)


def build_sequences(vision_summary: VisionSummary) -> SequenceSummary:
    peaks = vision_summary.estimated_motion_peaks
    cycle_times = [round(peaks[i] - peaks[i - 1], 4) for i in range(1, len(peaks))]
    total_sequences = len(cycle_times) if cycle_times else max(1, len(peaks))
    return SequenceSummary(
        total_sequences=total_sequences,
        strategy="motion-peak-segmentation",
        estimated_cycle_times_s=cycle_times,
        peak_timestamps_s=peaks,
    )
