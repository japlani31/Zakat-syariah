# 📖 PANDUAN — ZakatKu: Keuangan Syariah
### Prodi S1 Kewirausahaan · Universitas Muhammadiyah Metro

---

## ✅ LANGKAH 1 — Install Library

Buka Terminal / Command Prompt, ketik:

```
pip install streamlit pandas plotly
```

---

## ✅ LANGKAH 2 — Jalankan di Laptop

```
cd zakat-syariah
streamlit run app.py
```

Browser otomatis terbuka di: http://localhost:8501

---

## ✅ LANGKAH 3 — Deploy ke Streamlit Cloud (Online Gratis)

1. Upload semua file ke GitHub (repository baru)
2. Buka https://streamlit.io → Sign up dengan GitHub
3. Klik "New app" → pilih repo → main file: app.py
4. Klik Deploy → selesai!

---

## 📁 STRUKTUR FILE

```
zakat-syariah/
├── app.py                                    ← Beranda utama
├── requirements.txt                          ← Library
├── PANDUAN.md                                ← File ini
└── pages/
    ├── 1_🌾_Zakat_Maal_dan_Perdagangan.py   ← Zakat harta & bisnis
    ├── 2_💼_Zakat_Penghasilan.py             ← Zakat profesi/gaji
    ├── 3_🤝_Akad_Bisnis_Syariah.py           ← Panduan & simulasi akad
    └── 4_📊_Laporan_Keuangan_Islami.py       ← Laporan laba rugi syariah
```

---

## ⚠️ DISCLAIMER

Aplikasi ini bersifat EDUKATIF untuk mahasiswa kewirausahaan.
Untuk keputusan zakat yang sah, selalu konsultasikan dengan:
- BAZNAS (Badan Amil Zakat Nasional)
- Majelis Ulama Indonesia (MUI)
- Ulama atau ustadz terpercaya setempat
