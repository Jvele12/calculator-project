import pytest
from src.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (5, 2, 3),
    (-1, -1, 0),
    (10, 0, 10),
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (4, 3, 12),
    (0, 5, 0),
    (-2, 3, -6),
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected

def test_divide_normal():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
