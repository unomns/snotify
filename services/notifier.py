import httpx


class TelegramNotifier:

    def __init__(self, token: str, chat_id: str):
        self.token = token
        self.chat_id = chat_id

    def send(self, msg: str) -> None:
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        payload = {
            "chat_id": self.chat_id,
            "text": msg,
            "parse_mode": "HTML",
        }
        res = httpx.post(url, json=payload, timeout=10)

        if res.status_code != 200 or not res.json().get("ok"):
            raise Exception(f"Telegram send failed: {res.text}")
