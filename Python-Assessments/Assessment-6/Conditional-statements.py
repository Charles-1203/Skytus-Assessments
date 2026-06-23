# Check if a person is eligible to vote (age ≥ 18).


age=int(input("Enter your Age:"))

if(age>=18):
    print("Yes Eligible to vote")
else:
    print("No ,Eligible to ")
    
# Grade calculator based on marks: 90+ = A, 80+ = B, else C.

english=float(input("Enter  your marks in english :"))

if (english>=90):
    print("Grade A")
elif english>=80:
    print("Grade B")
else:
    print("Grade C")



# Simulate a traffic light: Red = Stop, Yellow = Wait, Green = Go.

traffic_light=input("Enter the traffic light color (Red, Yellow, Green):")

if traffic_light=="Red":
    print("Stop")
elif traffic_light=="Yellow":
    print("Wait")
elif traffic_light=="Green":
    print("Go")
else:
    print("Invalid traffic light color")

# ATM withdrawal check: sufficient balance or not.


balance=float(input("Enter your account balance:"))
withdrawal_amount=float(input("Enter the amount you want to withdraw:"))
  
if withdrawal_amount<=balance:
    print("Withdrawal successful")
else:
    print("Insufficient balance")





# Check if a number is positive, negative, or zero.
number=float(input("Enter a number:"))
if number>0:
    print("Positive")
elif number<0:
    print("Negative")
else:
    print("Zero")

# Check if a number lies within a given range.
range_start=float(input("Enter the start of the range:"))
range_end=float(input("Enter the end of the range:"))
if range_start<=number<=range_end:
    print("Number is within the range")
else:
    print("Number is not within the range")

# Username & password verification.
username=input("Enter your username:")
password=input("Enter your password:")
if username=="admin" and password=="password":
    print("Login successful")
else:
    print("Invalid username or password")

# Electricity bill calculator based on units consumed.
units=float(input("Enter the number of units consumed:"))
if units<=100:
    bill=units*1.5
elif units<=200:
    bill=100*1.5+(units-100)*2
else:
    bill=100*1.5+100*2+(units-200)*3
print("Electricity bill:", bill)

# Simple calculator (add, subtract, multiply, divide).

num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))       
operation=input("Enter the operation (+, -, *, /):")

if operation=="+":
    result=num1+num2
elif operation=="-":
    result=num1-num2
elif operation=="*":
    result=num1*num2
elif operation=="/":
    if num2!=0:
        result=num1/num2
    else:
        result="Error: Division by zero"
else:
    result="Invalid operation"
print("Result:", result)

# Check type of triangle (equilateral, isosceles, scalene).
side1=float(input("Enter the length of side 1:"))
side2=float(input("Enter the length of side 2:"))
side3=float(input("Enter the length of side 3:"))

if side1==side2==side3:
    print("Equilateral triangle")
elif side1==side2 or side2==side3 or side1==side3:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
