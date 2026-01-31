# ==================================================
# PYTHON BEGINNER → ADVANCED INDEX
# File: python_beginner_to_advanced_index.py
# Purpose: Learn Python step-by-step with explanations
# ==================================================


# ==================================================
# 1. PRINTING (BEGINNER)
# ==================================================

print("Hello, Python!")
# print() outputs text or values to the console
# Used for debugging, messages, and learning


# ==================================================
# 2. VARIABLES & DATA TYPES
# ==================================================

age = 20
# Integer: whole numbers

price = 19.99
# Float: decimal numbers

name = "Alex"
# String: text data

is_logged_in = True
# Boolean: True or False

print(age, price, name, is_logged_in)
# Printing multiple values at once


# ==================================================
# 3. TYPE CHECKING & CASTING
# ==================================================

print(type(age))
# type() shows the data type of a variable

user_age = int("25")
# int() converts a string to an integer
# Needed for math operations


# ==================================================
# 4. USER INPUT
# ==================================================

username = input("Enter your username: ")
# input() gets data from the user (always a string)

print("Welcome,", username)


# ==================================================
# 5. OPERATORS
# ==================================================

x = 10
y = 3

print(x + y)   # Addition
print(x - y)   # Subtraction
print(x * y)   # Multiplication
print(x / y)   # Division
print(x % y)   # Remainder
print(x ** y)  # Power


# ==================================================
# 6. CONDITIONAL STATEMENTS
# ==================================================

if x > y:
    print("x is greater than y")
else:
    print("x is not greater than y")

# if/else lets programs make decisions


# ==================================================
# 7. ELIF (MULTIPLE CONDITIONS)
# ==================================================

score = 78

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Fail")


# ==================================================
# 8. LOOPS
# ==================================================

# FOR LOOP
for i in range(5):
    print("Iteration:", i)
# Used when you know how many times to loop

# WHILE LOOP
count = 0
while count < 3:
    print("Count:", count)
    count += 1
# Used when loop depends on a condition


# ==================================================
# 9. LISTS
# ==================================================

numbers = [1, 2, 3, 4]
# Lists store multiple values

numbers.append(5)
# Adds a value to the list

print(numbers[0])
# Access by index (starts at 0)


# ==================================================
# 10. TUPLES
# ==================================================

colors = ("red", "green", "blue")
# Tuples are immutable (cannot change)
# Used for fixed data


# ==================================================
# 11. SETS
# ==================================================

unique_numbers = {1, 2, 2, 3}
# Sets remove duplicates automatically
print(unique_numbers)


# ==================================================
# 12. DICTIONARIES
# ==================================================

user = {
    "name": "Alex",
    "age": 20,
    "active": True
}
# Dictionaries store key-value pairs

print(user["name"])


# ==================================================
# 13. FUNCTIONS
# ==================================================

def greet(person):
    # Function takes an argument
    print("Hello,", person)

greet("Sam")

# Functions help reuse code


# ==================================================
# 14. RETURN VALUES
# ==================================================

def add(a, b):
    return a + b
    # return sends a value back

result = add(3, 4)
print(result)


# ==================================================
# 15. DEFAULT PARAMETERS
# ==================================================

def power(base, exponent=2):
    return base ** exponent
# Default values are used if not provided

print(power(5))
print(power(5, 3))


# ==================================================
# 16. LAMBDA FUNCTIONS (INTERMEDIATE)
# ==================================================

square = lambda n: n * n
# Short one-line anonymous function

print(square(6))


# ==================================================
# 17. LIST COMPREHENSIONS
# ==================================================

squares = [n * n for n in range(5)]
# Short syntax for creating lists

print(squares)


# ==================================================
# 18. ERROR HANDLING
# ==================================================

try:
    value = int(input("Enter a number: "))
    print(10 / value)
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")

# Prevents crashes


# ==================================================
# 19. FILE HANDLING
# ==================================================

with open("example.txt", "w") as file:
    file.write("Hello file!")
# Writes text to a file

with open("example.txt", "r") as file:
    print(file.read())
# Reads from a file


# ==================================================
# 20. MODULES & IMPORTS
# ==================================================

import math

print(math.sqrt(25))
# Use built-in or external modules


# ==================================================
# 21. OBJECT-ORIENTED PROGRAMMING (ADVANCED)
# ==================================================

class Person:
    # Class defines a blueprint

    def __init__(self, name, age):
        # Constructor initializes data
        self.name = name
        self.age = age

    def introduce(self):
        # Method inside class
        print("My name is", self.name)

p1 = Person("Alex", 20)
p1.introduce()


# ==================================================
# 22. INHERITANCE
# ==================================================

class Student(Person):
    def study(self):
        print(self.name, "is studying")

student = Student("Emma", 22)
student.study()


# ==================================================
# 23. DECORATORS (ADVANCED)
# ==================================================

def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hi():
    print("Hi!")

say_hi()
# Decorators modify behavior of functions


# ==================================================
# 24. GENERATORS
# ==================================================

def count_up(n):
    for i in range(n):
        yield i
        # yield returns values one at a time

for num in count_up(3):
    print(num)


# ==================================================
# 25. END OF FILE
# ==================================================

print("Python Beginner → Advanced Index Complete 🚀")
