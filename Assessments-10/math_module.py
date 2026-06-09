def sum(a, b):
    result = a + b
    print(f"The sum of {a} and {b} is: {result}")

def product(a, b):
    result = a * b
    print(f"The product of {a} and {b} is: {result}")

def difference(a, b):
    result = a - b
    print(f"The difference between {a} and {b} is: {result}")   

def quotient(a, b):
    if b != 0:
        result = a / b
        print(f"The quotient of {a} and {b} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")

def factorial(num):
    if num < 0:
        print("Error: Factorial is not defined for negative numbers.")
    elif num == 0 or num == 1:
        print(f"The factorial of {num} is: 1")
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        print(f"The factorial of {num} is: {result}")