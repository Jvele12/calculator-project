from app.exceptions import ValidationError
from app.calculator_config import MAX_INPUT_VALUE

def validate_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValidationError("Inputs must be numeric values.")

    if abs(a) > MAX_INPUT_VALUE or abs(b) > MAX_INPUT_VALUE:
        raise ValidationError(
            f"Inputs exceed maximum allowed value of {MAX_INPUT_VALUE}."
        )


def validate_operation_name(name, valid_ops):
    if name.lower() not in valid_ops:
        raise ValidationError(
            f"Unsupported operation '{name}'. Use one of: {', '.join(valid_ops)}"
        )
