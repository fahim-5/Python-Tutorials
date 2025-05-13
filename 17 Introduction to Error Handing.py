"""
Introduction to Error Handling in Python - Complete Tutorial

This Python file covers all fundamental aspects of error handling in Python
with practical examples and explanations.
"""

# =============================================
# Section 1: Introduction to Errors in Python
# =============================================
print("\n=== Section 1: Introduction to Errors in Python ===\n")

"""
In Python, errors can be broadly classified into two categories:
1. Syntax Errors: Occur when the parser encounters incorrect syntax
2. Exceptions: Occur during execution (even if syntax is correct)

Error handling primarily deals with exceptions - unexpected events that occur
during program execution that disrupt the normal flow.
"""

# Example of a SyntaxError (uncomment to see)
# print("Hello world)

# Example of exceptions
print("\nExamples of common exceptions:")
try:
    # ZeroDivisionError
    result = 10 / 0
except ZeroDivisionError:
    print("1. ZeroDivisionError: division by zero")

try:
    # TypeError
    result = "10" + 5
except TypeError:
    print("2. TypeError: can only concatenate str to str")

try:
    # ValueError
    num = int("abc")
except ValueError:
    print("3. ValueError: invalid literal for int()")

try:
    # IndexError
    my_list = [1, 2, 3]
    item = my_list[5]
except IndexError:
    print("4. IndexError: list index out of range")

try:
    # KeyError
    my_dict = {"name": "Alice"}
    value = my_dict["age"]
except KeyError:
    print("5. KeyError: 'age'")

try:
    # FileNotFoundError
    with open("nonexistent_file.txt") as f:
        content = f.read()
except FileNotFoundError:
    print("6. FileNotFoundError: file does not exist")

# =============================================
# Section 2: Basic Error Handling with try-except
# =============================================
print("\n=== Section 2: Basic Error Handling with try-except ===\n")

"""
The try-except block is the fundamental construct for handling exceptions:
- try: Code that might raise an exception
- except: Code that executes if an exception occurs
"""

# Basic example
print("\n--- Basic try-except example ---")
try:
    num = int(input("Enter a number: "))
    print(f"You entered: {num}")
except ValueError:
    print("That's not a valid number!")

# Handling multiple exception types
print("\n--- Handling multiple exceptions ---")
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    result = numerator / denominator
    print(f"Result: {result}")
