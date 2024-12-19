from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from marshmallow import ValidationError
from datetime import datetime

from init import db
from models.loan import Loan, loan_schema, loans_schema
from models.book import Book
from models.member import Member
from utils.error_handlers import handle_integrity_error, handle_validation_error
from utils.validate_date_range import validate_date_format

loans_bp = Blueprint("loans", __name__, url_prefix = "/loans")

# Read All - /loans - GET
@loans_bp.route("/")
def get_loans():
    stmt = db.select(Loan).order_by(Loan.id)
    loans_list = db.session.scalars(stmt)
    return loans_schema.dump(loans_list)

# Read All - Member_id - /loans/member_id - GET
"""Read all Loans attached to a Member"""
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

# Update Loan - /loans/id - PUT, PATCH
@loans_bp.route("/<int:loan_id>", methods=["PUT", "PATCH"])
def update_loan(loan_id):
    stmt = db.select(Loan).filter_by(id=loan_id)
    loan = db.session.scalar(stmt)
    body_data = request.get_json()

    if not body_data:
        return {"message": "No data provided or invalid JSON"}, 400

    if loan:
        try:
            validated_data = loan_schema.load(body_data)

            # Borrow Date and Return Date Validation using validate_date_format
            if "borrow_date" in validated_data or "return_date" in validated_data:
                borrow_date = validated_data.get("borrow_date", loan.borrow_date)
                return_date = validated_data.get("return_date", loan.return_date)

                # Validate the date format for both borrow_date and return_date
                borrow_date_obj, borrow_date_error = validate_date_format(borrow_date)
                if borrow_date_error:
                    return {"message": borrow_date_error}, 400

                return_date_obj, return_date_error = validate_date_format(return_date)
                if return_date_error:
                    return {"message": return_date_error}, 400

                # Ensure Borrow Date is Before Return Date
                if borrow_date_obj >= return_date_obj:
                    return {"message": "Borrow date must be before return date"}, 400

                loan.borrow_date = borrow_date_obj
                loan.return_date = return_date_obj

            # Book ID Validation and Existence Check
            if "book_id" in validated_data:
                try:
                    loan.book_id = int(validated_data["book_id"])
                    if loan.book_id <= 0:
                        return {"message": "Book ID must be a positive integer"}, 400

                    # Check if the book exists in the database
                    book = db.session.query(Book).filter_by(id=loan.book_id).first()
                    if not book:
                        return {"message": f"Book with ID {loan.book_id} does not exist"}, 400
                except ValueError:
                    return {"message": "Book ID must be an integer"}, 400

            # Member ID Validation and Existence Check
            if "member_id" in validated_data:
                try:
                    loan.member_id = int(validated_data["member_id"])
                    if loan.member_id <= 0:
                        return {"message": "Member ID must be a positive integer"}, 400

                    # Check if the member exists in the database
                    member = db.session.query(Member).filter_by(id=loan.member_id).first()
                    if not member:
                        return {"message": f"Member with ID {loan.member_id} does not exist"}, 400
                except ValueError:
                    return {"message": "Member ID must be an integer"}, 400

            db.session.commit()
            return {"message": "Loan updated successfully", "loan": loan_schema.dump(loan)}, 200

        except ValidationError as err:
            return handle_validation_error(err)

        except IntegrityError as err:
            return handle_integrity_error(err)

    else:
        return {"message": f"Loan with id {loan_id} does not exist"}, 404
    
# Update Loan By Member - /loans/member/member_id - PUT, PATCH
@loans_bp.route("/member/<int:member_id>", methods=["PUT", "PATCH"])
def update_loan_by_member(member_id):
    stmt = db.select(Loan).filter_by(member_id = member_id)
    loan = db.session.scalar(stmt)
    body_data = request.get_json()

    if not body_data:
        return {"message": "No data provided or invalid JSON"}, 400

    if loan:
        try:
            validated_data = loan_schema.load(body_data)

            # Borrow Date and Return Date Validation using validate_date_format
            if "borrow_date" in validated_data or "return_date" in validated_data:
                borrow_date = validated_data.get("borrow_date", loan.borrow_date)
                return_date = validated_data.get("return_date", loan.return_date)

                # Validate the date format for both borrow_date and return_date
                borrow_date_obj, borrow_date_error = validate_date_format(borrow_date)
                if borrow_date_error:
                    return {"message": borrow_date_error}, 400

                return_date_obj, return_date_error = validate_date_format(return_date)
                if return_date_error:
                    return {"message": return_date_error}, 400

                # Ensure Borrow Date is Before Return Date
                if borrow_date_obj >= return_date_obj:
                    return {"message": "Borrow date must be before return date"}, 400

                loan.borrow_date = borrow_date_obj
                loan.return_date = return_date_obj

            # Book ID Validation and Existence Check
            if "book_id" in validated_data:
                try:
                    loan.book_id = int(validated_data["book_id"])
                    if loan.book_id <= 0:
                        return {"message": "Book ID must be a positive integer"}, 400

                    # Check if the book exists in the database
                    book = db.session.query(Book).filter_by(id=loan.book_id).first()
                    if not book:
                        return {"message": f"Book with ID {loan.book_id} does not exist"}, 400
                except ValueError:
                    return {"message": "Book ID must be an integer"}, 400

            # Member ID Validation and Existence Check
            if "member_id" in validated_data:
                try:
                    loan.member_id = int(validated_data["member_id"])
                    if loan.member_id <= 0:
                        return {"message": "Member ID must be a positive integer"}, 400

                    # Check if the member exists in the database
                    member = db.session.query(Member).filter_by(id=loan.member_id).first()
                    if not member:
                        return {"message": f"Member with ID {loan.member_id} does not exist"}, 400
                except ValueError:
                    return {"message": "Member ID must be an integer"}, 400

            db.session.commit()
            return {"message": "Loan updated successfully", "loan": loan_schema.dump(loan)}, 200

        except ValidationError as err:
            return handle_validation_error(err)

        except IntegrityError as err:
            return handle_integrity_error(err)

    else:
        return {"message": f"Member with id {member_id} does not exist"}, 404