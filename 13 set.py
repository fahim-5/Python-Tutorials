"""
Python Sets Complete Tutorial

Covers:
- Definition and characteristics
- Set creation and operations
- Set methods
- Set operations
- Frozen sets
- Use cases
"""

print("\n=== Python Sets Tutorial ===\n")

# Section 1: Definition & Characteristics
print("\n--- Section 1: Definition & Characteristics ---\n")
"""
Definition:
A set is an unordered, mutable collection of unique elements enclosed in curly braces {}.

Key Characteristics:
1. Unordered - no index-based access
2. Mutable - can add/remove elements
3. Contains only unique elements
4. Optimized for membership tests
5. Supports mathematical set operations
6. Elements must be hashable
"""

# Section 2: Set Creation
print("\n--- Section 2: Set Creation ---\n")
empty_set = set()
print("Empty set:", empty_set)

fruits = {"apple", "banana", "cherry"}
print("Fruits set:", fruits)

# From list (removes duplicates)
numbers = set([1, 2, 2, 3, 3, 3])
print("Unique numbers:", numbers)

# Section 3: Basic Operations
print("\n--- Section 3: Basic Operations ---\n")
fruits.add("orange")
print("After add:", fruits)

fruits.remove("banana")
print("After remove:", fruits)

fruits.discard("mango")  # No error if missing
print("After discard:", fruits)

popped = fruits.pop()
print("Popped item:", popped)
print("Remaining:", fruits)

# Section 4: Set Methods
print("\n--- Section 4: Set Methods ---\n")
a = {1, 2, 3}
b = {2, 3, 4}

print("Union:", a.union(b))             # {1,2,3,4}
print("Intersection:", a.intersection(b)) # {2,3}
print("Difference:", a.difference(b))   # {1}
print("Symmetric Difference:", a.symmetric_difference(b)) # {1,4}

print("Is subset?", a.issubset({1,2,3,4}))  # True
print("Is superset?", a.issuperset({1,2}))  # True

# Section 5: Set Operations
print("\n--- Section 5: Set Operations ---\n")
print("| operator:", a | b)  # Union
print("& operator:", a & b)  # Intersection
print("- operator:", a - b)  # Difference
print("^ operator:", a ^ b)  # Symmetric Difference

# Section 6: Frozen Sets
print("\n--- Section 6: Frozen Sets ---\n")
immutable_set = frozenset([1, 2, 3])
print("Frozen set:", immutable_set)
try:
    immutable_set.add(4)
except AttributeError as e:
    print("Error:", e)

# Section 7: Use Cases
print("\n--- Section 7: Use Cases ---\n")
# Remove duplicates
names = ["Alice", "Bob", "Alice", "Charlie"]
unique_names = set(names)
print("Unique names:", unique_names)

# Membership testing
print("Is 'apple' present?", 'apple' in fruits)

# Common elements between lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = set(list1) & set(list2)
print("Common elements:", common)

# Section 8: Practical Examples
print("\n--- Section 8: Practical Examples ---\n")
# Venn diagram operations
math_students = {"Alice", "Bob", "Charlie"}
physics_students = {"Bob", "David", "Eve"}

print("Both subjects:", math_students & physics_students)
print("Either subject:", math_students | physics_students)
print("Only math:", math_students - physics_students)

# Email list cleaning
emails = ["user@example.com", "admin@example.com", "user@example.com"]
clean_emails = set(emails)
print("Clean email list:", clean_emails)

print("\n=== Sets Tutorial Complete ===")