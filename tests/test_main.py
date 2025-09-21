from src.main import repl

def test_add_operation(capsys):
    repl(inputs=["add", "2", "3", "exit"])
    captured = capsys.readouterr()
    output = captured.out
    assert "Result is 5.0" in output
    assert "Thanks for Using this application, Goodbye" in output


def test_subtract_operation(capsys):
    repl(inputs=["subtract", "10", "4", "exit"])
    captured = capsys.readouterr()
    output = captured.out
    assert "Result is 6.0" in output
    assert "Thanks for Using this application, Goodbye" in output


def test_multiply_operation(capsys):
    repl(inputs=["multiply", "3", "5", "exit"])
    captured = capsys.readouterr()
    output = captured.out
    assert "Result is 15.0" in output
    assert "Thanks for Using this application, Goodbye" in output


def test_divide_valid(capsys):
    repl(inputs=["divide", "8", "2", "exit"])
    captured = capsys.readouterr()
    output = captured.out
    assert "Result is 4.0" in output
    assert "Thanks for Using this application, Goodbye" in output


def test_divide_by_zero(capsys):
    repl(inputs=["divide", "5", "0", "exit"])
    captured = capsys.readouterr()
    output = captured.out
    assert "Error: division by zero" in output


def test_invalid_operation(capsys):
    repl(inputs=["xyz", "exit"])
    captured = capsys.readouterr()
    output = captured.out
    assert "Invalid, Please try again" in output


def test_exit_immediately(capsys):
    repl(inputs=["exit"])
    captured = capsys.readouterr()
    output = captured.out
    assert "Welcome to my Calculator App" in output
    assert "Thanks for Using this application, Goodbye" in output
