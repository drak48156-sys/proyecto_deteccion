from __future__ import annotations

from dataclasses import dataclass, asdict

from app.features.extractor import FeatureSummary


@dataclass
class PatternSummary:
    consistency_score: float
    anomaly_score: float
    drift_score: float

    def to_dict(self) -> dict:
        return asdict(self)


def _clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def evaluate_patterns(feature_summary: FeatureSummary) -> PatternSummary:
    consistency = 100.0 - (feature_summary.variability_index * 100.0)
    anomaly = feature_summary.variability_index * 100.0
    drift = ((feature_summary.max_cycle_time_s - feature_summary.min_cycle_time_s) / feature_summary.mean_cycle_time_s * 100.0) if feature_summary.mean_cycle_time_s > 0 else 0.0

    return PatternSummary(
        consistency_score=round(_clamp(consistency), 2),
        anomaly_score=round(_clamp(anomaly), 2),
        drift_score=round(_clamp(drift), 2),
    )
