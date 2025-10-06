import pandas as pd
from app.calculator_config import HISTORY_FILE, AUTOSAVE

class HistoryManager:
    def __init__(self):
        try:
            self.df = pd.read_csv(HISTORY_FILE)
        except FileNotFoundError:
            self.df = pd.DataFrame(columns=["Operation", "Operands", "Result"])

    def add(self, operation, operands, result):
        new_row = {"Operation": operation, "Operands": operands, "Result": result}
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)
        if AUTOSAVE:
            self.save()

    def save(self):
        self.df.to_csv(HISTORY_FILE, index=False)

    def load(self):
        self.df = pd.read_csv(HISTORY_FILE)

    def clear(self):
        self.df = pd.DataFrame(columns=["Operation", "Operands", "Result"])
