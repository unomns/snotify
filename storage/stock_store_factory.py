from storage.sqlite_stock_store import SqliteStockStore
from storage.interfaces import StockStore


def get_stock_store(driver: str, **kwards) -> StockStore:
    if driver == "sqlite":
        return SqliteStockStore(kwards["db_path"])

    raise NotImplementedError(f"Drive `{driver}` is not supported")
