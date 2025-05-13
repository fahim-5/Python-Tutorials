"""
Python Conditional Statements Complete Tutorial

Covers:
- if statements
- else clauses
- elif statements
- Nested conditionals
- Ternary operations
- Truth value testing
- Pattern matching (Python 3.10+)
"""

print("\n=== Python Conditional Statements Tutorial ===\n")

# Section 1: Basic if statement
print("\n--- Section 1: Basic if Statement ---\n")
age = 20
if age >= 18:
    print("You are an adult")
    print("You can vote in elections!")

# Section 2: if-else statement
print("\n--- Section 2: if-else Statement ---\n")
temperature = 35
if temperature > 30:
    print("It's hot outside!")
else:
    print("It's not too hot")

# Section 3: if-elif-else chain
print("\n--- Section 3: if-elif-else Chain ---\n")
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f"Score: {score}, Grade: {grade}")

# Section 4: Nested conditionals
print("\n--- Section 4: Nested Conditionals ---\n")
is_weekend = True
time = 14  # 24-hour format
if is_weekend:
    if 6 <= time < 12:
        print("Weekend morning")
    elif 12 <= time < 18:
        print("Weekend afternoon")
    else:
        print("Weekend evening")
else:
    print("Regular weekday")

# Section 5: Ternary conditional operator
print("\n--- Section 5: Ternary Operator ---\n")
balance = 1500
status = "Gold" if balance >= 1000 else "Silver"
print(f"Account status: {status}")

# Section 6: Logical operators in conditionals
print("\n--- Section 6: Logical Operators ---\n")
has_ticket = True
has_id = False
age = 17

if has_ticket and (has_id or age >= 18):
    print("Entry allowed")
else:
    print("Entry denied")

# Section 7: Truth Value Testing
print("\n--- Section 7: Truth Value Testing ---\n")
test_values = [0, 1, "", "Hello", None, [], [1,2,3]]

for value in test_values:
    if value:
        print(f"'{value}' is considered True")
    else:
        print(f"'{value}' is considered False")

# Section 8: Match-Case (Python 3.10+)
print("\n--- Section 8: Match-Case (Python 3.10+) ---\n")
http_status = 404

match http_status:
    case 200:
        print("OK")
    case 301 | 302:
        print("Redirect")
    case 400:
        print("Bad Request")
    case 401 | 403:
        print("Authentication Error")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown Status")

# Section 9: Handling Multiple Conditions
print("\n--- Section 9: Multiple Conditions ---\n")
num = 15
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)

# Section 10: Conditional Expressions with Collections
print("\n--- Section 10: Collection Conditionals ---\n")
shopping_cart = ["apples", "milk", "bread"]

if shopping_cart:
    print("Processing your order with:")
    for item in shopping_cart:
        print(f"- {item.capitalize()}")
else:
    print("Your cart is empty!")

# Section 11: Type Checking in Conditionals
print("\n--- Section 11: Type Checking ---\n")
value = 3.1415

if isinstance(value, int):
    print("Integer value")
elif isinstance(value, float):
    print("Floating point value")
elif isinstance(value, str):
    print("String value")
else:
    print("Unknown type")

# Section 12: Short-Circuit Evaluation
print("\n--- Section 12: Short-Circuit Evaluation ---\n")
def check_value():
    print("Function called!")
    return True

print("Case 1:", (False and check_value()))
print("Case 2:", (True or check_value()))

# Section 13: Conditional List Comprehensions
print("\n--- Section 13: Conditional Comprehensions ---\n")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_squares = [x**2 for x in numbers if x % 2 == 0]
print("Even squares:", even_squares)

# Section 14: Error Prevention Patterns
print("\n--- Section 14: Error Prevention ---\n")
user_input = "123a"

# Safe conversion pattern
if user_input.isdigit():
    number = int(user_input)
    print(f"Valid number: {number}")
else:
    print("Invalid number format")

# Section 15: The 'pass' Placeholder
print("\n--- Section 15: 'pass' Statement ---\n")
temp = -5
if temp < 0:
    pass  # TODO: Implement negative handling
else:
    print("Processing positive temperature")

print("\n=== Tutorial Complete ===")