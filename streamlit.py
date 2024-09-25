import streamlit as st

# Input for temperature
x = st.number_input("Masukkan Suhu")
sx = st.selectbox("Satuan", ["C", "F", "R", "K"])

# Output display
st.write("Suhu Anda:", x, "dengan satuan:", sx)

# Input for conversion target
sy = st.selectbox("Konversi ke", ["C", "F", "R", "K"])

# Temperature conversion logic
if sx == "C":
    if sy == "F":
        result = (x * 9/5) + 32  # Celsius to Fahrenheit
    elif sy == "R":
        result = x * 4/5  # Celsius to Reamur
    elif sy == "K":
        result = x + 273.15  # Celsius to Kelvin
    else:
        result = x  # Celsius to Celsius
elif sx == "F":
    if sy == "C":
        result = (x - 32) * 5/9  # Fahrenheit to Celsius
    elif sy == "R":
        result = (x - 32) * 4/9  # Fahrenheit to Reamur
    elif sy == "K":
        result = (x - 32) * 5/9 + 273.15  # Fahrenheit to Kelvin
    else:
        result = x  # Fahrenheit to Fahrenheit
elif sx == "R":
    if sy == "C":
        result = x * 5/4  # Reamur to Celsius
    elif sy == "F":
        result = (x * 9/4) + 32  # Reamur to Fahrenheit
    elif sy == "K":
        result = (x * 5/4) + 273.15  # Reamur to Kelvin
    else:
        result = x  # Reamur to Reamur
elif sx == "K":
    if sy == "C":
        result = x - 273.15  # Kelvin to Celsius
    elif sy == "F":
        result = (x - 273.15) * 9/5 + 32  # Kelvin to Fahrenheit
    elif sy == "R":
        result = (x - 273.15) * 4/5  # Kelvin to Reamur
    else:
        result = x  # Kelvin to Kelvin

# Display the conversion result
st.write("Hasil Konversi dari", x, sx, "adalah", result, sy)

