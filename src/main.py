from flask import Flask, render_template, request, redirect
from data.data_collection import DataCollector
from data.data_storage import StockDatabase
import datetime

app = Flask(__name__, template_folder='../web/templates', static_folder='../web/static')

# 初始化组件
api_key = 'YOUR_REAL_API_KEY'  # 请替换为真实API密钥
db = StockDatabase()
collector = DataCollector(api_key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def handle_submit():
    symbol = request.form['symbol']
    
    # 移除重复初始化，使用全局组件
    # 添加调试日志
    print(f"开始获取{symbol}历史数据，时间范围：{start_date}至{end_date}")
    
    try:
        # 获取最近30天历史数据
        end_date = datetime.date.today()
        start_date = end_date - datetime.timedelta(days=30)
        hist_data = collector.get_historical_data(symbol, start_date, end_date)
        
        if not hist_data.empty:
            db.store_historical_data(symbol, hist_data)
            return redirect(f'/success?symbol={symbol}&count={len(hist_data)}')
        print(f"获取到空数据集，响应状态：{hist_data.shape}")
        return "未获取到有效数据，请检查股票代码有效性"
    except Exception as e:
        print(f"数据获取异常：{str(e)}")
        return f"数据获取失败: {str(e)}，请检查API密钥配置"

@app.route('/success')
def show_success():
    symbol = request.args.get('symbol')
    count = request.args.get('count')
    return f'成功录入{symbol} {count}条数据'

if __name__ == '__main__':
    app.run(debug=True)

    try:
        if choice == '1':
            file_path = input("请输入CSV文件路径: ")
            df = collector.import_from_csv(file_path)
            if not df.empty:
                symbol = input("请输入股票代码: ")
                db.store_historical_data(symbol, df)
                print(f"成功导入{symbol} {len(df)}条数据")
        
        elif choice in ('2', '3', '4'):
            symbol = input("请输入股票代码: ")
            
            if choice == '2':
                start = input("开始日期(YYYY-MM-DD): ")
                end = input("结束日期(YYYY-MM-DD): ")
                start_date = datetime.datetime.strptime(start, "%Y-%m-%d").date()
                end_date = datetime.datetime.strptime(end, "%Y-%m-%d").date()
                hist_data = collector.get_historical_data(symbol, start_date, end_date)
                if not hist_data.empty:
                    db.store_historical_data(symbol, hist_data)
                    print(f"成功存储{symbol} {len(hist_data)}条历史数据")
            
            if choice == '3':
                quote = collector.get_realtime_quote(symbol)
                print(f"最新报价:\n{quote}")
            
            if choice == '4':
                index_code = input("请输入指数代码(如hs300/spx): ").lower()
                days = int(input("查询最近多少天数据: "))
                index_df = collector.get_index_data(index_code, days)
                if not index_df.empty:
                    db.store_historical_data(index_code, index_df)
                    print(f"成功存储{index_code}指数{len(index_df)}条数据")

        else:
            print("无效的输入，请重新选择")
    
    except Exception as e:
        print(f"操作失败: {str(e)}")