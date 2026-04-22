import streamlit as st
import pandas as pd
import folium
from io import BytesIO
from streamlit_folium import st_folium

from utils.layout import render_header, render_footer
from utils.data_processing import prepare_data, check_required_columns
from utils.modeling import train_and_evaluate, predict_all
from utils.recommendation import add_rr_recommendation

render_header(
    "Rekomendasi Rehabilitasi–Rekonstruksi",
    "Modul DSS yang mengubah hasil klasifikasi kerusakan menjadi rekomendasi rehabilitasi dan rekonstruksi."
)

uploaded = st.file_uploader("Upload dataset utama (.xlsx)", type=["xlsx"], key="rr")

if uploaded is not None:
    df = pd.read_excel(uploaded)
    missing = check_required_columns(df)

    if missing:
        st.error(f"Kolom wajib belum lengkap: {missing}")
        st.stop()

    df = prepare_data(df)

    if st.button("Generate RR Recommendation"):
        pipeline, metrics = train_and_evaluate(df)
        out = predict_all(pipeline, df)
        out = add_rr_recommendation(out)

        c1, c2, c3 = st.columns(3)
        c1.metric("Minor", int((out["pred_label"] == "Minor").sum()))
        c2.metric("Moderate", int((out["pred_label"] == "Moderate").sum()))
        c3.metric("Severe", int((out["pred_label"] == "Severe").sum()))

        st.markdown('<div class="section-box">', unsafe_allow_html=True)
        st.subheader("Tabel Rekomendasi")
        st.dataframe(
            out[["titik_koordinat", "pred_label", "RR_recommendation"]].head(50),
            use_container_width=True
        )
        st.markdown('</div>', unsafe_allow_html=True)

        valid_points = out.dropna(subset=["lat", "lon"]).copy()

        if not valid_points.empty:
            center = [valid_points["lat"].mean(), valid_points["lon"].mean()]
            fmap = folium.Map(location=center, zoom_start=9, control_scale=True)

            color_map = {
                "Minor": "green",
                "Moderate": "orange",
                "Severe": "red"
            }

            for _, row in valid_points.iterrows():
                folium.CircleMarker(
                    location=[row["lat"], row["lon"]],
                    radius=6,
                    color=color_map.get(row["pred_label"], "blue"),
                    fill=True,
                    fill_opacity=0.85,
                    popup=(
                        f"Damage: {row['pred_label']}<br>"
                        f"RR: {row['RR_recommendation']}"
                    )
                ).add_to(fmap)

            st.markdown('<div class="section-box">', unsafe_allow_html=True)
            st.subheader("Peta Hasil RR")
            st_folium(fmap, height=520, returned_objects=[])
            st.markdown('</div>', unsafe_allow_html=True)

        output = BytesIO()
        out.to_excel(output, index=False)

        st.download_button(
            "Download Hasil RR (Excel)",
            data=output.getvalue(),
            file_name="hasil_rr.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )

render_footer()