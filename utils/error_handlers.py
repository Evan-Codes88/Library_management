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
        else:
            return format_error_response(f"A unique constraint violation occurred on a column. Details: {error_detail}", status_code=409)

    # Check for NOT_NULL_VIOLATION
    elif err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
        column_name = getattr(err.orig.diag, 'column_name', 'unknown')
        return format_error_response(f"The '{column_name}' is required and cannot be null", status_code=400)
    
    else:
        return format_error_response("An integrity error occurred. Please try again", status_code=400)


def validate_isbn(self, value):
    if not (validate.Regexp(r"^(?:\d{1,5}-)?(?:\d{1,7}-)?(?:\d{1,6}-)?\d{1,3}[\dX]$", value) or validate.Regexp(r"^(?:\d{3}-)?\d{1,5}-\d{1,7}-\d{1,6}-\d{1}$", value)):
        raise ValidationError("ISBN must be either 10 or 13 digits long.")
