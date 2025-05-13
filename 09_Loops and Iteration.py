"""
Python Loops and Iteration Complete Tutorial

Covers:
- for loops
- while loops
- Loop control (break, continue, pass)
- Nested loops
- Iterating through different data structures
- List comprehensions
- enumerate() and zip()
- Generators
"""

print("\n=== Python Loops and Iteration Tutorial ===\n")

# Section 1: Basic for loop
print("\n--- Section 1: Basic for Loop ---\n")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I love {fruit}!")

# Section 2: range() function
print("\n--- Section 2: range() Function ---\n")
print("Counting 0-4:")
for i in range(5):
    print(i, end=' ')

print("\n\nCounting 5-9:")
for i in range(5, 10):
    print(i, end=' ')

print("\n\nEven numbers 0-10:")
for i in range(0, 11, 2):
    print(i, end=' ')

# Section 3: while loop
print("\n\n--- Section 3: while Loop ---\n")
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# Section 4: Loop control statements
print("\n--- Section 4: Loop Control ---\n")
print("break example:")
for num in range(10):
    if num == 5:
        break
    print(num, end=' ')

print("\n\ncontinue example:")
for num in range(10):
    if num % 2 == 0:
        continue
    print(num, end=' ')

print("\n\npass example:")
for num in range(3):
    pass  # TODO: Implement later

# Section 5: Nested loops
print("\n\n--- Section 5: Nested Loops ---\n")
print("Multiplication table:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}×{j}={i*j}", end='\t')
    print()

# Section 6: Iterating different data structures
print("\n--- Section 6: Iterating Data Structures ---\n")
print("String iteration:")
for char in "Python":
    print(char, end=' ')

print("\n\nDictionary iteration:")
student = {"name": "Alice", "age": 20, "major": "CS"}
for key, value in student.items():
    print(f"{key}: {value}")

print("\nFile iteration:")
with open("sample.txt", "w") as f:
    f.write("First line\nSecond line\nThird line")
with open("sample.txt") as f:
    for line in f:
        print(line.strip())

# Section 7: enumerate()
print("\n--- Section 7: enumerate() ---\n")
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Index {index}: {color}")

# Section 8: zip()
print("\n--- Section 8: zip() ---\n")
names = ["Alice", "Bob", "Charlie"]
ages = [24, 30, 28]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Section 9: List comprehensions
print("\n--- Section 9: List Comprehensions ---\n")
squares = [x**2 for x in range(10)]
print("Squares:", squares)

even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("Even squares:", even_squares)

# Section 10: Generators
print("\n--- Section 10: Generators ---\n")
def countdown(n):
    while n > 0:
        yield n
        n -= 1

print("Countdown:")
for num in countdown(5):
    print(num, end=' ')

# Section 11: else clause in loops
print("\n\n--- Section 11: else Clause ---\n")
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} = {x}×{n//x}")
            break
    else:
        print(f"{n} is prime")

# Section 12: itertools.islice
print("\n--- Section 12: itertools.islice ---\n")
import itertools
print("First 5 even numbers:")
for num in itertools.islice(itertools.count(0, 2), 5):
    print(num, end=' ')

# Section 13: Error prevention
print("\n\n--- Section 13: Error Prevention ---\n")
print("Safe list modification:")
original = [1, 2, 3, 4, 5]
for num in original.copy():
    if num % 2 == 0:
        original.remove(num)
print("Modified list:", original)

print("\nAvoiding infinite loops:")
counter = 0
while True:
    counter += 1
    if counter >= 5:
        break
    print("Controlled loop iteration")

# Section 14: Practical examples
print("\n--- Section 14: Practical Examples ---\n")
print("Palindrome check:")
word = "madam"
is_palindrome = word == word[::-1]
print(f"'{word}' is palindrome:", is_palindrome)

print("\nPrime number check:")
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print("Is 17 prime?", is_prime(17))
print("Is 25 prime?", is_prime(25))

print("\n=== Tutorial Complete ===")