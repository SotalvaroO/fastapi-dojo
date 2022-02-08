from array import array
from models.book_entity import BookEntity
from db.data import book_data
from util.dict_to_book import dict_to_book

books = book_data.get("books")


def get_all_books():
    return books


def get_book_by_isbn(isbn: str):
    for book in books:

        if book.get("isbn") == isbn:
            return book
    return None


def create_book(book: BookEntity):
    books.append(book.__dict__)
    return book


def update_book(book: BookEntity):

    books[books.index(get_book_by_isbn(book.isbn))] = book.__dict__
    return book


def delete_book(isbn: str):
    book = get_book_by_isbn(isbn)
    if not book:
        return None
    books.remove(book)
    return book
