from app.operation import arithmetic

class Calculation:
    def __init__(self, a, b, operation_name, result):
        self.a = a
        self.b = b
        self.operation_name = operation_name
        self.result = result

    def __str__(self):
        return f"{self.a} {self.operation_name} {self.b} = {self.result}"

class CalculationFactory:
    def __init__(self):
        self.history = []

    def create_calculation(self, a, b, operation_name):
        operations = {
            '+': arithmetic.add,
            '-': arithmetic.subtract,
            '*': arithmetic.multiply,
            '/': arithmetic.divide,
        }

        if operation_name not in operations:
            raise ValueError("Invalid operation")

        try:
            result = operations[operation_name](a, b)
        except ZeroDivisionError:
            result = "Error: Division by zero"

        calculation = Calculation(a, b, operation_name, result)
        self.history.append(calculation)
        return calculation

    def show_history(self):
        return [str(calc) for calc in self.history]
