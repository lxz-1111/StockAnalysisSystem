import requests
import pandas as pd

class DataCollector:
    def __init__(self, api_key):
        self.base_url = 'https://api.marketdata.com/v1'  # 替换为真实数据接口地址
        self.api_key = api_key

    def import_from_csv(self, file_path):
        """
        从CSV文件导入股票数据
        :param file_path: CSV文件路径
        :return: 包含股票数据的DataFrame
        """
        try:
            df = pd.read_csv(file_path, parse_dates=['date'])
            # 统一列名格式
            df.columns = df.columns.str.lower().str.replace(' ', '_')
            return df
        except FileNotFoundError:
            print(f"CSV文件未找到: {file_path}")
            return pd.DataFrame()
        except pd.errors.ParserError as e:
            print(f"CSV解析失败: {str(e)}")
            return pd.DataFrame()

    def get_historical_data(self, symbol, start_date, end_date):
        params = {
            'symbol': symbol,
            'apikey': self.api_key,
            'start_date': start_date,
            'end_date': end_date
        }
        try:
            response = requests.get(f"{self.base_url}/historical", params=params)
            response.raise_for_status()
            return pd.DataFrame(response.json())
        except requests.exceptions.RequestException as e:
            print(f"历史数据获取失败: {str(e)}")
            return pd.DataFrame()

    def get_realtime_quote(self, symbol):
        try:
            response = requests.get(f"{self.base_url}/realtime/{symbol}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"实时报价获取失败: {str(e)}")
            return {}

    def get_index_data(self, index_code, days=30):
        """
        获取主流指数数据
        :param index_code: 指数代码（如hs300, spx）
        :param days: 最近天数
        :return: 包含指数数据的DataFrame
        """
        params = {
            'index': index_code,
            'apikey': self.api_key,
            'days': days
        }
        try:
            response = requests.get(f"{self.base_url}/indices", params=params)
            response.raise_for_status()
            return pd.DataFrame(response.json())
        except requests.exceptions.RequestException as e:
            print(f"指数数据获取失败: {str(e)}")
            return pd.DataFrame()