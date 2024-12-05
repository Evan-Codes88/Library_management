from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from marshmallow import ValidationError
from collections import OrderedDict

from init import db
from models.author import Author, author_schema, authors_schema

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
        new_author = Author(
            name = body_data.get("name"),
            birth_year = body_data.get("birth_year")
        )
        db.session.add(new_author)
        db.session.commit()
        return author_schema.dump(new_author), 201
    
    except ValidationError as err:
        errors = [message for messages in err.messages.values() for message in messages]
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
            author.name = validated_data.get("name") or author.name
            author.birth_year = validated_data.get("birth_year") or author.birth_year
            db.session.commit()
            return author_schema.dump(author)
        
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
        return {"message": f"Author with id {author_id} does not exist"}