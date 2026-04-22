import streamlit as st
from utils.layout import inject_global_css, render_sidebar, render_header, render_footer

inject_global_css()
render_sidebar()

render_header(
    "Pengetahuan Dasar Gempa Bumi",
    "Halaman ini berisi konsep dasar, istilah penting, dan mitigasi sederhana terkait gempa bumi."
)

st.markdown("""
<style>
.knowledge-hero {
    background: linear-gradient(135deg, #eff6ff, #dbeafe);
    border: 1px solid #bfdbfe;
    border-radius: 24px;
    padding: 28px 30px;
    margin-bottom: 24px;
    overflow: hidden;
}

.knowledge-title {
    font-size: 2rem;
    font-weight: 800;
    color: #1e3a8a;
    margin-bottom: 10px;
}

.knowledge-desc {
    font-size: 1rem;
    color: #334155;
    line-height: 1.7;
}

.hero-illustration {
    background: radial-gradient(circle at 30% 30%, #93c5fd, #3b82f6);
    border-radius: 22px;
    height: 220px;
    position: relative;
    overflow: hidden;
    box-shadow: inset 0 0 30px rgba(255,255,255,0.20);
}

.wave {
    position: absolute;
    width: 180%;
    height: 180%;
    left: -40%;
    top: -55%;
    background: rgba(255,255,255,0.12);
    border-radius: 40%;
    animation: rotateWave 14s linear infinite;
}

.wave.two {
    top: -50%;
    animation-duration: 18s;
    background: rgba(255,255,255,0.08);
}

.wave.three {
    top: -45%;
    animation-duration: 22s;
    background: rgba(255,255,255,0.06);
}

.epicenter {
    position: absolute;
    left: 50%;
    top: 55%;
    transform: translate(-50%, -50%);
    width: 26px;
    height: 26px;
    background: #f97316;
    border-radius: 50%;
    box-shadow: 0 0 0 0 rgba(249, 115, 22, 0.6);
    animation: pulseEpicenter 2s infinite;
}

.ring {
    position: absolute;
    left: 50%;
    top: 55%;
    transform: translate(-50%, -50%);
    border: 3px solid rgba(255,255,255,0.55);
    border-radius: 50%;
}

.ring.r1 { width: 70px; height: 70px; }
.ring.r2 { width: 120px; height: 120px; }
.ring.r3 { width: 170px; height: 170px; }

.mountain {
    position: absolute;
    bottom: 0;
    width: 0;
    height: 0;
    border-left: 90px solid transparent;
    border-right: 90px solid transparent;
    border-bottom: 120px solid rgba(15, 23, 42, 0.18);
}

.m1 { left: 10px; }
.m2 { left: 110px; border-left-width: 110px; border-right-width: 110px; border-bottom-width: 150px; }
.m3 { right: 5px; border-left-width: 80px; border-right-width: 80px; border-bottom-width: 110px; }

.floating-badge {
    display: inline-block;
    background: #ffffff;
    border: 1px solid #dbeafe;
    color: #1e3a8a;
    border-radius: 999px;
    padding: 7px 14px;
    font-size: 0.85rem;
    font-weight: 600;
    margin-right: 8px;
    margin-bottom: 10px;
    box-shadow: 0 4px 12px rgba(59, 130, 246, 0.08);
}

.info-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 22px;
    padding: 22px;
    box-shadow: 0 6px 16px rgba(15, 23, 42, 0.05);
    margin-bottom: 18px;
    height: 100%;
}

.info-icon {
    font-size: 1.8rem;
    margin-bottom: 10px;
}

.info-heading {
    font-size: 1.7rem;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 8px;
}

.info-text {
    color: #475569;
    font-size: 1rem;
    line-height: 1.8;
}

.mitigation-box {
    background: linear-gradient(135deg, #ffffff, #f8fbff);
    border: 1px solid #dbeafe;
    border-radius: 22px;
    padding: 24px;
    box-shadow: 0 8px 18px rgba(59, 130, 246, 0.06);
    margin-top: 8px;
}

.mitigation-title {
    font-size: 1.55rem;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 16px;
}

.mitigasi-item {
    display: flex;
    gap: 14px;
    align-items: flex-start;
    margin-bottom: 14px;
    padding: 12px 14px;
    border-radius: 16px;
    background: #ffffff;
    border: 1px solid #e2e8f0;
}

.mitigasi-bullet {
    min-width: 42px;
    height: 42px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.2rem;
    background: #dbeafe;
}

.mitigasi-content {
    color: #475569;
    line-height: 1.7;
}

.mitigasi-content b {
    color: #1e3a8a;
}

.fact-box {
    background: linear-gradient(135deg, #eff6ff, #ffffff);
    border: 1px solid #bfdbfe;
    border-radius: 20px;
    padding: 18px 20px;
    margin-top: 18px;
    color: #334155;
    line-height: 1.7;
}

@keyframes rotateWave {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

@keyframes pulseEpicenter {
    0% { box-shadow: 0 0 0 0 rgba(249, 115, 22, 0.65); }
    70% { box-shadow: 0 0 0 24px rgba(249, 115, 22, 0); }
    100% { box-shadow: 0 0 0 0 rgba(249, 115, 22, 0); }
}
</style>
""", unsafe_allow_html=True)

