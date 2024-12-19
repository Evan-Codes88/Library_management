from marshmallow import fields, validate

from init import db, ma

class Author(db.Model):
    """
    Represents an author in the library system.

    Attributes:
        id (int): The unique identifier for the author.
        name (str): The name of the author.
        birth_year (int): The birth year of the author.
        books (list): A list of books associated with the author.

    Relationships:
        books (list): A relationship with the Book model, indicating all books written by the author.
    """
    __tablename__ = "author"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False, unique = True)
    birth_year = db.Column(db.Integer)

    # Relationship with the Book model, indicating which books belong to this author.
    books = db.relationship("Book", back_populates = "author", cascade = "all, delete-orphan")

class AuthorSchema(ma.Schema):
    """
    Marshmallow schema for serialising and deserialising Author objects.

    This schema defines the structure of the data that can be passed to and from the Author model, including 
    validation for certain fields.

    Attributes:
        name (str): The name of the author.
        birth_year (int): The birth year of the author.
    """
    name = fields.String(
    validate = [
        validate.Length(min = 2, error = "Name must be at least 2 characters long."),
        validate.Regexp(r"^[A-Za-z\s\-.']+$", error = "Name can only contain letters, spaces, hyphens, apostraphes and periods.")
    ])
    birth_year = fields.Integer(
        validate = validate.Range(min=1900, max=2024, error="Birth year must be between 1900 and 2024.")
    )
    class Meta:
        """
        Specifies the fields to include when serialising the Author object.
        """
        fields = ("id", "name", "birth_year")

author_schema = AuthorSchema()
authors_schema = AuthorSchema(many = True)