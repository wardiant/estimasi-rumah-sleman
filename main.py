import streamlit as st
import pickle
import numpy as np

# Muat model yang sudah disimpan (sesuaikan nama file model)
model = pickle.load(open('estimasi_rumah.sav', 'rb'))

# Dictionary untuk lokasi dengan value numerik
locations = {
    "Berbah, Sleman": 0,
    "Depok, Sleman": 1,
    "Gamping, Sleman": 2,
    "Godean, Sleman": 3,
    "Kalasan, Sleman": 4,
    "Minggir, Sleman": 5,
    "Mlati, Sleman": 6,
    "Moyudan, Sleman": 7,
    "Ngaglik, Sleman": 8,
    "Ngemplak, Sleman": 9,
    "Pakem, Sleman": 10,
    "Prambanan, Sleman": 11,
    "Sayegan, Sleman": 12,
    "Sleman, Sleman": 13,
    "Tempel, Sleman": 14,
    "Turi, Sleman": 15,
}

# Judul aplikasi
st.title("Estimasi Harga Rumah")

# Form input untuk data
st.header("Masukkan Detail Rumah")
bed = st.number_input("Jumlah Kamar Tidur", min_value=0, step=1)
bath = st.number_input("Jumlah Kamar Mandi", min_value=0, step=1)
carport = st.number_input("Jumlah Carport", min_value=0, step=1)
surface_area = st.number_input("Luas Tanah (m²)", min_value=0, step=1)
building_area = st.number_input("Luas Bangunan (m²)", min_value=0, step=1)
# Dropdown untuk memilih lokasi
location_name = st.selectbox("Pilih Lokasi", options=list(locations.keys()))
location_encoded = locations[location_name]

# Tombol untuk memprediksi harga
if st.button("Prediksi Harga"):
    # Masukkan data ke dalam array
    features = np.array([[bed, bath, carport, surface_area, building_area, location_encoded]])
    
    # Lakukan prediksi harga
    predicted_price = model.predict(features)[0]
    
    # Tampilkan hasil prediksi
    st.success(f"Estimasi Harga Rumah: Rp {predicted_price:,.0f}")
