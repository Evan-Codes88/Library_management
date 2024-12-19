from marshmallow import fields, validate

from init import db, ma

class Genre(db.Model):
    """
    Represents a genre in the library system.

    Attributes:
        id (int): The unique identifier for the genre.
        genre_name (str): The name of the genre.
        books (list): A list of books associated with this genre.

    Relationships:
        books (list): A relationship with the Book model, indicating all books that belong to this genre.
    """
    __tablename__ = "genre"
    id = db.Column(db.Integer, primary_key = True)
    genre_name = db.Column(db.String(100), nullable = False, unique = True)

    # Relationship with the Book model, indicating which books belong to this genre.
    books = db.relationship("Book", back_populates = "genre", cascade = "all, delete-orphan")

class GenreSchema(ma.Schema):
    """
    Marshmallow schema for serialising and deserialising Genre objects.

    This schema defines the structure of the data that can be passed to and from the Genre model, including 
    validation for certain fields.

    Attributes:
        genre_name (str): The name of the genre.
    """
    genre_name = fields.String(
        validate = [
            validate.Length(min = 2, error = "Genre Name must be at least 2 characters long."),
            validate.Regexp(r'^[A-Za-z\s]+$', error = "Genre Name can only contain letters and spaces.")
        ]
    )
    class Meta:
        """
        Specifies the fields to include when serialising the Genre object.
        """
        fields = ("id", "genre_name")

genre_schema = GenreSchema()
genres_schema = GenreSchema(many = True)