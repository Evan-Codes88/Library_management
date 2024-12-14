from marshmallow import fields, validate

from init import db, ma
from utils.validate_date_range import validate_date_range



class Member(db.Model):
    __tablename__ = "members"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False, unique = True)
    membership_number = db.Column(db.String(8), nullable = False, unique = True)
    email = db.Column(db.String(100), nullable = False, unique = True)
    join_date = db.Column(db.Date)

    loan = db.relationship("Loans", back_populates = "members", cascade = "all, delete-orphan")

class MemberSchema(ma.Schema):
    name = fields.String(
        validate = [
            validate.Length(min = 2, error = "Name must be at least 2 characters long."),
            validate.Regexp(r"^[A-Za-z\s\-.']+$", error = "Name can only contain letters, spaces, hyphens, and periods.")
    ])
    membership_number = fields.String(
        validate = validate.Regexp(r'^\d{8}$', error = "Membership Number must contain 8 digits.")
    )
    email = fields.String(
        validate =
        validate.Regexp(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', error = "Please enter a valid email address 'e.g., example@email.com'")
    )
    join_date = fields.Date(validate=validate_date_range)  # Apply custom date validation

    class Meta:
        fields = ("id", "name", "membership_number", "email", "join_date")

member_schema = MemberSchema()
members_schema = MemberSchema(many = True)