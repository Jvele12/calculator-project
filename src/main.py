from src.operations import add, subtract, multiply, divide

def repl(inputs=None, output_fn=print):
    index = 0 
    def get_input(prompt):
        nonlocal index
        if inputs is not None:
            if index < len(inputs):
                value = inputs[index]
                index += 1
                return value
            else:
                return "exit"
        return input(prompt)
        
    output_fn("Welcome to my Calculator App")
    while True:
        operation = get_input(f"Please select an option you would like to do add,sub,mul,div").lower() 
        
        if operation == "exit":
            output_fn("Thanks for Using this application, Goodbye")
            break
        if operation not in ['add', 'subtract', 'multiply', 'divide']:
            output_fn("Invalid, Please try again")
            continue

        try:
            a = float(get_input(f"Please enter your first number"))
            b  = float(get_input(f"Please enter your second number"))

            if operation == 'add':
                result = add(a,b) 
            elif operation == 'subtract':
                result = subtract(a,b)
            elif operation == 'multiply':
                result = multiply(a,b)
            elif operation == 'divide':
                result = divide(a,b)
            else:
                output_fn("Invalid, Please try again")
                continue
            output_fn(f"Result is {result}\n")
        except (ValueError, ZeroDivisionError) as e:
            output_fn(f"Error: {e}\n")
        
if __name__ == "__main__":
    repl()