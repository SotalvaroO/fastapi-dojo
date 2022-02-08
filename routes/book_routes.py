from array import array
from fastapi import APIRouter, status, Response
from models.book_entity import BookEntity
from db.data import book_data
from repository import book_repository

route = APIRouter(prefix='/book', tags=['book'])


@route.get('', status_code=200)
def get_books(response: Response):
    books: array[BookEntity] = book_repository.get_all_books()
    if not books:
        response.status_code = status.HTTP_204_NO_CONTENT
    response.status_code = status.HTTP_200_OK
    return {"message": "Obtenido con exito", "status_code": 200, "body": books}


@route.get('/{isbn}', status_code=200)
def get_book_by_isbn(isbn: str, response: Response):
    book: BookEntity = book_repository.get_book_by_isbn(isbn)
    if not book:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Not found", "status_code": 404}
    response.status_code = status.HTTP_200_OK
    return {"message": "Exito", "status_code": 200, "body": book}


@route.post('', status_code=201)
def create_book(book: BookEntity, response: Response):
    isbn: str = book.isbn
    book_db = book_repository.get_book_by_isbn(isbn)
    if not book_db:
        book_db = book_repository.create_book(book)
        response.status_code = status.HTTP_201_CREATED
        return {"message": "Creado", "status_code": 201, "body": book_db}
    response.status_code = status.HTTP_400_BAD_REQUEST
    return {"message": "El elemento ya existe", "status_code": 400}


@route.put('', status_code=200)
def update_book(book: BookEntity, response: Response):
    book_db = book_repository.get_book_by_isbn(book.isbn)
    if not book_db:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "El elemento no existe", "status_code": 404}
    book_db = book_repository.update_book(book)
    response.status_code = status.HTTP_200_OK
    return {"message": "Actualizado", "status_code": 200, "body": book_db}


@route.delete('/{isbn}', status_code=200)
def delete_book(isbn: str, response: Response):
    book_db = book_repository.delete_book(isbn)
    if not book_db:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "El elemento no existe", "status_code": 404}
    response.status_code = status.HTTP_200_OK
    return {"message": "Eliminado", "status_code": 200, "body": book_db}
