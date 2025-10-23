from app.operations import (
    Add, Subtract, Multiply, Divide,
    Power, Root, Modulus, IntDivide,
    Percent, AbsDiff
)

class OperationFactory:
    @staticmethod
    def create_operation(name: str):
        operations = {
            "add": Add,
            "subtract": Subtract,
            "multiply": Multiply,
            "divide": Divide,
            "power": Power,
            "root": Root,
            "modulus": Modulus,
            "int_divide": IntDivide,
            "percent": Percent,
            "abs_diff": AbsDiff
        }

        operation_class = operations.get(name.lower())
        if not operation_class:
            raise ValueError(f"Invalid operation: '{name}'")

        return operation_class()
