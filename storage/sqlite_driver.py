import sqlite3
from storage.schema import create_all
from storage.sqlite_user_store import SqliteUserStore
from storage.sqlite_stock_store import SqliteStockStore
from storage.interfaces import DatabaseDriverInterface

class SqliteDriver(DatabaseDriverInterface):
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        create_all(self.conn)

        self.user_store = SqliteUserStore(self.conn)
        self.stock_store = SqliteStockStore(self.conn)

    def close(self):
        self.conn.close()