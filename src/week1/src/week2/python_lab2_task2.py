"""
Lab 3.2 – Comprehensions and Transformations

Goals:
- Practice list, set, and dictionary comprehensions.
- Transform and filter data concisely.

Instructions:
Given the list:
    numbers = [3, 8, -2, 7, 0, -5, 10]

1. Create a list `squares` with the square of each number.
2. Create a list `positives` containing only positive numbers.
3. Create a set `even_squares` of the squares of even numbers.
4. Create a dictionary `cubes` mapping each number to its cube.
5. Print all results.
"""

# Given list of numbers
numbers = [3, 8, -2, 7, 0, -5, 10]

# 1. Create a list `squares` with the square of each number
squares = [num ** 2 for num in numbers]

# 2. Create a list `positives` containing only positive numbers
positives = [num for num in numbers if num > 0]

# 3. Create a set `even_squares` of the squares of even numbers
even_squares = {num ** 2 for num in numbers if num % 2 == 0}

# 4. Create a dictionary `cubes` mapping each number to its cube
cubes = {num: num ** 3 for num in numbers}

# Print results
print("Squares:", squares)
print("Positives:", positives)
print("Even squares:", even_squares)
print("Cubes:", cubes)
