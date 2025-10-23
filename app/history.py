import os
import pandas as pd
from datetime import datetime
from app.calculator_config import HISTORY_DIR, AUTO_SAVE
from app.logger import LoggingObserver, AutoSaveObserver


class HistoryManager:
    def __init__(self):
        self._history = []  
        self._observers = []

        self.history_file = os.path.join(HISTORY_DIR, "calculator_history.csv")
        os.makedirs(HISTORY_DIR, exist_ok=True)

        if os.path.exists(self.history_file):
            try:
                df = pd.read_csv(self.history_file)
                self._history = df.to_dict("records")
            except Exception:
                print("⚠️ Failed to read history file. Starting fresh.")
                self._history = []
        else:
            self._history = []

        log_obs = LoggingObserver()
        auto_obs = AutoSaveObserver(self)
        self.attach_observer(log_obs)
        self.attach_observer(auto_obs)

    # -----------------------------
    # Observer pattern integration
    # -----------------------------
    def attach_observer(self, observer):
        self._observers.append(observer)

    def detach_observer(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self, calculation):
        for observer in self._observers:
            observer.update(calculation)

    # -----------------------------
    # Core History Functionality
    # -----------------------------
    def add(self, calculation):
        record = {
            "Operation": calculation.operation,
            "Operands": f"{calculation.a}, {calculation.b}",
            "Result": calculation.result,
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        self._history.append(record)
        self.notify_observers(calculation)

        if AUTO_SAVE:
            self.save()

    def get_all(self):
        return self._history.copy()

    def restore(self, state):
        self._history = state or []
        self.save()

    def save(self):
        df = pd.DataFrame(self._history)
        df.to_csv(self.history_file, index=False)

    def load(self):
        if os.path.exists(self.history_file):
            df = pd.read_csv(self.history_file)
            self._history = df.to_dict("records")
        else:
            print("⚠️ No history file found.")

    def clear(self):
        self._history = []
        self.save()
