from dotenv import load_dotenv
import os

load_dotenv()

STOCK_URL = os.getenv("STOCK_URL", "https://")
STOCK_PORT = os.getenv("STOCK_PORT", "80")
STOCK_API_KEY = os.getenv("STOCK_API_KEY", "")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")
POLL_INTERVAL_SECONDS = int(os.getenv("POLL_INTERVAL_SECONDS", "60"))
