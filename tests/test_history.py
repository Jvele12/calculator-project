import pandas as pd
from app.history import HistoryManager

def test_load_and_clear(tmp_path):
    file = tmp_path / "hist.csv"
    df = pd.DataFrame([{"Operation": "add", "Operands": [1, 2], "Result": 3}])
    df.to_csv(file, index=False)

    hist = HistoryManager()
    hist.df = pd.read_csv(file)
    hist.clear()
    assert hist.df.empty

    hist.save()
    hist.load()
    assert isinstance(hist.df, pd.DataFrame)

def test_history_add_and_load(tmp_path, monkeypatch):
    monkeypatch.setattr("app.calculator_config.HISTORY_FILE", str(tmp_path / "fake.csv"))
    hist = HistoryManager()
    hist.add("add", [1, 2], 3)
    assert not hist.df.empty

    hist.save()
    hist.load()
    assert isinstance(hist.df, pd.DataFrame)