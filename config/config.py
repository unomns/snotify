from dotenv import load_dotenv
import os

load_dotenv()

# Telegram
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")
POLL_INTERVAL_SECONDS = int(os.getenv("POLL_INTERVAL_SECONDS", "60"))

# Database
DB_DRIVER = os.getenv("DB_DRIVER", "sqlite")
DB_PATH = os.getenv("DB_PATH", "data/app.db")
