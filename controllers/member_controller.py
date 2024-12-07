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
        return {"message": f"Genre with id {member_id} does not exist"}, 404
    
