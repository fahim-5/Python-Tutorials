# python_input_tutorial.py

# ---------------------------------------
# PYTHON INPUT TUTORIAL: GETTING USER DATA
# ---------------------------------------

# 1. BASIC INPUT
# input() reads a line from user and returns it as a string

name = input("Enter your name: ")
print("Hello,", name)

# 2. NUMERIC INPUT: TYPE CASTING
# By default, input returns string. Use int(), float(), etc. to convert.

age = int(input("Enter your age: "))
print("You will be", age + 1, "next year.")

height = float(input("Enter your height in meters: "))
print("Your height is", height, "meters.")

# 3. BOOLEAN INPUT: CUSTOM LOGIC
answer = input("Do you like Python? (yes/no): ").strip().lower()
likes_python = answer == "yes"
print("Likes Python:", likes_python)

# 4. MULTIPLE INPUT VALUES IN ONE LINE
# Example: Enter 10 20 30

raw_data = input("Enter three numbers separated by space: ")
num1, num2, num3 = map(int, raw_data.split())
print("Sum:", num1 + num2 + num3)

# 5. LIST OF INTEGERS FROM USER INPUT
# Example: Enter 5 space-separated integers

nums = list(map(int, input("Enter space-separated numbers: ").split()))
print("You entered:", nums)
print("Maximum number:", max(nums))

# 6. ADVANCED: SPLIT BY COMMA, SLASH, ETC.
csv_input = input("Enter comma-separated items: ")
items = [item.strip() for item in csv_input.split(",")]
print("Items:", items)

# 7. DEFAULT VALUES USING `or`
# If user enters nothing, assign a default

username = input("Enter username (press enter for 'guest'): ") or "guest"
print("Logged in as:", username)

# 8. SAFE INPUT WITH try-except
# Prevent crashes from bad input

try:
    score = int(input("Enter your score (0–100): "))
    print("Your score is:", score)
except ValueError:
    print("Oops! Please enter a valid number.")

# END OF TUTORIAL
print("\n--- INPUT TUTORIAL COMPLETE ---")