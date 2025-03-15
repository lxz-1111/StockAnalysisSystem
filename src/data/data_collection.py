import requests
import pandas as pd

class DataCollector:
    def __init__(self, api_key):
        self.base_url = 'https://api.example.com/stock'
        self.api_key = api_key

    def get_historical_data(self, symbol, start_date, end_date):
        params = {
            'symbol': symbol,
            'apikey': self.api_key,
            'start_date': start_date,
            'end_date': end_date
        }
        response = requests.get(f"{self.base_url}/historical", params=params)
        return pd.DataFrame(response.json())

    def get_realtime_quote(self, symbol):
        response = requests.get(f"{self.base_url}/realtime/{symbol}")
        return response.json()