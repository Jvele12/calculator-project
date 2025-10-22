class OperationStrategy:
    def execute(self, a, b):
        raise NotImplementedError

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
        return a ** b

class Root(OperationStrategy):
    def execute(self, a, b):
        if b <= 0:
            raise ValueError("Invalid root")
        return a ** b  
