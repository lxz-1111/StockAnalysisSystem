import sqlite3
from datetime import datetime

class StockDatabase:
    def __init__(self, db_path='stocks.db'):
        self.conn = sqlite3.connect(db_path)
        self._create_tables()

    def _create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS historical_data (
                symbol TEXT,
                date DATE,
                open REAL,
                high REAL,
                low REAL,
                close REAL,
                volume INTEGER,
                PRIMARY KEY (symbol, date)
            )
        ''')
        self.conn.commit()

    def store_historical_data(self, symbol, df):
        df['symbol'] = symbol
        df.to_sql('historical_data', self.conn, if_exists='append', index=False)