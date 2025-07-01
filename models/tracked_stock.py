from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class TrackedStock:
    user_id: int
    symbol: str
    time_added: Optional[datetime] = None