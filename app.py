import streamlit as st
from utils.layout import inject_global_css, render_sidebar, render_header, render_footer

st.set_page_config(
    page_title="Earthquake Disaster Intelligence Platform",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

inject_global_css()
render_sidebar()

render_header(
    "🌍 Earthquake Disaster Intelligence Platform",
    "Portal informasi dan analitik gempa bumi untuk edukasi dasar, pembaruan gempa terkini, "
    "pemetaan area rawan gempa, serta analisis studi kasus Cianjur yang mencakup klasifikasi kerusakan, "
    "rekomendasi rehabilitasi–rekonstruksi, dan prioritas wilayah."
)

st.markdown("## 📌 Menu Portal")

c1, c2, c3 = st.columns(3)
c4, c5, c6 = st.columns(3)

with c1:
    st.markdown("""
    <div class="section-box">
        <h4>📘 Pengetahuan Dasar Gempa</h4>
        <p>Berisi pengertian gempa bumi, istilah penting, penyebab, dan mitigasi dasar.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="section-box">
        <h4>🚨 Info Gempa Terkini</h4>
        <p>Menampilkan pembaruan informasi gempa terbaru dari sumber resmi BMKG.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="section-box">
        <h4>🗺️ Peta Rawan Gempa Indonesia</h4>
        <p>Menyajikan konteks area rawan gempa di Indonesia dengan fokus Cianjur dan Jawa Barat.</p>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="section-box">
        <h4>📍 Studi Kasus Cianjur</h4>
        <p>Berisi ringkasan dataset, klasifikasi kerusakan, rekomendasi RR, dan prioritas wilayah dalam satu halaman terpadu.</p>
    </div>
    """, unsafe_allow_html=True)

with c5:
    st.markdown("""
    <div class="section-box">
        <h4>ℹ️ Tentang Sistem</h4>
        <p>Informasi singkat mengenai tujuan pengembangan platform dan sumber data utama.</p>
    </div>
    """, unsafe_allow_html=True)

with c6:
    st.markdown("""
    <div class="section-box">
        <h4>🧭 Petunjuk Penggunaan</h4>
        <p>Pilih halaman dari menu sidebar untuk mulai mengeksplorasi seluruh modul sistem.</p>
    </div>
    """, unsafe_allow_html=True)

render_footer()