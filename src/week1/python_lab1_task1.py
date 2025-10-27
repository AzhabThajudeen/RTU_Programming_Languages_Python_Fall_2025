"""
Task 1 – Simple Function with Arithmetic
---------------------------------------
Write a function circle_area(radius) that returns the area of a circle.
Formula: area = π × radius²
Use the math module for π.
Ask user for radius and print result with 2 decimals.
"""

import math

def circle_area(radius):
    # Calculate the area of a circle using the formula π × r²
    area = math.pi * (radius ** 2)
    return area

# Main part of the program
radius = float(input("Enter the radius: "))
area = circle_area(radius)

print("Area of the circle = {:.2f}".format(area))