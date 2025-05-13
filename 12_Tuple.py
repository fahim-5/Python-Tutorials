"""
Python Tuples Complete Tutorial

Covers:
- Definition and characteristics
- Tuple creation and basic operations
- Tuple methods
- Packing/unpacking
- Use cases and best practices
"""

print("\n=== Python Tuples Tutorial ===\n")

# Section 1: Definition and Characteristics
print("\n--- Section 1: Definition & Characteristics ---\n")
"""
Definition:
A tuple is an immutable, ordered collection of elements enclosed in parentheses ().

Key Characteristics:
1. Immutable - cannot be modified after creation
2. Ordered - maintains insertion order
3. Allows duplicate values
4. Can contain different data types
5. Faster than lists for fixed data
6. Hashable (if all elements are hashable)
7. Used for data integrity and fixed collections
"""

# Section 2: Tuple Creation
print("\n--- Section 2: Tuple Creation ---\n")
# Empty tuple
empty_tuple = ()
print("Empty tuple:", empty_tuple)

# Single element tuple (requires trailing comma)
single_item = (42,)
print("Single item tuple:", single_item)

# Multiple elements
colors = ("red", "green", "blue")
print("Colors tuple:", colors)

# Without parentheses (tuple packing)
numbers = 1, 2, 3
print("Packed tuple:", numbers)

# Using tuple constructor
mixed = tuple(["apple", 5, True])
print("Mixed tuple:", mixed)

# Section 3: Accessing Elements
print("\n--- Section 3: Accessing Elements ---\n")
print("First color:", colors[0])        # red
print("Last color:", colors[-1])        # blue
print("Slice 1-2:", colors[1:3])        # ('green', 'blue')
print("Reverse:", colors[::-1])         # ('blue', 'green', 'red')

# Section 4: Tuple Methods
print("\n--- Section 4: Tuple Methods ---\n")
# count()
version = (3, 8, 1, 3, 5, 3)
print("Count of 3:", version.count(3))  # 3

# index()
print("Index of 8:", version.index(8))  # 1

# Section 5: Tuple Operations
print("\n--- Section 5: Tuple Operations ---\n")
# Concatenation
combined = (1, 2) + (3, 4)
print("Concatenated:", combined)        # (1, 2, 3, 4)

# Repetition
repeated = ("Hi",) * 3
print("Repeated:", repeated)            # ('Hi', 'Hi', 'Hi')

# Membership
print("Is 'red' present?", 'red' in colors)  # True

# Length
print("Number of colors:", len(colors)) # 3

# Section 6: Tuple Packing/Unpacking
print("\n--- Section 6: Packing & Unpacking ---\n")
# Packing
coordinates = 12.5, 5.6, 9.1
print("Packed coordinates:", coordinates)

# Unpacking
x, y, z = coordinates
print(f"Unpacked: x={x}, y={y}, z={z}")

# Extended unpacking
first, *rest = (1, 2, 3, 4, 5)
print("First:", first, "Rest:", rest)   # First: 1 Rest: [2, 3, 4, 5]

# Section 7: Immutability Demonstration
print("\n--- Section 7: Immutability ---\n")
try:
    colors[0] = "yellow"
except TypeError as e:
    print("Error:", e)  # 'tuple' object does not support item assignment

# Section 8: Nested Tuples
print("\n--- Section 8: Nested Tuples ---\n")
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
print("Matrix element [1][2]:", matrix[1][2])  # 6

# Section 9: Conversion
print("\n--- Section 9: Conversion ---\n")
# Tuple to list
colors_list = list(colors)
print("List from tuple:", colors_list)

# List to tuple
numbers_tuple = tuple([1, 2, 3])
print("Tuple from list:", numbers_tuple)

# Section 10: Use Cases
print("\n--- Section 10: Use Cases ---\n")
# Dictionary keys
locations = {
    (35.6895, 139.6917): "Tokyo",
    (40.7128, -74.0060): "New York"
}
print("Dictionary with tuple keys:", locations)

# Multiple return values
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)/len(numbers)

stats = get_stats((10, 20, 30, 40))
print(f"Min: {stats[0]}, Max: {stats[1]}, Avg: {stats[2]}")

# Section 11: Performance
print("\n--- Section 11: Performance ---\n")
import timeit

list_time = timeit.timeit('x = [1, 2, 3, 4, 5]', number=1000000)
tuple_time = timeit.timeit('x = (1, 2, 3, 4, 5)', number=1000000)
print(f"Creation time: List {list_time:.4f} vs Tuple {tuple_time:.4f}")

# Section 12: Practical Examples
print("\n--- Section 12: Practical Examples ---\n")
# RGB colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# File info (name, size, type)
file_info = ("report.pdf", 2.5, "MB")
print("File:", file_info)

# Coordinates
points = [(0,0), (1,2), (3,4)]
print("Coordinates:", points)

print("\n=== Tutorial Complete ===")