except ValueError:
    print("Please enter valid integers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Catching multiple exceptions in one except block
print("\n--- Catching multiple exceptions together ---")
try:
    num = int(input("Enter a number: "))
    reciprocal = 1 / num
    print(f"Reciprocal: {reciprocal}")
except (ValueError, ZeroDivisionError) as e:
    print(f"An error occurred: {e}")

# =============================================
# Section 3: The else and finally Clauses
# =============================================
print("\n=== Section 3: The else and finally Clauses ===\n")

"""
A complete try-except block can include:
- else: Runs if no exceptions occur
- finally: Always runs, regardless of exceptions
"""

# Example with else
print("\n--- Using else clause ---")
try:
    num = float(input("Enter a number: "))
except ValueError:
    print("That's not a valid number!")
else:
    print(f"Square of {num} is {num ** 2}")

# Example with finally
print("\n--- Using finally clause ---")
try:
    file = open("example.txt", "w")
    file.write("Hello, World!")
    # Uncomment to simulate an error
    # raise ValueError("Simulated error")
except IOError as e:
    print(f"File error: {e}")
else:
    print("File written successfully")
finally:
    file.close()
    print("File closed (finally block executed)")

# =============================================
# Section 4: Accessing Exception Information
# =============================================
print("\n=== Section 4: Accessing Exception Information ===\n")

"""
When an exception occurs, you can access:
- The exception object itself (with 'as' keyword)
- The traceback (using traceback module)
"""

# Accessing exception object
print("\n--- Accessing exception object ---")
try:
    num = int("abc")
except ValueError as e:
    print(f"Error message: {e}")
    print(f"Exception type: {type(e).__name__}")

# Using traceback
print("\n--- Using traceback module ---")
import traceback

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Exception occurred:")
    traceback.print_exc()  # Prints full traceback to stderr

# =============================================
# Section 5: Raising Exceptions
# =============================================
print("\n=== Section 5: Raising Exceptions ===\n")

"""
You can raise exceptions manually using the 'raise' keyword.
This is useful for:
- Validating inputs
- Signaling error conditions in your code
- Re-raising caught exceptions
"""

# Basic raise example
print("\n--- Basic raise example ---")
def calculate_age(birth_year):
    if birth_year < 1900 or birth_year > 2023:
        raise ValueError("Invalid birth year")
    return 2023 - birth_year

try:
    age = calculate_age(1850)
except ValueError as e:
    print(f"Error: {e}")

# Re-raising exceptions
print("\n--- Re-raising exceptions ---")
try:
    try:
        num = int("abc")
    except ValueError:
        print("Caught ValueError, re-raising...")
        raise  # Re-raises the current exception
except ValueError:
    print("Caught the re-raised exception")

# Creating custom exceptions
print("\n--- Custom exceptions ---")
class InvalidEmailError(Exception):
    """Raised when an email doesn't contain '@'"""
    pass

def validate_email(email):
    if "@" not in email:
        raise InvalidEmailError(f"Invalid email: {email}")
    return True

try:
    validate_email("user.example.com")
except InvalidEmailError as e:
    print(f"Validation error: {e}")

# =============================================
# Section 6: Common Error Handling Patterns
# =============================================
print("\n=== Section 6: Common Error Handling Patterns ===\n")

# Pattern 1: Input validation loop
print("\n--- Pattern 1: Input validation loop ---")
while True:
    try:
        age = int(input("Please enter your age: "))
        if age <= 0:
            raise ValueError("Age must be positive")
        break
    except ValueError as e:
        print(f"Invalid input: {e}. Please try again.")

print(f"Your age is: {age}")

# Pattern 2: Default value on error
print("\n--- Pattern 2: Default value on error ---")
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return float('inf')  # Infinity
    except TypeError:
        return None

print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
print(f"10 / 'a' = {safe_divide(10, 'a')}")

# Pattern 3: Resource cleanup with context managers
print("\n--- Pattern 3: Using context managers ---")
"""
The 'with' statement (context manager) is often better than try-finally
for resource management as it handles cleanup automatically.
"""

try:
    with open("example.txt", "w") as f:
        f.write("Hello, World!")
        # File automatically closed after block
except IOError as e:
    print(f"File error: {e}")

# =============================================
# Section 7: Advanced Topics
# =============================================
print("\n=== Section 7: Advanced Topics ===\n")

# Exception chaining
print("\n--- Exception chaining ---")
try:
    try:
        num = int("abc")
    except ValueError as e:
        raise RuntimeError("Failed to process input") from e
except RuntimeError as e:
    print(f"Caught exception: {e}")
    print(f"Original cause: {e.__cause__}")

# Suppressing exceptions
print("\n--- Suppressing exceptions ---")
from contextlib import suppress

# Instead of:
# try:
#     os.remove("somefile.txt")
# except FileNotFoundError:
#     pass

with suppress(FileNotFoundError):
    import os
    os.remove("somefile.txt")
    print("This will execute if no error occurs")

print("Continues after suppressed exception")

# Assertions for debugging
print("\n--- Using assertions ---")
def calculate_discount(price, discount):
    assert 0 <= discount <= 1, "Discount must be between 0 and 1"
    return price * (1 - discount)

try:
    print(f"Discount: {calculate_discount(100, 0.2)}")
    print(f"Invalid discount: {calculate_discount(100, 1.2)}")
except AssertionError as e:
    print(f"Assertion failed: {e}")

# =============================================
# Section 8: Best Practices
# =============================================
print("\n=== Section 8: Best Practices ===\n")

print("""
Error Handling Best Practices:
1. Be specific with exception types - don't catch all exceptions blindly
2. Use try-except blocks only for code that might raise exceptions
3. Keep try blocks as small as possible
4. Document exceptions that your functions might raise
5. Clean up resources properly (use context managers when possible)
6. Don't use exceptions for normal control flow
7. Create custom exceptions for your application's error cases
8. Include meaningful error messages
9. Consider logging exceptions for debugging
10. Handle exceptions at the appropriate level of abstraction

Anti-patterns to avoid:
- Bare except clauses (catch all exceptions without specifying type)
- Silent exception handling (empty except blocks)
- Overly broad exception handling
- Using exceptions for normal program flow
""")

# =============================================
# Section 9: Practical Application Example
# =============================================
print("\n=== Section 9: Practical Application Example ===\n")

import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ConfigManager:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = self._load_config()
    
    def _load_config(self):
        """Load configuration from JSON file with error handling"""
        try:
            with open(self.config_file) as f:
                config = json.load(f)
            logger.info("Configuration loaded