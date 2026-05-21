import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Laporan Keuangan Islami", page_icon="📊", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Amiri:wght@400;700&display=swap');
html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; }
.stApp { background: linear-gradient(160deg, #0a1628, #0d2137, #0a1f1a); }
section[data-testid="stSidebar"] { background: rgba(255,255,255,0.03) !important; border-right: 1px solid rgba(255,255,255,0.07); }
section[data-testid="stSidebar"] * { color: #d4af7a !important; }
h1,h2,h3 { color: white !important; }
p, li, label { color: rgba(255,255,255,0.8) !important; }
.stTextInput input, .stNumberInput input, .stTextArea textarea {
    background: #ffffff !important; color: #111111 !important;
    border: 1.5px solid rgba(212,175,122,0.4) !important; border-radius: 8px !important; font-weight:500 !important;
}
div[data-baseweb="select"] > div { background: #ffffff !important; color: #111111 !important; border-radius: 8px !important; }
div[data-baseweb="select"] * { color: #111111 !important; }
div[data-baseweb="popover"] li { color: #111111 !important; background: #fff !important; }
div[data-baseweb="popover"] li:hover { background: #f5f0e8 !important; }
.section-title { font-size:1.3rem; font-weight:800; color:white; margin:1.5rem 0 0.75rem; padding-bottom:0.5rem; border-bottom:2px solid rgba(212,175,122,0.4); }
.report-header { background:linear-gradient(135deg,rgba(212,175,122,0.15),rgba(72,199,142,0.08)); border:1px solid rgba(212,175,122,0.3); border-radius:16px; padding:1.5rem; margin-bottom:1.5rem; text-align:center; }
.report-row { display:flex; justify-content:space-between; padding:0.5rem 0.75rem; border-bottom:1px solid rgba(255,255,255,0.06); }
.report-row:hover { background:rgba(255,255,255,0.03); }
.report-section { background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.09); border-radius:12px; padding:1rem; margin-bottom:1rem; }
.total-row { display:flex; justify-content:space-between; padding:0.75rem; background:rgba(212,175,122,0.1); border-radius:8px; margin-top:0.5rem; font-weight:700; }
.stButton button { background:linear-gradient(90deg,#d4af7a,#48c78e) !important; color:#0a1628 !important; font-weight:700 !important; border:none !important; border-radius:10px !important; padding:0.6rem 2rem !important; font-size:1rem !important; }
.arabic { font-family:'Amiri',serif; font-size:1rem; color:#d4af7a; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p style="font-size:2rem;font-weight:800;background:linear-gradient(90deg,#d4af7a,#48c78e);-webkit-background-clip:text;-webkit-text-fill-color:transparent">📊 Laporan Keuangan Islami</p>', unsafe_allow_html=True)
st.markdown('<p class="arabic">وَلَا تَأْكُلُوا أَمْوَالَكُم بَيْنَكُم بِالْبَاطِلِ — "Janganlah kamu memakan harta sesamamu dengan cara yang batil" (QS. Al-Baqarah: 188)</p>', unsafe_allow_html=True)
st.markdown("---")

st.markdown('<div class="section-title">📋 Identitas Bisnis</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    nama_usaha  = st.text_input("Nama Usaha", placeholder="Contoh: Dapur Berkah")
    jenis_usaha = st.selectbox("Jenis Usaha", ["Perdagangan","Jasa","Produksi/Manufaktur","Pertanian"])
with col2:
    pemilik     = st.text_input("Nama Pemilik", placeholder="Nama lengkap")
    periode     = st.text_input("Periode Laporan", placeholder="Contoh: Januari 2025")
with col3:
    akad_usaha  = st.selectbox("Akad Utama Bisnis", ["Mudharabah","Musyarakah","Murabahah","Ijarah","Mandiri (Modal Sendiri)"])

st.markdown("---")

tab1, tab2, tab3 = st.tabs(["📈 Laporan Laba Rugi", "⚖️ Neraca Syariah", "💚 Dana Sosial & Zakat"])

# ── TAB 1: LABA RUGI ─────────────────────────────────────────────
with tab1:
    st.markdown('<div class="section-title">📈 Laporan Laba Rugi Syariah</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Pendapatan**")
        pend_utama  = st.number_input("Pendapatan Usaha Utama (Rp)", min_value=0, value=20000000, step=500000, format="%d")
        pend_lain   = st.number_input("Pendapatan Lain-lain Halal (Rp)", min_value=0, value=500000, step=100000, format="%d")
        bagi_hasil_diterima = st.number_input("Bagi Hasil Diterima (jika ada) (Rp)", min_value=0, value=0, step=100000, format="%d")

        st.markdown("**Harga Pokok Penjualan**")
        hpp_bahan   = st.number_input("Bahan Baku / HPP (Rp)", min_value=0, value=8000000, step=500000, format="%d")
        tenaga_kerja= st.number_input("Biaya Tenaga Kerja Langsung (Rp)", min_value=0, value=2000000, step=500000, format="%d")
        overhead    = st.number_input("Overhead Produksi (Rp)", min_value=0, value=1000000, step=500000, format="%d")

    with col2:
        st.markdown("**Biaya Operasional**")
        biaya_sewa  = st.number_input("Biaya Sewa Tempat (Rp)", min_value=0, value=1500000, step=100000, format="%d")
        biaya_gaji  = st.number_input("Gaji & Tunjangan (Rp)", min_value=0, value=3000000, step=100000, format="%d")
        biaya_listrik=st.number_input("Listrik, Air, Internet (Rp)", min_value=0, value=600000, step=50000, format="%d")
        biaya_market= st.number_input("Biaya Pemasaran (Rp)", min_value=0, value=500000, step=50000, format="%d")
        biaya_depr  = st.number_input("Penyusutan Aset (Rp)", min_value=0, value=300000, step=50000, format="%d")
        biaya_lain  = st.number_input("Biaya Operasional Lain (Rp)", min_value=0, value=200000, step=50000, format="%d")

        st.markdown("**Kewajiban Syariah**")
        persen_zakat = st.slider("Zakat Usaha (%)", 0.0, 10.0, 2.5, 0.5,
            help="Umumnya 2.5% dari laba/aset sesuai ketentuan")
        persen_infaq = st.slider("Infaq & Sedekah (%)", 0.0, 10.0, 2.5, 0.5)

    if st.button("📊 Generate Laporan", key="btn_lr"):
        total_pendapatan = pend_utama + pend_lain + bagi_hasil_diterima
        total_hpp        = hpp_bahan + tenaga_kerja + overhead
        laba_kotor       = total_pendapatan - total_hpp
        total_ops        = biaya_sewa + biaya_gaji + biaya_listrik + biaya_market + biaya_depr + biaya_lain
        laba_ops         = laba_kotor - total_ops
        zakat_usaha      = max(0, laba_ops) * persen_zakat / 100
        infaq_val        = max(0, laba_ops) * persen_infaq / 100
        laba_bersih      = laba_ops - zakat_usaha - infaq_val
        gross_margin     = (laba_kotor / total_pendapatan * 100) if total_pendapatan > 0 else 0
        net_margin       = (laba_bersih / total_pendapatan * 100) if total_pendapatan > 0 else 0

        # Header laporan
        st.markdown(f"""<div class="report-header">
            <div style="font-size:0.8rem;color:rgba(212,175,122,0.7);letter-spacing:2px;text-transform:uppercase">Laporan Laba Rugi Syariah</div>
            <div style="font-size:1.4rem;font-weight:800;color:#d4af7a;margin:0.3rem 0">{nama_usaha or 'Nama Usaha'}</div>
            <div style="color:rgba(255,255,255,0.5);font-size:0.85rem">Pemilik: {pemilik or '-'} | Akad: {akad_usaha} | Periode: {periode or '-'}</div>
        </div>""", unsafe_allow_html=True)

        def baris(label, nilai, indent=False, bold=False):
            style = "padding-left:1.5rem;" if indent else ""
            weight = "font-weight:700;" if bold else ""
            color = "#d4af7a" if bold else "rgba(255,255,255,0.8)"
            return f"""<div class="report-row" style="{style}">
                <span style="color:{color};{weight}">{label}</span>
                <span style="color:{color};{weight}">Rp {nilai:,.0f}</span>
            </div>"""

        def total_baris(label, nilai, color="#d4af7a"):
            return f"""<div class="total-row">
                <span style="color:{color}">{label}</span>
                <span style="color:{color}">Rp {nilai:,.0f}</span>
            </div>"""

        st.markdown('<div class="report-section">', unsafe_allow_html=True)
        st.markdown('<div style="color:#48c78e;font-weight:700;margin-bottom:0.5rem">A. PENDAPATAN</div>', unsafe_allow_html=True)
        st.markdown(baris("Pendapatan Usaha Utama", pend_utama, indent=True), unsafe_allow_html=True)
        if pend_lain > 0: st.markdown(baris("Pendapatan Lain-lain Halal", pend_lain, indent=True), unsafe_allow_html=True)
        if bagi_hasil_diterima > 0: st.markdown(baris("Bagi Hasil Diterima", bagi_hasil_diterima, indent=True), unsafe_allow_html=True)
        st.markdown(total_baris("Total Pendapatan", total_pendapatan, "#48c78e"), unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="report-section">', unsafe_allow_html=True)
        st.markdown('<div style="color:#f9c74f;font-weight:700;margin-bottom:0.5rem">B. HARGA POKOK PENJUALAN (HPP)</div>', unsafe_allow_html=True)
        st.markdown(baris("Bahan Baku / Pembelian", hpp_bahan, indent=True), unsafe_allow_html=True)
        st.markdown(baris("Tenaga Kerja Langsung", tenaga_kerja, indent=True), unsafe_allow_html=True)
        st.markdown(baris("Overhead Produksi", overhead, indent=True), unsafe_allow_html=True)
        st.markdown(total_baris("Total HPP", total_hpp, "#f9c74f"), unsafe_allow_html=True)
        st.markdown(total_baris(f"LABA KOTOR (Gross Margin: {gross_margin:.1f}%)", laba_kotor, "#48c78e"), unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="report-section">', unsafe_allow_html=True)
        st.markdown('<div style="color:#90e0ef;font-weight:700;margin-bottom:0.5rem">C. BIAYA OPERASIONAL</div>', unsafe_allow_html=True)
        for label, val in [("Sewa Tempat", biaya_sewa),("Gaji & Tunjangan", biaya_gaji),
                           ("Listrik, Air, Internet", biaya_listrik),("Pemasaran", biaya_market),
                           ("Penyusutan Aset", biaya_depr),("Biaya Lain-lain", biaya_lain)]:
            if val > 0: st.markdown(baris(label, val, indent=True), unsafe_allow_html=True)
        st.markdown(total_baris("Total Biaya Operasional", total_ops, "#f3722c"), unsafe_allow_html=True)
        st.markdown(total_baris("LABA OPERASIONAL", laba_ops, "#48c78e"), unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="report-section">', unsafe_allow_html=True)
        st.markdown('<div style="color:#d4af7a;font-weight:700;margin-bottom:0.5rem">D. KEWAJIBAN SYARIAH ☪️</div>', unsafe_allow_html=True)
        st.markdown(baris(f"Zakat Usaha ({persen_zakat}%)", zakat_usaha, indent=True), unsafe_allow_html=True)
        st.markdown(baris(f"Infaq & Sedekah ({persen_infaq}%)", infaq_val, indent=True), unsafe_allow_html=True)
        st.markdown(total_baris("Total Kewajiban Syariah", zakat_usaha + infaq_val, "#d4af7a"), unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown(f"""<div style="background:linear-gradient(90deg,rgba(72,199,142,0.2),rgba(212,175,122,0.1));
            border:2px solid rgba(72,199,142,0.5);border-radius:12px;padding:1.25rem;margin-top:0.5rem">
            <div style="display:flex;justify-content:space-between;align-items:center">
                <span style="color:white;font-size:1.1rem;font-weight:800">💰 LABA BERSIH (Net Margin: {net_margin:.1f}%)</span>
                <span style="color:#48c78e;font-size:1.3rem;font-weight:800">Rp {laba_bersih:,.0f}</span>
            </div>
        </div>""", unsafe_allow_html=True)

        # Chart
        fig = go.Figure(go.Bar(
            x=["Pendapatan","HPP","Biaya Ops","Kewajiban Syariah","Laba Bersih"],
            y=[total_pendapatan, total_hpp, total_ops, zakat_usaha+infaq_val, laba_bersih],
            marker_color=["#48c78e","#f94144","#f3722c","#d4af7a","#90e0ef"],
            text=[f"Rp {v:,.0f}" for v in [total_pendapatan, total_hpp, total_ops, zakat_usaha+infaq_val, laba_bersih]],
            textposition="outside", textfont=dict(color="white", size=11)
        ))
        fig.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            title=dict(text="Visualisasi Laporan Laba Rugi Syariah", font=dict(color="white")),
            font=dict(color="rgba(255,255,255,0.7)"), height=400)
        st.plotly_chart(fig, use_container_width=True)

# ── TAB 2: NERACA ────────────────────────────────────────────────
with tab2:
    st.markdown('<div class="section-title">⚖️ Neraca Sederhana Syariah</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**ASET**")
        kas_n          = st.number_input("Kas & Bank (Rp)", min_value=0, value=5000000, step=500000, format="%d", key="n_kas")
        piutang_n      = st.number_input("Piutang Murabahah/Dagang (Rp)", min_value=0, value=3000000, step=500000, format="%d", key="n_piut")
        persediaan_n   = st.number_input("Persediaan/Stok (Rp)", min_value=0, value=7000000, step=500000, format="%d", key="n_pers")
        aset_tetap_n   = st.number_input("Aset Tetap Bersih (Rp)", min_value=0, value=20000000, step=1000000, format="%d", key="n_aset")
    with col2:
        st.markdown("**KEWAJIBAN & EKUITAS**")
        hutang_dagang_n = st.number_input("Hutang Dagang (Rp)", min_value=0, value=2000000, step=500000, format="%d", key="n_hd")
        hutang_bank_n   = st.number_input("Pembiayaan Bank Syariah (Rp)", min_value=0, value=10000000, step=1000000, format="%d", key="n_hb")
        dana_zakat_n    = st.number_input("Dana Zakat Belum Dibayar (Rp)", min_value=0, value=500000, step=100000, format="%d", key="n_zk")
        modal_n         = st.number_input("Modal Pemilik / Ekuitas (Rp)", min_value=0, value=22500000, step=1000000, format="%d", key="n_mod")

    if st.button("Tampilkan Neraca", key="btn_neraca"):
        total_aset_n  = kas_n + piutang_n + persediaan_n + aset_tetap_n
        total_kwjb_n  = hutang_dagang_n + hutang_bank_n + dana_zakat_n
        total_ekuitas_n = modal_n
        total_pasiva  = total_kwjb_n + total_ekuitas_n
        balance       = total_aset_n == total_pasiva

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""<div class="report-section">
                <div style="color:#48c78e;font-weight:700;margin-bottom:0.75rem;font-size:1rem">ASET</div>""", unsafe_allow_html=True)
            for lbl, val in [("Kas & Bank", kas_n),("Piutang Murabahah", piutang_n),
                             ("Persediaan", persediaan_n),("Aset Tetap Bersih", aset_tetap_n)]:
                st.markdown(f'<div class="report-row"><span style="color:rgba(255,255,255,0.75)">{lbl}</span><span style="color:rgba(255,255,255,0.75)">Rp {val:,.0f}</span></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="total-row"><span style="color:#48c78e">Total Aset</span><span style="color:#48c78e">Rp {total_aset_n:,.0f}</span></div></div>', unsafe_allow_html=True)

        with col2:
            st.markdown("""<div class="report-section">
                <div style="color:#f3722c;font-weight:700;margin-bottom:0.75rem">KEWAJIBAN & EKUITAS</div>""", unsafe_allow_html=True)
            for lbl, val in [("Hutang Dagang", hutang_dagang_n),("Pembiayaan Bank Syariah", hutang_bank_n),("Dana Zakat", dana_zakat_n)]:
                st.markdown(f'<div class="report-row"><span style="color:rgba(255,255,255,0.75)">{lbl}</span><span style="color:rgba(255,255,255,0.75)">Rp {val:,.0f}</span></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="total-row"><span style="color:#f3722c">Total Kewajiban</span><span style="color:#f3722c">Rp {total_kwjb_n:,.0f}</span></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="report-row"><span style="color:#d4af7a;font-weight:700">Modal / Ekuitas</span><span style="color:#d4af7a;font-weight:700">Rp {modal_n:,.0f}</span></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="total-row"><span style="color:#48c78e">Total Pasiva</span><span style="color:#48c78e">Rp {total_pasiva:,.0f}</span></div></div>', unsafe_allow_html=True)

        if abs(total_aset_n - total_pasiva) < 1000:
            st.markdown('<div style="background:rgba(72,199,142,0.1);border:1px solid rgba(72,199,142,0.3);border-radius:10px;padding:0.75rem 1rem;margin-top:0.5rem"><p style="margin:0;color:#48c78e">✅ Neraca SEIMBANG — Total Aset = Total Pasiva</p></div>', unsafe_allow_html=True)
        else:
            selisih = abs(total_aset_n - total_pasiva)
            st.markdown(f'<div style="background:rgba(249,65,68,0.1);border:1px solid rgba(249,65,68,0.3);border-radius:10px;padding:0.75rem 1rem;margin-top:0.5rem"><p style="margin:0;color:#f94144">⚠️ Neraca TIDAK SEIMBANG — selisih Rp {selisih:,.0f}. Periksa kembali angka modal/ekuitas.</p></div>', unsafe_allow_html=True)

# ── TAB 3: DANA SOSIAL ───────────────────────────────────────────
with tab3:
    st.markdown('<div class="section-title">💚 Kalkulator Dana Sosial & Zakat Bisnis</div>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:0.85rem;color:rgba(255,255,255,0.5)">Rencanakan kewajiban dan program sosial bisnis Anda secara islami.</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        laba_tahunan_s = st.number_input("Laba Bersih Tahunan (Rp)", min_value=0, value=50000000, step=1000000, format="%d", key="ds_laba")
        omzet_tahunan  = st.number_input("Omzet/Aset Bisnis (Rp)", min_value=0, value=200000000, step=5000000, format="%d", key="ds_omzet")
    with col2:
        zk_pct  = st.slider("Zakat Bisnis (%)", 0.0, 5.0, 2.5, 0.25, key="ds_zk")
        infaq_pct = st.slider("Infaq & Sedekah (%)", 0.0, 10.0, 2.5, 0.25, key="ds_inf")
        wakaf_pct = st.slider("Wakaf Produktif (%)", 0.0, 5.0, 1.0, 0.25, key="ds_wkf")

    if st.button("Hitung Dana Sosial", key="btn_sosial"):
        zakat_s  = omzet_tahunan * zk_pct / 100
        infaq_s  = laba_tahunan_s * infaq_pct / 100
        wakaf_s  = laba_tahunan_s * wakaf_pct / 100
        total_sosial = zakat_s + infaq_s + wakaf_s
        laba_setelah = laba_tahunan_s - total_sosial

        col1,col2,col3,col4 = st.columns(4)
        for col,(val,lbl) in zip([col1,col2,col3,col4],[
            (f"Rp {zakat_s:,.0f}","Zakat Bisnis/Tahun"),
            (f"Rp {infaq_s:,.0f}","Infaq & Sedekah/Tahun"),
            (f"Rp {wakaf_s:,.0f}","Wakaf Produktif/Tahun"),
            (f"Rp {total_sosial:,.0f}","Total Dana Sosial"),
        ]):
            with col:
                st.markdown(f'<div style="background:rgba(212,175,122,0.1);border:1px solid rgba(212,175,122,0.25);border-radius:12px;padding:1rem;text-align:center"><div style="color:#d4af7a;font-size:1.2rem;font-weight:800">{val}</div><div style="color:rgba(255,255,255,0.5);font-size:0.78rem;margin-top:0.2rem">{lbl}</div></div>', unsafe_allow_html=True)

        st.markdown(f"""<br><div style="background:rgba(72,199,142,0.1);border:1px solid rgba(72,199,142,0.3);border-radius:12px;padding:1.25rem;margin-top:0.5rem">
            💚 <strong>Total Dana Sosial: Rp {total_sosial:,.0f}/tahun</strong> ({total_sosial/laba_tahunan_s*100:.1f}% dari laba)<br>
            💰 Laba setelah kewajiban sosial: <strong>Rp {laba_setelah:,.0f}</strong><br><br>
            <div style="font-size:0.85rem;color:rgba(255,255,255,0.6)">
            💡 <em>"Perumpamaan orang-orang yang menafkahkan hartanya di jalan Allah adalah seperti sebutir benih yang menumbuhkan tujuh bulir, pada tiap-tiap bulir: seratus biji."</em> — QS. Al-Baqarah: 261
            </div>
        </div>""", unsafe_allow_html=True)
