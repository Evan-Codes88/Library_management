from marshmallow import fields, ValidationError


from init import db, ma

class Loan(db.Model):
    """
    Represents a loan record in the library system.

    Attributes:
        id (int): The unique identifier for the loan.
        borrow_date (date): The date the book was borrowed.
        return_date (date): The date the book is due to be returned.
        book_id (int): The unique identifier for the book being loaned.
        member_id (int): The unique identifier for the member borrowing the book.
    
    Relationships:
        book (Book): A relationship with the Book model, indicating which book is being loaned.
        member (Member): A relationship with the Member model, indicating which member borrowed the book.
    
    Constraints:
        A unique constraint is enforced on the combination of `book_id` and `member_id`, ensuring that a specific book 
        can only be loaned to a member once at a time.
    """
    __tablename__ = "loans"

    id = db.Column(db.Integer, primary_key = True)
    borrow_date = db.Column(db.Date, nullable = False)
    return_date = db.Column(db.Date, nullable = False)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable = False)
    member_id = db.Column(db.Integer, db.ForeignKey("members.id") , nullable = False)

     # Relationship with the Book model, indicating the book being loaned.
    book = db.relationship("Book", back_populates = "loans")
    # Relationship with the Member model, indicating the member who borrowed the book.
    member = db.relationship("Member", back_populates = "loans")
   
   # Ensures that a book can only be loaned to a member once at a time.
    __table_args__ = (db.UniqueConstraint('book_id', 'member_id', name='uni_book_member'),)

class LoanSchema(ma.Schema):
    """
    Marshmallow schema for serialising and deserialising Loan objects.

    This schema defines the structure of the data that can be passed to and from the Loan model, including 
    validation for certain fields.

    Attributes:
        borrow_date (date): The date the book was borrowed.
        return_date (date): The date the book is due to be returned.
        member_name (str): The name of the member who borrowed the book.
    """
    borrow_date = fields.Date(required=True)
    return_date = fields.Date(required=True)
    member_name = fields.Method("get_member_name")

    def validate_dates(self, data, **kwargs):
        """
        Validates the relationship between borrow_date and return_date.
        """
        borrow_date = data.get("borrow_date")
        return_date = data.get("return_date")

        if borrow_date and return_date:
            if return_date < borrow_date:
                raise ValidationError(
                    {"return_date": "Return date must be on or after the borrow date."}
                )

    def get_member_name(self, obj):
        """
        Retrieves the name of the member associated with the loan.

        Args:
            obj (Loan): The loan object for which the member name is being retrieved.
        
        Returns:
            str: The name of the member, if available.
        """
        return obj.member.name if obj.member else None

    class Meta:
        """
        Specifies the fields to include when serialising the Loan object.
        """
        fields = ("id", "borrow_date", "return_date", "book_id", "member_id", "member_name")

loan_schema = LoanSchema()
loans_schema = LoanSchema(many = True)