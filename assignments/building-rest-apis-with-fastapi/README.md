# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API with FastAPI that manages a small collection of books. You will practice defining HTTP routes, validating request data with Pydantic, and returning appropriate status codes for CRUD operations.

## 📝 Tasks

### 🛠️ Create Read Routes

#### Description
Complete the starter application so clients can retrieve all books and retrieve one book by its ID.

#### Requirements
Completed program should:

- Start with `uvicorn` and expose a FastAPI application
- Implement `GET /books` to return the complete list of books
- Implement `GET /books/{book_id}` to return one book or a `404` response when the ID does not exist
- Return JSON responses with each book's `id`, `title`, and `author`


### 🛠️ Add and Validate Books

#### Description
Define a Pydantic request model and add a route that accepts JSON data to create a new book.

#### Requirements
Completed program should:

- Define a `BookCreate` model requiring a non-empty `title` and `author`
- Implement `POST /books` and assign a unique integer ID to each new book
- Return the created book with a `201 Created` status code
- Reject requests that are missing required fields or provide invalid data with FastAPI validation errors

Example request:

```json
{
  "title": "The Hobbit",
  "author": "J. R. R. Tolkien"
}
```


### 🛠️ Complete the CRUD API

#### Description
Add update and delete operations, handling missing resources consistently.

#### Requirements
Completed program should:

- Implement `PUT /books/{book_id}` to replace an existing book's title and author
- Implement `DELETE /books/{book_id}` to remove an existing book
- Return a `404` response when an update or delete targets an unknown ID
- Return the updated book from `PUT` and a clear confirmation from `DELETE`
- Verify the routes using FastAPI's interactive documentation at `/docs` or an API client
