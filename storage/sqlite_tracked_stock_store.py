import sqlite3
from typing import Optional, List
from models.tracked_stock import TrackedStock
from datetime import datetime
from storage.interfaces import TrackedStockStore


class SqliteTrackedStockStore(TrackedStockStore):
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def track(self, user_id: int,  symbol: str) -> None:
        with self.conn:
            self.conn.execute("""
                INSERT OR IGNORE INTO tracked_stocks (user_id, symbol)
                VALUES (?, ?)
            """, (user_id, symbol.upper()))

    def untrack(self, user_id: int, symbol: str) -> None:
        pass

    def list_tracked(self, user_id: int) -> List[TrackedStock]:
        cur = self.conn.cursor()
        cur.execute(
            """
            SELECT * FROM tracked_stocks
            WHERE user_id = ?
            """, (user_id,)
        )
        rows = cur.fetchall()

        return [
            TrackedStock(
                user_id=row["user_id"],
                symbol=row["symbol"],
                time_added=datetime.fromisoformat(row["time_added"])
            )
            for row in rows
        ]
