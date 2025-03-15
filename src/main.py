from data.data_collection import DataCollector
from data.data_storage import StockDatabase
import datetime

# 初始化组件
api_key = 'your_api_key_here'
db = StockDatabase()
collector = DataCollector(api_key)

# 示例使用流程
try:
    # 获取历史数据
    symbol = 'AAPL'
    start = datetime.date(2023, 1, 1)
    end = datetime.date(2023, 12, 31)
    hist_data = collector.get_historical_data(symbol, start, end)
    
    # 存储到数据库
    db.store_historical_data(symbol, hist_data)
    print(f'成功存储{symbol} {len(hist_data)}条历史数据')
    
    # 获取实时报价
    quote = collector.get_realtime_quote(symbol)
    print(f'{symbol} 实时报价：{quote}')

except Exception as e:
    print(f'操作失败: {str(e)}')