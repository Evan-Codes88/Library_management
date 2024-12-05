from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from marshmallow import ValidationError
from collections import OrderedDict

from init import db
from models.genre import Genre, genre_schema, genres_schema

genres_bp = Blueprint("genres", __name__, url_prefix = "/genres")

# Read All - /genres - GET
@genres_bp.route("/")
def get_genres():
    stmt = db.select(Genre).order_by(Genre.id)
    genres_list = db.session.scalars(stmt)
    return genres_schema.dump(genres_list)


# Read One - /genres/id - GET
@genres_bp.route("/<int:genre_id>")
def get_genre(genre_id):
    stmt = db.select(Genre).filter_by(id = genre_id)
    genre = db.session.scalar(stmt)
    if genre:
        return genre_schema.dump(genre)
    else:
        return {"message": f"Genre with id {genre_id} does not exist"}, 404

    