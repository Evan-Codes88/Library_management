from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from marshmallow import ValidationError

from init import db
from models.loan import Loan, loan_schema, loans_schema
from utils.error_handlers import handle_integrity_error, handle_validation_error, validate_isbn
from utils.strip import validate_and_strip_field

loans_bp = Blueprint("loans", __name__, url_prefix = "/loans")

# Read All - /loans - GET
@loans_bp.route("/")
def get_loans():
    stmt = db.select(Loan).order_by(Loan.id)
    loans_list = db.session.scalars(stmt)
    return loans_schema.dump(loans_list)

# Read All - Member_id - /loans/member_id - GET
@loans_bp.route("/member/<int:member_id>")
def get_loan_from_member(member_id):
    stmt = db.select(Loan).filter_by(member_id = member_id)
    loans = db.session.scalars(stmt)
    if loans:
        return loans_schema.dump(loans)
    else:
        return {"message": f"Member with id {member_id} does not have any loans"}, 404

# Read One - /loans/id - GET
@loans_bp.route("/<int:loan_id>")
def get_loan(loan_id):
    stmt = db.select(Loan).filter_by(id = loan_id)
    loan = db.session.scalar(stmt)
    if loan:
        return loan_schema.dump(loan)
    else:
        return {"message": f"Loan with id {loan_id} does not exist"}, 404
    
