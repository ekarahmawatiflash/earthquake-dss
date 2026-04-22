import streamlit as st
from utils.layout import inject_global_css, render_sidebar, render_header, render_footer

inject_global_css()
render_sidebar()
render_header(
    "Beranda",
    "Halaman ini menampilkan ringkasan portal gempa bumi dan modul utama yang tersedia."
)


c1, c2, c3 = st.columns(3)
c1.metric("Fokus Bencana", "Gempa Bumi")
c2.metric("Wilayah Studi", "Cianjur / Jawa Barat")
c3.metric("Jenis Sistem", "Spatial DSS")

st.markdown("""
<div class="section-box">
    <h4>Ringkasan Sistem</h4>
    <p>
        Platform ini mengintegrasikan informasi gempa, pemetaan kerentanan, klasifikasi
        kerusakan bangunan, rekomendasi rehabilitasi–rekonstruksi, serta penentuan prioritas wilayah.
    </p>
</div>
""", unsafe_allow_html=True)

render_footer()