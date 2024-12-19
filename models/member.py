from marshmallow import fields, validate

from init import db, ma
from utils.validate_date_range import validate_date_range



class Member(db.Model):
    """
    Represents a member of the library system.

    Attributes:
        id (int): The unique identifier for the member.
        name (str): The name of the member.
        membership_number (str): A unique 8-digit membership number for the member.
        email (str): The email address of the member.
        join_date (date): The date the member joined the library.
    
    Relationships:
        loans (list): A list of loan records associated with the member, representing the books borrowed by the member.
    """
    __tablename__ = "members"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False, unique = True)
    membership_number = db.Column(db.String(8), nullable = False, unique = True)
    email = db.Column(db.String(100), nullable = False, unique = True)
    join_date = db.Column(db.Date)

    # Relationship with the Loan model, indicating the books borrowed by the member.
    loans = db.relationship("Loan", back_populates = "member", cascade = "all, delete-orphan")

class MemberSchema(ma.Schema):
    """
    Marshmallow schema for serialising and deserialising Member objects.

    This schema defines the structure of the data that can be passed to and from the Member model, including 
    validation for certain fields.

    Attributes:
        name (str): The name of the member.
        membership_number (str): The unique 8-digit membership number of the member.
        email (str): The email address of the member.
        join_date (date): The date the member joined the library.
    """
    name = fields.String(
        validate = [
            validate.Length(min = 2, error = "Name must be at least 2 characters long."),
            validate.Regexp(r"^[A-Za-z\s\-.']+$", error = "Name can only contain letters, spaces, hyphens, apostraphes and periods.")
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
        """
        Specifies the fields to include when serialising the Member object.
        """
        fields = ("id", "name", "membership_number", "email", "join_date")

member_schema = MemberSchema()
members_schema = MemberSchema(many = True)