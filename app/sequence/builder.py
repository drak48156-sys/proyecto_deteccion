from __future__ import annotations

from dataclasses import dataclass, asdict
from statistics import mean

from app.vision.tracker import VisionSummary


@dataclass
class SequenceSummary:
    total_sequences: int
    strategy: str
    estimated_cycle_times_s: list[float]
    peak_timestamps_s: list[float]
    grouped_phase_windows_s: list[list[float]]

    def to_dict(self) -> dict:
        return asdict(self)


def _group_peaks_into_sequences(peaks: list[float]) -> list[list[float]]:
    if not peaks:
        return []

    intervals = [peaks[i] - peaks[i - 1] for i in range(1, len(peaks))]
    baseline_gap = mean(intervals) if intervals else 0.0
    group_threshold = max(6.0, baseline_gap * 1.6) if baseline_gap > 0 else 6.0

    groups: list[list[float]] = [[peaks[0]]]
    for ts in peaks[1:]:
        if ts - groups[-1][-1] <= group_threshold:
            groups[-1].append(ts)
        else:
            groups.append([ts])
    return groups


def build_sequences(vision_summary: VisionSummary) -> SequenceSummary:
    peaks = vision_summary.estimated_motion_peaks
    grouped = _group_peaks_into_sequences(peaks)

    cycle_times: list[float] = []
    for group in grouped:
        if len(group) >= 2:
            cycle_times.append(round(group[-1] - group[0], 4))

    if not cycle_times and len(peaks) >= 2:
        cycle_times = [round(peaks[i] - peaks[i - 1], 4) for i in range(1, len(peaks))]

    total_sequences = len(cycle_times) if cycle_times else max(1, len(grouped))
    return SequenceSummary(
        total_sequences=total_sequences,
        strategy="motion-peak-grouping",
        estimated_cycle_times_s=cycle_times,
        peak_timestamps_s=peaks,
        grouped_phase_windows_s=[[round(x, 4) for x in group] for group in grouped],
    )
