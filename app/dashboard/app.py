from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

from app.pipeline import run_pipeline


REPORT_PATH = Path("outputs/report.json")
TMP_DIR = Path("data/interim/uploads")
TMP_DIR.mkdir(parents=True, exist_ok=True)

st.set_page_config(page_title="PatternSight MVP", layout="wide")
st.title("PatternSight MVP")
st.caption("Interfaz inicial para subir video, correr análisis y ver resultados")

with st.sidebar:
    st.header("Ejecutar análisis")
    uploaded_video = st.file_uploader("Sube un video", type=["mp4", "mov", "avi", "mkv"])
    sample_stride = st.slider("Sample stride", min_value=5, max_value=60, value=15, step=5)
    run_clicked = st.button("Analizar video", use_container_width=True)

    if run_clicked:
        if uploaded_video is None:
            st.warning("Primero sube un video.")
        else:
            target_path = TMP_DIR / uploaded_video.name
            target_path.write_bytes(uploaded_video.getbuffer())
            with st.spinner("Procesando video..."):
                report = run_pipeline(str(target_path), sample_stride=sample_stride)
            st.success("Análisis completado")
            st.session_state["latest_report"] = report

report = st.session_state.get("latest_report")
if report is None and REPORT_PATH.exists():
    report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))

if report is None:
    st.info("Sube un video en la barra lateral para comenzar.")
else:
    vision = report.get("vision", {})
    sequences = report.get("sequences", {})
    features = report.get("features", {})
    patterns = report.get("patterns", {})

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("FPS", vision.get("metadata", {}).get("fps", 0))
    col2.metric("Duración (s)", round(vision.get("metadata", {}).get("duration_s", 0), 2))
    col3.metric("Secuencias", features.get("total_sequences", 0))
    col4.metric("Consistency", patterns.get("consistency_score", 0))

    st.subheader("Resumen del análisis")
    summary_col1, summary_col2 = st.columns(2)
    with summary_col1:
        st.json(features)
    with summary_col2:
        st.json(patterns)

    motion_signal = vision.get("motion_signal", [])
    timestamps = vision.get("timestamps_s", [])
    if motion_signal and timestamps:
        signal_df = pd.DataFrame({"t": timestamps, "motion": motion_signal})
        fig = px.line(signal_df, x="t", y="motion", title="Señal de movimiento estimada")
        st.plotly_chart(fig, use_container_width=True)

    cycle_times = sequences.get("estimated_cycle_times_s", [])
    if cycle_times:
        cycles_df = pd.DataFrame({"sequence": list(range(1, len(cycle_times) + 1)), "cycle_time_s": cycle_times})
        fig_cycles = px.bar(cycles_df, x="sequence", y="cycle_time_s", title="Tiempo estimado por secuencia")
        st.plotly_chart(fig_cycles, use_container_width=True)

    grouped = sequences.get("grouped_phase_windows_s", [])
    if grouped:
        st.subheader("Ventanas de fase agrupadas")
        st.write(grouped[:10])

    with st.expander("Reporte completo"):
        st.json(report)
