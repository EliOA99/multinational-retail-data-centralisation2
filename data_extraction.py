import pandas as pd
import requests
from io import StringIO

class DataExtractor:

    def extract_from_s3_json(self, s3_url):
        response = requests.get(s3_url)
        json_data = response.json()
        return pd.json_normalize(json_data)
