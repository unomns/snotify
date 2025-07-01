from telegram.ext import ApplicationBuilder
from bot.dispatcher import register_handlers
from config.config import TELEGRAM_BOT_TOKEN


def main():
    print(f"starting.. bot_token:{TELEGRAM_BOT_TOKEN}")
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    register_handlers(app)
    app.run_polling()


main()
