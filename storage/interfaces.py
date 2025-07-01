from abc import ABC, abstractmethod
from models.stock import Stock
from models.user import User
from models.tracked_stock import TrackedStock
from typing import Optional, List


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
    def get_user_by_chat_id(self, chat_id: str)-> Optional[User]:
        pass


class TrackedStockStore(ABC):
    @abstractmethod
    def track(self, user_id: int,  symbol: str) -> None:
        pass

    @abstractmethod
    def untrack(self, user_id: int, symbol: str) -> None:
        pass

    @abstractmethod
    def list_tracked(self, user_id: int) -> List[TrackedStock]:
        pass


class DatabaseDriverInterface(ABC):
    user_store: UserStore
    stock_store: StockStore
    tracked_store: TrackedStockStore

    @abstractmethod
    def close(self) -> None:
        pass
