import streamlit as st

st.title("🎈 Aplikasi Luas Segitiga")
st.write(
    "Aplikasi ini untuk menghitung luas segitiga."
)
alas = st.number_input("Masukkan nilai alas (cm)")
st.write("Alas= ", alas)
tinggi = st.number_input("Masukkan tinggi (cm)")
st.write("Tinggi= ", tinggi)
Luas=(alas*tinggi)/2
st.write("Luas segitiga=",Luas)
