# Function to check if a number is prime.
n=int(input("Enter a number:"))
def is_prime(n):
    if(n%2==0):
        print(n,"is not a prime number")
    else:
        print(n,"is a prime number")
is_prime(n)

# Function to reverse a string.

str=input("Enter a string:")
def reverse_string(str):
    return str[::-1]

reversed_str=reverse_string(str)
print("Reversed string:",reversed_str)



# Function to find factorial.

n=int(input("Enter a number:"))
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

result=factorial(n)
print("Factorial of",n,"is",result)

# Function to calculate simple interest.

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100  
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
interest = simple_interest(principal, rate, time)
print("Simple Interest:", interest) 


# Function to check if a word is palindrome.

def is_palindrome(word):
    word=word.lower()
    return word == word[::-1]       

word=input("Enter a word:")
if is_palindrome(word):
    print(word,"is a palindrome.")
else:
    print(word,"is not a palindrome.")


# Function to count vowels in a string.

def count_vowels(string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

string=input("Enter a string:")
vowel_count = count_vowels(string)
print("Number of vowels in the string:", vowel_count)

# Function to merge two lists.

def merge_lists(list1, list2):
    return list1 + list2
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = merge_lists(list1, list2)
print("Merged list:", merged_list)


# Function to find GCD of two numbers.

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = gcd(num1, num2)
print("GCD of", num1, "and", num2, "is", result)

# Function to find area of rectangle.
def area_of_rectangle(length, width):
    return length * width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = area_of_rectangle(length, width)
print("Area of the rectangle:", area)



# Function to check Armstrong number.
def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == num

num = int(input("Enter a number: "))
if is_armstrong(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")

