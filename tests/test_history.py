import os
import pandas as pd
from app.history import HistoryManager
from app.calculation import Calculation


def test_add_and_save(tmp_path, monkeypatch):
    monkeypatch.setattr("app.calculator_config.HISTORY_DIR", str(tmp_path))
    hist = HistoryManager()

    calc = Calculation("add", 2, 3, 5)
    hist.add(calc)

    assert len(hist.get_all()) == 1

    hist.save()
    expected_file = os.path.join(tmp_path, "calculator_history.csv")
    assert os.path.exists(expected_file)

    hist.load()
    assert isinstance(hist.get_all(), list)


def test_restore_and_clear(tmp_path, monkeypatch):
    monkeypatch.setattr("app.calculator_config.HISTORY_DIR", str(tmp_path))
    hist = HistoryManager()

    calc1 = Calculation("add", 1, 2, 3)
    calc2 = Calculation("subtract", 5, 1, 4)
    hist.add(calc1)
    hist.add(calc2)

    assert len(hist.get_all()) == 2

    old_state = hist.get_all()[:-1]
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
