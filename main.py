from flask import Flask, request, render_template
import pickle
import numpy as np

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Muat model yang sudah disimpan (sesuaikan nama file model)
model = pickle.load(open('estimasi_rumah.sav', 'rb'))

# Halaman utama
@app.route('/')
def home():
    return render_template('index.html')

# Endpoint untuk prediksi
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Ambil data input dari form
        bed = int(request.form['bed'])
        bath = int(request.form['bath'])
        carport = int(request.form['carport'])
        surface_area = int(request.form['surface_area'])
        building_area = int(request.form['building_area'])
        location_encoded = int(request.form['location_encoded'])
        
        # Masukkan data ke dalam array
        features = np.array([[bed, bath, carport, surface_area, building_area, 
                            location_encoded]])

        # Prediksi harga
        predicted_price = model.predict(features)[0]

        # Tampilkan hasil
        return render_template('index.html', 
                               prediction_text=f"Estimasi Harga Rumah: Rp {predicted_price:,.0f}")
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
