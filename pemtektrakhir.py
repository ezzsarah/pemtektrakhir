import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.set_page_config(page_title="Pemtek A💖", layout="centered")

st.title("Pemtek A💖")

# Salam & gambar hati
nama = "P2 Gacor"
AsprakPeTu = "Irpunk_Sartaq_Gipps"

t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t)**3
y = (12 * np.cos(t)
     - 5 * np.cos(2 * t)
     - 3 * np.cos(3 * t)
     - np.cos(4 * t))

fig, ax = plt.subplots(figsize=(7,6))
ax.fill(x, y, color='red', alpha=0.9)
ax.text(0, 0, f"Hi guyss, Selamat menamatkan \npraktikum pemtek iaa, \nTengkyu atas kerjasamanya, \nand cemungutss projeknyaa, \n{nama} ",
        fontsize=18, color="white", ha='center', va='center')
ax.set_aspect('equal')
ax.axis('off')
st.pyplot(fig)

st.markdown(f"**Asprak PeDuaa,**  \n{AsprakPeTu}")

st.write("---")
st.subheader("Kesan Pesannya Gusyy 💬")

# --- Setup koneksi ke Google Sheets ---
conn = st.connection("gsheets", type=GSheetsConnection)

# Worksheet / sheet name misalnya "Sheet1"
WS_NAME = "Sheet1"

with st.form("form_pesan"):
    pengirim_pesan = st.text_input("Nama (nama panggung):", "")
    pesan = st.text_area("Gaskkann Isi:", "", height=150)
    submitted = st.form_submit_button("Submit y")

if submitted:
    if pengirim_pesan.strip() and pesan.strip():
        new_row = {"Nama": pengirim_pesan, "Pesan": pesan}
        conn.append(worksheet=Sheet1, data=[new_row])
        st.success("Terima kasih! P2 ❤️")
    else:
        st.warning("Nama dan pesan tidak boleh kosong.")

st.subheader("🔒 Asprak Archive")
password = st.text_input("ssttt:", type="password")
if password == "PeDua":
    try:
        df = conn.read(worksheet=WS_NAME)
        st.write("Submitted:", len(df))
        for idx, row in df.iterrows():
            st.write(f"**KesanPesan {idx+1}**")
            st.write("Dari:", row.get("Nama", "Anonim"))
            st.write("Isi:", row.get("Pesan", ""))
            st.write("---")
    except Exception as e:
        st.error("Gagal membaca data — cek konfigurasi Google Sheet & permission.")
elif password:
    st.error("Password salah.")

