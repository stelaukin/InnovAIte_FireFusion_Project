import json
import random
from pathlib import Path


class GeoJsonService:
    def __init__(self):
        pass


    def get_geojson(self):

        choice = str(random.randint(0, 9))

        data_file = Path(__file__).resolve().parents[2] / "data" / f"geojson_data-{choice}.json"
        data = json.loads(data_file.read_text())

        return {
            "type": "FeatureCollection",
            "features": data
        }