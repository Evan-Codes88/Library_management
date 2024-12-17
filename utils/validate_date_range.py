from datetime import date, timedelta
from marshmallow import ValidationError, validates_schema


def validate_date_range(value):
    min_date = date(2001, 1, 1) # January 1st 2001 (This is set for this date as this is when the "library" was created.)
    today_date = date.today()

    if value < min_date:
        raise ValidationError(f"Date must be on or after {min_date.strftime('%B %d, %Y')}.")
    if value > today_date:
        raise ValidationError(f"Date must be on or before {today_date.strftime('%B %d, %Y')}.")
    

@validates_schema
def validate_dates(self, data):
    """
    Validates the relationship between borrow_date and return_date.
    """
    borrow_date = data.get("borrow_date")
    return_date = data.get("return_date")

    if borrow_date and return_date:
        if return_date < borrow_date:
            raise ValidationError({"return_date": "Return date must be on or after the borrow date."})