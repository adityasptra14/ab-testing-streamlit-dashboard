import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as st_sns

# 1. Konfigurasi Halaman Dasar
st.set_page_config(page_title="E-Commerce A/B Testing Dashboard", layout="wide")
st.title("🛒 Dashboard A/B Testing: Optimasi Tombol Checkout")
st.markdown("""
Dashboard interaktif ini mensimulasikan uji statistik (Z-Test) untuk membandingkan performa rasio konversi (*Conversion Rate*) antara desain halaman lama (Kontrol) dengan desain halaman baru (Varian B).
""")

# 2. Sidebar untuk Kontrol Input Interaktif (Fitur Simulasi bagi User)
st.sidebar.header("⚙️ Pengaturan Eksperimen")
sample_size = st.sidebar.slider("Total Pengunjung per Varian:", min_value=1000, max_value=25000, value=5000, step=1000)
baseline_cr = st.sidebar.slider("Conversion Rate Kontrol (Lama) %:", min_value=5.0, max_value=20.0, value=12.0, step=0.5)
lift_cr = st.sidebar.slider("Estimasi Kenaikan Varian B (Lift) %:", min_value=0.1, max_value=5.0, value=1.5, step=0.1)

# 3. Proses Simulasi Data Berdasarkan Input User
st.subheader("1. Ringkasan Data Eksperimen")
col1, col2 = st.columns(2)

# Menghitung konversi untuk Kontrol A
cr_a = baseline_cr / 100
conv_a = int(sample_size * cr_a)

# Menghitung konversi untuk Varian B
cr_b = (baseline_cr + lift_cr) / 100
conv_b = int(sample_size * cr_b)

# Menampilkan metrik utama dalam format kartu (cards)
with col1:
    st.info(f"**Varian A (Desain Lama - Kontrol)**\n- Pengunjung: {sample_size:,}\n- Jumlah Pembeli: {conv_a:,}\n- Conversion Rate: **{cr_a*100:.1f}%**")

with col2:
    st.success(f"**Varian B (Desain Baru)**\n- Pengunjung: {sample_size:,}\n- Jumlah Pembeli: {conv_b:,}\n- Conversion Rate: **{cr_b*100:.1f}%**")

# 4. Melakukan Uji Statistik Z-Test untuk Proporsi
st.subheader("2. Hasil Uji Statistik (Hypothesis Testing)")

# Rumus perhitungan Z-Score dan P-Value
pooled_prob = (conv_a + conv_b) / (sample_size + sample_size)
se = np.sqrt(pooled_prob * (1 - pooled_prob) * (2 / sample_size))
z_stat = (cr_b - cr_a) / se
p_value = stats.norm.sf(abs(z_stat)) * 2 # Two-sided test

st.write(f"**P-Value yang Dihasilkan:** `{p_value:.4f}`")

# Memberikan kesimpulan bisnis otomatis berdasarkan angka P-Value
if p_value < 0.05:
    st.balloons()
    st.success("🎉 **Kesimpulan:** Perbedaan konversi **SIGNIFIKAN SECARA STATISTIK** (P-Value < 0.05). Desain baru (Varian B) terbukti lebih baik dan aman untuk diterapkan secara permanen ke seluruh pengguna.")
else:
    st.warning("⏳ **Kesimpulan:** Perbedaan konversi **TIDAK SIGNIFIKAN** (P-Value > 0.05). Tidak cukup bukti bahwa desain baru lebih baik. Disarankan untuk menambah sampel data atau mencoba desain lain.")

# 5. Visualisasi Perbandingan Conversion Rate
st.subheader("3. Visualisasi Performa Konversi")
fig, ax = plt.subplots(figsize=(8, 4))
bars = ax.bar(['Varian A (Lama)', 'Varian B (Baru)'], [cr_a*100, cr_b*100], color=['#3498db', '#2ecc71'])

# Menambahkan angka di atas grafik batang
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 0.2, f"{yval:.1f}%", ha='center', va='bottom', fontweight='bold')

ax.set_ylim(0, max(cr_a, cr_b)*100 + 3)
ax.set_ylabel('Conversion Rate (%)')
ax.set_title('Perbandingan Conversion Rate (A vs B)')
st.pyplot(fig)
