import sqlite3
from typing import Optional
from models.stock import Stock
from datetime import datetime

class SQLiteStockStore:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self._init_table()

    def _init_table(self):
        with self.conn:
            self.conn.execute(
                """
                CREATE TABLE IF NOT EXISTS stocks (
                    symbol TEXT PRIMARY KEY,
                    price REAL NOT NULL,
                    time_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                """
            )

    def save_price(self, s: Stock):
        with self.conn:
            self.conn.execute(
                """
                INSERT INTO stocks (symbol, price)
                VALUES (?, ?)
                ON CONFLICT(symbol) DO UPDATE SET price=excluded.price, time_updated=CURRENT_TIMESTAMP;
                """, (s.symbol, s.price)
            )

    def load_price(self, symbol: str) -> Optional[Stock]:
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM stocks WHERE symbol = ?", (symbol,))
        row = cur.fetchone()

        if row:
            return Stock(
                symbol=row["symbol"],
                price=row["price"],
                time_updated=datetime.fromisoformat(row["time_updated"])
            )
        
        return None
