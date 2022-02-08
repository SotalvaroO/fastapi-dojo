from models.book_entity import BookEntity



def dict_to_book(dictionary: dict):
    book: BookEntity ={}
    book.isbn = dictionary.get("isbn")
    book.name = dictionary.get("name")
    book.synopsis = dictionary.get("synopsis")
    book.author = dictionary.get("author")
    book.category = dictionary.get("category")
    book.edition = dictionary.get("edition")
    return book