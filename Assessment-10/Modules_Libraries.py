# Create a custom math module and import it in another file.
import math_module  
result = math_module.sum()


# Create a module to perform string operations.

import string_module
input_string = "Hello World"
vowel_count = string_module.count_vowels(input_string)
print(f"The number of vowels in '{input_string}' is: {vowel_count}")
word_count = string_module.count_words(input_string)
print(f"The number of words in '{input_string}' is: {word_count}")
substring_count = string_module.count_occurrences(input_string, "o")
print(f"The number of occurrences of 'o' in '{input_string}' is: {substring_count}")

# Use random module to generate 5 random integers.
import random

for i in range(5):
    print(random.randint(1,1000))

# Use datetime module to display current date and time.

import datetime

current_datetime = datetime.datetime.now()
print("Current date and time:", current_datetime)


# Use math module to find factorial of a number.

# Create a package shapes with modules for circle and rectangle.

# Import multiple functions from one module and use them.

# Write a program to shuffle a list using random module.

# Write a program to calculate the difference between two dates.

# Use os module to list files in a directory.