import pytest
from app.calculator_repl import Calculator

def test_basic_operation(monkeypatch, capsys):
    calc = Calculator()
    
    result = calc.perform("add", 2, 3)
    assert result == 5

def test_repl_loop(monkeypatch, capsys):
    inputs = iter([
        "add 2 3", 
        "history",  
        "exit"      
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    from app.calculator_repl import main_repl  
    main_repl()

    captured = capsys.readouterr()
    assert "5" in captured.out  

def test_repl_exit_branch(monkeypatch, capsys):
    inputs = iter(["exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    from app.calculator_repl import main_repl
    main_repl()
    out = capsys.readouterr().out
    assert "Goodbye" in out
