from marshmallow import fields, validate

from init import db, ma
from utils.error_handlers import validate_isbn

class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    isbn = db.Column(db.String, unique = True)
    available_copies = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"), nullable = False)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"), nullable = False)

    author = db.relationship("Author", back_populates = "books")
    genre = db.relationship("Genre", back_populates = "books")
    loans = db.relationship("Loan", back_populates = "book", cascade = "all, delete-orphan")


class BookSchema(ma.Schema):
    title = fields.String(
        validate = [
            validate.Length(min = 2, error = "Title must be at least 2 characters long."),
            validate.Regexp(r"^[A-Za-z\s\-.']+$", error = "Name can only contain letters, spaces, hyphens, apostraphes and periods.")
        ])
    isbn = fields.String(
        validate = validate_isbn
    )

    class Meta:
        fields = ("id", "title", "isbn", "available_copies", "author_id", "genre_id")

book_schema = BookSchema()
books_schema = BookSchema(many = True)