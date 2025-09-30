import builtins
import runpy
from pathlib import Path
from io import StringIO
from app.calculator.repl import run

def run_repl(monkeypatch, inputs):
    """Helper function to simulate REPL input."""
    input_iter = iter(inputs)
    monkeypatch.setattr(builtins, 'input', lambda _: next(input_iter))

    output = StringIO()
    monkeypatch.setattr('sys.stdout', output)

    run()
    return output.getvalue()

def test_exit_command(monkeypatch):
    output = run_repl(monkeypatch, ["exit"])
    assert "Goodbye!" in output

def test_help_command(monkeypatch):
    output = run_repl(monkeypatch, ["help", "exit"])
    assert "Available commands" in output

def test_invalid_command(monkeypatch):
    output = run_repl(monkeypatch, ["foo", "exit"])
    assert "Invalid command" in output

def test_basic_addition(monkeypatch):
    output = run_repl(monkeypatch, ["+", "2", "3", "history", "exit"])
    assert "Result: 5.0" in output
    assert "2.0 + 3.0 = 5.0" in output

def test_invalid_number_input(monkeypatch):
    output = run_repl(monkeypatch, ["+", "five", "3", "exit"])
    assert "Invalid input. Please enter numbers only." in output

def test_repl_addition_direct(monkeypatch):
    from app.calculator.repl import run

    inputs = ["+", "2", "3", "exit"]
    input_iter = iter(inputs)
    monkeypatch.setattr(builtins, 'input', lambda _: next(input_iter))

    output = StringIO()
    monkeypatch.setattr('sys.stdout', output)

    run()
    result_output = output.getvalue()
    assert "Result: 5.0" in result_output

