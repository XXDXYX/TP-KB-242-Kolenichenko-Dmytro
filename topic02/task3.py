def enterOperation():
    operation = input("Enter operation (+, -, *, /): ")
    return operation
def enterNumberA():
    a = int(input("Enter first number: "))
    return a
def enterNumberB():
    b = int(input("Enter second number: "))
    return b
def calculate(a, b, operation):
    match operation:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            if b != 0:
                return a / b
            else:
                return "Error"
        case _:
            return "Invalid operation"
print(calculate(enterNumberA(), enterNumberB(), enterOperation()))       