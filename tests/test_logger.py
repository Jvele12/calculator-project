import os
import pandas as pd
from app.logger import LoggingObserver, AutoSaveObserver, Observer
from app.calculation import Calculation


# ------------------------------
# 1️⃣ Base Observer Abstract Method
# ------------------------------
def test_observer_base_class():
    obs = Observer()
    try:
        obs.update(None)
    except NotImplementedError:
        assert True
    else:
        assert False, "Expected NotImplementedError"


# ------------------------------
# 2️⃣ LoggingObserver Behavior
# ------------------------------
def test_logging_observer_logs(tmp_path, capsys, monkeypatch):
    """Verify LoggingObserver writes and prints messages."""
    log_dir = tmp_path / "logs"
    log_file = log_dir / "test.log"

    # Patch the LOG_FILE env so it writes to tmp_path
    monkeypatch.setattr("app.calculator_config.LOG_FILE", str(log_file))
    observer = LoggingObserver()

    calc = Calculation("add", 2, 3, 5)
    observer.update(calc)
    out = capsys.readouterr().out

    # Ensure print occurred
    assert "🪵 Logged:" in out

    # Ensure log file was written
    assert os.path.exists(log_file)
    with open(log_file, "r", encoding="utf-8") as f:
        content = f.read()
    assert "add(2, 3) = 5" in content


# ------------------------------
# 3️⃣ AutoSaveObserver Creates and Writes CSV
# ------------------------------
def test_autosave_observer_creates_csv(tmp_path, capsys):
    """Ensure AutoSaveObserver writes a CSV and prints confirmation."""
    class DummyHistory:
        history_file = str(tmp_path / "calc.csv")  # convert to str for os.path.exists()

    obs = AutoSaveObserver(DummyHistory())
    calc = Calculation("add", 2, 3, 5)
    obs.update(calc)
    out = capsys.readouterr().out

    # Ensure print message and file exist
    assert "Auto-saved" in out
    assert os.path.exists(DummyHistory.history_file)

    # Verify file contents
    df = pd.read_csv(DummyHistory.history_file)
    assert "Operation" in df.columns
    assert df.iloc[0]["Result"] == 5


# ------------------------------
# 4️⃣ AutoSaveObserver Print and Append
# ------------------------------
def test_autosave_observer_saves_and_prints(tmp_path, capsys):
    """Ensure subsequent calls append correctly."""
    class DummyHistory:
        history_file = str(tmp_path / "auto_history.csv")

    obs = AutoSaveObserver(DummyHistory())

    calc1 = Calculation("add", 1, 2, 3)
    calc2 = Calculation("subtract", 5, 2, 3)

    obs.update(calc1)
    obs.update(calc2)

    out = capsys.readouterr().out
    assert "Auto-saved" in out
    assert os.path.exists(DummyHistory.history_file)

    df = pd.read_csv(DummyHistory.history_file)
    assert len(df) == 2
    assert set(df["Operation"]) == {"add", "subtract"}
