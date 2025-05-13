"""
Python Expressions Complete Tutorial

This file contains all expression-related concepts in Python with examples.
Run this file to see all examples in action.
"""

# Section 1: Basic Expressions
print("\n=== Section 1: Basic Expressions ===\n")
print("Literal expressions:")
print(5)        # Integer literal
print(3.14)     # Float literal
print("Hello")  # String literal
print(True)     # Boolean literal

print("\nVariable expressions:")
x = 10
y = 20
print(x)        # Variable expression
print(x + y)    # More complex expression

print("\nFunction call expressions:")
length = len("Python")
print(length)   # Prints 6

print("\nMixed expressions:")
result = x * y + length
print(result)   # Prints 206 (10*20 + 6)

print("\nExpressions in control structures:")
if x + y > 15:
    print("The sum is greater than 15")


# Section 2: Arithmetic Operations
print("\n=== Section 2: Arithmetic Operations ===\n")
a = 10
b = 3

print("a + b =", a + b)  # 13
print("a - b =", a - b)  # 7
print("a * b =", a * b)  # 30
print("a / b =", a / b)  # 3.333...
print("a // b =", a // b)  # 3
print("a % b =", a % b)  # 1
print("a ** b =", a ** b)  # 1000

print("\nComplex expressions:")
result = (a + b) * 2 - (a / b)
print("Complex expression result:", result)  # ~23.666...

print("\nOperator precedence:")
print(2 + 3 * 4)  # 14, not 20
print((2 + 3) * 4)  # 20


# Section 3: Comparison Operators
print("\n=== Section 3: Comparison Operators ===\n")
x = 10
y = 5
z = 10

print("x == y:", x == y)  # False
print("x == z:", x == z)  # True
print("x != y:", x != y)  # True
print("x > y:", x > y)    # True
print("x < y:", x < y)    # False
print("5 < x < 15:", 5 < x < 15)  # True

print("\nString comparisons:")
print("'apple' == 'apple':", 'apple' == 'apple')  # True
print("'apple' < 'banana':", 'apple' < 'banana')  # True


# Section 4: Logical Operators
print("\n=== Section 4: Logical Operators ===\n")
a = True
b = False

print("a and b:", a and b)  # False
print("a or b:", a or b)  # True
print("not a:", not a)  # False

print("\nPractical example:")
age = 25
has_license = True
can_drive = age >= 18 and has_license
print("Can drive:", can_drive)  # True


# Section 5: Assignment Operators
print("\n=== Section 5: Assignment Operators ===\n")
x = 10
print("Initial x:", x)

x += 5; print("x += 5 →", x)  # 15
x -= 3; print("x -= 3 →", x)  # 12
x *= 2; print("x *= 2 →", x)  # 24
x /= 4; print("x /= 4 →", x)  # 6.0

print("\nWalrus operator example:")
if (n := len("hello")) > 3:
    print(f"Length is {n}")  # Length is 5


# Section 6: Bitwise Operators
print("\n=== Section 6: Bitwise Operators ===\n")
a = 10  # 1010
b = 4   # 0100

print("a & b =", a & b)  # 0
print("a | b =", a | b)  # 14
print("a ^ b =", a ^ b)  # 14
print("a << 1 =", a << 1)  # 20
print("a >> 1 =", a >> 1)  # 5

print("\nEven/odd check:")
num = 15
print(f"{num} is odd" if num & 1 else f"{num} is even")


# Section 7: Identity Operators
print("\n=== Section 7: Identity Operators ===\n")
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("a is b:", a is b)  # True
print("a is c:", a is c)  # False
print("x is None check:")
x = None
print("x is None:", x is None)  # True


# Section 8: Membership Operators
print("\n=== Section 8: Membership Operators ===\n")
fruits = ["apple", "banana", "cherry"]
print("'banana' in fruits:", "banana" in fruits)  # True

person = {"name": "Alice", "age": 25}
print("'name' in person:", "name" in person)  # True


# Section 9: Operator Precedence
print("\n=== Section 9: Operator Precedence ===\n")
print("3 + 4 * 5 =", 3 + 4 * 5)  # 23
print("(3 + 4) * 5 =", (3 + 4) * 5)  # 35
print("-3 ** 2 =", -3 ** 2)  # -9
print("True or False and True:", True or False and True)  # True


# Section 10: Conditional Expressions
print("\n=== Section 10: Conditional Expressions ===\n")
age = 20
status = "Adult" if age >= 18 else "Minor"
print("Status:", status)  # Adult

numbers = [1, 2, 3, 4, 5]
result = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print("Even/Odd list:", result)


# Section 11: List and Dict Comprehensions
print("\n=== Section 11: List and Dict Comprehensions ===\n")
squares = [x**2 for x in range(5)]
print("Squares list:", squares)

squares_dict = {x: x**2 for x in range(5)}
print("Squares dictionary:", squares_dict)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print("Flattened matrix:", flattened)


print("\n=== Tutorial Complete ===")