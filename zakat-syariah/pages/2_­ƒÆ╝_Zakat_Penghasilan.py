import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Zakat Penghasilan", page_icon="💼", layout="wide")

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
.result-val { font-size:1.4rem; font-weight:800; color:#d4af7a; }
.result-lbl { font-size:0.78rem; color:rgba(255,255,255,0.5); margin-top:0.2rem; }
.wajib-box { background:rgba(72,199,142,0.1); border:1px solid rgba(72,199,142,0.35); border-radius:12px; padding:1.25rem; margin:0.5rem 0; }
.tidak-box { background:rgba(249,199,79,0.1); border:1px solid rgba(249,199,79,0.35); border-radius:12px; padding:1.25rem; margin:0.5rem 0; }
.info-card { background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.09); border-radius:12px; padding:1rem 1.25rem; margin-bottom:0.75rem; }
.stButton button { background:linear-gradient(90deg,#d4af7a,#48c78e) !important; color:#0a1628 !important; font-weight:700 !important; border:none !important; border-radius:10px !important; padding:0.6rem 2rem !important; font-size:1rem !important; }
.arabic { font-family:'Amiri',serif; font-size:1.1rem; color:#d4af7a; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p style="font-size:2rem;font-weight:800;background:linear-gradient(90deg,#d4af7a,#48c78e);-webkit-background-clip:text;-webkit-text-fill-color:transparent">💼 Kalkulator Zakat Penghasilan & Profesi</p>', unsafe_allow_html=True)
st.markdown('<p class="arabic">خُذْ مِنْ أَمْوَالِهِمْ صَدَقَةً تُطَهِّرُهُمْ — "Ambillah dari harta mereka sedekah (zakat) yang membersihkan mereka" (QS. At-Taubah: 103)</p>', unsafe_allow_html=True)
st.markdown("---")

# ── NISAB PENGHASILAN ────────────────────────────────────────────
st.markdown('<div class="section-title">⚖️ Nisab Zakat Penghasilan</div>', unsafe_allow_html=True)
st.markdown('<p style="font-size:0.85rem;color:rgba(255,255,255,0.5)">Nisab zakat penghasilan = 520 kg beras atau setara 85 gram emas per tahun (para ulama berbeda pendapat — ini menggunakan pendapat mayoritas/BAZNAS)</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    harga_beras = st.number_input("Harga Beras per Kg (Rp)", min_value=5000, value=13000, step=500, format="%d")
with col2:
    nisab_beras  = 520 * harga_beras
    st.markdown(f"""<div class="result-card" style="margin-top:1.8rem">
        <div class="result-val">Rp {nisab_beras:,.0f}/tahun</div>
        <div class="result-lbl">Nisab (520 kg beras × Rp {harga_beras:,})</div>
    </div>""", unsafe_allow_html=True)
with col3:
    nisab_per_bulan = nisab_beras / 12
    st.markdown(f"""<div class="result-card" style="margin-top:1.8rem">
        <div class="result-val">Rp {nisab_per_bulan:,.0f}/bulan</div>
        <div class="result-lbl">Setara per Bulan</div>
    </div>""", unsafe_allow_html=True)

st.markdown("---")

tab1, tab2, tab3 = st.tabs(["👔 Karyawan / Profesional", "🏢 Pengusaha / Wirausaha", "📊 Perbandingan Metode"])

# ── TAB 1: KARYAWAN ──────────────────────────────────────────────
with tab1:
    st.markdown('<div class="section-title">👔 Zakat Penghasilan Karyawan & Profesional</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Pemasukan**")
        gaji_pokok     = st.number_input("Gaji Pokok per Bulan (Rp)", min_value=0, value=5000000, step=500000, format="%d")
        tunjangan      = st.number_input("Tunjangan (transport, makan, dll) (Rp)", min_value=0, value=1000000, step=100000, format="%d")
        honor_lain     = st.number_input("Honor / Penghasilan Lain (Rp/bulan)", min_value=0, value=500000, step=100000, format="%d")
    with col2:
        st.markdown("**Pengeluaran Wajib (boleh dikurangkan)**")
        biaya_hidup    = st.number_input("Kebutuhan Pokok Keluarga (Rp/bulan)", min_value=0, value=2000000, step=100000, format="%d",
            help="Makan, listrik, air, transport wajib — kebutuhan dasar yang tidak bisa dihindari")
        cicilan        = st.number_input("Cicilan Hutang (KPR, motor, dll) (Rp/bulan)", min_value=0, value=500000, step=100000, format="%d")
        metode_gaji = st.selectbox("Metode Perhitungan", [
            "Bruto (dari total penghasilan)",
            "Netto (setelah dikurangi kebutuhan pokok)"
        ])

    if st.button("Hitung Zakat Penghasilan", key="btn_gaji"):
        total_penghasilan = gaji_pokok + tunjangan + honor_lain
        penghasilan_netto = total_penghasilan - biaya_hidup - cicilan
        penghasilan_netto = max(0, penghasilan_netto)

        dasar_zakat = total_penghasilan if "Bruto" in metode_gaji else penghasilan_netto
        zakat_bulanan = dasar_zakat * 0.025 if dasar_zakat >= nisab_per_bulan else 0
        zakat_tahunan = zakat_bulanan * 12

        col1, col2, col3, col4 = st.columns(4)
        for col, (val, lbl) in zip([col1,col2,col3,col4], [
            (f"Rp {total_penghasilan:,.0f}", "Total Penghasilan/Bulan"),
            (f"Rp {dasar_zakat:,.0f}", "Dasar Zakat"),
            (f"Rp {zakat_bulanan:,.0f}", "Zakat per Bulan"),
            (f"Rp {zakat_tahunan:,.0f}", "Zakat per Tahun"),
        ]):
            with col:
                st.markdown(f'<div class="result-card"><div class="result-val">{val}</div><div class="result-lbl">{lbl}</div></div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        if dasar_zakat >= nisab_per_bulan:
            st.markdown(f"""<div class="wajib-box">
                ✅ <strong>WAJIB ZAKAT PENGHASILAN</strong><br>
                Zakat bulanan: <strong style="color:#48c78e">Rp {zakat_bulanan:,.0f}</strong> | 
                Zakat tahunan: <strong style="color:#48c78e">Rp {zakat_tahunan:,.0f}</strong><br>
                📋 Metode: <strong>{metode_gaji}</strong> | Tarif: 2.5%<br>
                💡 Bisa dibayar setiap bulan saat menerima gaji (lebih mudah) atau sekali setahun.
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown(f"""<div class="tidak-box">
                🟡 Penghasilan belum mencapai nisab (Rp {nisab_per_bulan:,.0f}/bulan).<br>
                Anda dianjurkan tetap bersedekah dan berinfaq.
            </div>""", unsafe_allow_html=True)

        # Breakdown chart
        fig = go.Figure(go.Waterfall(
            orientation="v",
            measure=["absolute","relative","relative","relative","total"],
            x=["Total Penghasilan","Kebutuhan Pokok","Cicilan","Zakat (2.5%)","Sisa Bersih"],
            y=[total_penghasilan, -biaya_hidup, -cicilan, -zakat_bulanan,
               total_penghasilan - biaya_hidup - cicilan - zakat_bulanan],
            connector={"line": {"color": "rgba(255,255,255,0.2)"}},
            decreasing={"marker": {"color": "#f94144"}},
            increasing={"marker": {"color": "#48c78e"}},
            totals={"marker": {"color": "#d4af7a"}}
        ))
        fig.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            title=dict(text="Breakdown Penghasilan Bulanan", font=dict(color="white")),
            font=dict(color="rgba(255,255,255,0.7)"), height=380)
        st.plotly_chart(fig, use_container_width=True)

# ── TAB 2: WIRAUSAHA ─────────────────────────────────────────────
with tab2:
    st.markdown('<div class="section-title">🏢 Zakat Penghasilan Wirausaha / Freelancer</div>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:0.85rem;color:rgba(255,255,255,0.5)">Untuk wirausaha, zakat dihitung dari laba bersih (omzet dikurangi biaya operasional). Ada dua pendapat ulama yang bisa dipilih.</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        omzet_bulan    = st.number_input("Omzet / Pendapatan Kotor per Bulan (Rp)", min_value=0, value=15000000, step=500000, format="%d")
        biaya_ops      = st.number_input("Biaya Operasional Bisnis per Bulan (Rp)", min_value=0, value=8000000, step=500000, format="%d")
        biaya_pribadi  = st.number_input("Biaya Kebutuhan Pribadi/Keluarga (Rp/bulan)", min_value=0, value=3000000, step=500000, format="%d")
    with col2:
        pendapat_ulama = st.selectbox("Pendapat Ulama yang Diikuti", [
            "Pendapat 1: Dari laba bersih setelah biaya ops (Yusuf Qaradhawi)",
            "Pendapat 2: Dari laba bersih setelah semua pengeluaran wajib",
            "Pendapat 3: Dari omzet bruto (lebih hati-hati)"
        ])

    if st.button("Hitung Zakat Wirausaha", key="btn_wira"):
        laba_bersih_bisnis = omzet_bulan - biaya_ops
        laba_setelah_pribadi = max(0, laba_bersih_bisnis - biaya_pribadi)

        if "Pendapat 1" in pendapat_ulama:
            dasar = laba_bersih_bisnis
            label_metode = "Laba Bersih (setelah biaya operasional)"
        elif "Pendapat 2" in pendapat_ulama:
            dasar = laba_setelah_pribadi
            label_metode = "Laba Bersih (setelah semua pengeluaran wajib)"
        else:
            dasar = omzet_bulan
            label_metode = "Omzet Bruto (paling hati-hati)"

        zakat_w = dasar * 0.025 if dasar >= nisab_per_bulan else 0

        col1, col2, col3 = st.columns(3)
        for col, (val, lbl) in zip([col1, col2, col3], [
            (f"Rp {dasar:,.0f}", f"Dasar Zakat ({label_metode[:20]}...)"),
            (f"Rp {zakat_w:,.0f}", "Zakat per Bulan (2.5%)"),
            (f"Rp {zakat_w*12:,.0f}", "Zakat per Tahun"),
        ]):
            with col:
                st.markdown(f'<div class="result-card"><div class="result-val">{val}</div><div class="result-lbl">{lbl}</div></div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        if dasar >= nisab_per_bulan:
            st.markdown(f"""<div class="wajib-box">
                ✅ <strong>WAJIB ZAKAT PENGHASILAN WIRAUSAHA</strong><br>
                Metode: <strong>{label_metode}</strong><br>
                Zakat bulanan: <strong style="color:#48c78e">Rp {zakat_w:,.0f}</strong><br>
                💡 Para ulama berbeda pendapat dalam metode ini. Pilih yang sesuai keyakinan dan konsultasikan dengan ulama/BAZNAS setempat.
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="tidak-box">🟡 Penghasilan bersih belum mencapai nisab (Rp {nisab_per_bulan:,.0f}/bulan).</div>', unsafe_allow_html=True)

# ── TAB 3: PERBANDINGAN METODE ───────────────────────────────────
with tab3:
    st.markdown('<div class="section-title">📊 Perbandingan Metode Zakat Penghasilan</div>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:0.85rem;color:rgba(255,255,255,0.5)">Simulasikan berapa zakat Anda dengan berbagai metode agar bisa memilih yang paling sesuai.</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        sim_penghasilan = st.number_input("Penghasilan Kotor per Bulan (Rp)", min_value=0, value=8000000, step=500000, format="%d", key="sim_p")
        sim_kebutuhan   = st.number_input("Total Kebutuhan Wajib per Bulan (Rp)", min_value=0, value=3000000, step=500000, format="%d", key="sim_k")

    metode_data = [
        ("Bruto Penuh", sim_penghasilan, "Dari total penghasilan tanpa dikurangi apapun"),
        ("Netto (setelah kebutuhan)", max(0, sim_penghasilan - sim_kebutuhan), "Dikurangi kebutuhan hidup wajib"),
        ("Haul Tahunan", sim_penghasilan * 12, "Dihitung dan dibayar sekali per tahun"),
    ]
    results = []
    for nama, dasar, ket in metode_data:
        z = dasar * 0.025 if dasar >= (nisab_per_bulan if "Tahun" not in nama else nisab_beras) else 0
        results.append({"Metode": nama, "Dasar (Rp)": f"Rp {dasar:,.0f}", "Zakat (Rp)": f"Rp {z:,.0f}", "Keterangan": ket})

    st.dataframe(results, use_container_width=True, hide_index=True)

    fig = go.Figure(go.Bar(
        x=[r["Metode"] for r in results],
        y=[float(r["Zakat (Rp)"].replace("Rp ","").replace(",","")) for r in results],
        marker_color=["#d4af7a","#48c78e","#90e0ef"],
        text=[r["Zakat (Rp)"] for r in results], textposition="outside",
        textfont=dict(color="white")
    ))
    fig.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        title=dict(text="Perbandingan Besaran Zakat per Metode", font=dict(color="white")),
        font=dict(color="rgba(255,255,255,0.7)"), yaxis_title="Zakat (Rp)", height=380)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""<div style="background:rgba(212,175,122,0.08);border:1px solid rgba(212,175,122,0.2);border-radius:12px;padding:1rem 1.25rem;margin-top:0.5rem">
        <p style="margin:0;font-size:0.85rem;color:rgba(255,255,255,0.65)">
        ⚠️ <strong style="color:#d4af7a">Catatan:</strong> Para ulama kontemporer berbeda pendapat tentang metode zakat penghasilan.
        Fatwa MUI No. 3 Tahun 2003 mengakui zakat penghasilan/profesi. BAZNAS menganjurkan metode netto.
        Untuk kepastian hukum, konsultasikan dengan ulama atau lembaga zakat resmi.
        </p>
    </div>""", unsafe_allow_html=True)
