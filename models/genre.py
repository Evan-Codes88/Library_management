from marshmallow import fields, validate

from init import db, ma

class Genre(db.Model):
    __tablename__ = "genres"

    id = db.Column(db.Integer, primary_key = True)
    genre_name = db.Column(db.String(100), nullable = False)

class GenreSchema(ma.Schema):
    genre_name = fields.String(
        validate = [
            validate.Length(min = 2, error = "Genre Name must be at least 2 characters long."),
            validate.Regexp('^[A-Za-z\s]+$', error = "Genre Name can only contain letters and spaces.")
        ]
    )
    class Meta:
        fields = ("id", "genre_name")

genre_schema = GenreSchema()
genres_schema = GenreSchema(many = True)