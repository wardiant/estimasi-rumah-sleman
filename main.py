import streamlit as st
import pickle
import numpy as np

# Muat model yang sudah disimpan (sesuaikan nama file model)
model = pickle.load(open('estimasi_rumah.sav', 'rb'))

# Judul aplikasi
st.title("Estimasi Harga Rumah")

# Form input untuk data
st.header("Masukkan Detail Rumah")
bed = st.number_input("Jumlah Kamar Tidur", min_value=0, step=1)
bath = st.number_input("Jumlah Kamar Mandi", min_value=0, step=1)
carport = st.number_input("Jumlah Carport", min_value=0, step=1)
surface_area = st.number_input("Luas Tanah (m²)", min_value=0, step=1)
building_area = st.number_input("Luas Bangunan (m²)", min_value=0, step=1)
location_encoded = st.selectbox("Lokasi Rumah (Encoded)", options=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])  # Sesuaikan pilihan lokasi jika diperlukan

# Tombol untuk memprediksi harga
if st.button("Prediksi Harga"):
    # Masukkan data ke dalam array
    features = np.array([[bed, bath, carport, surface_area, building_area, location_encoded]])
    
    # Lakukan prediksi harga
    predicted_price = model.predict(features)[0]
    
    # Tampilkan hasil prediksi
    st.success(f"Estimasi Harga Rumah: Rp {predicted_price:,.0f}")
