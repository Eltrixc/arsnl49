import streamlit as st

x = st.number_input("Masukkan Suhu")
sx = st.text_input("Satuan", "C")
st.write("Suhu Anda", x, "dengan satuan", sx)
st.write("Kuadratnya", x*x)
