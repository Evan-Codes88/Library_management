from marshmallow import fields, ValidationError, validates_schema
from datetime import date

from init import db, ma
from models.book import Book

class Loan(db.Model):
    """
    Represents a loan record in the library system.
    """
    __tablename__ = "loans"

    id = db.Column(db.Integer, primary_key=True)
    borrow_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date, nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey("members.id"), nullable=False)
    status = db.Column(db.String(50), default="active")  # Add status field to track loan status

    # Relationship with the Book model
    book = db.relationship("Book", back_populates="loans")
    # Relationship with the Member model
    member = db.relationship("Member", back_populates="loans")

    # Unique constraint for the combination of book_id and member_id
    __table_args__ = (db.UniqueConstraint('book_id', 'member_id', name='uni_book_member'),)

class LoanSchema(ma.SQLAlchemyAutoSchema):
    borrow_date = fields.Date(required=True)
    return_date = fields.Date(required=True)
    member_name = fields.Method("get_member_name")

    MAX_LOAN_DURATION = 30  # Maximum loan duration in days
    MAX_BORROW_LIMIT = 5    # Maximum number of books a member can borrow at a time

    @validates_schema
    def validate_dates_and_limits(self, data, **kwargs):
        borrow_date = data.get("borrow_date")
        return_date = data.get("return_date")
        member_id = data.get("member_id")
        book_id = data.get("book_id")

        # Validate borrow and return dates
        if borrow_date and return_date:
            if return_date < borrow_date:
                raise ValidationError(
                    {"return_date": "Return date must be on or after the borrow date."}
                )
            # Validate loan duration
            loan_duration = (return_date - borrow_date).days
            if loan_duration > self.MAX_LOAN_DURATION:
                raise ValidationError(
                    {"return_date": f"Loan duration cannot exceed {self.MAX_LOAN_DURATION} days."}
                )

        # Validate maximum borrowing limits per member
        if member_id:
            active_loans_count = Loan.query.filter(
                Loan.member_id == member_id,
                Loan.status == "active"  # Only count active loans
            ).count()

            if active_loans_count >= self.MAX_BORROW_LIMIT:
                raise ValidationError(
                    {"member_id": f"Member cannot have more than {self.MAX_BORROW_LIMIT} active loans."}
                )

        # Validate available copies of the book
        if book_id:
            book = Book.query.get(book_id)
            if book and book.available_copies <= 0:
                raise ValidationError(
                    {"book_id": "There are no available copies of this book to loan."}
                )
            # Decrement available copies after the loan
            book.available_copies -= 1
            db.session.commit()  # Commit the change to the database

    def get_member_name(self, obj):
        return obj.member.name if obj.member else None

    class Meta:
        fields = ("id", "borrow_date", "return_date", "book_id", "member_id", "member_name")



loan_schema = LoanSchema()
loans_schema = LoanSchema(many=True)