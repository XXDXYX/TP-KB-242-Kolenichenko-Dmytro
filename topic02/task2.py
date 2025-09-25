def enterOperation():
    operation = input("Enter operation (+, -, *, /): ")
    return operation
def enterNumberA():
    a = float(input("Enter first number: "))
    return a
def enterNumberB():
    b = float(input("Enter second number: "))
    return b
def calculate(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            return "Error"

print(calculate(enterNumberA(), enterNumberB(), enterOperation()))
