from marshmallow import fields, validate

from init import db, ma
from utils.error_handlers import validate_isbn

class Book(db.Model):
    """
    Represents a book in the library system.

    Attributes:
        id (int): The unique identifier for the book.
        title (str): The title of the book.
        isbn (str): The International Standard Book Number (ISBN) of the book.
        available_copies (int): The number of copies currently available in the library.
        author_id (int): The ID of the author, referencing the authors table.
        genre_id (int): The ID of the genre, referencing the genres table.
        author (Author): The associated author object.
        genre (Genre): The associated genre object.
        loans (list): A list of loan records associated with the book.
    """
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    isbn = db.Column(db.String, unique = True)
    available_copies = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"), nullable = False)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"), nullable = False)

    # Relationship With The Author Model
    author = db.relationship("Author", back_populates = "books")
    # Relationship With The Genre Model
    genre = db.relationship("Genre", back_populates = "books")
    # Relationship with the Loan model, indicating which loans are associated with this book.
    loans = db.relationship("Loan", back_populates = "book", cascade = "all, delete-orphan")


class BookSchema(ma.Schema):
    """
    Marshmallow schema for serialising and deserialising Book objects.

    This schema defines the structure of the data that can be passed to and from the Book model, including 
    validation for certain fields and custom methods for extracting specific information.

    Attributes:
        title (str): The title of the book.
        isbn (str): The ISBN of the book.
        author_name (str): The name of the author associated with the book.
    """
    title = fields.String(
        validate = [
            validate.Length(min = 2, error = "Title must be at least 2 characters long."),
            validate.Regexp(r"^[A-Za-z\s\-.']+$", error = "Name can only contain letters, spaces, hyphens, apostraphes and periods.")
        ])
    isbn = fields.String(
        validate = validate_isbn
    )

    author_name = fields.Method("get_author_name")

    def get_author_name(self, obj):
        """
        Retrieves the name of the author associated with the book.

        Args:
            obj (Book): The book object.

        Returns:
            str: The name of the author, or None if the author is not found.
        """
        return obj.author.name if obj.author else None

    class Meta:
        """
        Specifies the fields to include when serialising the Book object.
        """
        fields = ("id", "title", "isbn", "available_copies", "author_id", "author_name", "genre_id")

book_schema = BookSchema()
books_schema = BookSchema(many = True)