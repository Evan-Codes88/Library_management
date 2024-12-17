from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from marshmallow import ValidationError

from init import db
from models.book import Book, book_schema, books_schema
from utils.error_handlers import handle_integrity_error, handle_validation_error
from utils.strip import validate_and_strip_field

books_bp = Blueprint("books", __name__, url_prefix = "/books")

# Read All - /books - GET
@books_bp.route("/")
def get_books():
    stmt = db.select(Book).order_by(Book.id)
    books_list = db.session.scalars(stmt)
    return books_schema.dump(books_list)

# Read One - /books/id - GET
@books_bp.route("/<int:book_id>")
def get_book(book_id):
    stmt = db.select(Book).filter_by(id = book_id)
    book = db.session.scalar(stmt)
    if book:
        return book_schema.dump(book)
    else:
        return {"message": f"Book with id {book_id} does not exist"}, 404

# Create Book - /books - POST
@books_bp.route("/", methods = ["POST"])
def create_book():
    try:
        body_data = book_schema.load(request.get_json())

        new_book = Book(
            title = body_data.get("title"),
            isbn = body_data.get("isbn"),
            available_copies = body_data.get("available_copies"),
            author_id = body_data.get("author_id"),
            genre_id = body_data.get("genre_id")
        )
        db.session.add(new_book)
        db.session.commit()
        return book_schema.dump(new_book), 201
    
    except ValidationError as err:
        return handle_validation_error(err)
    
    except IntegrityError as err:
       return handle_integrity_error(err)
    
# Delete Book - /books/id - DELETE
@books_bp.route("/<int:book_id>", methods = ["DELETE"])
def delete_book(book_id):
    stmt = db.select(Book).filter_by(id = book_id)
    book = db.session.scalar(stmt)
    if book:
        db.session.delete(book)
        db.session.commit()
        return {"message": f"Book '{book.title}' was successfully deleted"}
    else:
        return {"message": f"Book with id {book_id} does not exist"}, 404

# Delete Book - ISBN /books/isbn - DELETE
@books_bp.route("/isbn/<string:isbn>", methods = ["DELETE"])
def delete_by_isbn(isbn):
    stmt = db.select(Book).filter_by(isbn = isbn)
    book = db.session.scalar(stmt)
    if book:
        db.session.delete(book)
        db.session.commit()
        return {"message": f"Book '{book.title}' was successfully deleted"}
    else:
        return {"message": f"Book with isbn {isbn} does not exist"}, 404