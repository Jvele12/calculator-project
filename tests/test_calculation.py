import pytest
from app.calculation import Calculation, CalculationFactory
from app.operation_factory import OperationFactory


def test_calculation_creation():
    calc = Calculation("add", 2, 3, 5)
    assert calc.operation == "add"
    assert calc.result == 5


def test_calculation_factory_valid():
    calc = CalculationFactory.create("add", 2, 3)
    assert isinstance(calc, Calculation)
    assert calc.result == 5


def test_calculation_factory_invalid():
    with pytest.raises(ValueError):
        CalculationFactory.create("nonsense", 1, 2)


def test_calculation_factory_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        CalculationFactory.create("divide", 10, 0)
