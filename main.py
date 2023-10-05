import json
from typing import Optional, Literal
from uuid import uuid4
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
import os.path
import random as rd
from pydantic import BaseModel

app = FastAPI()


# Book Model
class Book(BaseModel):
    name: str
    price: float
    genre: Literal["fiction", "non-fiction", "romance", "drama"]
    book_id: Optional[str] = uuid4().hex


BOOKS_FILE = "books.json"
BOOK_DATABASE = []

if os.path.exists(BOOKS_FILE):
    with open(BOOKS_FILE, "r") as f:
        BOOK_DATABASE = json.load(f)


# /
@app.get("/")
async def home():
    return {"Message": "Welcome to my bookstore!"}


# /list-books
@app.get("/list-books")
async def list_books():
    return {"books": BOOK_DATABASE}


# /list-books-index
@app.get("/list-books-index")
def list_books_index():
    for index in range(len(BOOK_DATABASE)):
        yield {"books": f"Index {index} is {BOOK_DATABASE[index]['name']}."}


"""
# Experiment
# Put for loop in yield won't return
"""
"""
# /list-books-index
@app.get("/list-books-index")
def list_books_index():
    print("IN")
    yield {"books": f"Index {index} is {BOOK_DATABASE[index]['name']}." for index in range(len(BOOK_DATABASE))}
"""


# /book-by-index/{index} /book-by-index/0
@app.get("/book-by-index/{index}")
async def book_by_index(index: int):
    if index < 0 or index >= len(BOOK_DATABASE):
        # Fail
        raise HTTPException(404, f"Index {index} is out of the range of {len(BOOK_DATABASE)}.")
    else:
        return {"book": BOOK_DATABASE[index]}


# /get-book?id=cd1a0a8100de4ef7923ba0780ae48c32
@app.get("/get-book")
async def get_book(book_id: str):
    for book in BOOK_DATABASE:
        if book["book_id"] == book_id:
            return book

    raise HTTPException(404, f"Book not found: {book_id}")


# /get-random-book
@app.get("/get-random-book")
async def get_random_book():
    return rd.choice(BOOK_DATABASE)


# /add-book
@app.post("/add-book")
async def add_book(book: Book):
    book.book_id = uuid4().hex
    json_book = jsonable_encoder(book)
    BOOK_DATABASE.append(json_book)
    with open(BOOKS_FILE, "w") as f:
        json.dump(BOOK_DATABASE, f)
    return {"Message": f"Book {book} was added.", "book_id": book.book_id}


# /delete-book-by-index/{index} /delete-book-by-index/0
@app.delete("/delete-book-by-index/{index}")
async def delete_book_by_index(index: int):
    if index < 0 or index >= len(BOOK_DATABASE):
        # Fail
        raise HTTPException(404, f"Index {index} is out of the range of {len(BOOK_DATABASE)}.")
    else:
        book_removed = BOOK_DATABASE[index]
        BOOK_DATABASE.remove(BOOK_DATABASE[index])
        with open(BOOKS_FILE, "w") as f:
            json.dump(BOOK_DATABASE, f)
        return {"book": f"Book {book_removed} was deleted."}


# /delete-book
@app.delete("/delete-book")
async def delete_book(book_name: str):
    for book in BOOK_DATABASE:
        if book["name"] == book_name:
            BOOK_DATABASE.remove(book)
            with open(BOOKS_FILE, "w") as f:
                json.dump(BOOK_DATABASE, f)
            return {"Message": f"Book {book_name} was deleted."}
    # Fail
    raise HTTPException(404, f"Book: {book_name} does not exist.")


# /update-book-name
@app.put("/update-book-name")
async def update_book_name(book_name: str, update_name: str):
    # Find the book by index/name
    # Update the book name
    count = 0
    for book in BOOK_DATABASE:
        if book["name"] == book_name:
            count += 1
            book["name"] = update_name

    with open(BOOKS_FILE, "w") as f:
        json.dump(BOOK_DATABASE, f)

    if count == 0:
        raise HTTPException(404, f"Book: {book_name} does not exist.")
    else:
        return {"Message": f"Book: {book_name} does exist and the name is updated."}


# /update-book-price
@app.put("/update-book-price")
async def update_book_price(book_name: str, update_price: float):
    # Find the book by index/name
    # Update the price of book
    count = 0
    for book in BOOK_DATABASE:
        if book["name"] == book_name:
            count += 1
            book["price"] = update_price

    with open(BOOKS_FILE, "w") as f:
        json.dump(BOOK_DATABASE, f)

    if count == 0:
        raise HTTPException(404, f"Book: {book_name} does not exist.")
    else:
        return {"Message": f"Book: {book_name} does exist and the price was updated to {update_price}."}


# /update-book-genre
@app.put("/update-book-genre")
async def update_book_genre(book_name: str, genre: str):
    # Check validity of genre
    # Find the book by index/name
    # Update the genre of book
    pass


# http://127.0.0.1:8000/get-current-time
# http://127.0.0.1:8000/
# http://pixegami.com/
# HTTP request methods: GET, POST, PUT, PATCH, DELETE

"""
# /
@app.get("/")
async def root():
    return {"message": "Hello World", "var": 1234}

# /
@app.get("/get-current-time")
async def get_current_time():
    return {"message": " The current time is 16:00PM"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
"""
