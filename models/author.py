from marshmallow import fields, validate

from init import db, ma

class Author(db.Model):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key = True)

    name = db.Column(db.String(100), nullable = False, unique = True)
    birth_year = db.Column(db.Integer)

class AuthorSchema(ma.Schema):
    # Field level validation
    name = fields.String(
    validate = [
        validate.Length(min=2, error="Name must be at least 2 characters long."),
        validate.Regexp('^[A-Za-z\s\-.]+$', error="Name can only contain letters, spaces, hyphens, and periods.")
    ])
    birth_year = fields.Integer(
        validate=validate.Range(min=1800, max=2024, error="Birth year must be between 1900 and 2024.")
    )
    class Meta:
        fields = ("id", "name", "birth_year")

author_schema = AuthorSchema()
authors_schema = AuthorSchema(many = True)