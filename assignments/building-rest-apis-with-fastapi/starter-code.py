from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Books API")


class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)


class Book(BookCreate):
    id: int


books: list[Book] = [
    Book(id=1, title="The Little Prince", author="Antoine de Saint-Exupery"),
    Book(id=2, title="A Wrinkle in Time", author="Madeleine L'Engle"),
]


@app.get("/books", response_model=list[Book])
def list_books() -> list[Book]:
    """Return all books."""
    return books


# Add GET /books/{book_id}, POST /books, PUT /books/{book_id}, and
# DELETE /books/{book_id} below. Use HTTPException for missing books.
