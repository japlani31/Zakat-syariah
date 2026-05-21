import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Zakat Maal & Perdagangan", page_icon="🌾", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Amiri:wght@400;700&display=swap');
html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; }
.stApp { background: linear-gradient(160deg, #0a1628, #0d2137, #0a1f1a); }
section[data-testid="stSidebar"] { background: rgba(255,255,255,0.03) !important; border-right: 1px solid rgba(255,255,255,0.07); }
section[data-testid="stSidebar"] * { color: #d4af7a !important; }
h1,h2,h3 { color: white !important; }
p, li, label { color: rgba(255,255,255,0.8) !important; }
.stTextInput input, .stNumberInput input {
    background: #ffffff !important; color: #111111 !important;
    border: 1.5px solid rgba(212,175,122,0.4) !important; border-radius: 8px !important; font-weight: 500 !important;
}
div[data-baseweb="select"] > div { background: #ffffff !important; color: #111111 !important; border-radius: 8px !important; }
div[data-baseweb="select"] * { color: #111111 !important; }
div[data-baseweb="popover"] li { color: #111111 !important; background: #fff !important; }
div[data-baseweb="popover"] li:hover { background: #f5f0e8 !important; }
.section-title { font-size:1.3rem; font-weight:800; color:white; margin:1.5rem 0 0.75rem; padding-bottom:0.5rem; border-bottom:2px solid rgba(212,175,122,0.4); }
.result-card { background:rgba(212,175,122,0.1); border:1px solid rgba(212,175,122,0.35); border-radius:16px; padding:1.25rem; text-align:center; }
.result-val { font-size:1.5rem; font-weight:800; color:#d4af7a; }
.result-lbl { font-size:0.78rem; color:rgba(255,255,255,0.5); margin-top:0.2rem; }
.wajib-box { background:rgba(72,199,142,0.1); border:1px solid rgba(72,199,142,0.35); border-radius:12px; padding:1.25rem; margin:0.5rem 0; }
.tidak-box { background:rgba(249,199,79,0.1); border:1px solid rgba(249,199,79,0.35); border-radius:12px; padding:1.25rem; margin:0.5rem 0; }
.info-card { background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.09); border-radius:12px; padding:1rem 1.25rem; margin-bottom:0.75rem; }
.stButton button { background:linear-gradient(90deg,#d4af7a,#48c78e) !important; color:#0a1628 !important; font-weight:700 !important; border:none !important; border-radius:10px !important; padding:0.6rem 2rem !important; font-size:1rem !important; }
.arabic { font-family:'Amiri',serif; font-size:1.1rem; color:#d4af7a; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p style="font-family:sans-serif;font-size:2rem;font-weight:800;background:linear-gradient(90deg,#d4af7a,#48c78e);-webkit-background-clip:text;-webkit-text-fill-color:transparent">🌾 Kalkulator Zakat Maal & Perdagangan</p>', unsafe_allow_html=True)
st.markdown('<p class="arabic">وَأَقِيمُوا الصَّلَاةَ وَآتُوا الزَّكَاةَ — "Dan dirikanlah sholat dan tunaikanlah zakat" (QS. Al-Baqarah: 43)</p>', unsafe_allow_html=True)
st.markdown("---")

# ── NISAB REFERENSI ─────────────────────────────────────────────
st.markdown('<div class="section-title">⚖️ Referensi Nisab Terkini</div>', unsafe_allow_html=True)
st.markdown('<p style="font-size:0.85rem;color:rgba(255,255,255,0.5)">Sesuaikan dengan harga emas terkini. Nilai default adalah estimasi — selalu cek ke BAZNAS atau LAZ setempat.</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    harga_emas = st.number_input("Harga Emas per Gram (Rp)", min_value=100000, value=1150000, step=10000, format="%d",
        help="Cek harga emas terkini di logammulia.com atau BAZNAS")
with col2:
    nisab_emas_gram = 85  # standar 85 gram emas
    nisab_maal = harga_emas * nisab_emas_gram
    st.markdown(f"""<div class="result-card" style="margin-top:1.8rem">
        <div class="result-val">Rp {nisab_maal:,.0f}</div>
        <div class="result-lbl">Nisab Zakat Maal (85 gram emas)</div>
    </div>""", unsafe_allow_html=True)
with col3:
    nisab_perdagangan = nisab_maal
    st.markdown(f"""<div class="result-card" style="margin-top:1.8rem">
        <div class="result-val">Rp {nisab_perdagangan:,.0f}</div>
        <div class="result-lbl">Nisab Zakat Perdagangan</div>
    </div>""", unsafe_allow_html=True)

# ── TABS ─────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs(["💰 Zakat Maal (Harta)", "🏪 Zakat Perdagangan", "🏦 Zakat Tabungan", "📚 Panduan & Dalil"])

# ── TAB 1: ZAKAT MAAL ────────────────────────────────────────────
with tab1:
    st.markdown('<div class="section-title">💰 Kalkulator Zakat Maal (Harta Kekayaan)</div>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:0.85rem;color:rgba(255,255,255,0.5)">Zakat Maal wajib atas harta yang telah mencapai nisab dan haul (tersimpan 1 tahun penuh). Tarif: 2.5%</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Harta Lancar**")
        uang_tunai     = st.number_input("Uang Tunai & Tabungan (Rp)", min_value=0, value=5000000, step=500000, format="%d")
        investasi      = st.number_input("Investasi (saham, reksa dana, dll) (Rp)", min_value=0, value=2000000, step=500000, format="%d")
        piutang_lancar = st.number_input("Piutang yang Bisa Ditagih (Rp)", min_value=0, value=1000000, step=500000, format="%d")
        emas_perak     = st.number_input("Emas & Perak (nilai rupiah) (Rp)", min_value=0, value=0, step=500000, format="%d")
    with col2:
        st.markdown("**Harta Bisnis**")
        stok_barang    = st.number_input("Stok Barang Dagangan (Rp)", min_value=0, value=3000000, step=500000, format="%d")
        aset_bisnis    = st.number_input("Aset Bisnis Produktif (Rp)", min_value=0, value=0, step=500000, format="%d")
        penghasilan_lain = st.number_input("Penghasilan Lain-lain (Rp)", min_value=0, value=0, step=500000, format="%d")
        hutang_jatuh_tempo = st.number_input("Hutang Jatuh Tempo (pengurang) (Rp)", min_value=0, value=500000, step=500000, format="%d",
            help="Hutang yang harus dibayar dalam waktu dekat — boleh dikurangkan dari harta")

    if st.button("Hitung Zakat Maal", key="btn_maal"):
        total_harta = uang_tunai + investasi + piutang_lancar + emas_perak + stok_barang + aset_bisnis + penghasilan_lain
        harta_bersih = total_harta - hutang_jatuh_tempo
        zakat_maal = harta_bersih * 0.025
        sudah_haul = harta_bersih >= nisab_maal

        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f'<div class="result-card"><div class="result-val">Rp {total_harta:,.0f}</div><div class="result-lbl">Total Harta Kotor</div></div>', unsafe_allow_html=True)
        with col2:
            st.markdown(f'<div class="result-card"><div class="result-val">Rp {harta_bersih:,.0f}</div><div class="result-lbl">Harta Bersih (setelah hutang)</div></div>', unsafe_allow_html=True)
        with col3:
            st.markdown(f'<div class="result-card"><div class="result-val" style="color:#48c78e">Rp {zakat_maal:,.0f}</div><div class="result-lbl">Zakat yang Wajib Dibayar (2.5%)</div></div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        if sudah_haul:
            st.markdown(f"""<div class="wajib-box">
                ✅ <strong>WAJIB ZAKAT</strong> — Harta bersih Anda (Rp {harta_bersih:,.0f}) telah mencapai/melebihi nisab (Rp {nisab_maal:,.0f})<br>
                💰 Zakat yang harus dibayarkan: <strong style="color:#48c78e">Rp {zakat_maal:,.0f}</strong><br>
                📅 Pastikan harta ini sudah tersimpan selama <strong>1 tahun (haul)</strong> sebelum berzakat.<br>
                🏦 Salurkan melalui BAZNAS, LAZ terpercaya, atau langsung kepada mustahiq.
            </div>""", unsafe_allow_html=True)
        else:
            selisih = nisab_maal - harta_bersih
            st.markdown(f"""<div class="tidak-box">
                🟡 <strong>BELUM WAJIB ZAKAT</strong> — Harta bersih belum mencapai nisab.<br>
                Kekurangan: <strong>Rp {selisih:,.0f}</strong> lagi untuk mencapai nisab.<br>
                💡 Anda tetap dianjurkan bersedekah dan berinfaq meski belum wajib zakat.
            </div>""", unsafe_allow_html=True)

        # Pie chart komposisi harta
        labels_h = ["Uang & Tabungan","Investasi","Piutang","Emas/Perak","Stok Barang","Aset Bisnis","Lain-lain"]
        values_h = [uang_tunai, investasi, piutang_lancar, emas_perak, stok_barang, aset_bisnis, penghasilan_lain]
        labels_h = [l for l, v in zip(labels_h, values_h) if v > 0]
        values_h = [v for v in values_h if v > 0]
        if values_h:
            fig = go.Figure(go.Pie(labels=labels_h, values=values_h, hole=0.45,
                marker_colors=["#d4af7a","#48c78e","#90e0ef","#f9c74f","#c77dff","#f3722c","#adb5bd"]))
            fig.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)",
                title=dict(text="Komposisi Harta", font=dict(color="white")),
                font=dict(color="white"), height=350)
            st.plotly_chart(fig, use_container_width=True)

# ── TAB 2: ZAKAT PERDAGANGAN ────────────────────────────────────
with tab2:
    st.markdown('<div class="section-title">🏪 Kalkulator Zakat Perdagangan (Bisnis)</div>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:0.85rem;color:rgba(255,255,255,0.5)">Zakat perdagangan dihitung dari aset lancar bisnis dikurangi kewajiban jangka pendek, jika mencapai nisab setelah 1 tahun. Tarif: 2.5%</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Aset Lancar Bisnis**")
        kas_bisnis     = st.number_input("Kas & Bank Bisnis (Rp)", min_value=0, value=10000000, step=500000, format="%d")
        piutang_bisnis = st.number_input("Piutang Dagang (Rp)", min_value=0, value=5000000, step=500000, format="%d")
        stok_bisnis    = st.number_input("Nilai Stok/Persediaan (Rp)", min_value=0, value=8000000, step=500000, format="%d")
        aset_lancar_lain = st.number_input("Aset Lancar Lain (Rp)", min_value=0, value=0, step=500000, format="%d")
    with col2:
        st.markdown("**Kewajiban / Hutang Bisnis**")
        hutang_dagang  = st.number_input("Hutang Dagang (Rp)", min_value=0, value=3000000, step=500000, format="%d")
        hutang_bank    = st.number_input("Cicilan Bank/Pinjaman Jatuh Tempo (Rp)", min_value=0, value=2000000, step=500000, format="%d")
        kewajiban_lain = st.number_input("Kewajiban Lain Jatuh Tempo (Rp)", min_value=0, value=0, step=500000, format="%d")

    if st.button("Hitung Zakat Perdagangan", key="btn_dagang"):
        total_aset     = kas_bisnis + piutang_bisnis + stok_bisnis + aset_lancar_lain
        total_kwjb     = hutang_dagang + hutang_bank + kewajiban_lain
        harta_dagang   = total_aset - total_kwjb
        zakat_dagang   = harta_dagang * 0.025 if harta_dagang >= nisab_perdagangan else 0

        col1, col2, col3, col4 = st.columns(4)
        for col, (val, lbl) in zip([col1,col2,col3,col4], [
            (f"Rp {total_aset:,.0f}", "Total Aset Lancar"),
            (f"Rp {total_kwjb:,.0f}", "Total Kewajiban"),
            (f"Rp {harta_dagang:,.0f}", "Harta Dagang Bersih"),
            (f"Rp {zakat_dagang:,.0f}", "Zakat Wajib (2.5%)"),
        ]):
            with col:
                st.markdown(f'<div class="result-card"><div class="result-val">{val}</div><div class="result-lbl">{lbl}</div></div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        if harta_dagang >= nisab_perdagangan:
            st.markdown(f"""<div class="wajib-box">
                ✅ <strong>WAJIB ZAKAT PERDAGANGAN</strong><br>
                Harta dagang bersih Rp {harta_dagang:,.0f} ≥ Nisab Rp {nisab_perdagangan:,.0f}<br>
                💰 Zakat yang harus dibayar: <strong style="color:#48c78e">Rp {zakat_dagang:,.0f}</strong><br>
                📅 Dihitung pada akhir haul (satu tahun penuh berputar dalam bisnis).
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown(f"""<div class="tidak-box">
                🟡 Harta dagang bersih belum mencapai nisab (Rp {nisab_perdagangan:,.0f}).<br>
                Kurang: Rp {nisab_perdagangan - harta_dagang:,.0f} lagi.
            </div>""", unsafe_allow_html=True)

# ── TAB 3: ZAKAT TABUNGAN ───────────────────────────────────────
with tab3:
    st.markdown('<div class="section-title">🏦 Kalkulator Zakat Tabungan & Deposito</div>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:0.85rem;color:rgba(255,255,255,0.5)">Tabungan yang tersimpan ≥ 1 tahun dan mencapai nisab wajib dizakati. Tarif: 2.5%. Bunga bank konvensional bukan objek zakat — melainkan bisa disalurkan sebagai sedekah.</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        saldo_awal    = st.number_input("Saldo Awal Tahun (Rp)", min_value=0, value=15000000, step=500000, format="%d")
        saldo_akhir   = st.number_input("Saldo Akhir Tahun / Saat Ini (Rp)", min_value=0, value=18000000, step=500000, format="%d")
        deposito      = st.number_input("Deposito Syariah (pokok saja) (Rp)", min_value=0, value=0, step=500000, format="%d")
    with col2:
        metode_tab = st.selectbox("Metode Perhitungan", ["Saldo Terendah (Konservatif)", "Saldo Akhir Tahun (Umum)"])
        bunga_riba = st.number_input("Bunga/Riba Diterima (bukan objek zakat) (Rp)", min_value=0, value=0, step=100000, format="%d",
            help="Bunga bank konvensional — disalurkan sebagai sedekah, bukan zakat")

    if st.button("Hitung Zakat Tabungan", key="btn_tab"):
        dasar_tab = (min(saldo_awal, saldo_akhir) if "Terendah" in metode_tab else saldo_akhir) + deposito
        zakat_tab = dasar_tab * 0.025 if dasar_tab >= nisab_maal else 0

        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f'<div class="result-card"><div class="result-val">Rp {dasar_tab:,.0f}</div><div class="result-lbl">Dasar Perhitungan Zakat</div></div>', unsafe_allow_html=True)
        with col2:
            st.markdown(f'<div class="result-card"><div class="result-val" style="color:#48c78e">Rp {zakat_tab:,.0f}</div><div class="result-lbl">Zakat Tabungan (2.5%)</div></div>', unsafe_allow_html=True)
        with col3:
            st.markdown(f'<div class="result-card"><div class="result-val" style="color:#f9c74f">Rp {bunga_riba:,.0f}</div><div class="result-lbl">Bunga Riba → Sedekah</div></div>', unsafe_allow_html=True)

        if dasar_tab >= nisab_maal:
            st.markdown(f"""<div class="wajib-box">
                ✅ <strong>WAJIB ZAKAT TABUNGAN</strong><br>
                Zakat: <strong style="color:#48c78e">Rp {zakat_tab:,.0f}</strong><br>
                {"⚠️ Bunga riba Rp " + f"{bunga_riba:,.0f}" + " — haram dikonsumsi, salurkan sebagai sedekah (bukan zakat)." if bunga_riba > 0 else ""}
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="tidak-box">🟡 Belum wajib zakat. Kurang Rp {nisab_maal-dasar_tab:,.0f} dari nisab.</div>', unsafe_allow_html=True)

# ── TAB 4: PANDUAN & DALIL ──────────────────────────────────────
with tab4:
    st.markdown('<div class="section-title">📚 Panduan & Dalil Zakat Maal</div>', unsafe_allow_html=True)
    panduan = [
        ("📖 Dalil Al-Qur'an", "QS. At-Taubah: 103 — \"Ambillah zakat dari sebagian harta mereka, dengan zakat itu kamu membersihkan dan menyucikan mereka.\"", "#d4af7a"),
        ("⚖️ Nisab", "Nisab zakat maal = 85 gram emas murni. Jika total harta bersih ≥ nisab dan sudah 1 tahun (haul), wajib zakat.", "#48c78e"),
        ("📅 Haul", "Haul adalah syarat harta telah dimiliki selama 1 tahun hijriyah (354 hari). Untuk zakat perdagangan, dihitung sejak usaha berjalan.", "#90e0ef"),
        ("💸 Tarif Zakat", "Tarif zakat maal & perdagangan: 2.5% dari harta/aset bersih yang memenuhi nisab dan haul.", "#f9c74f"),
        ("🏦 Penyaluran", "Salurkan melalui: BAZNAS (Badan Amil Zakat Nasional), LAZ resmi, atau langsung kepada 8 asnaf mustahiq.", "#c77dff"),
        ("❌ Harta Dikurangi", "Hutang yang jatuh tempo boleh dikurangi dari harta sebelum dihitung nisab dan zakatnya.", "#f3722c"),
    ]
    for title, desc, color in panduan:
        st.markdown(f"""<div class="info-card" style="border-left:3px solid {color}">
            <div style="color:{color};font-weight:700;margin-bottom:0.3rem">{title}</div>
            <div style="color:rgba(255,255,255,0.7);font-size:0.88rem">{desc}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("""<div style="background:rgba(212,175,122,0.08);border:1px solid rgba(212,175,122,0.2);border-radius:12px;padding:1rem 1.25rem;margin-top:1rem">
        <p style="margin:0;font-size:0.85rem;color:rgba(255,255,255,0.6)">
        ⚠️ <strong style="color:#d4af7a">Disclaimer:</strong> Kalkulator ini bersifat edukatif. 
        Untuk keputusan zakat yang lebih akurat, konsultasikan dengan BAZNAS, MUI, atau ulama setempat. 
        Harga emas dan nisab dapat berubah — selalu cek harga terkini.
        </p>
    </div>""", unsafe_allow_html=True)
