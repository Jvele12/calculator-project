import pytest
from app.input_validators import validate_numbers, validate_operation_name
from app.exceptions import ValidationError

def test_validate_numbers_type():
    with pytest.raises(ValidationError):
        validate_numbers("x", 3)

def test_validate_numbers_range(monkeypatch):
    monkeypatch.setattr("app.input_validators.MAX_INPUT_VALUE", 10)
    with pytest.raises(ValidationError):
        validate_numbers(20, 3)

def test_validate_operation_name():
    with pytest.raises(ValidationError):
        validate_operation_name("invalid", ["add", "subtract"])
