import streamlit as st

def inject_global_css():
    st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-family: 'Segoe UI', sans-serif;
        background-color: #f8fafc;
    }

    .block-container {
        padding-top: 2.5rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    /* =========================
       SIDEBAR
    ========================= */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #eaf2ff 0%, #dbeafe 100%);
        border-right: 1px solid #cbd5e1;
    }

    section[data-testid="stSidebar"] * {
        color: #0f172a !important;
    }

    section[data-testid="stSidebar"] .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .sidebar-brand {
        background: rgba(255,255,255,0.75);
        border: 1px solid #bfdbfe;
        border-radius: 18px;
        padding: 18px 16px;
        margin-bottom: 18px;
        box-shadow: 0 8px 20px rgba(59, 130, 246, 0.12);
    }

    .sidebar-brand h2 {
        margin: 0;
        font-size: 1.15rem;
        font-weight: 800;
        color: #1e3a8a !important;
        line-height: 1.4;
    }

    .sidebar-brand p {
        margin-top: 8px;
        margin-bottom: 0;
        font-size: 0.88rem;
        color: #334155 !important;
        line-height: 1.5;
    }

    .sidebar-section-title {
        font-size: 0.82rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #2563eb !important;
        margin-top: 0.5rem;
        margin-bottom: 0.5rem;
    }

    .sidebar-note {
        background: rgba(255,255,255,0.7);
        border-left: 4px solid #3b82f6;
        border-radius: 14px;
        padding: 12px 14px;
        margin-top: 18px;
        font-size: 0.86rem;
        color: #1e293b !important;
        line-height: 1.5;
    }

    /* =========================
       HEADER
    ========================= */
    .page-header {
        background: linear-gradient(135deg, #60a5fa, #93c5fd);
        color: white;
        padding: 34px 42px;
        border-radius: 0;
        margin-top: -2.5rem;
        margin-left: -2rem;
        margin-right: -2rem;
        margin-bottom: 24px;
        box-shadow: 0 8px 20px rgba(59, 130, 246, 0.18);
    }

    .page-header h1 {
        margin: 0;
        font-size: 2.2rem;
        font-weight: 800;
        color: white;
    }

    .page-header p {
        margin-top: 10px;
        margin-bottom: 0;
        font-size: 1.05rem;
        color: #eff6ff;
        line-height: 1.6;
    }

    /* =========================
       CONTENT CARDS
    ========================= */
    .section-box {
        background: white;
        border-radius: 18px;
        padding: 18px 20px;
        box-shadow: 0 4px 14px rgba(15, 23, 42, 0.06);
        border: 1px solid #e2e8f0;
        margin-bottom: 18px;
    }

    .section-box h4 {
        margin-top: 0;
        margin-bottom: 10px;
        color: #0f172a;
    }

    .section-box p {
        margin-bottom: 0;
        color: #475569;
        line-height: 1.6;
    }

    /* =========================
       FOOTER
    ========================= */
    .footer {
        margin-top: 40px;
        background: #eaf2ff;
        color: #334155;
        padding: 22px 28px;
        border-radius: 18px;
        text-align: center;
        font-size: 0.92rem;
        line-height: 1.6;
        border: 1px solid #bfdbfe;
    }

    .footer strong {
        color: #1e3a8a;
    }
    </style>
    """, unsafe_allow_html=True)


def render_sidebar():
    with st.sidebar:
        st.markdown("""
        <div class="sidebar-brand">
            <h2>🌍 Earthquake Portal</h2>
            <p>
                Portal informasi dan analitik gempa bumi Indonesia
                dengan studi kasus utama Cianjur, Jawa Barat.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="sidebar-section-title">Navigasi</div>', unsafe_allow_html=True)

        st.markdown("""
        <div class="sidebar-note">
            Gunakan menu di bawah untuk berpindah antar halaman portal.
        </div>
        """, unsafe_allow_html=True)


def render_header(title: str, description: str):
    st.markdown(f"""
    <div class="page-header">
        <h1>{title}</h1>
        <p>{description}</p>
    </div>
    """, unsafe_allow_html=True)


def render_footer():
    st.markdown("""
    <div class="footer">
        <strong>Earthquake Disaster Intelligence Platform</strong><br>
        Portal informasi dan analitik gempa bumi berbasis web<br>
        Studi kasus: Cianjur, Jawa Barat<br>
        Dikembangkan untuk edukasi, pemetaan kerentanan, klasifikasi kerusakan,
        dan rekomendasi rehabilitasi–rekonstruksi.
    </div>
    """, unsafe_allow_html=True)