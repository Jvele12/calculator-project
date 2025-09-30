import pytest
from app.calculation.calculation_factory import CalculationFactory, Calculation

@pytest.fixture
def factory():
    return CalculationFactory()

def test_addition(factory):
    calc = factory.create_calculation(2, 3, '+')
    assert isinstance(calc, Calculation)
    assert calc.result == 5
    assert str(calc) == "2 + 3 = 5"

def test_invalid_operation(factory):
    with pytest.raises(ValueError):
        factory.create_calculation(2, 3, '%')  # '%' is not supported

def test_division_by_zero(factory):
    calc = factory.create_calculation(2, 0, '/')
    assert calc.result == "Error: Division by zero"

def test_history_tracking(factory):
    factory.create_calculation(1, 1, '+')
    factory.create_calculation(2, 2, '-')
    history = factory.show_history()
    assert len(history) == 2
    assert "1 + 1 = 2" in history[0]
    assert "2 - 2 = 0" in history[1]
