from storage.sqlite_driver import SqliteDriver
from storage.interfaces import DriverInterface


def get_db_storage(driver: str, **kwards) -> DriverInterface:
    if driver == "sqlite":
        return SqliteDriver(kwards["db_path"])

    raise NotImplementedError(f"Drive `{driver}` is not supported")
