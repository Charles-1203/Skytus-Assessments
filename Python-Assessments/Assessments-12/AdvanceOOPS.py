# Write a program to handle division by zero error.

try:
    num1 =int(input("Enter the numerator: "))
    num2 = int(input("Enter the denominator: "))
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is: {result}")
except ZeroDivisionError:
    print("Error: Denominator cannot be zero.")
except Exception as e:
    print("Error: Please enter valid numbers.")

# Write a program to handle invalid integer input.

try:
    num = int(input("Enter an integer: "))
    print(f"You entered: {num}")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
except Exception as e:
    print("Error: Please enter a valid integer.")


# Write a program to open a file and handle the “file not found” error.

try:
    file_name = input("Enter the file name to open: ")
    with open(file_name, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("Error: An unexpected error occurred.")

# Write a program to demonstrate multiple exception blocks.

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is: {result}")
except ZeroDivisionError:
    print("Error: Denominator cannot be zero.")
except ValueError:
    print("Error: Invalid input. Please enter valid integers.")
except Exception as e:
    print("Error: An unexpected error occurred.")




# Write a program to use finally for resource cleanup.

try:
    file_name = input("Enter the file name to open: ")
    file = open(file_name, 'r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("Error: An unexpected error occurred.")
finally:
    try:
        file.close()
    except NameError:
        pass  
    
        

# Write a program to create a custom exception for invalid age (<18).

class InvalidAgeError(Exception):
    pass

def validate_age(age):
    if age < 18:
        raise InvalidAgeError("Invalid age: Age must be 18 or older.")
    else:
        print("Age is valid.")
try:
    age = int(input("Enter your age: "))
    validate_age(age)
except InvalidAgeError as e:
    print(e)
except ValueError:
    print("Error: Please enter a valid integer for age.")


# Write a program to handle IndexError when accessing a list.

try:
    my_list = [1, 2, 3]
    index = int(input("Enter the index to access: "))
    print(f"Element at index {index}: {my_list[index]}")
except IndexError:
    print("Error: Index out of range.")
except ValueError:
    print("Error: Please enter a valid integer for index.") 



# Write a program that takes two numbers and handles all possible errors.

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is: {result}")
except ZeroDivisionError:
    print("Error: Denominator cannot be zero.")
except ValueError:
    print("Error: Invalid input. Please enter valid integers.")
except Exception as e:
    print("Error: An unexpected error occurred.")


    
# Write a program to log errors to a file instead of printing them.

import logging
logging.basicConfig(filename='error_log.txt', level=logging.ERROR)
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is: {result}")
except ZeroDivisionError as e:
    logging.error("Denominator cannot be zero.")
except ValueError as e:
    logging.error("Invalid input. Please enter valid integers.")
except Exception as e:
    logging.error(f"An unexpected error occurred: {e}")


# Write a program that validates an email format and raises an exception for invalid ones.

import re
class InvalidEmailError(Exception):
    pass
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        raise InvalidEmailError("Invalid email format.")
    else:
        print("Email is valid.")



            