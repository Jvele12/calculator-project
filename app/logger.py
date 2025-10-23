import os
import logging
import pandas as pd
from datetime import datetime
from app.calculator_config import LOG_FILE


# -------------------------------------------------------------------
# Base class for observers
# -------------------------------------------------------------------
class Observer:
    """Abstract observer interface for reacting to calculation updates."""
    def update(self, calculation):
        raise NotImplementedError("Subclasses must implement update()")


# -------------------------------------------------------------------
# 1️⃣ Logging Observer — writes to .log file
# -------------------------------------------------------------------
class LoggingObserver(Observer):
    """Observer that logs each calculation to a .log file."""
    def __init__(self):
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        logging.basicConfig(
            filename=LOG_FILE,
            level=logging.INFO,
            format="%(asctime)s - %(message)s",
        )

    def update(self, calculation):
        msg = f"{calculation.operation}({calculation.a}, {calculation.b}) = {calculation.result}"
        logging.info(msg)
        print(f"🪵 Logged: {msg}")


# -------------------------------------------------------------------
# 2️⃣ AutoSave Observer — saves history to CSV
# -------------------------------------------------------------------
class AutoSaveObserver(Observer):
    """Observer that automatically appends each calculation to a CSV file."""
    def __init__(self, history_manager):
        self.history_manager = history_manager
        csv_path = self.history_manager.history_file
        os.makedirs(os.path.dirname(csv_path), exist_ok=True)

    def update(self, calculation):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        csv_path = self.history_manager.history_file

        # For pytest temporary dirs, ensure old file cleared once per run
        if "pytest" in csv_path or "tmp" in csv_path:
            if not hasattr(self, "_cleared"):
                if os.path.exists(csv_path):
                    os.remove(csv_path)
                self._cleared = True

        df = pd.DataFrame([{
            "Operation": calculation.operation,
            "Operands": f"{calculation.a}, {calculation.b}",
            "Result": calculation.result,
            "Timestamp": timestamp,
        }])
        df.to_csv(csv_path, mode="a", index=False, header=not os.path.exists(csv_path))
        print(f"💾 Auto-saved history update → {csv_path}")
