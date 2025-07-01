import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from storage.sqlite_driver import SqliteDriver
from config import DB_PATH, TELEGRAM_BOT_TOKEN

driver = SqliteDriver(DB_PATH)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = str(update.effective_chat.id)
    driver.user_store.add_user(chat_id)
    await context.bot.send_message(
        chat_id=chat_id,
        text="👋 Welcome! You're now registered.\nUse /track SYMBOL to monitor a stock."
    )


async def track(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = str(update.effective_chat.id)
    if len(context.args) != 1:
        await context.bot.send_message(
            chat_id=chat_id,
            text="❗ Usage: /track SYMBOL"
        )
        return

    symbol = context.args[0].upper()

    user = driver.user_store.get_user_by_chat_id(chat_id=chat_id)
    if user is None:
        await context.bot.send_message(chat_id=chat_id, text="Could not find your account. Try /start one more time.")
        return

    driver.tracked_stock_store.track(user.id, symbol)

    await context.bot.send_message(
        chat_id=chat_id,
        text=f"You're tracking: <b>{symbol}</b>",
        parse_mode="HTML"
    )


async def list_tracked(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = str(update.effective_chat.id)

    user = driver.user_store.get_user_by_chat_id(chat_id=chat_id)
    if user is None:
        await context.bot.send_message(chat_id=chat_id, text="Could not find your account. Try /start one more time.")
        return

    tracked = driver.tracked_stock_store.list_tracked(user.id)
    if not tracked:
        await context.bot.send_message(chat_id=chat_id, text="You're not tracking any stocks yet.")
    else:
        lines = [f"- {ts.symbol}" for ts in tracked]
        text = "You're tracking:\n" + "\n".join(lines)
        await context.bot.send_message(chat_id=chat_id, text=text)


def main():
    print(f"starting.. bot_token:{TELEGRAM_BOT_TOKEN}")
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("track", track))
    app.add_handler(CommandHandler("list", list_tracked))

    app.run_polling()


if __name__ == "__main__":
    main()

# TODO: Add auto-reloading (watchdog)
