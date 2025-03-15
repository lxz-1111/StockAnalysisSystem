import datetime
from data.data_collection import DataCollector

# 初始化数据采集器
api_key = 'YOUR_REAL_API_KEY'  # 替换为真实API密钥
dc = DataCollector(api_key)

# 测试历史数据获取
try:
    print("测试历史数据采集...")
    hist_data = dc.get_historical_data('AAPL', 
        datetime.date(2023,1,1), 
        datetime.date(2023,12,31))
    
    print(f"获取到{len(hist_data)}条历史记录")
    print("数据结构样例:")
    print(hist_data.head())
    print("列名:", hist_data.columns.tolist())
except Exception as e:
    print("历史数据测试失败:", str(e))

# 测试实时报价
try:
    print("\n测试实时报价...")
    quote = dc.get_realtime_quote('AAPL')
    print("报价数据:")
    print(f"时间: {quote.get('timestamp')}")
    print(f"最新价: {quote.get('last_price')}")
    print(f"成交量: {quote.get('volume')}")
except Exception as e:
    print("实时报价测试失败:", str(e))