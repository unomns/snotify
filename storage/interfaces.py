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


class UserStore(ABC):
    @abstractmethod
    def add_user(self, chat_id: str):
        pass

    @abstractmethod
    def get_user_by_chat_id(self, chat_id: str):
        pass


class DriverInterface(ABC):
    user_store: UserStore
    stock_store: StockStore

    @abstractmethod
    def close(self) -> None:
        pass
