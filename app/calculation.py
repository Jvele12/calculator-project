from app.operation_factory import OperationFactory

class Calculation:
    def __init__(self, operation, a, b, result):
        self.operation = operation
        self.a = a
        self.b = b
        self.result = result

    def __repr__(self):
        return f"Calculation({self.operation}, {self.a}, {self.b}) = {self.result}"

class CalculationFactory:
    @staticmethod
    def create(operation_name, a, b):
        operation = OperationFactory.create_operation(operation_name)
        try:
            result = operation.execute(a, b)
        except ZeroDivisionError:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return Calculation(operation_name, a, b, result)
