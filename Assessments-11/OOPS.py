# Create a Car class with attributes like brand, model, and speed, and methods to accelerate/brake.

class Car:
    brand="BMW"
    Model="X3"
    speed=0
    def accelerate(self, increase):
        self.speed += increase
        print(f"Accelerating... Current speed: {self.speed} km/h")

    def brake(self, decrease):
        self.speed -= decrease
        if self.speed < 0:
            self.speed = 0
        print(f"Braking... Current speed: {self.speed} km/h")    


charles=Car()
print(f"Car Brand: {charles.brand}, Model: {charles.Model}")
charles.accelerate(50)
charles.brake(20)   

# Create a BankAccount class with deposit and withdraw methods.

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount}. Current Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount}. Current Balance: ${self.balance}")

# Create a Student class with a method to calculate average marks.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        if len(self.marks) == 0:
            return 0
        average = sum(self.marks) / len(self.marks)
        print(f"{self.name}'s Average Marks: {average}")
    

# Create a Rectangle class with methods to find area and perimeter.

class Rectangle:
    def  __init__(self, length, width):
        self.length = length
        self.width = width

    def find_area(self):
        return self.length * self.width

    def find_perimeter(self):
        return 2 * (self.length + self.width)
    

# Create an Employee class that displays salary details.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_salary(self):
        print(f"Employee Name: {self.name}, Salary: ${self.salary}")
        

# Create a Book class to store title, author, and price, and display details.

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: ${self.price}")

# Create a Circle class to find area and circumference.

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def find_area(self):
        return math.pi * self.radius ** 2

    def find_circumference(self):
        return 2 * math.pi * self.radius

# Create a Laptop class with a method to apply discounts on price.

class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def apply_discount(self, discount_percentage):
        discount_amount = self.price * (discount_percentage / 100)
        discounted_price = self.price - discount_amount
        print(f"Original Price: ${self.price}, Discounted Price: ${discounted_price}")

# Create a Flight class with seat booking functionality.

class Flight:
    def __init__(self, flight_number, total_seats):
        self.flight_number = flight_number
        self.total_seats = total_seats
        self.booked_seats = 0

    def book_seat(self):
        if self.booked_seats < self.total_seats:
            self.booked_seats += 1
            print(f"Seat booked successfully. Total booked seats: {self.booked_seats}")
        else:
            print("No seats available.")


# Create a Shop class with a method to add and list products.

class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Product '{product}' added to the shop.")

    def list_products(self):
        print("Products available in the shop:")
        for product in self.products:
            print(f"- {product}")
