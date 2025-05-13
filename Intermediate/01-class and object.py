"""
Python Classes and Objects Tutorial - Part 1
This tutorial covers:
1. Creating classes and instantiating objects
2. The __init__ method (constructor)
3. Instance attributes vs class attributes
"""

# =============================================
# 1. Creating Classes and Instantiating Objects
# =============================================
print("\n=== 1. Creating Classes and Instantiating Objects ===\n")

# A class is a blueprint for creating objects
# Use the 'class' keyword to define a class
class Book:
    pass  # 'pass' is a placeholder for empty class

# Creating an object (instance of the Book class)
# This is called "instantiation"
book1 = Book()  # book1 is now a Book object
print(type(book1))  # Output: <class '__main__.Book'>

# =============================================
# 2. The __init__ Method (Constructor)
# =============================================
print("\n=== 2. The __init__ Method (Constructor) ===\n")

# The __init__ method is called automatically when creating a new object
# It's used to initialize the object's attributes (called "constructor" in other languages)
class Student:
    def __init__(self, name, grade):
        # 'self' refers to the current object being created
        self.name = name  # Initialize name attribute
        self.grade = grade  # Initialize grade attribute
        print(f"New student created: {name}")

# Creating Student objects
student1 = Student("Alice", "A")  # Output: New student created: Alice
student2 = Student("Bob", "B")   # Output: New student created: Bob

# Accessing attributes
print(student1.name)  # Output: Alice
print(student2.grade) # Output: B

# =============================================
# 3. Instance Attributes vs Class Attributes
# =============================================
print("\n=== 3. Instance Attributes vs Class Attributes ===\n")

class Car:
    # Class attribute - shared by ALL instances
    wheels = 4  # All cars have 4 wheels
    
    def __init__(self, brand, model):
        # Instance attributes - unique to EACH instance
        self.brand = brand
        self.model = model

# Create Car objects
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Accessing instance attributes (unique to each object)
print(car1.brand)  # Output: Toyota
print(car2.model)  # Output: Civic

# Accessing class attribute (same for all objects)
print(car1.wheels)  # Output: 4
print(car2.wheels)  # Output: 4
print(Car.wheels)   # Output: 4 (can access through class)

# Modifying class attribute (affects all instances)
Car.wheels = 6
print(car1.wheels)  # Output: 6
print(car2.wheels)  # Output: 6

# Modifying instance attribute (only affects that instance)
car1.wheels = 8
print(car1.wheels)  # Output: 8 (now specific to car1)
print(car2.wheels)  # Output: 6 (still using class value)
print(Car.wheels)   # Output: 6 (class value unchanged)

# =============================================
# Key Differences Summary
# =============================================
print("\n=== Key Differences Summary ===")
print("""
Instance Attributes:
- Defined inside __init__ method using self.attribute_name
- Unique to each object
- Can have different values for different objects

Class Attributes:
- Defined directly in the class (not inside methods)
- Shared by all objects of the class
- Changing them affects all instances (unless overridden)
""")

# =============================================
# Practical Example
# =============================================
print("\n=== Practical Example ===")

class BankAccount:
    # Class attribute
    interest_rate = 0.05  # 5% interest for all accounts
    
    def __init__(self, account_holder, balance=0):
        # Instance attributes
        self.holder = account_holder
        self.balance = balance
    
    def display(self):
        print(f"Account Holder: {self.holder}")
        print(f"Balance: ${self.balance}")
        print(f"Interest Rate: {self.interest_rate * 100}%")

# Create accounts
account1 = BankAccount("John Doe", 1000)
account2 = BankAccount("Jane Smith")

account1.display()
# Output:
# Account Holder: John Doe
# Balance: $1000
# Interest Rate: 5.0%

account2.display()
# Output:
# Account Holder: Jane Smith
# Balance: $0
# Interest Rate: 5.0%

# Change interest rate for all accounts
BankAccount.interest_rate = 0.06
account1.display()
# Output:
# Account Holder: John Doe
# Balance: $1000
# Interest Rate: 6.0%