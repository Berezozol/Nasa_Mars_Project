# src/nasa_api.py
import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")
# В .env: NASA_MAIN_API_URL="https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/latest_photos"
NASA_API_URL = os.getenv(
    "NASA_MAIN_API_URL",
    "https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/latest_photos",
)

def jprint(obj):
    """Красиво печатает ЛЮБОЙ JSON-объект целиком."""
    print(json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True))

def fetch_latest_json(rover: str = "curiosity", camera: str | None = None) -> dict:
    """
    Тянет ПОЛНЫЙ JSON c /rovers/{rover}/latest_photos.
    Возвращает объект как есть (dict), ничего не срезаем.
    """
    url = NASA_API_URL.format(rover=rover.lower())
    params = {"api_key": API_KEY}
    if camera:
        params["camera"] = camera.upper()  # фильтр по камере (опционально)

    resp = requests.get(url, params=params, timeout=30)
    resp.raise_for_status()
    data = resp.json()          # <-- ВЕСЬ JSON
    return data

if __name__ == "__main__":
    data = fetch_latest_json(rover="curiosity")  # можно добавить camera="MAST"
    jprint(data)  # печать полного JSON в консоль
