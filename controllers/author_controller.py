from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from marshmallow import ValidationError
from collections import OrderedDict

from init import db
from models.author import Author, author_schema, authors_schema
from utils.error_handlers import handle_integrity_error, handle_validation_error
from utils.strip import validate_and_strip_field

authors_bp = Blueprint("authors", __name__, url_prefix = "/authors")

# Read All - /authors - GET
@authors_bp.route("/")
def get_authors():
    stmt = db.select(Author).order_by(Author.id)
    authors_list = db.session.scalars(stmt)
    return authors_schema.dump(authors_list)

# Read One - /authors/id - GET
@authors_bp.route("/<int:author_id>")
def get_author(author_id):
    stmt = db.select(Author).filter_by(id = author_id)
    author = db.session.scalar(stmt)
    if author:
        return author_schema.dump(author)
    else:
        return {"message": f"Author with id {author_id} does not exist"}, 404
    
# Create - /authors - POST
@authors_bp.route("/", methods = ["POST"])
def create_author():
    try:
        body_data = author_schema.load(request.get_json())
        body_data["name"] = body_data["name"].strip()
        # Ensure name is not empty after stripping
        if not body_data["name"]:
            return {"message": "Name cannot be empty"}, 400

        new_author = Author(
            name = body_data.get("name"),
            birth_year = body_data.get("birth_year")
        )
        db.session.add(new_author)
        db.session.commit()
        return author_schema.dump(new_author), 201
    
    except ValidationError as err:
        return handle_validation_error(err)
    
    except IntegrityError as err:
       return handle_integrity_error(err)
        
# Delete - /authors/id - DELETE
@authors_bp.route("/<int:author_id>", methods = ["DELETE"])
def delete_author(author_id):
    stmt = db.select(Author).filter_by(id = author_id)
    author = db.session.scalar(stmt)
    if author:
        db.session.delete(author)
        db.session.commit()
        return {"message": f"Author '{author.name}' deleted successfully"}
    else:
        return {"message": f"Author with id {author_id} does not exist"}, 404


# Update - /authors/id - PUT, PATCH
@authors_bp.route("/<int:author_id>", methods = ["PUT", "PATCH"])
def update_author(author_id):
    stmt = db.select(Author).filter_by(id = author_id)
    author = db.session.scalar(stmt)
    body_data = request.get_json()

    if not body_data:
        return {"message": "No data provided or invalid JSON"}, 400

    if author:
        try:
            validated_data = author_schema.load(body_data)

            # Update only provided fields
            if "name" in validated_data:
                author.name = validate_and_strip_field(validated_data, "name")
                if not author.name:
                    return {"message": "Name cannot be empty"}, 400

            if "birth_year" in validated_data:
                author.birth_year = validated_data["birth_year"]

            db.session.commit()
            return author_schema.dump(author)
        
        except ValidationError as err:
            return handle_validation_error(err)
        
        except IntegrityError as err:
            return handle_integrity_error(err)
    else:
        return {"message": f"Author with id {author_id} does not exist"}, 404