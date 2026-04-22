import streamlit as st
import pandas as pd

from utils.layout import render_header, render_footer
from utils.data_processing import prepare_data, check_required_columns
from utils.modeling import train_and_evaluate, predict_all
from utils.recommendation import add_rr_recommendation
from utils.scoring import compute_priority_score

render_header(
    "Prioritas Wilayah",
    "Menentukan area intervensi berdasarkan tingkat kerusakan dan kerentanan wilayah."
)

uploaded = st.file_uploader("Upload dataset utama (.xlsx)", type=["xlsx"], key="priority")

if uploaded is not None:
    df = pd.read_excel(uploaded)
    missing = check_required_columns(df)

    if missing:
        st.error(f"Kolom wajib belum lengkap: {missing}")
        st.stop()

    df = prepare_data(df)

    if st.button("Run Priority Analysis"):
        pipeline, metrics = train_and_evaluate(df)
        out = predict_all(pipeline, df)
        out = add_rr_recommendation(out)
        out = compute_priority_score(out)

        st.markdown('<div class="section-box">', unsafe_allow_html=True)
        st.subheader("Hasil Prioritas")
        st.dataframe(
            out[[
                "titik_koordinat",
                "pred_label",
                "priority_score",
                "priority_label",
                "RR_recommendation"
            ]].head(50),
            use_container_width=True
        )
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="section-box">', unsafe_allow_html=True)
        st.subheader("Ringkasan Prioritas")
        summary = out["priority_label"].value_counts().reset_index()
        summary.columns = ["Priority Level", "Count"]
        st.dataframe(summary, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

render_footer()