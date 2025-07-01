import logging
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from storage.sqlite_driver import SqliteDriver
from config.config import DB_PATH
from services.fetcher import StockFetcher


driver = SqliteDriver(DB_PATH)
fetcher = StockFetcher()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger(__name__)


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

    try:
        price = fetcher.get_current_price(symbol)
        message = f"✅ You're now tracking <b>{symbol}</b>\nCurrent price: $<b>{price}</b>"
    except Exception as e:
        logger.warning(
            f"Track. Failed to fetch price for '{symbol}' (user {chat_id}): {e}")
        message = f"✅ You're now tracking <b>{symbol}</b>\nPrice is currently unavailable."

    await context.bot.send_message(chat_id=chat_id, text=message, parse_mode="HTML")


async def untrack(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = str(update.effective_chat.id)
    if len(context.args) != 1:
        await context.bot.send_message(
            chat_id=chat_id,
            text="❗ Usage: /untrack SYMBOL"
        )
        return

    symbol = context.args[0].upper()

    user = driver.user_store.get_user_by_chat_id(chat_id=chat_id)
    if user is None:
        await context.bot.send_message(chat_id=chat_id, text="Could not find your account. Try /start one more time.")
        return

    driver.tracked_stock_store.untrack(user.id, symbol)

    await context.bot.send_message(
        chat_id=chat_id,
        text=f"You are no longer tracking <b>{symbol}</b>",
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
        return

    lines = []
    for ts in tracked:
        try:
            price = fetcher.get_current_price(ts.symbol)
            lines.append(f"- <b>{ts.symbol}</b>: ${price}")
        except Exception as e:
            logger.warning(
                f"ListTracked. Failed to fetch price for '{ts.symbol}' (user {chat_id}): {e}")
            lines.append(f"- <b>{ts.symbol}</b>: (price unavailable)")

    text = "You're tracking:\n" + "\n".join(lines)
    await context.bot.send_message(chat_id=chat_id, text=text, parse_mode="HTML")


def register_handlers(application):
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("track", track))
    application.add_handler(CommandHandler("untrack", untrack))
    application.add_handler(CommandHandler("list", list_tracked))
