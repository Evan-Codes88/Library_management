from datetime import date, datetime
from marshmallow import ValidationError, validates_schema


def validate_date_range(value):
    min_date = date(2001, 1, 1) # January 1st 2001 (This is set for this date as this is when the "library" was created.)
    today_date = date.today()

    if value < min_date:
        raise ValidationError(f"Date must be on or after {min_date.strftime('%B %d, %Y')}.")
    if value > today_date:
        raise ValidationError(f"Date must be on or before {today_date.strftime('%B %d, %Y')}.")
    

def validate_date_format(date_input):
    """
    Validates the date format (YYYY-MM-DD) and converts it to a datetime object.
    Handles both string and datetime.date inputs.
    Returns a tuple (datetime_object, error_message).
    """
    # If the date is already a datetime object (e.g. from the database), return it directly
    if isinstance(date_input, datetime):
        return date_input, None
    # If the date is a datetime.date object, convert it to datetime
    elif isinstance(date_input, date):  # `date` from datetime module
        return datetime.combine(date_input, datetime.min.time()), None
    # If the date is a string, try parsing it
    elif isinstance(date_input, str):
        try:
            date_obj = datetime.strptime(date_input, "%Y-%m-%d")
            return date_obj, None
        except ValueError:
            return None, "Date must be a string in the format YYYY-MM-DD"
    else:
        return None, "Date must be a string in the format YYYY-MM-DD"