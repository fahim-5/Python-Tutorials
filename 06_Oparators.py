# python_operators_tutorial.py

# ---------------------------------------
# PYTHON OPERATORS TUTORIAL
# ---------------------------------------

# Operators are used to perform operations on variables and values.

# 1. ARITHMETIC OPERATORS
a = 10
b = 3

print("Addition:", a + b)        # 13
print("Subtraction:", a - b)     # 7
print("Multiplication:", a * b)  # 30
print("Division:", a / b)        # 3.333...
print("Floor Division:", a // b) # 3
print("Modulus:", a % b)         # 1
print("Exponentiation:", a ** b) # 1000

# 2. ASSIGNMENT OPERATORS
x = 5
x += 3   # x = x + 3
print("x after += 3:", x)  # 8

x *= 2   # x = x * 2
print("x after *= 2:", x)  # 16

x -= 4
x /= 2
print("x after -= and /=:", x)  # 6.0

# 3. COMPARISON OPERATORS (Return True/False)
print("Equal:", a == b)       # False
print("Not Equal:", a != b)   # True
print("Greater Than:", a > b) # True
print("Less Than:", a < b)    # False
print("Greater or Equal:", a >= b)
print("Less or Equal:", a <= b)

# 4. LOGICAL OPERATORS (Used in conditions)
is_python_fun = True
is_java_fun = False

print("AND:", is_python_fun and is_java_fun)  # False
print("OR:", is_python_fun or is_java_fun)    # True
print("NOT:", not is_python_fun)              # False

# 5. BITWISE OPERATORS (Operate on bits)
x = 5  # 0101
y = 3  # 0011

print("Bitwise AND:", x & y)   # 0001 -> 1
print("Bitwise OR:", x | y)    # 0111 -> 7
print("Bitwise XOR:", x ^ y)   # 0110 -> 6
print("Bitwise NOT:", ~x)      # -(x+1)
print("Left Shift:", x << 1)   # 1010 -> 10
print("Right Shift:", x >> 1)  # 0010 -> 2

# 6. IDENTITY OPERATORS
a = [1, 2]
b = a
c = [1, 2]

print("a is b:", a is b)       # True (same memory)
print("a is c:", a is c)       # False (same value, different object)
print("a == c:", a == c)       # True (same value)

# 7. MEMBERSHIP OPERATORS
colors = ['red', 'green', 'blue']

print("'red' in colors:", 'red' in colors)
print("'black' not in colors:", 'black' not in colors)

# 8. OPERATOR PRECEDENCE (PEMDAS-like)
result = 3 + 4 * 2 ** 2 - (5 // 2)
print("Operator precedence result:", result)

# END OF TUTORIAL
print("\n--- OPERATORS TUTORIAL COMPLETE ---")