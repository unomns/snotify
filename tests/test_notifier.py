import os
import pytest
from services.notifier import TelegramNotifier

def test_send_message(monkeypatch):
    messages = []

    def fake_post(url, json, timeout):
        messages.append((url, json))
        return type("Response", (), {"status_code": 200, "json": lambda: {"ok": True}})
    
    import services.notifier
    services.notifier.httpx.post = fake_post # monkeypatch httpx.post

    notifier = TelegramNotifier(token="dummy", chat_id="123456")
    notifier.send("Test message")

    assert len(messages) == 1
    assert "sendMessage" in messages[0][0]
    assert messages[0][1]["text"] == "Test message"