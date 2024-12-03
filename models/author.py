from marshmallow import fields

from init import db, ma

class Author(db.Model):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key = True)

    name = db.Column(db.String(100), nullable = False)
    birth_year = db.Column(db.Integer)

class AuthorSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "birth_year")

author_schema = AuthorSchema()
authors_schema = AuthorSchema(many = True)