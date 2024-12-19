from marshmallow import fields, ValidationError
from datetime import date


from init import ma
from models.loan import Loan


class LoanSchema(ma.Schema):
    """
    Marshmallow schema for serialising and deserialising Loan objects.

    This schema defines the structure of the data that can be passed to and from the Loan model. It includes
    validation for ensuring the integrity of loan data, such as checking borrow and return dates, enforcing
    maximum loan durations, and limiting the number of active loans a member can have.

    Attributes:
        borrow_date (fields.Date): The date the book was borrowed, required for loan creation.
        return_date (fields.Date): The date the book is due to be returned, required for loan creation.
        member_name (fields.Method): A custom method field to retrieve the member's name from the associated Loan object.
    
    Constants:
        MAX_LOAN_DURATION (int): The maximum duration (in days) for which a loan can be issued.
        MAX_BORROW_LIMIT (int): The maximum number of active loans a member can have simultaneously.
    """
    borrow_date = fields.Date(required=True)
    return_date = fields.Date(required=True)
    member_name = fields.Method("get_member_name")

    MAX_LOAN_DURATION = 30  # Maximum loan duration in days
    MAX_BORROW_LIMIT = 5    # Maximum number of books a member can borrow at a time

    def validate_dates_and_limits(self, data):
        """
        Validates the loan data provided during creation or update.

        This function checks:
        1. That the return date is not earlier than the borrow date.
        2. That the loan duration does not exceed the maximum allowed duration.
        3. That the member has not exceeded the maximum borrowing limit for active loans.

        Args:
            data (dict): The loan data to validate. Must include 'borrow_date', 'return_date', and 'member_id'.

        Raises:
            ValidationError: If any validation checks fail. The error message details the specific issue.
        """
        borrow_date = data.get("borrow_date")
        return_date = data.get("return_date")
        member_id = data.get("member_id")

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
                Loan.return_date >= date.today()
            ).count()

            if active_loans_count >= self.MAX_BORROW_LIMIT:
                raise ValidationError(
                    {"member_id": f"Member cannot have more than {self.MAX_BORROW_LIMIT} active loans."}
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
loans_schema = LoanSchema(many=True)
