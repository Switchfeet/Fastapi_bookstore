import requests
from fastapi_bookstore import ENDPOINT
import random as rd

"""
response = requests.get(ENDPOINT)
print(response)

data = response.json()
print(data)
"""


def test_can_call_endpoint():
    """
    GIVEN a Fastapi application configured for testing
    WHEN the GET method is called
    THEN check the response is valid
    """
    response = requests.get(ENDPOINT)
    assert response.status_code == 200


def test_can_list_all_books():
    """
    GIVEN a Fastapi application configured for testing
    WHEN the GET method is called to list all books
    THEN check the response is valid
    """
    list_book_response = requests.get(ENDPOINT + "/list-books")
    assert list_book_response.status_code == 200


def test_can_get_book_by_index():
    """
    GIVEN a Fastapi application configured for testing
    WHEN the GET method is called to list book with index
    THEN check the response is valid
    """
    payload = new_book_payload()
    add_book_response = requests.post(ENDPOINT + "/add-book", json=payload)
    # add_book_response = add_book(payload)
    assert add_book_response.status_code == 200

    add_book_data = add_book_response.json()
    print(add_book_data)

    list_index_response = requests.get(ENDPOINT + f"/get-book-index?book_name={add_book_data['book_name']}")
    assert list_index_response.status_code == 200

    list_index_data = list_index_response.json()
    assert list_index_data["book"] == add_book_data["book_name"]


def test_can_get_book_by_id():
    """
    GIVEN a Fastapi application configured for testing
    WHEN the GET method is called to get book by book id
    THEN check the response is valid
    """
    payload = new_book_payload()
    add_book_response = requests.post(ENDPOINT + "/add-book", json=payload)
    assert add_book_response.status_code == 200

    add_book_data = add_book_response.json()
    print(add_book_data)

    # print(book_id)
    get_book_id_response = requests.get(ENDPOINT + f"/get-book?book_id={add_book_data['book_id']}")
    assert get_book_id_response.status_code == 200

    get_book_id_data = get_book_id_response.json()
    assert get_book_id_data["name"] == payload["name"]
    assert get_book_id_data["price"] == payload["price"]
    assert get_book_id_data["genre"] == payload["genre"]


def test_can_get_random_book():
    """
    GIVEN a Fastapi application configured for testing
    WHEN the GET method is called to get a random book
    THEN check the response is valid
    """
    random_book_response = requests.get(ENDPOINT + "/get-random-book")
    assert random_book_response.status_code == 200

    random_book_data = random_book_response.json()

    get_book_id_response = requests.get(ENDPOINT + f"/get-book?book_id={random_book_data['book_id']}")
    assert get_book_id_response.status_code == 200

    get_book_id_data = get_book_id_response.json()
    assert get_book_id_data["name"] == random_book_data["name"]
    assert get_book_id_data["price"] == random_book_data["price"]
    assert get_book_id_data["genre"] == random_book_data["genre"]


def test_can_add_book():
    """
    GIVEN a Fastapi application configured for testing
    WHEN the POST method is called to add a book
    THEN check the response is valid
    """
    payload = new_book_payload()
    add_book_response = requests.post(ENDPOINT + "/add-book", json=payload)
    assert add_book_response.status_code == 200

    add_book_data = add_book_response.json()
    print(add_book_data)

    get_book_id_response = requests.get(ENDPOINT + f"/get-book?book_id={add_book_data['book_id']}")
    assert get_book_id_response.status_code == 200

    get_book_id_data = get_book_id_response.json()
    assert get_book_id_data["name"] == payload["name"]
    assert get_book_id_data["price"] == payload["price"]
    assert get_book_id_data["genre"] == payload["genre"]


def test_can_get_delete_book_by_index():
    """
    GIVEN a Fastapi application configured for testing
    WHEN the DELETE method is called to delete a book by index
    THEN check the response is valid
    """
    payload = new_book_payload()
    add_book_response = requests.post(ENDPOINT + "/add-book", json=payload)
    assert add_book_response.status_code == 200

    add_book_data = add_book_response.json()
    print(add_book_data)

    list_index_response = requests.get(ENDPOINT + f"/get-book-index?book_name={add_book_data['book_name']}")
    assert list_index_response.status_code == 200

    list_index_data = list_index_response.json()
    assert list_index_data["book"] == add_book_data['book_name']

    delete_book_response = requests.delete(ENDPOINT + f"/delete-book-by-index/{list_index_data['index']}")
    assert delete_book_response.status_code == 200


