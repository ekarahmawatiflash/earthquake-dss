import streamlit as st
import folium
from streamlit_folium import st_folium
from utils.layout import inject_global_css, render_sidebar, render_header, render_footer

inject_global_css()
render_sidebar()

render_header(
    "Peta Rawan Gempa Indonesia",
    "Visualisasi konteks kerawanan gempa di Indonesia dengan fokus studi kasus Cianjur, Jawa Barat."
)

st.markdown("""
<style>
.map-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 6px 16px rgba(15, 23, 42, 0.05);
    margin-bottom: 18px;
}

.map-card h3 {
    margin-top: 0;
    margin-bottom: 10px;
    color: #0f172a;
    font-size: 1.25rem;
    font-weight: 800;
}

.map-card p, .map-card li {
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
    margin-bottom: 8px;
}

.stat-number {
    font-size: 1.65rem;
    font-weight: 800;
    color: #2563eb;
}

.stat-label {
    margin-top: 6px;
    color: #475569;
    font-size: 0.9rem;
}

.note-box {
    background: #eff6ff;
    border-left: 5px solid #3b82f6;
    border-radius: 14px;
    padding: 14px 16px;
    margin-top: 16px;
    color: #334155;
    line-height: 1.7;
}

.map-wrapper {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 20px;
    padding: 18px;
    box-shadow: 0 6px 16px rgba(15, 23, 42, 0.05);
    margin-bottom: 18px;
}

.legend-row {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 12px;
    color: #334155;
    font-size: 0.97rem;
}

.legend-dot {
    width: 16px;
    height: 16px;
    border-radius: 50%;
    display: inline-block;
    flex-shrink: 0;
}

.section-subtitle {
    color: #475569;
    line-height: 1.7;
    margin-bottom: 14px;
}
</style>
""", unsafe_allow_html=True)

# Ringkasan atas
s1, s2, s3 = st.columns(3)
with s1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">3</div>
        <div class="stat-label">Kategori Kerawanan</div>
    </div>
    """, unsafe_allow_html=True)

with s2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">Indonesia</div>
        <div class="stat-label">Cakupan Peta</div>
    </div>
    """, unsafe_allow_html=True)

with s3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">Cianjur</div>
        <div class="stat-label">Fokus Studi</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

left, right = st.columns([1, 1.7], gap="large")

with left:
    st.markdown("""
    <div class="map-card">
        <h3>Keterangan</h3>
        <p>
            Indonesia berada pada kawasan tektonik aktif sehingga banyak wilayah memiliki
            potensi gempa bumi. Halaman ini menyajikan konteks spasial nasional dan
            menonjolkan Cianjur sebagai studi kasus utama.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="map-card">
        <h3>Legenda Kerawanan</h3>
        <div class="section-subtitle">
            Warna pada titik menunjukkan contoh tingkat kerawanan dan titik fokus studi kasus.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        """
        <div class="legend-row">
            <span class="legend-dot" style="background:#22c55e;"></span>
            <span>Kerawanan rendah</span>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div class="legend-row">
            <span class="legend-dot" style="background:#f59e0b;"></span>
            <span>Kerawanan sedang</span>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div class="legend-row">
            <span class="legend-dot" style="background:#ef4444;"></span>
            <span>Kerawanan tinggi</span>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div class="legend-row">
            <span class="legend-dot" style="background:#2563eb;"></span>
            <span>Titik studi kasus</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="note-box">
        <b>Catatan:</b> versi saat ini menampilkan peta konteks nasional.
        Pengembangan lanjutan dapat menambahkan layer rawan gempa berbasis data,
        GeoJSON, atau filter per provinsi.
    </div>
    """, unsafe_allow_html=True)

with right:
    fmap = folium.Map(location=[-2.5, 118], zoom_start=5, control_scale=True)

    # Titik studi kasus
    folium.Marker(
        location=[-6.816, 107.142],
        popup="Cianjur - Studi Kasus",
        tooltip="Cianjur",
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(fmap)

    # Titik konteks visual
    sample_points = [
        ("Sumatra Barat", -0.95, 100.35, "red"),
        ("Yogyakarta", -7.80, 110.37, "orange"),
        ("Sulawesi Tengah", -0.89, 119.87, "red"),
        ("Kalimantan Tengah", -2.21, 113.92, "green"),
        ("Papua", -4.26, 138.08, "orange"),
    ]

    for name, lat, lon, color in sample_points:
        folium.CircleMarker(
            location=[lat, lon],
            radius=8,
            color=color,
            fill=True,
            fill_opacity=0.85,
            popup=name,
            tooltip=name
        ).add_to(fmap)

    st.markdown("""
    <div class="map-wrapper">
        <h3>Visualisasi Peta</h3>
        <p class="section-subtitle">
            Peta ini memberikan gambaran konteks nasional area rawan gempa dan menampilkan
            beberapa titik representatif serta lokasi studi kasus di Cianjur.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st_folium(fmap, height=620, width=None, returned_objects=[])

b1, b2 = st.columns(2, gap="large")

with b1:
    st.markdown("""
    <div class="map-card">
        <h3>Kenapa Indonesia Rawan Gempa?</h3>
        <p>
            Indonesia berada di jalur cincin api (<i>Ring of Fire</i>) dan pada zona
            pertemuan lempeng tektonik, sehingga aktivitas seismiknya tinggi dan banyak
            wilayah memerlukan kesiapsiagaan.
        </p>
    </div>
    """, unsafe_allow_html=True)

with b2:
    st.markdown("""
    <div class="map-card">
        <h3>Pengembangan Selanjutnya</h3>
        <ul>
            <li>Layer GeoJSON rawan gempa</li>
            <li>Filter per provinsi</li>
            <li>Fokus Jawa Barat dan Cianjur</li>
            <li>Integrasi data risiko / bahaya gempa</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

render_footer()