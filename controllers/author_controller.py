from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes

from init import db
from models.author import Author, author_schema, authors_schema

authors_bp = Blueprint("authors", __name__, url_prefix = "/authors")

# Read All - /authors - GET
@authors_bp.route("/")
def get_authors():
    stmt = db.select(Author)
    authors_list = db.session.scalars(stmt)
    data = authors_schema.dump(authors_list)
    return data

# Read One - /authors/id - GET
@authors_bp.route("/<int:author_id>")
def get_author(author_id):
    stmt = db.select(Author).filter_by(id = author_id)
    author = db.session.scalar(stmt)
    if author:
        data = author_schema.dump(author)
        return data
    else:
        return {"message": f"Author with id {author_id} does not exist"}, 404