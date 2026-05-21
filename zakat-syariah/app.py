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

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""<div style="text-align:center;color:rgba(255,255,255,0.25);font-size:0.78rem;border-top:1px solid rgba(255,255,255,0.07);padding-top:1rem">
    ZakatKu · Prodi S1 Kewirausahaan · Universitas Muhammadiyah Metro · 
    <em>Nisab mengacu pada harga emas/perak terkini — selalu verifikasi ke lembaga zakat resmi (BAZNAS)</em>
</div>""", unsafe_allow_html=True)
