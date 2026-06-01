# Print numbers from 1 to 10.
i=1
while(i<=10):
    print(i)                                    
    i+=1



# Display multiplication table for a given number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        

n=input("Enter your Number :")
n=int(n)
print("Multiplication Table of ",n)
for i in range(1,11):
    print(n,"x",i,"=",n*i)

# Find factorial of a number.


n=input("Enter your Number :")
n=int(n)
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
print("Factorial of",n,"is",factorial)


# Generate the first N Fibonacci numbers.


n = int(input("Enter N: "))

a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# Check if a number is prime.
              
n=int(input("Enter a number: "))

if n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")   

# Reverse a number (e.g., 123 → 321).
str="123"

str=str[::-1]
print(str)
# Count digits in a number.

number="12345"

print(len(number))

# Find sum of even numbers between 1–100.
i=0
list=[]
for i in range (0,99,2):
    list.append(i)
sumation=sum(list)    
print("Sum off all even elements from 0-100 is:",sumation)

# Print a pyramid pattern.


for i in range(1, 4):
    print(" " * (4- i) + "*" * (2 * i - 1))

# Find all divisors of a number.