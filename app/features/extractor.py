from __future__ import annotations

from dataclasses import dataclass, asdict

from app.sequence.builder import SequenceSummary


@dataclass
class FeatureSummary:
    total_sequences: int
    mean_cycle_time_s: float
    variability_index: float

    def to_dict(self) -> dict:
        return asdict(self)


def extract_features(sequence_summary: SequenceSummary) -> FeatureSummary:
    total = max(1, sequence_summary.total_sequences)
    return FeatureSummary(
        total_sequences=total,
        mean_cycle_time_s=0.0,
        variability_index=0.0,
    )
