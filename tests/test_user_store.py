import os
import pytest
from storage.stock_store_factory import get_db_storage


TEST_DB_PATH = "test_data/test_users.db"


@pytest.fixture
def user_store():
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)

    return get_db_storage("sqlite", db_path=TEST_DB_PATH).user_store


def test_add_and_get_user(user_store):
    chat_id = "1234567"

    user_store.add_user(chat_id)
    user = user_store.get_user_by_chat_id(chat_id)

    assert user is not None
    assert user.telegram_chat_id == chat_id
