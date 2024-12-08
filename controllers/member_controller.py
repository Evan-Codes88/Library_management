from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from marshmallow import ValidationError

from init import db
from models.member import Member, member_schema, members_schema
from utils.error_handlers import handle_integrity_error, handle_validation_error
from utils.strip import validate_and_strip_field

members_bp = Blueprint("members", __name__, url_prefix = "/members")

# Read All - /members - GET
@members_bp.route("/")
def get_members():
    stmt = db.select(Member).order_by(Member.id)
    members_list = db.session.scalars(stmt)
    return members_schema.dump(members_list)

# Read One - /members/id - GET
@members_bp.route("/<int:member_id>")
def get_member(member_id):
    stmt = db.select(Member).filter_by(id = member_id)
    member = db.session.scalar(stmt)
    if member:
        return member_schema.dump(member)
    else:
        return {"message": f"Member with id {member_id} does not exist"}, 404
    
# Read Member from Membership Number - /members/membership_number - GET
@members_bp.route("/membership_number/<string:membership_number>")
def get_member_membership(membership_number):
    stmt = db.select(Member).filter_by(membership_number = membership_number)
    member = db.session.scalar(stmt)
    if member:
        return member_schema.dump(member)
    else:
        return {"message": f"Member with membership number {membership_number} does not exist"}, 404
    

# Create Member - /members - POST
@members_bp.route("/", methods = ["POST"])
def create_member():
    try:
        body_data = member_schema.load(request.get_json())
        
        new_member = Member(
            name = body_data.get("name"),
            membership_number = body_data.get("membership_number"),
            email = body_data.get("email"),
            join_date = body_data.get("join_date")
        )
        db.session.add(new_member)
        db.session.commit()
        return member_schema.dump(new_member), 201
    
    except ValidationError as err:
        return handle_validation_error(err)
    
    except IntegrityError as err:
       return handle_integrity_error(err)
    
# Delete Member off id - /members/id - DELETE
@members_bp.route("/<int:member_id>", methods = ["DELETE"])
def delete_member(member_id):
    stmt = db.select(Member).filter_by(id = member_id)
    member = db.session.scalar(stmt)
    if member:
        db.session.delete(member)
        db.session.commit()
        return {"message": f"Member '{member.name}' was successfully deleted"}
    else:
        return {"message": f"Member with id {member_id} does not exist"},404

# Delete Member off Membership Number - /members/membership_number - DELETE
@members_bp.route("/membership_number/<string:membership_number>", methods = ["DELETE"])
def delete_member_by_number(membership_number):
    stmt = db.select(Member).filter_by(membership_number = membership_number)
    member = db.session.scalar(stmt)
    if member:
        db.session.delete(member)
        db.session.commit()
        return {"message": f"Member '{member.name}' was successfully deleted"}
    else:
        return {"message": f"Member with id {membership_number} does not exist"},404

# Update Member - /members/id - PUT, PATCH
@members_bp.route("/<int:member_id>", methods = ["PUT", "PATCH"])
def update_member(member_id):
    stmt = db.select(Member).filter_by(id = member_id)
    member = db.session.scalar(stmt)
    body_data = request.get_json()

    if not body_data:
        return {"message": "No data provided or invalid JSON"}, 400

    if member:
        try:
            validated_data = member_schema.load(body_data)

              # Update only provided fields
            if "name" in validated_data:
                member.name = validate_and_strip_field(validated_data, "name")
                if not member.name:
                    return {"message": "Name cannot be empty"}, 400

            if "membership_number" in validated_data:
                member.membership_number = validate_and_strip_field(validated_data, "membership_number")
                if not member.membership_number:
                    return {"message": "Membership Number cannot be empty"}, 400

            if "email" in validated_data:
                member.email = validate_and_strip_field(validated_data, "email")
                if not member.email:
                    return {"message": "Email cannot be empty"}, 400

            if "join_date" in validated_data:
                member.join_date = validated_data["join_date"]

            db.session.commit()
            return member_schema.dump(member)

        except ValidationError as err:
            return handle_validation_error(err)
        
        except IntegrityError as err:
            return handle_integrity_error(err)
    else:
        return {"message": f"Member with id {member_id} does not exist"}, 404
    
# Update Member - /members/membership_number - PUT, PATCH
@members_bp.route("/membership_number/<string:membership_number>", methods = ["PUT", "PATCH"])
def update_member_by_number(membership_number):
    stmt = db.select(Member).filter_by(membership_number = membership_number)
    member = db.session.scalar(stmt)
    body_data = request.get_json()

    if not body_data:
        return {"message": "No data provided or invalid JSON"}, 400

    if member:
        try:
            validated_data = member_schema.load(body_data)

              # Update only provided fields
            if "name" in validated_data:
                member.name = validate_and_strip_field(validated_data, "name")
                if not member.name:
                    return {"message": "Name cannot be empty"}, 400

            if "membership_number" in validated_data:
                member.membership_number = validate_and_strip_field(validated_data, "membership_number")
                if not member.membership_number:
                    return {"message": "Membership Number cannot be empty"}, 400

            if "email" in validated_data:
                member.email = validate_and_strip_field(validated_data, "email")
                if not member.email:
                    return {"message": "Email cannot be empty"}, 400

            if "join_date" in validated_data:
                member.join_date = validated_data["join_date"]

            db.session.commit()
            return member_schema.dump(member)

        except ValidationError as err:
            return handle_validation_error(err)
        
        except IntegrityError as err:
            return handle_integrity_error(err)
    else:
        return {"message": f"Member with id {membership_number} does not exist"}, 404
    
