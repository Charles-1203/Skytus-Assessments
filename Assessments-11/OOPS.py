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

# Create a Student class with a method to calculate average marks.

# Create a Rectangle class with methods to find area and perimeter.

# Create an Employee class that displays salary details.

# Create a Book class to store title, author, and price, and display details.

# Create a Circle class to find area and circumference.

# Create a Laptop class with a method to apply discounts on price.

# Create a Flight class with seat booking functionality.

# Create a Shop class with a method to add and list products.
