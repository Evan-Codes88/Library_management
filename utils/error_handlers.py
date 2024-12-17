import re
from marshmallow import ValidationError, validate
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes


def format_error_response(message, errors=None, status_code=400):
    """Formats error responses consistently."""
    response = {"message": message}
    if errors:
        response["errors"] = errors
    return response, status_code



def handle_validation_error(err: ValidationError):
    errors = [message for messages in err.messages.values()for message in messages]
    return format_error_response("Validation failed", errors, 400)




def handle_integrity_error(err: IntegrityError):
    if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
        # Try to get detailed error message from PostgreSQL
        error_detail = str(err.orig).lower()

        # Check for specific fields in the error detail string
        if 'name' in error_detail:
            return format_error_response("The provided name is already taken. Please try another.", status_code=409)
        elif 'email' in error_detail:
            return format_error_response("The provided email is already in use. Please try another.", status_code=409)
        elif 'membership_number' in error_detail:
            return format_error_response("The provided membership number is already in use. Please try another.", status_code=409)
        elif 'isbn' in error_detail:
            return format_error_response("The provided isbn is already in use. Please try another.", status_code=409)
        else:
            return format_error_response(f"A unique constraint violation occurred on a column. Details: {error_detail}", status_code=409)

    # Check for NOT_NULL_VIOLATION
    elif err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
        column_name = getattr(err.orig.diag, 'column_name', 'unknown')
        return format_error_response(f"The '{column_name}' is required and cannot be null", status_code=400)
    
    else:
        return format_error_response("An integrity error occurred. Please try again", status_code=400)


def validate_isbn(value):
    try:
        # Define strict regex patterns for ISBN-10 and ISBN-13
        isbn_10_pattern = r"^\d{1,5}-\d{1,7}-\d{1,6}-\d{1,3}[\dX]$"  # ISBN-10 pattern
        isbn_13_pattern = r"^\d{3}-\d{1,5}-\d{1,7}-\d{1,6}-\d{1}$"  # ISBN-13 pattern

        # Check if the value matches ISBN-10 or ISBN-13 format
        if not (re.match(isbn_10_pattern, value) or re.match(isbn_13_pattern, value)):
            error_message = "ISBN must be either in 10-digit or 13-digit format."

            # If the length is too short or too long, append detailed message
            if len(value) < 10:
                error_message += " It appears to be too short to be a valid ISBN."
            elif len(value) > 13:
                error_message += " It seems too long to be a valid ISBN."
            
            # Check if the dashes are placed correctly (1 to 4 dashes)
            if "-" in value:
                dash_count = value.count("-")
                if dash_count < 3:
                    error_message += " There should be at least 3 hyphens to separate sections."
                elif dash_count > 4:
                    error_message += " Too many hyphens. There should be no more than 4 hyphens."

            # More detailed validation based on length and format
            if len(value) == 10 and not re.match(isbn_10_pattern, value):
                error_message += " For ISBN-10, ensure the correct number of digits and the optional hyphens."
            elif len(value) == 13 and not re.match(isbn_13_pattern, value):
                error_message += " For ISBN-13, ensure the correct number of digits and the optional hyphens."

            raise ValidationError({"isbn": [error_message]})

    except ValidationError as e:
        # Handle validation errors related to ISBN format
        raise e