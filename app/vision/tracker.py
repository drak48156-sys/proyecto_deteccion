from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path

import cv2
import numpy as np


@dataclass
class VideoMetadata:
    fps: float
    frame_count: int
    width: int
    height: int
    duration_s: float

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class VisionSummary:
    source: Path
    detector: str
    tracks_detected: int
    metadata: VideoMetadata
    sampled_frames: int
    sample_stride: int
    motion_signal_mean: float
    motion_signal_std: float
    motion_signal_p95: float
    motion_signal_max: float
    motion_signal: list[float]
    timestamps_s: list[float]
    estimated_motion_peaks: list[float]

    def to_dict(self) -> dict:
        data = asdict(self)
        data["source"] = str(self.source)
        return data


def _read_metadata(capture: cv2.VideoCapture) -> VideoMetadata:
    fps = float(capture.get(cv2.CAP_PROP_FPS) or 0.0)
    frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT) or 0)
    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH) or 0)
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT) or 0)
    duration_s = (frame_count / fps) if fps > 0 else 0.0
    return VideoMetadata(
        fps=fps,
        frame_count=frame_count,
        width=width,
        height=height,
        duration_s=duration_s,
    )


def _estimate_peaks(signal: np.ndarray, timestamps: np.ndarray) -> list[float]:
    if signal.size < 3:
        return []

    threshold = float(signal.mean() + signal.std())
    peaks: list[float] = []
    last_peak_time = -999.0
    min_gap_s = 2.0

    for i in range(1, signal.size - 1):
        if signal[i] > threshold and signal[i] >= signal[i - 1] and signal[i] >= signal[i + 1]:
            ts = float(timestamps[i])
            if ts - last_peak_time >= min_gap_s:
                peaks.append(ts)
                last_peak_time = ts
    return peaks


def run_tracking(video_path: Path, sample_stride: int = 15, max_samples: int = 1200) -> VisionSummary:
    capture = cv2.VideoCapture(str(video_path))
    if not capture.isOpened():
        raise RuntimeError(f"No se pudo abrir el video: {video_path}")

    metadata = _read_metadata(capture)
    prev_gray: np.ndarray | None = None
    motion_values: list[float] = []
    timestamps_s: list[float] = []
    sampled_frames = 0
    frame_idx = 0

    while True:
        ok, frame = capture.read()
        if not ok:
            break

        if frame_idx % sample_stride == 0:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.resize(gray, (320, 180))

            if prev_gray is not None:
                diff = cv2.absdiff(gray, prev_gray)
                motion_values.append(float(np.mean(diff)))
                timestamp = frame_idx / metadata.fps if metadata.fps > 0 else float(sampled_frames)
                timestamps_s.append(timestamp)
                sampled_frames += 1
                if sampled_frames >= max_samples:
                    break

            prev_gray = gray

        frame_idx += 1

    capture.release()

    signal = np.asarray(motion_values, dtype=float)
    timestamps = np.asarray(timestamps_s, dtype=float)
    peaks = _estimate_peaks(signal, timestamps) if signal.size else []

    return VisionSummary(
        source=video_path,
        detector="frame-diff-baseline",
        tracks_detected=len(peaks),
        metadata=metadata,
        sampled_frames=sampled_frames,
        sample_stride=sample_stride,
        motion_signal_mean=float(signal.mean()) if signal.size else 0.0,
        motion_signal_std=float(signal.std()) if signal.size else 0.0,
        motion_signal_p95=float(np.percentile(signal, 95)) if signal.size else 0.0,
        motion_signal_max=float(signal.max()) if signal.size else 0.0,
        motion_signal=signal.round(4).tolist(),
        timestamps_s=timestamps.round(4).tolist(),
        estimated_motion_peaks=[round(p, 4) for p in peaks],
    )
