from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from collections import OrderedDict


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
        return format_error_response("The provided name is already taken. Please try another", status_code = 409)
    elif err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
        return format_error_response(f"The '{err.orig.diag.column_name}' is required and cannot be null", status_code = 400)
    else:
        return format_error_response("An integrity error occurred. Please try again", status_code = 400)