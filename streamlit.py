import streamlit as st

# Input for temperature
x = st.number_input("Masukkan Suhu")
sx = st.selectbox("Satuan", ["C", "F"])

# Output display
st.write("Suhu Anda:", x, "dengan satuan:", sx)

# Input for conversion target
sy = st.selectbox("Konversi ke", ["C", "F"])

# Temperature conversion logic
if sx == "C" and sy == "F":
    result = (x * 9/5) + 32  # Celsius to Fahrenheit
elif sx == "F" and sy == "C":
    result = (x - 32) * 5/9  # Fahrenheit to Celsius
else:
    result = x  # No conversion needed

# Display the conversion result
st.write("Hasil Konversi dari", x, sx, "adalah", result, sy)
