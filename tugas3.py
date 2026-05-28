import streamlit as st
import pandas as pd
import os

# =============================
# FILE PENYIMPANAN DATA
# =============================
FILE_DATA = "data_mahasiswa.csv"

# =============================
# FUNCTION LOGIN
# =============================
def login():
    st.subheader("🔐 Login Sistem")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "dilla" and password == "akudilla":
            st.session_state["login"] = True
            st.success("Login berhasil!")
        else:
            st.error("Username / Password salah")

# =============================
# FUNCTION HITUNG NILAI
# =============================
def hitung_nilai(tugas, uts, uas):
    nilai_akhir = (0.3 * tugas) + (0.3 * uts) + (0.4 * uas)

    # RULE-BASED SYSTEM (IF-THEN)
    if nilai_akhir >= 85:
        grade = "A"
        ket = "Sangat Baik"
    elif nilai_akhir >= 75:
        grade = "B"
        ket = "Baik"
    elif nilai_akhir >= 65:
        grade = "C"
        ket = "Cukup"
    else:
        grade = "D"
        ket = "Kurang"

    return nilai_akhir, grade, ket

# =============================
# LOAD DATA
# =============================
def load_data():
    if os.path.exists(FILE_DATA):
        return pd.read_csv(FILE_DATA)
    else:
        return pd.DataFrame(columns=[
            "Nama", "NIM", "Tugas", "UTS", "UAS",
            "Nilai Akhir", "Grade", "Keterangan"
        ])

# =============================
# SIMPAN DATA
# =============================
def save_data(df):
    df.to_csv(FILE_DATA, index=False)

# =============================
# MAIN APP
# =============================
st.set_page_config(page_title="Penilaian Mahasiswa", layout="centered")
st.title("🎓 Sistem Penilaian Mahasiswa")

# SESSION LOGIN
if "login" not in st.session_state:
    st.session_state["login"] = False

if not st.session_state["login"]:
    login()
else:
    menu = st.sidebar.selectbox(
        "Menu",
        ["Input Nilai", "Data Mahasiswa", "Logout"]
    )

    # =============================
    # INPUT NILAI
    # =============================
    if menu == "Input Nilai":
        st.subheader("📊 Input Nilai Mahasiswa")

        nama = st.text_input("Nama")
        nim = st.text_input("NIM")
        tugas = st.number_input("Nilai Tugas", 0, 100)
        uts = st.number_input("Nilai UTS", 0, 100)
        uas = st.number_input("Nilai UAS", 0, 100)

        if st.button("Simpan"):
            if nama == "" or nim == "":
                st.warning("Nama & NIM wajib diisi!")
            else:
                nilai_akhir, grade, ket = hitung_nilai(tugas, uts, uas)

                data = load_data()

                data_baru = pd.DataFrame([{
                    "Nama": nama,
                    "NIM": nim,
                    "Tugas": tugas,
                    "UTS": uts,
                    "UAS": uas,
                    "Nilai Akhir": nilai_akhir,
                    "Grade": grade,
                    "Keterangan": ket
                }])

                data = pd.concat([data, data_baru], ignore_index=True)
                save_data(data)

                st.success("Data berhasil disimpan!")

                st.write("### Hasil:")
                st.write("Nilai Akhir:", round(nilai_akhir, 2))
                st.write("Grade:", grade)
                st.write("Keterangan:", ket)

    # =============================
    # DATA MAHASISWA (READ + DELETE)
    # =============================
    elif menu == "Data Mahasiswa":
        st.subheader("📋 Data Mahasiswa")

        data = load_data()

        if data.empty:
            st.info("Belum ada data")
        else:
            st.dataframe(data)

            st.subheader("🗑️ Hapus Data")
            index_hapus = st.number_input(
                "Masukkan index data yang ingin dihapus",
                min_value=0,
                max_value=len(data)-1,
                step=1
            )

            if st.button("Hapus"):
                data = data.drop(index_hapus).reset_index(drop=True)
                save_data(data)
                st.success("Data berhasil dihapus!")

    # =============================
    # LOGOUT
    # =============================
    elif menu == "Logout":
        st.session_state["login"] = False
        st.warning("Berhasil logout")