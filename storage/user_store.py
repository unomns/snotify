from typing import Optional
from models.user import User
from datetime import datetime
import sqlite3


class UserStore:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.conn.row_factory = sqlite3.Row

    def add_user(self, chat_id: str) -> None:
        with self.conn:
            self.conn.execute(
                """
                INSERT OR IGNORE INTO users (telegram_chat_id) VALUES (?)
                """, (chat_id,)
            )

    def get_user_by_chat_id(self, chat_id: str) -> Optional[User]:
        cur = self.conn.cursor()
        cur.execute(
            "SELECT * FROM users WHERE telegram_chat_id = ?", (chat_id,))
        row = cur.fetchone()

        if row:
            return User(
                id=row["id"],
                telegram_chat_id=row["telegram_chat_id"],
                time_joined=datetime.fromisoformat(row["time_joined"])
            )

        return None