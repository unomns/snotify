# 📈 Snotify — Stock Notification service

**Snotify** is a lightweight Telegram-based stock tracker.  
It lets users subscribe to stock symbols and instantly get the current price, all from a Telegram bot.

> 🔒 This repo contains the **public core** of a real micro-SaaS project.
> The private version includes production-grade orchestration and automated price monitoring.

---

## ✨ Features

- ✅ Telegram bot integration
- ✅ SQLite backend (MySQL-ready driver-based architecture)
- ✅ Per-user stock tracking
- ✅ Instant current price response on `/track` and `/list`
- ✅ Clean, testable structure with interfaces and stores

---

## 🚀 Quickstart

### 1. Clone and Install

```bash
git clone https://github.com/unomns/snotify.git
cd snotify
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Create `.env` file

```env
TELEGRAM_BOT_TOKEN=your_bot_token
DB_PATH=data/app.db
```

### 3. Run the Bot
```bash
make run
```

> ℹ️ The bot will run in the foreground.

---

## 🛠️ Commands (Telegram)

| Command           | Description                                   |
| ----------------- | --------------------------------------------- |
| `/start`          | Register yourself as a user                   |
| `/track SYMBOL`   | Start tracking a stock (e.g. `/track AAPL`)   |
| `/untrack SYMBOL` | End tracking a stock (e.g. `/untrack AAPL`)   |
| `/list`           | Show all your tracked stocks + current prices |
