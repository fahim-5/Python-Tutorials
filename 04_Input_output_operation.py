# python_input_output_tutorial.py

# ---------------------------------------
# PYTHON INPUT & OUTPUT OPERATIONS TUTORIAL
# ---------------------------------------

# 1. PRINTING OUTPUT WITH print()
print("Hello, Python world!")  # Basic output
print("Welcome to the Input/Output tutorial.")

# 2. PRINTING MULTIPLE VALUES
name = "Fahim"
age = 23
print("Name:", name, "Age:", age)  # Comma-separated (adds spaces)

# 3. USING STRING FORMATTING (f-strings)
print(f"My name is {name} and I am {age} years old.")

# Other formatting styles:
print("My name is {} and I am {} years old.".format(name, age))  # format()
print("My name is %s and I am %d years old." % (name, age))      # old-school style

# 4. CUSTOMIZING print()
print("This is line 1.", end=" ")  # end argument controls line ending
print("This is line 2.")
print("Red", "Green", "Blue", sep=" | ")  # sep controls separator between values

# 5. TAKING USER INPUT WITH input()
# input() always returns a string, so type casting is often needed.

# Uncomment below lines to test interactive input

# user_name = input("Enter your name: ")
# print(f"Nice to meet you, {user_name}!")

# user_age = int(input("Enter your age: "))  # Convert string to int
# print(f"You will be {user_age + 1} next year.")

# 6. TYPE CASTING USER INPUT
# Be cautious! Casting invalid input will raise ValueError
# Example:
# num = int(input("Enter a number: "))  # Try entering "abc" to see the error

# 7. READING MULTIPLE INPUTS IN ONE LINE
# Uncomment to try:
# data = input("Enter space-separated numbers: ")
# numbers = list(map(int, data.split()))
# print("You entered:", numbers)

# 8. GETTING BOOLEAN INPUT (Custom logic)
# Uncomment to try:
# answer = input("Do you want to continue? (yes/no): ").lower()
# is_continue = answer == "yes"
# print("Continue status:", is_continue)

# 9. ADVANCED FORMATTING WITH print()
from datetime import datetime

today = datetime.now()
print(f"Today's date is {today:%A, %B %d, %Y}")
print(f"Pi is approximately {3.1415926535:.2f}")  # Rounded to 2 decimal places

# END OF TUTORIAL
print("\n--- INPUT & OUTPUT TUTORIAL COMPLETE ---")