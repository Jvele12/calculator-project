from math import pow

class OperationStrategy:

    def execute(self, a, b):
        raise NotImplementedError("Subclasses must implement the execute method")


class Add(OperationStrategy):
    def execute(self, a, b):
        return a + b


class Subtract(OperationStrategy):
    def execute(self, a, b):
        return a - b


class Multiply(OperationStrategy):
    def execute(self, a, b):
        return a * b


class Divide(OperationStrategy):
    def execute(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b


class Power(OperationStrategy):
    def execute(self, a, b):
        return pow(a, b)


class Root(OperationStrategy):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot take 0th root")
        return pow(a, 1 / b)


class Modulus(OperationStrategy):
    def execute(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot take modulus by zero")
        return a % b


class IntDivide(OperationStrategy):
    def execute(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot perform integer division by zero")
        return a // b


class Percent(OperationStrategy):
    def execute(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot calculate percentage with divisor zero")
        return (a / b) * 100


class AbsDiff(OperationStrategy):
    def execute(self, a, b):
        return abs(a - b)
