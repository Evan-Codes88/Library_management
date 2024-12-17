from marshmallow import fields, ValidationError, validates_schema


from init import db, ma
from utils.validate_date_range import validate_dates

class Loan(db.Model):
    __tablename__ = "loans"

    id = db.Column(db.Integer, primary_key = True)
    borrow_date = db.Column(db.Date, nullable = False)
    return_date = db.Column(db.Date, nullable = False)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), nullable = False)
    member_id = db.Column(db.Integer, db.ForeignKey("member.id") , nullable = False)

    member = db.relationship("Members", back_populates = "loans")
    book = db.relationship("Books", back_populates = "loans")

class LoanSchema(ma.Schema):
    borrow_date = fields.Date(
         validate = validate_dates()
    )
    return_date = fields.Date(
        validate = validate_dates()
    )
            
    class Meta:
        fields = ("id", "borrow_date", "return_date", "book_id", "member_id")