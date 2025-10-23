import pytest
from app.calculation import Calculation, CalculationFactory


def test_calculation_creation():
    calc = Calculation("add", 2, 3, 5)
    assert calc.operation == "add"
    assert calc.a == 2
    assert calc.b == 3
    assert calc.result == 5
    assert "add" in repr(calc)


def test_calculation_factory_add():
    calc = CalculationFactory.create("add", 2, 3)
    assert isinstance(calc, Calculation)
    assert calc.result == 5


def test_calculation_factory_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        CalculationFactory.create("divide", 10, 0)
