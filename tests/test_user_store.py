import os
import pytest
from storage.user_store import UserStore
from storage.schema import create_all


TEST_DB_PATH = "test_data/test_users.db"


@pytest.fixture
def user_store():
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)

    from sqlite3 import connect
    conn = connect(TEST_DB_PATH)
    create_all(conn)
    return UserStore(conn)

def test_add_and_get_user(user_store):
    chat_id = "1234567"

    user_store.add_user(chat_id)
    user = user_store.get_user_by_chat_id(chat_id)

    assert user is not None
    assert user.telegram_chat_id == chat_id