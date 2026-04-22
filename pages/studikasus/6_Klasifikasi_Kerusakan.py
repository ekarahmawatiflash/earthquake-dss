import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from utils.layout import render_header, render_footer
from utils.data_processing import prepare_data, check_required_columns
from utils.modeling import train_and_evaluate, predict_all, get_feature_importance

render_header(
    "Klasifikasi Kerusakan",
    "Analisis machine learning untuk mengklasifikasikan tingkat kerusakan bangunan pascagempa."
)

uploaded = st.file_uploader("Upload dataset utama (.xlsx)", type=["xlsx"], key="classify")

if uploaded is not None:
    df = pd.read_excel(uploaded)
    missing = check_required_columns(df)

    if missing:
        st.error(f"Kolom wajib belum lengkap: {missing}")
        st.stop()

    df = prepare_data(df)

    if st.button("Run Classification"):
        pipeline, metrics = train_and_evaluate(df)
        out = predict_all(pipeline, df)
        fi_df = get_feature_importance(pipeline)

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Accuracy", f"{metrics['accuracy']:.4f}")
        c2.metric("Precision", f"{metrics['precision']:.4f}")
        c3.metric("Recall", f"{metrics['recall']:.4f}")
        c4.metric("F1-Score", f"{metrics['f1']:.4f}")

        st.markdown('<div class="section-box">', unsafe_allow_html=True)
        st.subheader("Classification Report")
        st.dataframe(metrics["report_df"], use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="section-box">', unsafe_allow_html=True)
        st.subheader("Confusion Matrix")
        st.dataframe(metrics["confusion_matrix"], use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="section-box">', unsafe_allow_html=True)
        st.subheader("Feature Importance")
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.barh(fi_df["feature"][::-1], fi_df["importance"][::-1])
        ax.set_title("XGBoost Feature Importance")
        ax.set_xlabel("Importance")
        st.pyplot(fig)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="section-box">', unsafe_allow_html=True)
        st.subheader("Hasil Prediksi")
        st.dataframe(out[["titik_koordinat", "pred_label"]].head(25), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

render_footer()