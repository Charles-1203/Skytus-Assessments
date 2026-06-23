# Create a custom math module and import it in another file.
import math_module  
result = math_module.sum(44,77)
print(result)


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


fact=math_module.factorial(5)

print(fact)


# Create a package shapes with modules for circle and rectangle.

from Shapes import circle
from Shapes import rectangle

radius = 5
print(f"Circumference of circle with radius {radius}: {circle.cricumference(radius)}")
print(f"Area of circle with radius {radius}: {circle.area(radius)}")

length = 10
breadth = 5
print(f"Area of rectangle with length {length} and breadth {breadth}: {rectangle.area(length, breadth)}")
print(f"Perimeter of rectangle with length {length} and breadth {breadth}: {rectangle.perimeter(length, breadth)}") 