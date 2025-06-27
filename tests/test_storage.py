import os
import pytest
from storage.stock_store_factory import get_db_storage
from models.stock import Stock

TEST_DB_PATH = "test_data/test_stock.db"

@pytest.fixture
def store():
    # Ensure test DB directory exists
    os.makedirs("test_data", exist_ok=True)
    
    # Remove existing DB before each run
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)
    
    return get_db_storage("sqlite", db_path=TEST_DB_PATH)

def test_save_and_load_stock_price(store):
    s = Stock(symbol="^GSPC", price=5500.00)

    store.stock_store.save_price(s)
    loaded_price = store.stock_store.load_price(s.symbol).price

    assert isinstance(loaded_price, float)
    assert loaded_price == s.price
