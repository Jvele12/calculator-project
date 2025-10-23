from app.history import HistoryManager
from app.calculator_memento import Caretaker
from app.calculation import Calculation
from app.operation_factory import OperationFactory


class Calculator:
    def __init__(self):
        self.history = HistoryManager()
        self.caretaker = Caretaker()
        self.factory = OperationFactory()

    def perform(self, operation_name, a, b):
        try:
            operation = self.factory.create_operation(operation_name)
            result = operation.execute(a, b)

            calc = Calculation(operation_name, a, b, result)
            self.history.add(calc)

            self.caretaker.save_state(self.history)

            print(f"✅ {operation_name}({a}, {b}) = {result}")
            return result

        except Exception as e:
            print(f"❌ Error performing operation '{operation_name}': {e}")
            return None


def main_repl():
    calc = Calculator()
    print("Welcome to the Advanced Calculator! Type 'help' for commands, or 'exit' to quit.\n")

    while True:
        user_input = input(">> ").strip()

        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break

        elif user_input.lower() == "help":
            print("Available operations: add, subtract, multiply, divide, power, root, modulus, int_divide, percent, abs_diff")
            print("Usage: <operation> <a> <b>")
            print("Example: power 2 3\n")
            continue

        elif not user_input:
            continue

        try:
            parts = user_input.split()
            if len(parts) != 3:
                print("⚠️ Invalid format. Use: <operation> <a> <b>")
                continue

            operation, a, b = parts
            a, b = float(a), float(b)

            result = calc.perform(operation, a, b)
            if result is not None:
                print("Result:", result)

        except ValueError:
            print("⚠️ Please enter numeric values for operands.")
        except Exception as e:
            print("⚠️ Unexpected error:", e)

class CalculationFactory:
    @staticmethod
    def create(operation_name, a, b):
        operation = OperationFactory.create_operation(operation_name)
        result = operation.execute(a, b)
        return Calculation(operation_name, a, b, result)