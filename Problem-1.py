#Problem-1:Simple Caluculator


class Calculator:
    def calculate(self, a, b, operation):
        if operation == "add":  #addition operation
            return a + b
        elif operation == "subtract":  #subtraction operation
            return a - b
        elif operation == "multiply":   #multiplication operation
            return a * b
        elif operation == "divide":     #division operation
            if b == 0:
                return "Cannot divide by zero"
            return a / b
        else:                           #if operation is not recognized
            return "Invalid operation"

# Here's how you use the Calculator class 
calc = Calculator()
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (add, subtract, multiply, divide): ").lower()

result = calc.calculate(a, b, op)
print("Result:", result)
