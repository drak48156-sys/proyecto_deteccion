from __future__ import annotations

import json
from pathlib import Path

import streamlit as st


REPORT_PATH = Path("outputs/report.json")

st.set_page_config(page_title="PatternSight MVP", layout="wide")
st.title("PatternSight MVP")
st.caption("Dashboard inicial del sistema de inteligencia operacional predictiva")

if not REPORT_PATH.exists():
    st.warning("Aún no existe outputs/report.json. Ejecuta primero el pipeline.")
else:
    report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    st.subheader("Features")
    st.json(report.get("features", {}))
    st.subheader("Patterns")
    st.json(report.get("patterns", {}))
