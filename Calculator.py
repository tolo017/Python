# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Get user operation
operation = input("Enter operation (+, -, *, /): ")

# Perform operation
if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
else:
    print("Invalid operation")

# Run the program
# python Calculator.py
# Enter first number: 10
# Enter second number: 5
# Enter operation (+, -, *, /): *

# Output
# 50.0

# Display the result
print("The result is: ", num1, operation, num2, "=", num1 + num2)
# The result is: 10.0 * 5.0 = 15.0