import functions

def input_numbers():
    x = float(input("Enter first number (x): "))
    y = float(input("Enter second number (y): "))
    return x, y

def input_operation():
    operation = input("Enter operation (+, -, *, /, q): ")
    return operation

def main():
    while True:
        x, y = input_numbers()
        operation = input_operation()
        if operation == '+':    
            result = functions.add(x, y)
        elif operation == '-':
            result = functions.subtract(x, y)
        elif operation == '*':
            result = functions.multiply(x, y)
        elif operation == '/':
            result = functions.divide(x, y)
        elif operation == 'q':
            print("Exiting the program.")
            break
        else:
            print("Invalid operation")
            continue
        print(f"Result: {result}")
