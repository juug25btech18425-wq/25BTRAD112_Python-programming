# Lab Exercise 4: Simple calculator and area calculation programs

# Simple calculator
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Program to calculate area of a circle
radius = float(input("Enter radius: "))
area = 3.14 * radius * radius
print("Area of circle:", area)

# Program to calculate area of a rectangle
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
print("Area of rectangle:", area)
