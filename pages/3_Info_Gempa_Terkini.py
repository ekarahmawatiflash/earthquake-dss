import streamlit as st
import pandas as pd
from utils.layout import inject_global_css, render_sidebar, render_header, render_footer
from utils.bmkg_api import get_autogempa, get_gempa_terkini, get_gempa_dirasakan

inject_global_css()
render_sidebar()

render_header(
    "Info Gempa Bumi Terkini",
    "Pembaruan informasi gempa terbaru dari sumber resmi BMKG, disajikan dalam bentuk ringkasan visual dan tabel informasi."
)

st.markdown("""
<style>
.eq-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 6px 16px rgba(15, 23, 42, 0.05);
    margin-bottom: 18px;
}

.eq-title {
    font-size: 1.3rem;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 8px;
}

.eq-subtitle {
    font-size: 0.95rem;
    color: #475569;
    line-height: 1.7;
}

.metric-mini {
    background: linear-gradient(135deg, #ffffff, #f8fbff);
    border: 1px solid #dbeafe;
    border-radius: 18px;
    padding: 16px;
    text-align: center;
    height: 100%;
    box-shadow: 0 4px 12px rgba(59, 130, 246, 0.05);
}

.metric-mini-number {
    font-size: 1.5rem;
    font-weight: 800;
    color: #1d4ed8;
}

.metric-mini-label {
    margin-top: 4px;
    color: #475569;
    font-size: 0.9rem;
}

.info-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
}

.info-item {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    padding: 12px 14px;
}

.info-item-label {
    font-size: 0.82rem;
    color: #64748b;
    margin-bottom: 4px;
}

.info-item-value {
    font-size: 0.98rem;
    color: #0f172a;
    font-weight: 600;
}

.badge {
    display: inline-block;
    padding: 8px 14px;
    border-radius: 999px;
    background: #eff6ff;
    border: 1px solid #bfdbfe;
    color: #1d4ed8;
    font-size: 0.85rem;
    font-weight: 700;
    margin-bottom: 10px;
}

.shake-box {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 20px;
    padding: 18px;
    box-shadow: 0 6px 16px rgba(15, 23, 42, 0.05);
}

.note-box {
    background: #eff6ff;
    border-left: 5px solid #3b82f6;
    border-radius: 14px;
    padding: 14px 16px;
    color: #334155;
    line-height: 1.7;
    margin-top: 18px;
}

.table-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 20px;
    padding: 18px;
    box-shadow: 0 6px 16px rgba(15, 23, 42, 0.05);
}
</style>
""", unsafe_allow_html=True)

# =========================
# DATA
# =========================
autogempa = None
terkini_df = None
dirasakan_df = None
error_messages = []

try:
    autogempa = get_autogempa()
except Exception as e:
    error_messages.append(f"Gagal mengambil data gempa terbaru: {e}")

try:
    terkini_df = get_gempa_terkini()
except Exception as e:
    error_messages.append(f"Gagal mengambil data 15 gempa M5.0+: {e}")

try:
    dirasakan_df = get_gempa_dirasakan()
except Exception as e:
    error_messages.append(f"Gagal mengambil data 15 gempa dirasakan: {e}")

if error_messages:
    for msg in error_messages:
        st.error(msg)

# =========================
# RINGKASAN ATAS
# =========================
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="metric-mini">
        <div class="metric-mini-number">BMKG</div>
        <div class="metric-mini-label">Sumber Data</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="metric-mini">
        <div class="metric-mini-number">15</div>
        <div class="metric-mini-label">Gempa M5.0+</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="metric-mini">
        <div class="metric-mini-number">15</div>
        <div class="metric-mini-label">Gempa Dirasakan</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["Gempa Terbaru", "15 Gempa M5.0+", "15 Gempa Dirasakan"])

