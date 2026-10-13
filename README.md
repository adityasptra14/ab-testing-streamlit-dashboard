# 🛒 End-to-End E-Commerce A/B Testing Dashboard

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]([https://ab-testing-app-dashboard-cj2v8slsrbjxqkc3uk3cdu.streamlit.app/#dashboard-a-b-testing-optimasi-tombol-checkout])

## 📌 Latar Belakang Bisnis (Business Problem)
Dalam operasional *E-Commerce*, perubahan kecil pada antarmuka pengguna (seperti warna atau posisi tombol *Checkout*) dapat berdampak signifikan terhadap total pendapatan. Namun, memutuskan apakah desain baru (Varian B) lebih baik dari desain lama (Kontrol A) tidak bisa didasarkan pada intuisi atau selisih persentase semata.

Proyek ini mendemonstrasikan proses eksperimen bisnis menggunakan uji hipotesis statistik (*A/B Testing*) yang dibalut ke dalam **Aplikasi Web Interaktif** agar pemangku kepentingan (manajemen) dapat melakukan simulasi data dan melihat bukti signifikansinya secara langsung.

---

## 🚀 Fitur Aplikasi (Live Dashboard)
Silakan klik *badge* **Streamlit** di atas atau tautan berikut untuk mencoba aplikasinya secara langsung:
👉 **[Live A/B Testing Dashboard]([https://ab-testing-app-dashboard-cj2v8slsrbjxqkc3uk3cdu.streamlit.app/#dashboard-a-b-testing-optimasi-tombol-checkout])**

*   **Interactive Simulation:** Pengguna dapat mengatur ukuran sampel (*traffic*) dan estimasi *Conversion Rate* (CR).
*   **Real-time Statistical Engine:** Sistem otomatis menghitung *Z-Score* dan *P-Value* di latar belakang.
*   **Automated Business Verdict:** Menyimpulkan secara instan apakah perbedaan konversi tersebut **"Signifikan secara Statistik"** (siap diluncurkan) atau **"Tidak Signifikan"** (butuh lebih banyak data/pengunjung).
*   **Dynamic Visualization:** Menggunakan `Plotly` untuk menyajikan perbandingan konversi yang responsif saat parameter diubah.

---

## 🛠️ Tools & Metodologi (Tech Stack)
*   **Web Framework:** `Streamlit`
*   **Data Processing:** `Pandas`, `NumPy`
*   **Statistical Analysis:** `Scipy` (Z-Test for Proportions)
*   **Data Visualization:** `Plotly Express`

---

## 📂 Struktur File di Repository Ini
*   `ab_testing_dashboard.py` — *Script* utama Python yang memuat mesin statistik uji hipotesis dan logika antarmuka Streamlit.
*   `requirements.txt` — Daftar dependensi *library* (Streamlit, Pandas, Scipy, Plotly) yang digunakan untuk proses *deployment* otomatis di Streamlit Cloud.
