from marshmallow import fields, validate, ValidationError
from datetime import date, timedelta

from init import db, ma

class Loan(db.Model):
    __tablename__ = "loans"

    id = db.Column(db.Integer, primary_key = True)
    borrow_date = db.Column(db.Date, nullable = False)
    return_date = db.Column(db.Date, nullable = False)
    book_id = db.Column(db.Integer, nullable = False)
    member_id = db.Column(db.In)
