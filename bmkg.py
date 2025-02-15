import requests
import time
import json
from datetime import datetime

def fetch_bmkg_data():
    try:
        # Ambil data gempa terkini
        url = "https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json"
        response = requests.get(url)
        data = response.json()

        # Proses data gempa
        gempa = data['Infogempa']['gempa']
        tanggal = gempa['Tanggal']
        jam = gempa['Jam']
        magnitude = gempa['Magnitude']
        kedalaman = gempa['Kedalaman']
        lokasi = gempa['Wilayah']

        # Format data untuk ditampilkan
        print(f"Gempa Terkini: {lokasi}")
        print(f"Tanggal: {tanggal}, Jam: {jam}")
        print(f"Magnitude: {magnitude}, Kedalaman: {kedalaman}")

        # Simpan data ke file atau kirim ke Home Assistant
        with open("/share/bmkg_data.json", "w") as f:
            json.dump(gempa, f)

    except Exception as e:
        print(f"Error fetching BMKG data: {e}")

if __name__ == "__main__":
    while True:
        fetch_bmkg_data()
        time.sleep(60)  # Update setiap 60 detik
