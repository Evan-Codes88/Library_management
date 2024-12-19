from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from marshmallow import ValidationError

from init import db
from models.genre import Genre, genre_schema, genres_schema
from utils.error_handlers import handle_integrity_error, handle_validation_error
from utils.strip import validate_and_strip_field

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
        body_data["genre_name"] = validate_and_strip_field(body_data, "genre_name")
        # Ensure name is not empty after stripping
        if not body_data["genre_name"]:
            return {"message": "Genre name cannot be empty"}, 400
        
        new_genre = Genre(
            genre_name = body_data.get("genre_name")
        )
        db.session.add(new_genre)
        db.session.commit()
        return genre_schema.dump(new_genre), 201
    
    except ValidationError as err:
        return handle_validation_error(err)
    
    except IntegrityError as err:
       return handle_integrity_error(err)

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

                # Update only provided fields
                if "genre_name" in validated_data:
                    genre.genre_name = validate_and_strip_field(validated_data, "genre_name")
                    if not genre.genre_name:
                        return {"message": "Genre Name cannot be empty"}, 400

                db.session.commit()
                return genre_schema.dump(genre)

            except ValidationError as err:
                return handle_validation_error(err)
            
            except IntegrityError as err:
                return handle_integrity_error(err)
    else:
        return {"message": f"Genre with id {genre_id} does not exist"}, 404