left, right = st.columns([1.3, 1])

with left:
    st.markdown("""
    <div class="knowledge-hero">
        <div class="knowledge-title">Memahami Gempa Bumi dengan Lebih Sederhana</div>
        <div class="knowledge-desc">
            Gempa bumi adalah salah satu bencana yang paling sering terjadi di Indonesia.
            Memahami konsep dasarnya akan membantu masyarakat lebih siap dalam menghadapi risiko,
            mengenali istilah penting, dan melakukan mitigasi dengan benar.
        </div>
        <div style="margin-top:16px;">
            <span class="floating-badge">🌍 Indonesia Rawan Gempa</span>
            <span class="floating-badge">📚 Edukasi Dasar</span>
            <span class="floating-badge">🛡️ Mitigasi</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with right:
    st.markdown("""
    <div class="hero-illustration">
        <div class="wave"></div>
        <div class="wave two"></div>
        <div class="wave three"></div>
        <div class="ring r1"></div>
        <div class="ring r2"></div>
        <div class="ring r3"></div>
        <div class="epicenter"></div>
        <div class="mountain m1"></div>
        <div class="mountain m2"></div>
        <div class="mountain m3"></div>
    </div>
    """, unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    st.markdown("""
    <div class="info-card">
        <div class="info-icon">🌐</div>
        <div class="info-heading">Apa itu gempa bumi?</div>
        <div class="info-text">
            Gempa bumi adalah getaran atau guncangan pada permukaan bumi akibat pelepasan energi
            dari dalam bumi. Energi ini kemudian merambat dalam bentuk gelombang seismik dan
            dirasakan sebagai getaran di permukaan.
        </div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="info-card">
        <div class="info-icon">📖</div>
        <div class="info-heading">Istilah penting</div>
        <div class="info-text">
            <b>Magnitudo</b> adalah ukuran energi gempa.<br>
            <b>Intensitas</b> adalah tingkat guncangan yang dirasakan.<br>
            <b>Episentrum</b> adalah titik di permukaan bumi tepat di atas sumber gempa.<br>
            <b>Hiposentrum</b> adalah sumber gempa di dalam bumi.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="mitigation-box">', unsafe_allow_html=True)
st.markdown('<div class="mitigation-title">Mitigasi Dasar Gempa Bumi</div>', unsafe_allow_html=True)

st.markdown("""
<div class="mitigasi-item">
    <div class="mitigasi-bullet">🎒</div>
    <div class="mitigasi-content">
        <b>Sebelum gempa</b><br>
        Siapkan tas siaga, kenali jalur evakuasi, dan pastikan barang berat di rumah lebih aman.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="mitigasi-item">
    <div class="mitigasi-bullet">🧎</div>
    <div class="mitigasi-content">
        <b>Saat gempa</b><br>
        Lakukan <i>drop, cover, hold on</i>, jauhi kaca, dan lindungi kepala dari benda yang bisa jatuh.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="mitigasi-item">
    <div class="mitigasi-bullet">🚶</div>
    <div class="mitigasi-content">
        <b>Setelah gempa</b><br>
        Evakuasi ke area aman, waspadai gempa susulan, dan ikuti informasi resmi dari instansi berwenang.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("""
<div class="fact-box">
    <b>Catatan penting:</b> edukasi gempa bumi tidak hanya membantu memahami penyebab dan dampaknya,
    tetapi juga meningkatkan kesiapsiagaan masyarakat dalam mengurangi risiko korban dan kerusakan.
</div>
""", unsafe_allow_html=True)

render_footer()