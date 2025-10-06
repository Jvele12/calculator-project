from app.operations import Add, Subtract, Multiply, Divide, Power, Root

class Calculation:
    def __init__(self, a, b, operation_name, result):
        self.a = a
        self.b = b
        self.operation_name = operation_name
        self.result = result

    def __str__(self):
        return f"{self.a} {self.operation_name} {self.b} = {self.result}"


class CalculationFactory:
    @staticmethod
    def create(operation, a, b):
        operations = {
            '+': Add(),
            'add': Add(),
            '-': Subtract(),
            'subtract': Subtract(),
            '*': Multiply(),
            'multiply': Multiply(),
            '/': Divide(),
            'divide': Divide(),
            '^': Power(),
            'power': Power(),
            'root': Root()
    }   

        if operation not in operations:
            raise ValueError(f"Invalid operation: {operation}")

        operation_obj = operations[operation]
        try:
            result = operation_obj.execute(a, b)
        except ZeroDivisionError:
            result = "Error: Division by zero"

        return Calculation(a, b, operation, result)

