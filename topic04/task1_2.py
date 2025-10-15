def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b

def divide(a,b):
   try:
       return a / b
   except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

while True:
   try:    
       x = int(input("Enter first number: "))
       y = int(input("Enter second number: "))
       operation = input("Enter operation (+, -, *, /, exit): ")
       match operation:
           case "+":
             print(f"x + y = {add(x,y)}")
           case "-":
            print(f"x - y = {subtract(x,y)}")
           case "*":
            print(f"x * y = {multiply(x,y)}")
           case "/":
            print(f"x / y = {divide(x,y)}")
           case "exit":
            break
   except ValueError:
    print("Error: Invalid input type. Please enter numbers only.")       