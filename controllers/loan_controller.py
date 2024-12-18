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
    
# Create Loan - /loans - POST
@loans_bp.route("/", methods = ["POST"])
def create_loan():
    try:
        body_data = loan_schema.load(request.get_json())

        existing_loan = Loan.query.filter_by(book_id=body_data.get("book_id"), member_id=body_data.get("member_id")).first()
        if existing_loan:
            return {"message": "This member has already borrowed this book."}, 400


        new_loan = Loan(
            borrow_date = body_data.get("borrow_date"),
            return_date = body_data.get("return_date"),
            book_id = body_data.get("book_id"),
            member_id = body_data.get("member_id")
        )
        db.session.add(new_loan)
        db.session.commit()
        return loan_schema.dump(new_loan), 201
    
    except ValidationError as err:
        return handle_validation_error(err)
    
    except IntegrityError as err:
       return handle_integrity_error(err)

# Delete Loan - /loans/id - DELETE
@loans_bp.route("/<int:loan_id>", methods = ["DELETE"])
def delete_loan(loan_id):
    stmt = db.select(Loan).filter_by(id = loan_id)
    loan = db.session.scalar(stmt)
    if loan:
        db.session.delete(loan)
        db.session.commit()
        return {"message":f"Loan with id {loan_id} was successfully deleted"}
    else:
        return {"message": f"Loan with id {loan_id} does not exist"}
    

# This is just a theoritical - In case a member wants to delete their loans because they don't want them yet (Or something Like That)
# Delete Loan - Member ID - /loans/member_id - Delete
@loans_bp.route("/member/<int:member_id>", methods = ["DELETE"])
def delete_loans_from_member(member_id):
    # Query to get all loans for the given member_id
    loans_to_delete = Loan.query.filter_by(member_id=member_id).all()

    if loans_to_delete:
        # Iterate over each loan and delete it
        for loan in loans_to_delete:
            db.session.delete(loan)
        
        # Commit the transaction to remove all loans
        db.session.commit()

        return {"message": f"All loans for member id '{member_id}' were successfully deleted."}
    else:
        return {"message": f"No loans found for member id '{member_id}'."}