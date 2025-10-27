"""
Write a function greet_user(name) that:
- removes extra spaces with .strip()
- capitalizes the first letter with .capitalize()
- returns "Hello, <Name>! Welcome to Python!"
Ask user for their name and print result.
"""

def greet_user(name):
    # Remove extra spaces and make the first letter uppercase
    name = name.strip()
    name = name.capitalize()
    return "Hello, " + name + "! Welcome to Python!"

# Main program
user_name = input("Enter your name: ")
greeting = greet_user(user_name)
print(greeting)