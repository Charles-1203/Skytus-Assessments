# 9. Write a program that uses `and` & `or` operators to check multiple conditions.

team = input("Enter Team Name: ")

wins = int(input("Enter total wins: "))
nrr = float(input("Enter Net Run Rate: "))
points = int(input("Enter points: "))

if (points >= 16 and nrr > 0) or (points >= 14 and wins >= 7):
    print(team, "is likely to qualify for IPL playoffs")
else:
    print(team, "may not qualify")


# 10. Divide two numbers and print the quotient and remainder separately.