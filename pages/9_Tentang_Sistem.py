import streamlit as st
from utils.layout import inject_global_css, render_sidebar, render_header, render_footer

inject_global_css()
render_sidebar()

render_header(
    "Tentang Sistem",
    "Informasi singkat mengenai tujuan pengembangan sistem dan cakupan modul utama."
)

st.markdown("""
<div class="section-box">
    <h4>Earthquake Disaster Intelligence Platform</h4>
    <p>
        Sistem ini dikembangkan untuk mendukung edukasi, pemetaan kerentanan,
        klasifikasi kerusakan bangunan, rekomendasi rehabilitasi dan rekonstruksi,
        serta analisis prioritas wilayah.
    </p>
</div>

<div class="section-box">
    <h4>Fokus Studi</h4>
    <p>
        Fokus studi diarahkan pada gempa bumi dengan studi kasus utama di Cianjur, Jawa Barat.
    </p>
</div>

<div class="section-box">
    <h4>Sumber Data</h4>
    <p>
        Informasi gempa terkini dapat memanfaatkan sumber resmi BMKG,
        sedangkan analisis kerusakan dan RR menggunakan dataset penelitian.
    </p>
</div>
""", unsafe_allow_html=True)

render_footer()