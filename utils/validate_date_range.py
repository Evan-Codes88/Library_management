from datetime import date, timedelta
from marshmallow import ValidationError


def validate_date_range(value):
    min_date = date(2001, 1, 1) # January 1st 2001
    tomorrow_date = date.today() + timedelta(days = 1)

    if value < min_date:
        raise ValidationError(f"Date must be on or after {min_date.strftime('%B %d, %Y')}.")
    if value > tomorrow_date:
        raise ValidationError(f"Date must be on or before {tomorrow_date.strftime('%B %d, %Y')}.")