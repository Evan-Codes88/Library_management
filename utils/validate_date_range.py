from datetime import date, timedelta
from marshmallow import ValidationError, validates_schema


def validate_date_range(value):
    min_date = date(2001, 1, 1) # January 1st 2001 (This is set for this date as this is when the "library" was created.)
    today_date = date.today()

    if value < min_date:
        raise ValidationError(f"Date must be on or after {min_date.strftime('%B %d, %Y')}.")
    if value > today_date:
        raise ValidationError(f"Date must be on or before {today_date.strftime('%B %d, %Y')}.")