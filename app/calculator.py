from app.history import HistoryManager
from app.calculator_memento import Caretaker
from app.calculation import Calculation
from app.operation_factory import OperationFactory
from app.input_validators import validate_numbers, validate_operation_name
from app.exceptions import CalculatorError, ValidationError
from colorama import Fore, Style, init

init(autoreset=True)

class Calculator:
    def __init__(self):
        self.history = HistoryManager()
        self.caretaker = Caretaker()
        self.factory = OperationFactory()

    def perform(self, operation_name, a, b):
        try:
            validate_numbers(a, b)
            valid_ops = [
                "add", "subtract", "multiply", "divide", "power", "root",
                "modulus", "int_divide", "percent", "abs_diff"
            ]
            validate_operation_name(operation_name, valid_ops)

            self.caretaker.save_state(self.history.get_all())

            operation = self.factory.create_operation(operation_name)
            result = operation.execute(a, b)

            calc = Calculation(operation_name, a, b, result)
            self.history.add(calc)

            print(Fore.GREEN + f"✅ {operation_name}({a}, {b}) = {result}")
            return result

        except ValidationError as e:
            print(Fore.YELLOW + f"⚠️ Error performing operation: {e}")
        except ZeroDivisionError:
            print(Fore.RED + "❌ Error: Division by zero is not allowed.")
        except CalculatorError as e:
            print(Fore.YELLOW + f"⚠️ Calculator Error: {e}")
        except Exception as e:
            print(Fore.RED + f"⚠️ Unexpected Error: {e}")

    def undo(self):
        prev_state = self.caretaker.undo()
        if prev_state is not None:
            self.history.restore(prev_state)
            print(Fore.CYAN + "↩️  Undid last operation.")
        else:
            print(Fore.YELLOW + "⚠️  Nothing to undo.")

    def redo(self):
        next_state = self.caretaker.redo()
        if next_state is not None:
            self.history.restore(next_state)
            print(Fore.CYAN + "↪️  Redid last undone operation.")
        else:
            print(Fore.YELLOW + "⚠️  Nothing to redo.")


def main_repl():
    calc = Calculator()
    print(Fore.MAGENTA + Style.BRIGHT + "🧮 Welcome to the Advanced Calculator!")
    print(Fore.MAGENTA + "Type 'help' for commands, or 'exit' to quit.\n")

    while True:
        user_input = input(Fore.WHITE + ">> ").strip().lower()
        if not user_input:
            continue

        if user_input == "exit":
            print(Fore.CYAN + "👋 Goodbye! Thanks for using the calculator.")
            break

        elif user_input == "help":
            print(Fore.GREEN + Style.BRIGHT + """
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
                print(Fore.YELLOW + "⚠️ Invalid format. Use: <operation> <a> <b>")
                continue

            operation, a, b = parts
            a, b = float(a), float(b)
            result = calc.perform(operation, a, b)
            if result is not None:
                print(Fore.CYAN + f"Result: {result}")

        except ValueError:
            print(Fore.YELLOW + "⚠️ Please enter numeric values for operands.")
        except Exception as e:
            print(Fore.RED + f"⚠️ Unexpected error: {e}")


if __name__ == "__main__":
    main_repl()
