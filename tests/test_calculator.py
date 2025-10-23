import pytest
from app.calculator import Calculator, main_repl


# -------------------------
# 1️⃣  Direct calculator logic
# -------------------------
def test_basic_addition():
    calc = Calculator()
    result = calc.perform("add", 2, 3)
    assert result == 5


def test_invalid_operation(capsys):
    calc = Calculator()
    result = calc.perform("weirdop", 2, 3)
    assert result is None
    out = capsys.readouterr().out
    assert "Error performing" in out


# -------------------------
# 2️⃣  REPL integration tests
# -------------------------
def test_repl_basic_flow(monkeypatch, capsys):
    inputs = iter([
        "add 2 3",
        "undo",
        "redo",
        "exit",
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main_repl()
    captured = capsys.readouterr().out

    assert "add(2.0, 3.0)" in captured
    assert "Undid last operation" in captured or "Nothing to undo" in captured
    assert "Goodbye" in captured


def test_repl_help_and_exit(monkeypatch, capsys):
    inputs = iter(["help", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main_repl()
    out = capsys.readouterr().out
    assert "Available operations" in out
    assert "Goodbye" in out
