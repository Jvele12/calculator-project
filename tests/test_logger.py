import os
import pandas as pd
from app.logger import LoggingObserver, AutoSaveObserver, Observer
from app.calculation import Calculation

def test_observer_base_class():
    obs = Observer()
    try:
        obs.update(None)
    except NotImplementedError:
        assert True
    else:
        assert False, "Expected NotImplementedError"

def test_logging_observer_logs(tmp_path, capsys):
    log_file = tmp_path / "test.log"
    os.environ["LOG_FILE"] = str(log_file)
    observer = LoggingObserver()
    calc = Calculation("add", 2, 3, 5)
    observer.update(calc)
    out = capsys.readouterr().out
    assert "🪵 Logged:" in out

def test_autosave_observer_creates_csv(tmp_path, capsys):
    class DummyHistory:
        history_file = tmp_path / "calc.csv"
    obs = AutoSaveObserver(DummyHistory())
    calc = Calculation("add", 2, 3, 5)
    obs.update(calc)
    out = capsys.readouterr().out
    assert os.path.exists(DummyHistory.history_file)
    df = pd.read_csv(DummyHistory.history_file)
    assert "Operation" in df.columns
    assert "💾 Auto-saved" in out

def test_autosave_observer_saves_and_prints(tmp_path, capsys):
    class DummyHistory:
        history_file = tmp_path / "auto_history.csv"

    obs = AutoSaveObserver(DummyHistory())
    calc = Calculation("add", 1, 2, 3)
    obs.update(calc)
    out = capsys.readouterr().out

    assert "Auto-saved" in out
    assert os.path.exists(DummyHistory.history_file)
    df = pd.read_csv(DummyHistory.history_file)
    assert df.iloc[0]["Result"] == 3