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

def test_logging_observer_logs(tmp_path, capsys, monkeypatch):
    log_dir = tmp_path / "logs"
    log_file = log_dir / "test.log"

    monkeypatch.setattr("app.calculator_config.LOG_FILE", str(log_file))
    observer = LoggingObserver()

    calc = Calculation("add", 2, 3, 5)
    observer.update(calc)
    out = capsys.readouterr().out

    assert "🪵 Logged:" in out

    assert os.path.exists(log_file)
    with open(log_file, "r", encoding="utf-8") as f:
        content = f.read()
    assert "add(2, 3) = 5" in content

def test_autosave_observer_creates_csv(tmp_path, capsys):
    class DummyHistory:
        history_file = str(tmp_path / "calc.csv")  

    obs = AutoSaveObserver(DummyHistory())
    calc = Calculation("add", 2, 3, 5)
    obs.update(calc)
    out = capsys.readouterr().out

    assert "Auto-saved" in out
    assert os.path.exists(DummyHistory.history_file)

    df = pd.read_csv(DummyHistory.history_file)
    assert "Operation" in df.columns
    assert df.iloc[0]["Result"] == 5

def test_autosave_observer_saves_and_prints(tmp_path, capsys):
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
