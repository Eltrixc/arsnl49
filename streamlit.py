import streamlit as st

x = st.number_input("Masukkan Suhu")
sx = st.text_input("Satuan", "C")
st.write("Suhu Anda", x, "dengan satuan", sx)
sx = st.text_input("Konversi", "C")
if (sx == "C"):
  pass
else:
  pass

st.write("Hasil Konversi dari ", x, sx, "adalah ...", sy)
