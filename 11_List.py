"""
Python Lists Complete Tutorial

Covers:
- List creation and basic operations
- List methods
- List comprehensions
- Sorting and copying
- Nested lists
- Common patterns and best practices
"""

print("\n=== Python Lists Tutorial ===\n")

# Section 1: List Creation
print("\n--- Section 1: List Creation ---\n")
# Empty list
empty_list = []
print("Empty list:", empty_list)

# List with elements
fruits = ["apple", "banana", "cherry"]
print("Fruits list:", fruits)

# Using list constructor
numbers = list(range(5))
print("Numbers list:", numbers)

# Mixed data types
mixed = [1, "two", 3.0, [4]]
print("Mixed list:", mixed)

# Section 2: Accessing Elements
print("\n--- Section 2: Accessing Elements ---\n")
print("First fruit:", fruits[0])          # apple
print("Last fruit:", fruits[-1])          # cherry
print("Slice 1-2:", fruits[1:3])          # ['banana', 'cherry']
print("Every second item:", numbers[::2]) # [0, 2, 4]

# Section 3: List Methods
print("\n--- Section 3: List Methods ---\n")

# append()
fruits.append("orange")
print("After append:", fruits)

# insert()
fruits.insert(1, "mango")
print("After insert:", fruits)

# extend()
more_fruits = ["grape", "pineapple"]
fruits.extend(more_fruits)
print("After extend:", fruits)

# remove()
fruits.remove("banana")
print("After remove:", fruits)

# pop()
popped = fruits.pop(2)
print("Popped item:", popped)
print("After pop:", fruits)

# index()
print("Index of cherry:", fruits.index("cherry"))

# count()
fruits.append("apple")
print("Apple count:", fruits.count("apple"))

# reverse()
fruits.reverse()
print("Reversed list:", fruits)

# sort()
numbers = [3, 1, 4, 2]
numbers.sort()
print("Sorted numbers:", numbers)
numbers.sort(reverse=True)
print("Reverse sorted:", numbers)

# copy()
numbers_copy = numbers.copy()
print("Copied list:", numbers_copy)

# clear()
numbers_copy.clear()
print("Cleared list:", numbers_copy)

# Section 4: List Operations
print("\n--- Section 4: List Operations ---\n")

# Concatenation
combined = [1, 2] + [3, 4]
print("Concatenated:", combined)

# Repetition
repeated = [0] * 5
print("Repeated:", repeated)

# Membership
print("Is 'apple' in fruits?", "apple" in fruits)

# Length
print("Length of fruits:", len(fruits))

# Section 5: List Comprehensions
print("\n--- Section 5: List Comprehensions ---\n")

# Basic comprehension
squares = [x**2 for x in range(10)]
print("Squares:", squares)

# Conditional comprehension
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("Even squares:", even_squares)

# Nested comprehension
matrix = [[1, 2], [3, 4]]
flattened = [num for row in matrix for num in row]
print("Flattened matrix:", flattened)

# Section 6: Sorting
print("\n--- Section 6: Sorting ---\n")

# Sorted function
words = ["banana", "apple", "cherry"]
sorted_words = sorted(words)
print("Sorted copy:", sorted_words)
print("Original list:", words)

# Custom sort
words.sort(key=len)
print("Sorted by length:", words)

# Section 7: Copying Lists
print("\n--- Section 7: Copying Lists ---\n")

# Shallow copy
original = [[1, 2], [3, 4]]
shallow_copy = original.copy()
shallow_copy[0][0] = 99
print("Original modified:", original)

# Deep copy
import copy
deep_copy = copy.deepcopy(original)
deep_copy[0][0] = 100
print("Deep copy modified:", deep_copy)
print("Original remains:", original)

# Section 8: Nested Lists
print("\n--- Section 8: Nested Lists ---\n")

# 2D list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(row)

print("Element at [1][2]:", matrix[1][2])

# Transposing matrix
transposed = [[row[i] for row in matrix] for i in range(3)]
print("Transposed matrix:")
for row in transposed:
    print(row)

# Section 9: Practical Examples
print("\n--- Section 9: Practical Examples ---\n")

# Stack (LIFO)
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print("Stack:", stack)
print("Popped:", stack.pop())

# Queue (FIFO) - collections.deque is better for performance
queue = []
queue.append(1)
queue.append(2)
queue.append(3)
print("Queue:", queue)
print("Dequeued:", queue.pop(0))

# Removing duplicates
duplicates = [2, 2, 3, 4, 3, 2]
unique = list(set(duplicates))
print("Unique list:", unique)

# Filtering list
numbers = [10, 25, 30, 45, 50]
filtered = [x for x in numbers if x % 3 == 0]
print("Numbers divisible by 3:", filtered)

# Section 10: Advanced Operations
print("\n--- Section 10: Advanced Operations ---\n")

# Zipping lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 28]
zipped = list(zip(names, ages))
print("Zipped pairs:", zipped)

# Enumerate
print("Enumerated fruits:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Unpacking
a, b, *rest = [1, 2, 3, 4, 5]
print("Unpacked values:", a, b, rest)

# Section 11: Performance Considerations
print("\n--- Section 11: Performance ---\n")

# append vs insert
print("Time complexity:")
print("- append(): O(1)")
print("- insert(0): O(n)")

# List vs generator
sum_of_squares = sum(x**2 for x in range(1000000))
print("Sum of squares (generator):", sum_of_squares)

print("\n=== Tutorial Complete ===")