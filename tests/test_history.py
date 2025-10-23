import os
import pandas as pd
from app.history import HistoryManager
from app.calculation import Calculation

def test_add_and_save(tmp_path, monkeypatch):
    monkeypatch.setattr("app.calculator_config.HISTORY_DIR", str(tmp_path))
    hist = HistoryManager()
    hist.clear()  # start clean

    calc = Calculation("add", 2, 3, 5)
    hist.add(calc)

    records = hist.get_all()
    assert isinstance(records, list)
    assert len(records) == 1

    hist.save()
    expected_file = os.path.join(tmp_path, "calculator_history.csv")
    assert os.path.exists(expected_file)

    df = pd.read_csv(expected_file)
    assert "Operation" in df.columns
    assert df.iloc[0]["Result"] == 5

def test_restore_and_clear(tmp_path, monkeypatch):
    monkeypatch.setattr("app.calculator_config.HISTORY_DIR", str(tmp_path))
    hist = HistoryManager()
    hist.clear()

    calc1 = Calculation("add", 1, 2, 3)
    calc2 = Calculation("subtract", 5, 1, 4)
    hist.add(calc1)
    hist.add(calc2)

    assert len(hist.get_all()) == 2

    old_state = hist.get_all()[:1]
    hist.restore(old_state)
    assert len(hist.get_all()) == 1

    hist.clear()
    assert len(hist.get_all()) == 0

def test_observer_trigger(monkeypatch, tmp_path):
    monkeypatch.setattr("app.calculator_config.HISTORY_DIR", str(tmp_path))
    hist = HistoryManager()

    triggered = {"notified": False}

    class DummyObserver:
        def update(self, calculation):
            triggered["notified"] = True

    hist.attach_observer(DummyObserver())
    calc = Calculation("multiply", 2, 4, 8)
    hist.add(calc)

    assert triggered["notified"] is True

def test_history_load_corrupted_csv(tmp_path, monkeypatch):
    bad_file = tmp_path / "calculator_history.csv"
    bad_file.write_text("not,a,valid,csv")
    monkeypatch.setattr("app.calculator_config.HISTORY_DIR", str(tmp_path))
    hist = HistoryManager()
    assert isinstance(hist.get_all(), list)


def test_history_load_failure(monkeypatch, tmp_path):
    bad_file = tmp_path / "bad.csv"
    bad_file.write_text("corrupt,data\nnot,valid")
    monkeypatch.setattr("app.calculator_config.HISTORY_DIR", str(tmp_path))
    hist = HistoryManager()
    assert isinstance(hist.get_all(), list)
