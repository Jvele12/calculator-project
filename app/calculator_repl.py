from app.history import HistoryManager
from app.calculator_memento import Caretaker
from app.calculation import CalculationFactory

class Calculator:
    def __init__(self):
        self.factory = CalculationFactory()

    def perform(self, operation, a, b):
        # create Calculation object
        calc = CalculationFactory.create(operation, a, b)
        result = calc.result        # ← remove parentheses
        print(result)
        return result


def main_repl():
    calc = Calculator()
    print("Welcome to the Advanced Calculator! Type 'exit' to quit.")

    while True:
        user_input = input("Enter operation (e.g. + 2 3): ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        try:
            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid format. Use: <operation> <a> <b>")
                continue

            operation, a, b = parts
            a, b = float(a), float(b)
            result = calc.perform(operation, a, b)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)
