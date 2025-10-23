import pytest
from app.operations import (
    Add, Subtract, Multiply, Divide, Power, Root,
    Modulus, IntDivide, Percent, AbsDiff, OperationStrategy
)

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
])
def test_add(a, b, expected):
    assert Add().execute(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (5, 2, 3),
    (10, 20, -10),
])
def test_subtract(a, b, expected):
    assert Subtract().execute(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 12),
    (5, 0, 0),
])
def test_multiply(a, b, expected):
    assert Multiply().execute(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (8, 2, 4),
    (9, 3, 3),
])
def test_divide(a, b, expected):
    assert Divide().execute(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Divide().execute(5, 0)

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 8),
    (5, 0, 1),
])
def test_power(a, b, expected):
    assert Power().execute(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (27, 3, 3),
    (16, 2, 4),
])
def test_root_valid(a, b, expected):
    assert Root().execute(a, b) == expected


def test_root_invalid():
    with pytest.raises(ValueError):
        Root().execute(9, 0)


@pytest.mark.parametrize("a, b, expected", [
    (10, 3, 1),
    (15, 5, 0),
])
def test_modulus(a, b, expected):
    assert Modulus().execute(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (10, 3, 3),
    (9, 2, 4),
])
def test_int_divide(a, b, expected):
    assert IntDivide().execute(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (25, 100, 25),
    (50, 200, 25),
])
def test_percent(a, b, expected):
    assert round(Percent().execute(a, b), 2) == expected


@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 5),
    (-2, 4, 6),
])
def test_abs_diff(a, b, expected):
    assert AbsDiff().execute(a, b) == expected

def test_operation_strategy_not_implemented():
    op = OperationStrategy()
    with pytest.raises(NotImplementedError):
        op.execute(1, 2)
