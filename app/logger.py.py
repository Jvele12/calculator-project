import os
import logging
import pandas as pd
from datetime import datetime
from app.calculator_config import LOG_FILE, HISTORY_DIR


# -------------------------------------------------------------------
# Base class for observers
# -------------------------------------------------------------------
class Observer:
    """Abstract observer base class."""
    def update(self, calculation):
        raise NotImplementedError("Subclasses must implement update()")


# -------------------------------------------------------------------
# 1️⃣ Logging Observer — writes to .log file
# -------------------------------------------------------------------
class LoggingObserver(Observer):
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
    def __init__(self, history_manager):
        self.history_manager = history_manager
        os.makedirs(HISTORY_DIR, exist_ok=True)

    def update(self, calculation):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        df = pd.DataFrame(
            [{
                "Operation": calculation.operation,
                "Operands": f"{calculation.a}, {calculation.b}",
                "Result": calculation.result,
                "Timestamp": timestamp,
            }]
        )
        csv_path = os.path.join(HISTORY_DIR, "calculator_history.csv")
        df.to_csv(csv_path, mode="a", index=False, header=not os.path.exists(csv_path))
        print(f"💾 Auto-saved history update → {csv_path}")
