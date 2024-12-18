from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from marshmallow import ValidationError

from init import db
from models.book import Book, book_schema, books_schema
from utils.error_handlers import handle_integrity_error, handle_validation_error, validate_isbn
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


# Update Book - /books/id - PUT, PATCH
@books_bp.route("/<int:book_id>", methods=["PUT", "PATCH"])
def update_book(book_id):
    stmt = db.select(Book).filter_by(id=book_id)
    book = db.session.scalar(stmt)
    body_data = request.get_json()

    if not body_data:
        return {"message": "No data provided or invalid JSON"}, 400
    
    if book:
        try:
            validated_data = book_schema.load(body_data)

            # Title Validation
            if "title" in validated_data:
                book.title = validate_and_strip_field(validated_data, "title")
                if not book.title:
                    return {"message": "Title cannot be empty"}, 400
            
            # ISBN Validation
            if "isbn" in validated_data:
                isbn = validated_data["isbn"]
                if not validate_isbn(isbn):  # Call the function to validate the ISBN
                    return {"message": "Invalid ISBN format"}, 400
                book.isbn = isbn

            # Available Copies Validation
            if "available_copies" in validated_data:
                try:
                    book.available_copies = int(validated_data["available_copies"])
                    if book.available_copies < 0:
                        return {"message": "Available copies cannot be negative"}, 400
                except ValueError:
                    return {"message": "Available copies must be an integer"}, 400
            
            # Author ID Validation
            if "author_id" in validated_data:
                try:
                    book.author_id = int(validated_data["author_id"])
                    if book.author_id <= 0:  # Optional: Ensure it's a positive integer
                        return {"message": "Author ID must be a positive integer"}, 400
                except ValueError:
                    return {"message": "Author ID must be an integer"}, 400

            # Genre ID Validation
            if "genre_id" in validated_data:
                try:
                    book.genre_id = int(validated_data["genre_id"])
                    if book.genre_id <= 0:  # Optional: Ensure it's a positive integer
                        return {"message": "Genre ID must be a positive integer"}, 400
                except ValueError:
                    return {"message": "Genre ID must be an integer"}, 400
                
            db.session.commit()
            return {"message": "Book updated successfully", "book": book_schema.dump(book)}, 200
        
        except ValidationError as err:
            return handle_validation_error(err)
        
        except IntegrityError as err:
            return handle_integrity_error(err)
    else:
        return {"message": f"Book with id {book_id} does not exist"}, 404
    

# Update Book - ISBN /books/isbn - PUT, PATCH
@books_bp.route("/isbn/<string:isbn>", methods=["PUT", "PATCH"])
def update_book_by_isbn(isbn):
    stmt = db.select(Book).filter_by(isbn = isbn)
    book = db.session.scalar(stmt)
    body_data = request.get_json()

    if not body_data:
        return {"message": "No data provided or invalid JSON"}, 400
    
    if book:
        try:
            validated_data = book_schema.load(body_data)

            # Title Validation
            if "title" in validated_data:
                book.title = validate_and_strip_field(validated_data, "title")
                if not book.title:
                    return {"message": "Title cannot be empty"}, 400
            
            # ISBN Validation
            if "isbn" in validated_data:
                isbn = validated_data["isbn"]
                if not validate_isbn(isbn):  # Call the function to validate the ISBN
                    return {"message": "Invalid ISBN format"}, 400
                book.isbn = isbn

            # Available Copies Validation
            if "available_copies" in validated_data:
                try:
                    book.available_copies = int(validated_data["available_copies"])
                    if book.available_copies < 0:
                        return {"message": "Available copies cannot be negative"}, 400
                except ValueError:
                    return {"message": "Available copies must be an integer"}, 400
            
            # Author ID Validation
            if "author_id" in validated_data:
                try:
                    book.author_id = int(validated_data["author_id"])
                    if book.author_id <= 0:  # Optional: Ensure it's a positive integer
                        return {"message": "Author ID must be a positive integer"}, 400
                except ValueError:
                    return {"message": "Author ID must be an integer"}, 400

            # Genre ID Validation
            if "genre_id" in validated_data:
                try:
                    book.genre_id = int(validated_data["genre_id"])
                    if book.genre_id <= 0:  # Optional: Ensure it's a positive integer
                        return {"message": "Genre ID must be a positive integer"}, 400
                except ValueError:
                    return {"message": "Genre ID must be an integer"}, 400
                
            db.session.commit()
            return {"message": "Book updated successfully", "book": book_schema.dump(book)}, 200
        
        except ValidationError as err:
            return handle_validation_error(err)
        
        except IntegrityError as err:
            return handle_integrity_error(err)
    else:
        return {"message": f"Book with isbn {isbn} does not exist"}, 404