def test_can_get_delete_book_by_name():
    """
    GIVEN a Fastapi application configured for testing
    WHEN the DELETE method is called to delete a book by name
    THEN check the response is valid
    """
    payload = {
        "name": "Testing book",
        "price": 6,
        "genre": "non-fiction"
    }
    # Add the book
    add_book_response = requests.post(ENDPOINT + "/add-book", json=payload)
    assert add_book_response.status_code == 200

    add_book_data = add_book_response.json()
    print(add_book_data)

    # Check the book was added and note the name and id
    list_index_response = requests.get(ENDPOINT + f"/get-book-index?book_name={add_book_data['book_name']}")
    assert list_index_response.status_code == 200

    list_index_data = list_index_response.json()
    assert list_index_data["book"] == add_book_data['book_name']

    delete_book_response = requests.delete(ENDPOINT + f"/delete-book?book_name={add_book_data['book_name']}")
    assert delete_book_response.status_code == 200

    # Check the book was deleted by getting the book via book id
    get_book_response = requests.get(ENDPOINT + f"/get-book?book_id={add_book_data['book_id']}")
    assert get_book_response.status_code == 404


def test_can_update_book_name():
    """
    GIVEN a Fastapi application configured for testing
    WHEN the PUT method is called to update the book name
    THEN check the response is valid
    """
    # Add the book
    payload = new_book_payload()
    add_book_response = requests.post(ENDPOINT + "/add-book", json=payload)
    assert add_book_response.status_code == 200

    # Update the book name
    add_book_data = add_book_response.json()
    print(add_book_data)
    update_book_name = "Python Testing with Pytest"

    update_book_response = requests.put(ENDPOINT + f"/update-book-name?book_name={add_book_data['book_name']}&"
                                                   f"update_name={update_book_name}")
    assert update_book_response.status_code == 200

    # Check the book name was updated via Get request
    get_book_response = requests.get(ENDPOINT + f"/get-book?book_id={add_book_data['book_id']}")
    assert get_book_response.status_code == 200

    get_book_data = get_book_response.json()
    assert get_book_data["name"] == update_book_name
    assert get_book_data["price"] == add_book_data["book_price"]


def test_can_update_book_price():
    """
    GIVEN a Fastapi application configured for testing
    WHEN the PUT method is called to update the book price
    THEN check the response is valid
    """
    # Add the book
    payload = new_book_payload()
    add_book_response = requests.post(ENDPOINT + "/add-book", json=payload)
    assert add_book_response.status_code == 200

    # Update the book price
    add_book_data = add_book_response.json()
    update_book_price = 5

    update_book_response = requests.put(ENDPOINT + f"/update-book-price?book_name={add_book_data['book_name']}&"
                                                   f"update_price={update_book_price}")
    assert update_book_response.status_code == 200

    # Check the book price was updated via Get request
    get_book_response = requests.get(ENDPOINT + f"/get-book?book_id={add_book_data['book_id']}")
    assert get_book_response.status_code == 200

    get_book_data = get_book_response.json()
    assert get_book_data["name"] == add_book_data["book_name"]
    assert get_book_data["price"] == update_book_price


def test_can_update_book_genre():
    """
    GIVEN a Fastapi application configured for testing
    WHEN the PUT method is called to update the book genre
    THEN check the response is valid
    """
    # Add the book
    payload = new_book_payload()
    add_book_response = requests.post(ENDPOINT + "/add-book", json=payload)
    assert add_book_response.status_code == 200

    # Update the book genre
    add_book_data = add_book_response.json()
    # Randomize an valid genre
    update_book_genre = rd.choice(["fiction", "non-fiction", "romance", "drama"])

    update_book_response = requests.put(ENDPOINT + f"/update-book-genre?book_name={add_book_data['book_name']}&"
                                                   f"update_genre={update_book_genre}")
    assert update_book_response.status_code == 200

    # Check the book genre was updated via Get request
    get_book_response = requests.get(ENDPOINT + f"/get-book?book_id={add_book_data['book_id']}")
    assert get_book_response.status_code == 200

    get_book_data = get_book_response.json()
    assert get_book_data["name"] == add_book_data["book_name"]
    assert get_book_data["genre"] == update_book_genre


# --------------
# Helper Function
# --------------
"""
def add_book(payload):
    requests.post(ENDPOINT + "/add-book", json=payload)


def update_book(payload):
    requests.put(ENDPOINT + "/add-book", json=payload)


def get_book(payload):
    requests.get(ENDPOINT + "/add-book", json=payload)


def delete_book(payload):
    requests.delete(ENDPOINT + "/add-book", json=payload)
"""


def new_book_payload():
    random_book = rd.choice(["The Bridges of Madison County", "Atomic Habits", "Rich Dad Poor Dad", "Harry Potter"])
    random_price = rd.choice([3, 5, 7, 9, 11])
    random_genre = rd.choice(["fiction", "non-fiction", "romance", "drama"])
    return {
        "name": random_book,
        "price": random_price,
        "genre": random_genre
    }
