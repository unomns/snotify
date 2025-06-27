from services.fetcher import StockFetcher
from services.notifier import TelegramNotifier
import config


def main():
    l = StockFetcher()
    price = l.get_current_price("^GSPC")
    print(f"S&P500 price is: ${price}")

    n = TelegramNotifier(config.TELEGRAM_BOT_TOKEN, config.TELEGRAM_CHAT_ID)
    n.send("🚨 Price alert for AAPL: 150.00 → 152.75")


main()
