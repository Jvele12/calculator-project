import pytest
from app.operations import Add, Subtract, Multiply, Divide, Power, Root
from app.operations import OperationStrategy

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
])
def test_add(a, b, expected):
    assert Add().execute(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 8),
    (4, 0.5, 2),
])
def test_power_and_root(a, b, expected):
    if b > 1:
        assert Power().execute(a, b) == expected
    else:
        assert Root().execute(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Divide().execute(5, 0)

def test_operation_strategy_not_implemented():
    op = OperationStrategy()
    with pytest.raises(NotImplementedError):
        op.execute(1, 2)


@pytest.mark.parametrize("cls,a,b,expected", [
    (Add, 1, 1, 2),
    (Subtract, 5, 2, 3),
    (Multiply, 3, 4, 12),
    (Divide, 8, 2, 4),
])
def test_all_basic_operations(cls, a, b, expected):
    assert cls().execute(a, b) == expected