import pytest
import requests
from fastapi_bookstore import ENDPOINT


# --------
# Fixtures
# --------

@pytest.fixture()
def get_endpoint():
    requests.get(ENDPOINT)


@pytest.fixture()
def add_book(payload):
    requests.post(ENDPOINT + "/add-book", json=payload)


@pytest.fixture()
def get_book_by_id():
    pass


@pytest.fixture()
def new_book_payload():
    return {
        "name": "Secret",
        "price": 5,
        "genre": "non-fiction"
    }
