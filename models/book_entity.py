from unicodedata import numeric
from pydantic import BaseModel


class BookEntity(BaseModel):
    isbn: str
    name: str
    synopsis: str
    author: str
    category: str
    edition: int