from mpi4py import MPI
import requests
import json

API_KEY = "MASUKKAN_API_KEY_KAMU"  # Ganti dengan API key OpenWeatherMap
cities = ["Jakarta", "Surabaya", "Bandung", "Medan"]

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

results = []

if rank < len(cities):
    city = cities[rank]
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    r = requests.get(url)
    data = r.json()
    temp = data["main"]["temp"]
    results.append({"city": city, "temp": temp})

# Simpan hasil ke JSON
with open("hasil_cuaca.json", "w") as f:
    json.dump(results, f)
