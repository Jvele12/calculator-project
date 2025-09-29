from app.calculation.calculation_factory import CalculationFactory

def run():
    factory = CalculationFactory()
    print("Welcome to my Python CLI Calculator!")
    print("Commands: +, -, *, /, help, history, exit")

    while True:
        user_input = input("Enter operation or command: ").strip()

        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        elif user_input.lower() == "help":
            print("Available commands:")
            print("+  -> addition")
            print("-  -> subtraction")
            print("*  -> multiplication")
            print("/  -> division")
            print("history -> view past calculations")
            print("exit -> quit program")
        elif user_input.lower() == "history":
            for record in factory.show_history():
                print(record)
        elif user_input in ['+', '-', '*', '/']:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            calc = factory.create_calculation(a, b, user_input)
            print(f"Result: {calc.result}")
        else:
            print("Invalid command. Type 'help' for available commands.")
