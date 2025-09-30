import pytest
from app.operation.arithmetic import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(-1, 5) == -5
    assert multiply(0, 5) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(-10, 2) == -5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
