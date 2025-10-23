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
            self.caretaker.save_state(self.history.get_all())

            operation = self.factory.create_operation(operation_name)
            result = operation.execute(a, b)

            calc = Calculation(operation_name, a, b, result)
            self.history.add(calc)

            print(f"✅ {operation_name}({a}, {b}) = {result}")
            return result

        except Exception as e:
            print(f"❌ Error performing operation '{operation_name}': {e}")
            return None

    def undo(self):
        prev_state = self.caretaker.undo()
        if prev_state is not None:
            self.history.restore(prev_state)
            print("↩️  Undid last operation.")
        else:
            print("⚠️  Nothing to undo.")

    def redo(self):
        next_state = self.caretaker.redo()
        if next_state is not None:
            self.history.restore(next_state)
            print("↪️  Redid last undone operation.")
        else:
            print("⚠️  Nothing to redo.")


def main_repl():
    calc = Calculator()
    print("Welcome to the Advanced Calculator! Type 'help' for commands, or 'exit' to quit.\n")

    while True:
        user_input = input(">> ").strip().lower()

        if not user_input:
            continue

        if user_input == "exit":
            print("👋 Goodbye!")
            break

        elif user_input == "help":
            print("""
Available operations:
  add, subtract, multiply, divide, power, root, modulus, int_divide, percent, abs_diff
Commands:
  undo   → undo last operation
  redo   → redo last undone operation
  exit   → exit program
Usage example:
  add 2 3
""")
            continue

        elif user_input == "undo":
            calc.undo()
            continue

        elif user_input == "redo":
            calc.redo()
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


if __name__ == "__main__":
    main_repl()
