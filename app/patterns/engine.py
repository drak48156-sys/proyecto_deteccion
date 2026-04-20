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


def evaluate_patterns(feature_summary: FeatureSummary) -> PatternSummary:
    return PatternSummary(
        consistency_score=0.0,
        anomaly_score=0.0,
        drift_score=0.0,
    )
