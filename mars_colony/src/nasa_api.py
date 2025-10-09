# src/nasa_api.py
from datetime import date
import os
import json
import requests
from dotenv import load_dotenv
import earth_data 

load_dotenv()

API_KEY = os.getenv("NASA_API_KEY")
ROVER_API_URL = os.getenv(
    "ROVER_MAIN_API_URL"
)

class WeatherWriter:
    @staticmethod
    def mars_weather_writer(weather_data: dict):
        with open('mars_data.txt', 'w') as f:
            f.write(json.dumps(weather_data, ensure_ascii=False, indent=2, sort_keys=True))
    def earth_weather_writer(weather_data: dict):
        with open('earth_data.txt', 'w') as f:
            f.write(json.dumps(weather_data, ensure_ascii=False, indent=2, sort_keys=True))
            

class MarsRover():
    def jprint(obj):
        print(json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True))

    def fetch_latest_json(rover: str = "curiosity", camera: str | None = None) -> dict:

        url = ROVER_API_URL.format(rover=rover.lower())
        params = {"api_key": API_KEY}
        if camera:
            params["camera"] = camera.upper()  

        resp = requests.get(url, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()        
        return data

    if __name__ == "__main__":
        data = fetch_latest_json(rover="curiosity")  
        jprint(data)  

class MarsWeather():
    def fetch_weather_json(sol: int | None = None) -> dict:
        url = "https://api.nasa.gov/insight_weather/"
        params = {
            "api_key": API_KEY,
            "feedtype": "json",
            "ver": "1.0"
        }
        if sol is not None:
            params["sol"] = sol

        resp = requests.get(url, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        return data

    if __name__ == "__main__":
        weather_mars_data = fetch_weather_json() 
        weather_earth_data = earth_data.EarthData.get_earth_data()
        MarsRover.fetch_latest_json()
        WeatherWriter.mars_weather_writer(weather_mars_data)
        WeatherWriter.earth_weather_writer(weather_earth_data)