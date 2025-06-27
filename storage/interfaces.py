from abc import ABC, abstractmethod
from models.stock import Stock
from typing import Optional

class StockStore(ABC):
    @abstractmethod
    def save_price(self, stock: Stock) -> None:
        pass

    @abstractmethod
    def load_price(self, symbol: str) -> Optional[Stock]:
        pass