"""
Python Dictionaries Complete Tutorial

Covers:
- Dictionary definition and characteristics
- CRUD operations
- Dictionary methods
- Dictionary comprehensions
- Nested dictionaries
- Use cases
"""

print("\n=== Python Dictionaries Tutorial ===\n")

# Section 1: Definition & Characteristics
print("\n--- Section 1: Definition & Characteristics ---\n")
"""
Definition:
A dictionary is an ordered, mutable collection of key-value pairs enclosed in curly braces {}.

Key Characteristics:
1. Key-value pairs (key: value)
2. Keys must be unique and hashable
3. Values can be any data type
4. Ordered (insertion order preserved)
5. Mutable - can modify values
6. Fast lookups using keys
"""

# Section 2: Dictionary Creation
print("\n--- Section 2: Dictionary Creation ---\n")
empty_dict = {}
print("Empty dict:", empty_dict)

student = {
    "name": "Alice",
    "age": 20,
    "courses": ["Math", "Physics"]
}
print("Student dict:", student)

# Using dict constructor
grades = dict([("Math", 90), ("Physics", 85)])
print("Grades dict:", grades)

# Section 3: CRUD Operations
print("\n--- Section 3: CRUD Operations ---\n")
# Create/Update
student["email"] = "alice@example.com"
print("After adding email:", student)

# Read
print("Name:", student["name"])
print("Get age:", student.get("age"))
print("Safe get:", student.get("phone", "Not available"))

# Delete
del student["age"]
print("After deleting age:", student)

# Section 4: Dictionary Methods
print("\n--- Section 4: Dictionary Methods ---\n")
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Update
student.update({"name": "Alice Smith", "phone": "123-4567"})
print("After update:", student)

# Pop
phone = student.pop("phone")
print("Popped phone:", phone)
print("After pop:", student)

# Section 5: Dictionary Comprehensions
print("\n--- Section 5: Dictionary Comprehensions ---\n")
squares = {x: x**2 for x in range(6)}
print("Squares dict:", squares)

# Conditional comprehension
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print("Even squares:", even_squares)

# Section 6: Nested Dictionaries
print("\n--- Section 6: Nested Dictionaries ---\n")
employees = {
    1: {"name": "John", "position": "Manager"},
    2: {"name": "Sarah", "position": "Developer"}
}
print("Employee 1:", employees[1])
print("Sarah's position:", employees[2]["position"])

# Section 7: Specialized Dictionaries
print("\n--- Section 7: Specialized Dictionaries ---\n")
from collections import defaultdict, OrderedDict

# Defaultdict
word_counts = defaultdict(int)
for word in ["apple", "banana", "apple"]:
    word_counts[word] += 1
print("Word counts:", word_counts)

# OrderedDict
ordered = OrderedDict()
ordered["a"] = 1
ordered["b"] = 2
print("OrderedDict:", ordered)

# Section 8: Use Cases
print("\n--- Section 8: Use Cases ---\n")
# Configuration settings
config = {
    "host": "localhost",
    "port": 8080,
    "debug": True
}

# JSON-like data
book = {
    "title": "Python Essentials",
    "authors": ["John Doe", "Jane Smith"],
    "price": 49.99,
    "stock": True
}

# Section 9: Practical Examples
print("\n--- Section 9: Practical Examples ---\n")
# Word frequency counter
text = "apple banana apple cherry banana apple"
frequency = {}
for word in text.split():
    frequency[word] = frequency.get(word, 0) + 1
print("Word frequency:", frequency)

# Inventory system
inventory = {
    "apple": {"price": 0.5, "quantity": 100},
    "banana": {"price": 0.3, "quantity": 150}
}

# Update inventory
def sell_item(item, quantity):
    if inventory[item]["quantity"] >= quantity:
        inventory[item]["quantity"] -= quantity
        return True
    return False

print("Sell 20 apples:", sell_item("apple", 20))
print("Updated inventory:", inventory["apple"])

# Section 10: Performance
print("\n--- Section 10: Performance ---\n")
import timeit

dict_time = timeit.timeit('d["key"]', 
    setup='d = {"key": 1}', number=1000000)
list_time = timeit.timeit('l[0]', 
    setup='l = [1]', number=1000000)
print(f"Lookup time: Dict {dict_time:.5f} vs List {list_time:.5f}")

print("\n=== Dictionaries Tutorial Complete ===")