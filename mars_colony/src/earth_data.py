import json

import requests




class EarthData:
    def __init__(self):
        self.data = "Earth data for Mars colony operations"

    def get_earth_data():
        def jprint(obj):
            print(json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True))
        
        def fetch_earth_json() -> dict:
            url = "https://api.nasa.gov/planetary/earth/assets"
            params = {
                "api_key": "DEMO_KEY",
                "lon": 100.75,
                "lat": 1.5,
                "dim": 0.1,
                "date": "2014-02-01"
            }
            resp = requests.get(url, params=params, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            return data