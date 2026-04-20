from __future__ import annotations

from dataclasses import dataclass, asdict
from statistics import mean, pstdev

from app.sequence.builder import SequenceSummary


@dataclass
class FeatureSummary:
    total_sequences: int
    mean_cycle_time_s: float
    variability_index: float
    min_cycle_time_s: float
    max_cycle_time_s: float

    def to_dict(self) -> dict:
        return asdict(self)


def extract_features(sequence_summary: SequenceSummary) -> FeatureSummary:
    cycles = sequence_summary.estimated_cycle_times_s
    total = max(1, sequence_summary.total_sequences)

    if not cycles:
        return FeatureSummary(
            total_sequences=total,
            mean_cycle_time_s=0.0,
            variability_index=0.0,
            min_cycle_time_s=0.0,
            max_cycle_time_s=0.0,
        )

    avg = float(mean(cycles))
    std = float(pstdev(cycles)) if len(cycles) > 1 else 0.0
    variability_index = (std / avg) if avg > 0 else 0.0

    return FeatureSummary(
        total_sequences=total,
        mean_cycle_time_s=round(avg, 4),
        variability_index=round(variability_index, 4),
        min_cycle_time_s=round(min(cycles), 4),
        max_cycle_time_s=round(max(cycles), 4),
    )
