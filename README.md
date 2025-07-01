# 📈 Snotify — Stock Notification service

Snotify is a lightweight Telegram-based micro-SaaS that lets users subscribe to stock price changes and receive alerts directly via Telegram.

---

## ✨ Features

- ✅ Telegram bot integration
- ✅ SQLite storage backend (MySQL-ready architecture)
- ✅ Per-user stock tracking
- ✅ Price change detection
- ✅ Telegram alerts on stock updates

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

### 2. Create `.env`
```env
TELEGRAM_BOT_TOKEN=your_bot_token
DB_PATH=data/app.db
```

### 3. Run the Bot
```bash
make run
```

---

## 🛠️ Commands (Telegram)

- `/start` → Register yourself as a user

- `/track` SYMBOL → Begin tracking a stock (e.g. /track AAPL)