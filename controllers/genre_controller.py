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

# Create - /genres - POST
@genres_bp.route("/", methods = ["POST"])
def create_genre():
    try:
        body_data = genre_schema.load(request.get_json())
        new_genre = Genre(
            genre_name = body_data.get("genre_name")
        )
        db.session.add(new_genre)
        db.session.commit()
        return genre_schema.dump(new_genre), 201
    
    except ValidationError as err:
        errors = [message for messages in err.messages.values()for message in messages]
        response = OrderedDict([
            ("message", "Validation failed"),
            ("errors", errors)
        ])
        return response, 400
    
    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return {"message": f"The '{err.orig.diag.column_name}' is required and cannot be null"}, 400
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return {"message": "The provided name is already taken. Please try another"}, 409

# Delete - /genre/id - DELETE
@genres_bp.route("/<int:genre_id>", methods = ["DELETE"])
def delete_genre(genre_id):
    stmt = db.select(Genre).filter_by(id = genre_id)
    genre = db.session.scalar(stmt)
    if genre:
        db.session.delete(genre)
        db.session.commit()
        return {"message": f"Genre '{genre.genre_name}' deleted successfully"}
    else:
        return {"message": f"Genre '{genre_id}' does not exist"},404
    
# Update - /genres/id - PUT, PATCH
@genres_bp.route("/<int:genre_id>", methods = ["PUT", "PATCH"])
def update_genre(genre_id):
    stmt = db.select(Genre).filter_by(id = genre_id)
    genre = db.session.scalar(stmt)
    body_data = request.get_json()

    if not body_data:
        return {"message": "No data provided or invalid JSON"}, 400

    if genre:
        try:
            validated_data = genre_schema.load(body_data)
            genre.genre_name = validated_data.get("genre_name") or genre.genre_name
            db.session.commit()
            return genre_schema.dump(genre)
        
        except ValidationError as err:
            errors = [message for messages in err.messages.values() for message in messages]
            return {"message": "Validation failed", "errors": errors}, 400
        
        except IntegrityError as err:

            if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
                return {"message": "The provided name is already taken. Please try another"}, 409
                        
            elif err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
                return {"message": f"The '{err.orig.diag.column_name}' is required and cannot be null"}, 400
            else:
                return {"message": "An integrity error occurred. Please try again"}, 400

    else:
        return {"message": f"Genre with id {genre_id} does not exist"}