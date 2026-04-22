import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import folium
from io import BytesIO
from streamlit_folium import st_folium

from utils.layout import inject_global_css, render_sidebar, render_header, render_footer
from utils.data_processing import prepare_data, check_required_columns
from utils.modeling import train_and_evaluate, predict_all, get_feature_importance
from utils.recommendation import add_rr_recommendation
from utils.scoring import compute_priority_score

inject_global_css()
render_sidebar()

render_header(
    "Studi Kasus Cianjur",
    "Halaman ini menggabungkan ringkasan dataset, klasifikasi kerusakan, rekomendasi rehabilitasi–rekonstruksi, dan analisis prioritas wilayah untuk studi kasus gempa Cianjur."
)

st.markdown("""
<style>
.dashboard-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 6px 16px rgba(15, 23, 42, 0.05);
    margin-bottom: 18px;
}

.dashboard-card h3 {
    margin-top: 0;
    margin-bottom: 10px;
    color: #0f172a;
    font-size: 1.25rem;
    font-weight: 800;
}

.dashboard-card p, .dashboard-card li {
    color: #475569;
    line-height: 1.7;
    font-size: 0.98rem;
}

.stat-card {
    background: linear-gradient(135deg, #ffffff, #f8fbff);
    border: 1px solid #dbeafe;
    border-radius: 18px;
    padding: 18px;
    text-align: center;
    box-shadow: 0 4px 12px rgba(59, 130, 246, 0.06);
    margin-bottom: 10px;
}

.stat-number {
    font-size: 1.7rem;
    font-weight: 800;
    color: #2563eb;
}

.stat-label {
    margin-top: 6px;
    color: #475569;
    font-size: 0.9rem;
}

.info-box {
    background: #eff6ff;
    border-left: 5px solid #3b82f6;
    border-radius: 14px;
    padding: 14px 16px;
    color: #334155;
    line-height: 1.7;
    margin-bottom: 18px;
}

.small-badge {
    display: inline-block;
    background: #eff6ff;
    border: 1px solid #bfdbfe;
    color: #1d4ed8;
    border-radius: 999px;
    padding: 6px 12px;
    font-size: 0.82rem;
    font-weight: 700;
    margin-right: 8px;
    margin-bottom: 10px;
}

.section-title {
    font-size: 1.15rem;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

uploaded = st.file_uploader("Upload dataset Cianjur (.xlsx)", type=["xlsx"], key="cianjur")

if uploaded is not None:
    df = pd.read_excel(uploaded)
    missing = check_required_columns(df)

    if missing:
        st.error(f"Kolom wajib belum lengkap: {missing}")
        st.stop()

    df = prepare_data(df)

    # Ringkasan atas
    s1, s2, s3, s4 = st.columns(4)
    with s1:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{len(df):,}</div>
            <div class="stat-label">Jumlah Data</div>
        </div>
        """, unsafe_allow_html=True)
    with s2:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{len(df.columns)}</div>
            <div class="stat-label">Jumlah Kolom</div>
        </div>
        """, unsafe_allow_html=True)
    with s3:
        valid_geo = int(df.dropna(subset=["lat", "lon"]).shape[0]) if {"lat", "lon"}.issubset(df.columns) else 0
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{valid_geo:,}</div>
            <div class="stat-label">Koordinat Valid</div>
        </div>
        """, unsafe_allow_html=True)
    with s4:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">Cianjur</div>
            <div class="stat-label">Wilayah Studi</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        Halaman ini menyatukan seluruh analisis utama dalam satu tempat:
        <b>ringkasan dataset</b>, <b>klasifikasi kerusakan</b>,
        <b>rekomendasi rehabilitasi–rekonstruksi</b>, dan <b>prioritas wilayah</b>.
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs([
        "Ringkasan Dataset",
        "Klasifikasi Kerusakan",
        "Rekomendasi RR",
        "Prioritas Wilayah"
    ])

    # Jalankan model sekali
    try:
        pipeline, metrics = train_and_evaluate(df)
        out_pred = predict_all(pipeline, df)
        out_rr = add_rr_recommendation(out_pred.copy())
        out_priority = compute_priority_score(out_rr.copy())
        fi_df = get_feature_importance(pipeline)
    except Exception as e:
        st.error(f"Proses analisis gagal: {e}")
        render_footer()
        st.stop()

    # TAB 1
    with tab1:
        c1, c2 = st.columns([1.2, 1])

        with c1:
            st.markdown("""
            <div class="dashboard-card">
                <h3>Preview Dataset</h3>
            """, unsafe_allow_html=True)
            st.dataframe(df.head(20), use_container_width=True, height=420)
            st.markdown("</div>", unsafe_allow_html=True)

        with c2:
            st.markdown("""
            <div class="dashboard-card">
                <h3>Informasi Dataset</h3>
                <p>Dataset ini digunakan sebagai dasar analisis kerusakan bangunan pascagempa dan rekomendasi tindakan pemulihan.</p>
            """, unsafe_allow_html=True)

            if "zona_kerentanan_enc" in df.columns:
                hazard_summary = df["zona_kerentanan_enc"].value_counts().reset_index()
                hazard_summary.columns = ["Zona Kerentanan", "Jumlah"]
                st.markdown('<div class="section-title">Distribusi Zona Kerentanan</div>', unsafe_allow_html=True)
                st.dataframe(hazard_summary, use_container_width=True, height=220)

            st.markdown("</div>", unsafe_allow_html=True)

    # TAB 2
    with tab2:
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Accuracy", f"{metrics['accuracy']:.4f}")
        m2.metric("Precision", f"{metrics['precision']:.4f}")
        m3.metric("Recall", f"{metrics['recall']:.4f}")
        m4.metric("F1-Score", f"{metrics['f1']:.4f}")

        top_left, top_right = st.columns([1.15, 1])

        with top_left:
            st.markdown("""
            <div class="dashboard-card">
                <h3>Classification Report</h3>
            """, unsafe_allow_html=True)
            st.dataframe(metrics["report_df"], use_container_width=True, height=320)
            st.markdown("</div>", unsafe_allow_html=True)

        with top_right:
            cm_df = pd.DataFrame(
                metrics["confusion_matrix"],
                index=["Actual Minor", "Actual Moderate", "Actual Severe"],
                columns=["Pred Minor", "Pred Moderate", "Pred Severe"]
            )
            st.markdown("""
            <div class="dashboard-card">
                <h3>Confusion Matrix</h3>
            """, unsafe_allow_html=True)
            st.dataframe(cm_df, use_container_width=True, height=320)
            st.markdown("</div>", unsafe_allow_html=True)

        bottom_left, bottom_right = st.columns([1, 1.2])

        with bottom_left:
            st.markdown("""
            <div class="dashboard-card">
                <h3>Feature Importance</h3>
            """, unsafe_allow_html=True)
            fig, ax = plt.subplots(figsize=(7, 4.5))
            ax.barh(fi_df["feature"][::-1], fi_df["importance"][::-1])
            ax.set_title("XGBoost Feature Importance")
            ax.set_xlabel("Importance")
            st.pyplot(fig)
            st.markdown("</div>", unsafe_allow_html=True)

        with bottom_right:
            st.markdown("""
            <div class="dashboard-card">
                <h3>Hasil Prediksi</h3>
            """, unsafe_allow_html=True)
            st.dataframe(
                out_pred[["titik_koordinat", "pred_label"]].head(30),
                use_container_width=True,
                height=360
            )
            st.markdown("</div>", unsafe_allow_html=True)

    # TAB 3
    with tab3:
        rr1, rr2, rr3 = st.columns(3)
        rr1.metric("Minor", int((out_rr["pred_label"] == "Minor").sum()))
        rr2.metric("Moderate", int((out_rr["pred_label"] == "Moderate").sum()))
        rr3.metric("Severe", int((out_rr["pred_label"] == "Severe").sum()))

        upper_left, upper_right = st.columns([1.05, 1.35])

        with upper_left:
            st.markdown("""
            <div class="dashboard-card">
                <h3>Rekomendasi RR</h3>
                <p>Hasil prediksi tingkat kerusakan diterjemahkan menjadi rekomendasi rehabilitasi–rekonstruksi.</p>
            """, unsafe_allow_html=True)

            st.markdown('<span class="small-badge">Minor</span>', unsafe_allow_html=True)
            st.markdown('<span class="small-badge">Moderate</span>', unsafe_allow_html=True)
            st.markdown('<span class="small-badge">Severe</span>', unsafe_allow_html=True)

            st.dataframe(
                out_rr[["titik_koordinat", "pred_label", "RR_recommendation"]].head(40),
                use_container_width=True,
                height=430
            )
            st.markdown("</div>", unsafe_allow_html=True)

            output_rr = BytesIO()
            out_rr.to_excel(output_rr, index=False)
            st.download_button(
                "Download Hasil RR (Excel)",
                data=output_rr.getvalue(),
                file_name="hasil_rr_cianjur.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )

        with upper_right:
            valid_points = out_rr.dropna(subset=["lat", "lon"]).copy()

            st.markdown("""
            <div class="dashboard-card">
                <h3>Peta Hasil RR</h3>
                <p>Visualisasi spasial hasil klasifikasi kerusakan dan rekomendasi tindakan.</p>
            """, unsafe_allow_html=True)

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

                st_folium(fmap, height=560, returned_objects=[])
            else:
                st.info("Koordinat valid tidak tersedia untuk menampilkan peta.")

            st.markdown("</div>", unsafe_allow_html=True)

    # TAB 4
    with tab4:
        left_p, right_p = st.columns([1.25, 1])

        with left_p:
            st.markdown("""
            <div class="dashboard-card">
                <h3>Hasil Prioritas Wilayah</h3>
                <p>Area intervensi ditentukan berdasarkan kerusakan, kerentanan, lereng, tanah, dan jarak.</p>
            """, unsafe_allow_html=True)
            st.dataframe(
                out_priority[[
                    "titik_koordinat",
                    "pred_label",
                    "priority_score",
                    "priority_label",
                    "RR_recommendation"
                ]].head(50),
                use_container_width=True,
                height=430
            )
            st.markdown("</div>", unsafe_allow_html=True)

            output_priority = BytesIO()
            out_priority.to_excel(output_priority, index=False)
            st.download_button(
                "Download Hasil Prioritas (Excel)",
                data=output_priority.getvalue(),
                file_name="hasil_prioritas_cianjur.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )

        with right_p:
            summary = out_priority["priority_label"].value_counts().reset_index()
            summary.columns = ["Priority Level", "Count"]

            st.markdown("""
            <div class="dashboard-card">
                <h3>Ringkasan Prioritas</h3>
            """, unsafe_allow_html=True)
            st.dataframe(summary, use_container_width=True, height=220)

            st.markdown("""
            <div class="info-box">
                <b>Interpretasi:</b> wilayah dengan <i>priority score</i> lebih tinggi
                dapat dipertimbangkan sebagai area intervensi yang lebih mendesak.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)

else:
    st.info("Upload dataset Cianjur untuk memulai analisis.")

render_footer()