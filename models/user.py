from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class User:
    id: int
    telegram_chat_id: str
    time_joined: Optional[datetime] = None