# =========================
# TAB 1 - GEMPA TERBARU
# =========================
with tab1:
    if autogempa:
        left, right = st.columns([1.15, 1])

        with left:
            st.markdown("""
            <div class="eq-card">
                <div class="badge">Update Gempa Terbaru</div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
                <div class="eq-title">{autogempa.get("Wilayah", "-")}</div>
                <div class="eq-subtitle">
                    Informasi gempa terbaru dari BMKG yang ditampilkan dalam format ringkas
                    untuk memudahkan pemantauan cepat.
                </div>
            """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown(f"""
            <div class="info-grid">
                <div class="info-item">
                    <div class="info-item-label">Magnitudo</div>
                    <div class="info-item-value">{autogempa.get("Magnitude", "-")}</div>
                </div>
                <div class="info-item">
                    <div class="info-item-label">Kedalaman</div>
                    <div class="info-item-value">{autogempa.get("Kedalaman", "-")}</div>
                </div>
                <div class="info-item">
                    <div class="info-item-label">Tanggal</div>
                    <div class="info-item-value">{autogempa.get("Tanggal", "-")}</div>
                </div>
                <div class="info-item">
                    <div class="info-item-label">Jam</div>
                    <div class="info-item-value">{autogempa.get("Jam", "-")}</div>
                </div>
                <div class="info-item">
                    <div class="info-item-label">Koordinat</div>
                    <div class="info-item-value">{autogempa.get("Coordinates", "-")}</div>
                </div>
                <div class="info-item">
                    <div class="info-item-label">Potensi</div>
                    <div class="info-item-value">{autogempa.get("Potensi", "-")}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            if autogempa.get("Dirasakan"):
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown(f"""
                <div class="note-box">
                    <b>Dirasakan:</b> {autogempa.get("Dirasakan", "-")}
                </div>
                """, unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)

        with right:
            st.markdown("""
            <div class="shake-box">
                <div class="eq-title">Shakemap BMKG</div>
                <div class="eq-subtitle">
                    Visualisasi lokasi dan intensitas guncangan untuk peristiwa gempa terbaru.
                </div>
            """, unsafe_allow_html=True)

            shakemap = autogempa.get("Shakemap", "")
            if shakemap:
                st.image(
                    f"https://data.bmkg.go.id/DataMKG/TEWS/{shakemap}",
                    use_container_width=True
                )
            else:
                st.info("Shakemap tidak tersedia.")

            st.markdown("</div>", unsafe_allow_html=True)

    else:
        st.warning("Data gempa terbaru belum tersedia.")

# =========================
# TAB 2 - 15 GEMPA M5.0+
# =========================
with tab2:
    st.markdown("""
    <div class="table-card">
        <div class="eq-title">Daftar 15 Gempa M5.0+</div>
        <div class="eq-subtitle">
            Data ini menampilkan daftar gempa berkekuatan M5.0 ke atas yang dirilis BMKG.
        </div>
    """, unsafe_allow_html=True)

    if isinstance(terkini_df, pd.DataFrame) and not terkini_df.empty:
        show_cols = [c for c in ["Tanggal", "Jam", "DateTime", "Coordinates", "Lintang", "Bujur", "Magnitude", "Kedalaman", "Wilayah", "Potensi"] if c in terkini_df.columns]
        st.dataframe(terkini_df[show_cols], use_container_width=True, height=420)
    else:
        st.info("Data 15 gempa M5.0+ belum tersedia.")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# TAB 3 - 15 GEMPA DIRASAKAN
# =========================
with tab3:
    st.markdown("""
    <div class="table-card">
        <div class="eq-title">Daftar 15 Gempa Dirasakan</div>
        <div class="eq-subtitle">
            Data ini menampilkan kejadian gempa yang dirasakan masyarakat berdasarkan rilis BMKG.
        </div>
    """, unsafe_allow_html=True)

    if isinstance(dirasakan_df, pd.DataFrame) and not dirasakan_df.empty:
        show_cols = [c for c in ["Tanggal", "Jam", "DateTime", "Coordinates", "Lintang", "Bujur", "Magnitude", "Kedalaman", "Wilayah", "Dirasakan"] if c in dirasakan_df.columns]
        st.dataframe(dirasakan_df[show_cols], use_container_width=True, height=420)
    else:
        st.info("Data 15 gempa dirasakan belum tersedia.")

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("""
<div class="note-box">
    <b>Sumber data:</b> BMKG. Informasi pada halaman ini ditampilkan untuk mendukung pemantauan cepat
    dan edukasi kebencanaan. Untuk keputusan resmi, tetap mengacu pada rilis dan kanal resmi BMKG.
</div>
""", unsafe_allow_html=True)

render_footer()