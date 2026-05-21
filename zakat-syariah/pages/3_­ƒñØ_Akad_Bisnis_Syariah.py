import streamlit as st

st.set_page_config(page_title="Akad Bisnis Syariah", page_icon="🤝", layout="wide")

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
.akad-card { background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.09); border-radius:16px; padding:1.5rem; margin-bottom:1rem; }
.akad-title { font-size:1.15rem; font-weight:800; margin-bottom:0.3rem; }
.arabic { font-family:'Amiri',serif; font-size:1rem; color:#d4af7a; }
.result-card { background:rgba(212,175,122,0.1); border:1px solid rgba(212,175,122,0.35); border-radius:16px; padding:1.25rem; text-align:center; }
.result-val { font-size:1.4rem; font-weight:800; color:#d4af7a; }
.result-lbl { font-size:0.78rem; color:rgba(255,255,255,0.5); margin-top:0.2rem; }
.stButton button { background:linear-gradient(90deg,#d4af7a,#48c78e) !important; color:#0a1628 !important; font-weight:700 !important; border:none !important; border-radius:10px !important; padding:0.6rem 2rem !important; font-size:1rem !important; }
.rekomendasi-box { background:rgba(72,199,142,0.1); border:1px solid rgba(72,199,142,0.35); border-radius:12px; padding:1.25rem; margin:0.5rem 0; }
.tag { display:inline-block; border-radius:20px; padding:0.15rem 0.7rem; font-size:0.75rem; font-weight:700; margin:0.15rem; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p style="font-size:2rem;font-weight:800;background:linear-gradient(90deg,#d4af7a,#48c78e);-webkit-background-clip:text;-webkit-text-fill-color:transparent">🤝 Panduan Akad Bisnis Syariah</p>', unsafe_allow_html=True)
st.markdown('<p class="arabic">يَا أَيُّهَا الَّذِينَ آمَنُوا أَوْفُوا بِالْعُقُودِ — "Wahai orang-orang beriman, penuhilah akad-akad itu" (QS. Al-Maidah: 1)</p>', unsafe_allow_html=True)
st.markdown("---")

tab1, tab2, tab3 = st.tabs(["📚 Jenis-Jenis Akad", "🔍 Rekomendasi Akad", "🧮 Simulasi Bagi Hasil"])

# ── TAB 1: JENIS AKAD ────────────────────────────────────────────
with tab1:
    st.markdown('<div class="section-title">📚 Jenis-Jenis Akad Bisnis Syariah</div>', unsafe_allow_html=True)

    akad_list = [
        {
            "nama": "Mudharabah (مضاربة)", "icon": "🤲",
            "warna": "#d4af7a",
            "arab": "رأس المال من رب المال والعمل من المضارب",
            "definisi": "Akad kerja sama di mana satu pihak (shahibul maal) menyediakan modal 100%, dan pihak lain (mudharib) mengelola usaha. Keuntungan dibagi sesuai nisbah yang disepakati, kerugian ditanggung shahibul maal kecuali akibat kelalaian mudharib.",
            "cocok": ["Investor dengan pengusaha","Koperasi syariah","Deposito bank syariah","Startup butuh modal"],
            "nisbah": "Fleksibel — contoh: 60% mudharib : 40% shahibul maal",
            "larangan": "Mudharib tidak boleh mencampur modal dengan harta pribadi tanpa izin"
        },
        {
            "nama": "Musyarakah (مشاركة)", "icon": "🏢",
            "warna": "#48c78e",
            "arab": "اشتراك في رأس المال والعمل والربح",
            "definisi": "Akad perkongsian di mana dua pihak atau lebih menyertakan modal dan/atau keahlian. Keuntungan dan kerugian dibagi proporsional sesuai porsi modal atau perjanjian.",
            "cocok": ["Usaha patungan/joint venture","PT syariah","Properti bersama","Kemitraan bisnis"],
            "nisbah": "Proporsional modal — contoh: Modal A 60% : Modal B 40%",
            "larangan": "Semua mitra berhak ikut mengelola kecuali disepakati lain"
        },
        {
            "nama": "Murabahah (مرابحة)", "icon": "🏷️",
            "warna": "#90e0ef",
            "arab": "البيع بالثمن الأصلي مع زيادة ربح معلومة",
            "definisi": "Akad jual beli di mana penjual menyatakan harga pokok dan margin keuntungan secara transparan kepada pembeli. Pembeli setuju membayar harga pokok + margin (bisa cicil).",
            "cocok": ["KPR syariah","Pembiayaan kendaraan","Pembelian stok barang","UMKM butuh modal belanja"],
            "nisbah": "Margin tetap disepakati di awal — tidak berubah",
            "larangan": "Penjual harus memiliki barang dulu sebelum menjual"
        },
        {
            "nama": "Ijarah (إجارة)", "icon": "🔑",
            "warna": "#c77dff",
            "arab": "عقد على المنافع بعوض",
            "definisi": "Akad sewa-menyewa manfaat suatu aset atau jasa dengan imbalan upah/sewa yang disepakati. Termasuk Ijarah Muntahiya bit Tamlik (sewa berakhir dengan kepemilikan).",
            "cocok": ["Sewa ruko/tempat usaha","Kontrak kerja","Leasing syariah","Outsourcing"],
            "nisbah": "Harga sewa tetap per periode",
            "larangan": "Obyek sewa harus halal dan manfaatnya jelas"
        },
        {
            "nama": "Salam (سلم)", "icon": "📦",
            "warna": "#f9c74f",
            "arab": "بيع آجل بعاجل",
            "definisi": "Akad jual beli di mana pembayaran dilakukan di muka (tunai), sedangkan barang diserahkan di kemudian hari sesuai spesifikasi yang disepakati.",
            "cocok": ["Pertanian/hasil bumi","Pre-order produk","Industri manufaktur","Bisnis kuliner pesanan"],
            "nisbah": "Harga dan spesifikasi barang harus jelas sejak awal",
            "larangan": "Tidak boleh untuk barang yang tidak bisa dispesifikasikan"
        },
        {
            "nama": "Istishna (استصناع)", "icon": "🏗️",
            "warna": "#f3722c",
            "arab": "عقد على مبيع في الذمة شرط فيه العمل",
            "definisi": "Akad pemesanan barang yang perlu dibuat/diproduksi dulu. Mirip salam, tapi pembayaran bisa bertahap sesuai kemajuan produksi.",
            "cocok": ["Konstruksi bangunan","Pembuatan software","Produksi furnitur custom","Manufaktur pesanan"],
            "nisbah": "Pembayaran bisa cicil sesuai progres pekerjaan",
            "larangan": "Spesifikasi barang harus sangat jelas di awal"
        },
    ]

    for akad in akad_list:
        st.markdown(f"""<div class="akad-card" style="border-left:4px solid {akad['warna']}">
            <div class="akad-title" style="color:{akad['warna']}">{akad['icon']} {akad['nama']}</div>
            <div class="arabic" style="font-size:0.9rem;margin-bottom:0.5rem">{akad['arab']}</div>
            <p style="font-size:0.9rem;margin-bottom:0.75rem">{akad['definisi']}</p>
            <div style="margin-bottom:0.5rem">
                {''.join(f'<span class="tag" style="background:rgba(212,175,122,0.15);color:#d4af7a;border:1px solid rgba(212,175,122,0.3)">✓ {c}</span>' for c in akad['cocok'])}
            </div>
            <div style="font-size:0.82rem;color:rgba(255,255,255,0.55)">
                📐 <strong style="color:rgba(255,255,255,0.7)">Nisbah/Harga:</strong> {akad['nisbah']} &nbsp;|&nbsp;
                ⚠️ <strong style="color:rgba(255,255,255,0.7)">Perhatian:</strong> {akad['larangan']}
            </div>
        </div>""", unsafe_allow_html=True)

# ── TAB 2: REKOMENDASI AKAD ──────────────────────────────────────
with tab2:
    st.markdown('<div class="section-title">🔍 Temukan Akad yang Tepat untuk Bisnis Anda</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        jenis_usaha = st.selectbox("Jenis Usaha Anda", [
            "Kuliner / Makanan & Minuman",
            "Fashion / Pakaian",
            "Properti / Kos-kosan",
            "Pertanian / Agribisnis",
            "Jasa Digital / IT",
            "Manufaktur / Produksi",
            "Perdagangan / Retail",
            "Pendidikan / Pelatihan",
        ])
        peran = st.selectbox("Peran Anda dalam Bisnis", [
            "Saya punya modal, cari pengelola",
            "Saya punya keahlian, butuh modal",
            "Saya dan mitra sama-sama setor modal",
            "Saya butuh beli barang untuk dijual kembali",
            "Saya butuh sewa aset/tempat usaha",
            "Saya terima pesanan produk custom",
        ])
    with col2:
        modal_cukup = st.selectbox("Kondisi Modal", [
            "Modal sudah cukup (mandiri)",
            "Butuh tambahan modal dari investor",
            "Modal patungan dengan mitra",
            "Butuh pembiayaan dari bank syariah",
        ])
        jangka = st.selectbox("Jangka Waktu Bisnis", [
            "Jangka pendek (< 1 tahun)",
            "Jangka menengah (1-3 tahun)",
            "Jangka panjang (> 3 tahun)",
        ])

    if st.button("🔍 Cari Akad yang Tepat", key="btn_akad"):
        rekomendasi = []
        alasan = []

        if "punya modal, cari pengelola" in peran:
            rekomendasi.append("Mudharabah")
            alasan.append("Anda sebagai shahibul maal, mitra Anda sebagai mudharib — sesuai kondisi Anda")
        if "keahlian, butuh modal" in peran:
            rekomendasi.append("Mudharabah")
            alasan.append("Anda sebagai mudharib (pengelola), cari investor sebagai shahibul maal")
        if "sama-sama setor modal" in peran:
            rekomendasi.append("Musyarakah")
            alasan.append("Kedua pihak berkontribusi modal — musyarakah paling tepat")
        if "beli barang untuk dijual" in peran:
            rekomendasi.append("Murabahah")
            alasan.append("Pembelian barang dengan margin transparan sesuai akad murabahah")
        if "sewa aset" in peran:
            rekomendasi.append("Ijarah")
            alasan.append("Sewa aset/tempat usaha sesuai dengan akad ijarah")
        if "pesanan produk custom" in peran:
            rekomendasi.append("Istishna")
            alasan.append("Produk dibuat sesuai pesanan — cocok untuk akad istishna")
        if "Pertanian" in jenis_usaha:
            rekomendasi.append("Salam")
            alasan.append("Hasil pertanian bisa diperjualbelikan dengan akad salam (bayar di muka)")
        if "Butuh pembiayaan dari bank" in modal_cukup:
            if "Murabahah" not in rekomendasi:
                rekomendasi.append("Murabahah")
                alasan.append("Bank syariah umumnya menggunakan akad murabahah untuk pembiayaan")

        # Hapus duplikat
        seen = set()
        unique_rek = []
        unique_alasan = []
        for r, a in zip(rekomendasi, alasan):
            if r not in seen:
                seen.add(r)
                unique_rek.append(r)
                unique_alasan.append(a)

        if unique_rek:
            st.markdown(f"""<div class="rekomendasi-box">
                <strong style="color:#48c78e;font-size:1.05rem">✅ Rekomendasi Akad untuk Bisnis Anda:</strong><br><br>
                {''.join(f'<div style="margin-bottom:0.5rem">🔹 <strong style="color:#d4af7a">{r}</strong> — {a}</div>' for r, a in zip(unique_rek, unique_alasan))}
                <br><div style="font-size:0.82rem;color:rgba(255,255,255,0.55)">
                ⚠️ Ini adalah rekomendasi awal berdasarkan kondisi umum. Untuk kepastian akad yang sah secara syariah, konsultasikan dengan DSN-MUI atau ulama yang berkompeten.
                </div>
            </div>""", unsafe_allow_html=True)
        else:
            st.info("Tidak ada rekomendasi spesifik. Konsultasikan langsung dengan lembaga syariah.")

# ── TAB 3: SIMULASI BAGI HASIL ───────────────────────────────────
with tab3:
    st.markdown('<div class="section-title">🧮 Simulasi Bagi Hasil Mudharabah & Musyarakah</div>', unsafe_allow_html=True)

    jenis_akad_sim = st.selectbox("Pilih Jenis Akad", ["Mudharabah", "Musyarakah"], key="akad_sim")

    if jenis_akad_sim == "Mudharabah":
        col1, col2 = st.columns(2)
        with col1:
            modal_shahib = st.number_input("Modal Shahibul Maal (Rp)", min_value=0, value=50000000, step=1000000, format="%d")
            nisbah_shahib = st.slider("Nisbah Shahibul Maal (%)", 10, 90, 40)
        with col2:
            laba_proyek = st.number_input("Estimasi Laba Proyek per Bulan (Rp)", min_value=0, value=10000000, step=500000, format="%d")
            nisbah_mudharib = 100 - nisbah_shahib
            st.markdown(f"""<div class="result-card" style="margin-top:1.8rem">
                <div class="result-val">{nisbah_mudharib}% : {nisbah_shahib}%</div>
                <div class="result-lbl">Nisbah Mudharib : Shahibul Maal</div>
            </div>""", unsafe_allow_html=True)

        if st.button("Hitung Bagi Hasil Mudharabah", key="btn_mudh"):
            bh_mudharib  = laba_proyek * nisbah_mudharib / 100
            bh_shahib    = laba_proyek * nisbah_shahib / 100
            roi_shahib   = (bh_shahib / modal_shahib * 100) if modal_shahib > 0 else 0
            payback      = (modal_shahib / bh_shahib) if bh_shahib > 0 else 999

            col1, col2, col3, col4 = st.columns(4)
            for col, (val, lbl) in zip([col1,col2,col3,col4],[
                (f"Rp {laba_proyek:,.0f}", "Laba Proyek/Bulan"),
                (f"Rp {bh_mudharib:,.0f}", f"Bagian Mudharib ({nisbah_mudharib}%)"),
                (f"Rp {bh_shahib:,.0f}", f"Bagian Shahibul Maal ({nisbah_shahib}%)"),
                (f"{payback:.1f} bulan", "Estimasi BEP Modal"),
            ]):
                with col:
                    st.markdown(f'<div class="result-card"><div class="result-val">{val}</div><div class="result-lbl">{lbl}</div></div>', unsafe_allow_html=True)

    else:  # Musyarakah
        col1, col2 = st.columns(2)
        with col1:
            modal_a = st.number_input("Modal Mitra A (Rp)", min_value=0, value=30000000, step=1000000, format="%d")
            modal_b = st.number_input("Modal Mitra B (Rp)", min_value=0, value=20000000, step=1000000, format="%d")
        with col2:
            laba_musya = st.number_input("Laba Bersih per Bulan (Rp)", min_value=0, value=8000000, step=500000, format="%d")
            total_modal = modal_a + modal_b
            pct_a = modal_a / total_modal * 100 if total_modal > 0 else 50
            pct_b = 100 - pct_a
            st.markdown(f"""<div class="result-card" style="margin-top:1.8rem">
                <div class="result-val">{pct_a:.1f}% : {pct_b:.1f}%</div>
                <div class="result-lbl">Proporsi Modal A : B</div>
            </div>""", unsafe_allow_html=True)

        if st.button("Hitung Bagi Hasil Musyarakah", key="btn_musya"):
            bh_a = laba_musya * pct_a / 100
            bh_b = laba_musya * pct_b / 100
            col1, col2, col3, col4 = st.columns(4)
            for col, (val, lbl) in zip([col1,col2,col3,col4],[
                (f"Rp {total_modal:,.0f}", "Total Modal Bersama"),
                (f"Rp {laba_musya:,.0f}", "Laba per Bulan"),
                (f"Rp {bh_a:,.0f}", f"Bagian Mitra A ({pct_a:.1f}%)"),
                (f"Rp {bh_b:,.0f}", f"Bagian Mitra B ({pct_b:.1f}%)"),
            ]):
                with col:
                    st.markdown(f'<div class="result-card"><div class="result-val">{val}</div><div class="result-lbl">{lbl}</div></div>', unsafe_allow_html=True)
