from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class SessionInput:
    video_path: Path
    imu_path: Optional[Path] = None


def load_session(video_path: str, imu_path: str | None = None) -> SessionInput:
    video = Path(video_path)
    if not video.exists():
        raise FileNotFoundError(f"Video no encontrado: {video}")

    imu = Path(imu_path) if imu_path else None
    if imu_path and imu and not imu.exists():
        raise FileNotFoundError(f"IMU no encontrado: {imu}")

    return SessionInput(video_path=video, imu_path=imu)
