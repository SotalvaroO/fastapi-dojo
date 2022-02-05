from fastapi import APIRouter
from models.book_entity import BookEntity
from db.data_json import book_data

route = APIRouter(prefix='/book', tags=['book'])

@route.get('')
def getBooks():
    return book_data

@route.get('/{isbn}')
def getBookByIsbn(isbn: str):
    found_book: str
    for book in book_data:
        if book.get('isbn')  == isbn:
            found_book = book
    return found_book

