from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Stock:
    symbol: str
    price: float
    time_updated: Optional[datetime] = None