import streamlit as st

st.set_page_config(
    page_title="ZakatKu — Keuangan Syariah",
    page_icon="☪️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Amiri:wght@400;700&display=swap');
html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; }
.stApp { background: linear-gradient(160deg, #0a1628 0%, #0d2137 40%, #0a1f1a 100%); min-height: 100vh; }
section[data-testid="stSidebar"] { background: rgba(255,255,255,0.03) !important; border-right: 1px solid rgba(255,255,255,0.07); }
section[data-testid="stSidebar"] * { color: #d4af7a !important; }
h1,h2,h3 { color: white !important; }
p, li { color: rgba(255,255,255,0.75) !important; }

/* INPUT HITAM */
.stTextInput input, .stNumberInput input, .stTextArea textarea {
    background: #ffffff !important; color: #111111 !important;
    border: 1.5px solid rgba(212,175,122,0.4) !important; border-radius: 8px !important; font-weight: 500 !important;
}
div[data-baseweb="select"] > div { background: #ffffff !important; color: #111111 !important; border-radius: 8px !important; }
div[data-baseweb="select"] * { color: #111111 !important; }
div[data-baseweb="popover"] li { color: #111111 !important; background: #ffffff !important; }
div[data-baseweb="popover"] li:hover { background: #f5f0e8 !important; }

.hero-wrap {
    background: linear-gradient(135deg, rgba(212,175,122,0.12), rgba(34,139,74,0.08));
    border: 1px solid rgba(212,175,122,0.25);
    border-radius: 24px; padding: 2.5rem 2rem; margin-bottom: 2rem;
}
.arabic-text { font-family: 'Amiri', serif; font-size: 1.8rem; color: #d4af7a; text-align: center; margin-bottom: 0.25rem; }
.hero-title { font-size: 2.6rem; font-weight: 800; background: linear-gradient(90deg, #d4af7a, #48c78e, #d4af7a); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.hero-sub { color: rgba(255,255,255,0.6); font-size: 1rem; margin-top: 0.4rem; }
.badge { display:inline-block; background:rgba(212,175,122,0.15); border:1px solid rgba(212,175,122,0.4); color:#d4af7a; border-radius:20px; padding:0.2rem 0.9rem; font-size:0.78rem; font-weight:700; letter-spacing:1px; text-transform:uppercase; margin-bottom:0.75rem; }
.menu-card { background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.09); border-radius: 16px; padding: 1.5rem; text-align: center; transition: all 0.3s; }
.menu-icon { font-size: 2.5rem; margin-bottom: 0.5rem; }
.menu-title { color: white; font-weight: 700; font-size: 1rem; }
.menu-desc { color: rgba(255,255,255,0.5); font-size: 0.82rem; margin-top: 0.3rem; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-wrap">
    <div class="arabic-text">بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ</div>
    <p style="text-align:center;color:rgba(212,175,122,0.7);font-size:0.85rem;margin-bottom:1.5rem">Dengan menyebut nama Allah Yang Maha Pengasih lagi Maha Penyayang</p>
    <div style="text-align:center">
        <div class="badge">☪️ Universitas Muhammadiyah Metro</div>
        <div class="hero-title">ZakatKu — Keuangan Syariah</div>
        <div class="hero-sub">Platform kalkulator zakat, akad syariah & perencanaan keuangan islami untuk mahasiswa kewirausahaan</div>
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
menus = [
    ("🌾", "Zakat Maal & Perdagangan", "Hitung zakat harta, tabungan, dan bisnis"),
    ("💼", "Zakat Penghasilan", "Kalkulator zakat profesi & gaji"),
    ("🤝", "Akad Bisnis Syariah", "Panduan Mudharabah, Musyarakah, Murabahah"),
    ("📊", "Laporan Keuangan Islami", "Laporan laba-rugi berbasis prinsip syariah"),
]
for col, (icon, title, desc) in zip([col1,col2,col3,col4], menus):
    with col:
        st.markdown(f"""<div class="menu-card">
            <div class="menu-icon">{icon}</div>
            <div class="menu-title">{title}</div>
            <div class="menu-desc">{desc}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""<div style="background:rgba(212,175,122,0.08);border:1px solid rgba(212,175,122,0.25);border-radius:12px;padding:1rem 1.5rem">
    <p style="margin:0;color:rgba(255,255,255,0.8)">👈 <strong style="color:#d4af7a">Pilih menu di sidebar kiri</strong> untuk mulai menggunakan fitur kalkulator zakat dan keuangan syariah.</p>
</div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div style="
    background: linear-gradient(135deg, rgba(249,199,79,0.13), rgba(249,115,22,0.10));
    border: 2px solid rgba(249,199,79,0.55);
    border-radius: 16px;
    padding: 1.6rem 1.8rem;
    margin-bottom: 1.5rem;
">
    <div style="display:flex; align-items:center; gap:0.6rem; margin-bottom:0.9rem;">
        <span style="font-size:1.5rem">⚠️</span>
        <span style="font-size:1.15rem; font-weight:800; color:#f9c74f; letter-spacing:0.5px;">DISCLAIMER — Penting untuk Dibaca</span>
    </div>
    <p style="color:#ffffff; font-size:0.97rem; font-weight:600; margin:0 0 0.9rem 0; line-height:1.6;">
        Aplikasi ini bersifat <strong style="color:#f9c74f">EDUKATIF</strong> untuk mahasiswa kewirausahaan.
        Perhitungan yang ditampilkan merupakan panduan umum dan <u>tidak menggantikan fatwa atau keputusan resmi lembaga zakat</u>.
    </p>
    <p style="color:#f0e6cc; font-size:0.93rem; font-weight:600; margin:0 0 0.6rem 0;">
        Untuk keputusan zakat yang sah, selalu konsultasikan dengan:
    </p>
    <div style="display:flex; flex-direction:column; gap:0.5rem;">
        <div style="display:flex; align-items:center; gap:0.75rem; background:rgba(255,255,255,0.07); border-radius:10px; padding:0.6rem 1rem;">
            <span style="font-size:1.2rem">🏛️</span>
            <div>
                <div style="color:#ffffff; font-weight:700; font-size:0.92rem;">BAZNAS — Badan Amil Zakat Nasional</div>
                <div style="color:rgba(255,255,255,0.6); font-size:0.80rem;">baznas.go.id · Lembaga resmi negara pengelola zakat</div>
            </div>
        </div>
        <div style="display:flex; align-items:center; gap:0.75rem; background:rgba(255,255,255,0.07); border-radius:10px; padding:0.6rem 1rem;">
            <span style="font-size:1.2rem">📜</span>
            <div>
                <div style="color:#ffffff; font-weight:700; font-size:0.92rem;">Majelis Ulama Indonesia (MUI)</div>
                <div style="color:rgba(255,255,255,0.6); font-size:0.80rem;">mui.or.id · Rujukan fatwa dan hukum Islam di Indonesia</div>
            </div>
        </div>
        <div style="display:flex; align-items:center; gap:0.75rem; background:rgba(255,255,255,0.07); border-radius:10px; padding:0.6rem 1rem;">
            <span style="font-size:1.2rem">🕌</span>
            <div>
                <div style="color:#ffffff; font-weight:700; font-size:0.92rem;">Ulama atau Ustadz Terpercaya Setempat</div>
                <div style="color:rgba(255,255,255,0.6); font-size:0.80rem;">Termasuk dosen atau pembimbing syariah di lingkungan UM Metro</div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""<div style="text-align:center;color:rgba(255,255,255,0.3);font-size:0.78rem;border-top:1px solid rgba(255,255,255,0.07);padding-top:1rem">
    ZakatKu · Prodi S1 Kewirausahaan · Universitas Muhammadiyah Metro ·
    <em>Nisab mengacu pada harga emas terkini — selalu verifikasi ke lembaga zakat resmi</em>
</div>""", unsafe_allow_html=True)
