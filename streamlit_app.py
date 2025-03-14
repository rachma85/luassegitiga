import streamlit as st

st.title("🎈 Aplikasi Luas Segitiga")
st.write(
    "Aplikasi ini untuk menghitung luas segitiga."
)
alas = st.number_input("Masukkan nilai alas (cm)")
st.write("Alas= ", number)
tinggi = st.number_input("Masukkan tinggi (cm)")
st.write("Tinggi= ", number)
Luas=0,5*alas*tinggi
st.write("Luas segitiga=",Luas)
