import pytest
from app.calculator_repl import Calculator
from app.calculation import CalculationFactory

def test_exit_branch(monkeypatch, capsys):
    inputs = iter(["exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    from app.calculator_repl import main_repl
    main_repl()
    captured = capsys.readouterr()
    assert "Goodbye" in captured.out

def test_invalid_operation_raises():
    with pytest.raises(ValueError):
        CalculationFactory.create("nonsense", 1, 2)

def test_divide_by_zero_handled():
    calc = CalculationFactory.create("/", 10, 0)
    assert "Error" in str(calc.result)