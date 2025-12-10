from operations import input_numbers, input_operation
import functions
class Calculator:
    def __init__(self,num1, num2, operation):
        self.operation = operation
        self.num1 = num1
        self.num2 = num2
    def calculate(self):
        if self.operation == '+':    
           return functions.add(self.num1, self.num2)
        elif self.operation == '-':
            return functions.subtract(self.num1, self.num2)
        elif self.operation == '*':
            return functions.multiply(self.num1, self.num2)
        elif self.operation == '/':
            return functions.divide(self.num1, self.num2)
        else:
            return "Invalid operation"

while True:
    num1, num2 = input_numbers()
    operation = input_operation()
    calc = Calculator(num1, num2, operation)
    if calc.operation == 'q':
        print("Exiting the calculator. Goodbye!")
        break
    result = calc.calculate()
    print(f"Result: {result}")
    with open("log.txt", "a") as log_file:
            log_file.write(f"{num1} {operation} {num2} = {result}\n")