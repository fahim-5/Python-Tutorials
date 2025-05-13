"""
Python Functions and Scope Complete Tutorial

Covers:
- Function definition and calling
- Parameters and arguments
- Return values
- Variable scope (local, global, nonlocal)
- Lambda functions
- Recursion
- Decorators
- *args and **kwargs
- Docstrings and annotations
"""

print("\n=== Python Functions and Scope Tutorial ===\n")

# Section 1: Basic function definition
print("\n--- Section 1: Basic Functions ---\n")
def greet():
    print("Hello, World!")

greet()  # Function call

# Section 2: Parameters and arguments
print("\n--- Section 2: Parameters/Arguments ---\n")
def personal_greet(name):
    print(f"Hello, {name}!")

personal_greet("Alice")  # Positional argument
personal_greet(name="Bob")  # Keyword argument

def power(base, exponent=2):  # Default parameter
    return base ** exponent

print("5 squared:", power(5))
print("2 cubed:", power(2, 3))

# Section 3: Return values
print("\n--- Section 3: Return Values ---\n")
def average(a, b):
    return (a + b) / 2

result = average(10, 20)
print("Average:", result)

def multi_return():
    return 1, "two", [3]

a, b, c = multi_return()
print(f"Returned values: {a}, {b}, {c}")

# Section 4: Variable scope
print("\n--- Section 4: Variable Scope ---\n")
global_var = "I'm global"

def scope_test():
    local_var = "I'm local"
    print(global_var)  # Access global
    print(local_var)

scope_test()
# print(local_var)  # This would cause NameError

# Section 5: global keyword
print("\n--- Section 5: global Keyword ---\n")
counter = 0

def increment():
    global counter
    counter += 1
    print("Counter inside:", counter)

increment()
print("Counter outside:", counter)

# Section 6: nonlocal keyword
print("\n--- Section 6: nonlocal Keyword ---\n")
def outer():
    outer_var = "outer"
    
    def inner():
        nonlocal outer_var
        outer_var = "modified"
        print("Inner:", outer_var)
    
    inner()
    print("Outer:", outer_var)

outer()

# Section 7: Lambda functions
print("\n--- Section 7: Lambda Functions ---\n")
square = lambda x: x ** 2
print("Square of 5:", square(5))

numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x*2, numbers))
print("Doubled numbers:", doubled)

# Section 8: Recursion
print("\n--- Section 8: Recursion ---\n")
def factorial(n):
    return 1 if n <= 1 else n * factorial(n-1)

print("5! =", factorial(5))

# Section 9: *args and **kwargs
print("\n--- Section 9: *args/**kwargs ---\n")
def flexible_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

flexible_function(1, 'a', name="Alice", age=25)

# Section 10: Decorators
print("\n--- Section 10: Decorators ---\n")
def simple_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello!")

say_hello()

# Section 11: Docstrings and annotations
print("\n--- Section 11: Docstrings/Annotations ---\n")
def calculate(a: float, b: float) -> float:
    """Calculate and return the average of two numbers."""
    return (a + b) / 2

print(calculate(10, 20))
print(calculate.__annotations__)
print(calculate.__doc__)

# Section 12: Closure example
print("\n--- Section 12: Closures ---\n")
def multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

double = multiplier(2)
print("Double of 5:", double(5))

# Section 13: Error handling
print("\n--- Section 13: Error Handling ---\n")
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero!"

print("10 / 2 =", safe_divide(10, 2))
print("5 / 0 =", safe_divide(5, 0))

# Section 14: Practical examples
print("\n--- Section 14: Practical Examples ---\n")
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print("Is 'madam' a palindrome?", is_palindrome("madam"))
print("Is 'Python' a palindrome?", is_palindrome("Python"))

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("First 10 Fibonacci numbers:", list(fibonacci(10)))

print("\n=== Tutorial Complete ===")