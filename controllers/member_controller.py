from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from marshmallow import ValidationError

from init import db
from models.member import Member, member_schema, members_schema
from utils.error_handlers import handle_integrity_error, handle_validation_error

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
@members_bp.route("/membership_number/<int:membership_number>")
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
    
