from marshmallow import ValidationError

def validate_and_strip_field(data, field):
    value = data.get(field, "").strip()
    if not value:
        raise ValidationError(f"{field} cannot be empty")
    return value
