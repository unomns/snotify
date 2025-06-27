def create_all(conn):
    conn.execute("""
            CREATE TABLE IF NOT EXISTS stocks (
                symbol TEXT PRIMARY KEY,
                price REAL NOT NULL,
                time_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_chat_id TEXT UNIQUE NOT NULL,
            time_joined TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS tracked_stocks (
            user_id INTEGER NOT NULL,
            symbol TEXT NOT NULL,
            time_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (user_id, symbol),
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
    """)