import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import json
from pathlib import Path

# Tentukan folder data relatif terhadap file skrip
BASE_DIR = Path(__file__).parent  # folder di mana skrip ini berada
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)  # buat folder kalau belum ada
JSON_FILE = DATA_DIR / "pesan.json"

st.title("Pemtek A💖")

# Isi salam — kamu bisa ganti langsung di sini
nama = "P2 Gacor"
AsprakPeTu = "Irpunk_Sartaq_Gipps"

# Gambar hati
t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t)**3
y = (12 * np.cos(t) 
     - 5 * np.cos(2 * t) 
     - 3 * np.cos(3 * t) 
     - np.cos(4 * t))

fig, ax = plt.subplots(figsize=(7,6))
ax.fill(x, y, color='red', alpha=0.9)
ax.text(0, 0, f"Hi guyss, Selamat menamatkan \npraktikum pemtek iaa, \nTengkyu atas kerjasamanya, \nand cemungutss projeknyaa, \n{nama} ", fontsize=18, 
        color="white", ha='center', va='center')
ax.set_aspect('equal')
ax.axis('off')
st.write("")
st.markdown(f"**Asprak PeDuaa,**  \n{AsprakPeTu}")
st.pyplot(fig)

# — kode plotting hati & salam kamu tetap sama — #

st.write("---")

st.subheader("Kesan Pesannya Gusyy 💬")

with st.form("form_pesan"):
    pengirim_pesan = st.text_input("Nama (nama panggung):", "")
    pesan = st.text_area("Gaskkann Isi:", "", height=150)
    submitted = st.form_submit_button("Submit y")

if submitted:
    data = {
        "pengirim": pengirim_pesan,
        "pesan": pesan
    }

    # baca dulu jika file ada
    if JSON_FILE.exists():
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            try:
                all_data = json.load(f)
                if not isinstance(all_data, list):
                    all_data = []
            except json.JSONDecodeError:
                all_data = []
    else:
        all_data = []

    all_data.append(data)

    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)

    st.success("Terima kasih! P2 ❤️")
    st.write("👉 Data tersimpan di:", JSON_FILE)

st.subheader("🔒 Asprak Archive")

password = st.text_input("ssttt:", type="password")
if password == "PeDua":
    if JSON_FILE.exists():
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            all_data = json.load(f)
        st.write("Submitted:", len(all_data))
        for idx, d in enumerate(all_data, 1):
            st.write(f"**KesanPesan {idx}**")
            st.write("Dari:", d.get("pengirim", "Anonim"))
            st.write("Isi:", d.get("pesan", ""))
            st.write("---")
    else:
        st.write("Belum ada data.")
elif password:
    st.error("Password salah.")
