# python_variables_and_data_types_tutorial.py

# ---------------------------------------
# PYTHON VARIABLES & DATA TYPES TUTORIAL
# ---------------------------------------

# VARIABLES:
# A variable is a named container for storing data in memory.
# You don't need to declare a data type explicitly.

# 1. VARIABLE ASSIGNMENT
name = "Fahim"
age = 23
height_in_meters = 1.75
is_developer = True

print("Name:", name)
print("Age:", age)
print("Height:", height_in_meters)
print("Is Developer:", is_developer)

# 2. DATA TYPES
# Python has several built-in data types. Let's explore the basics:

# --- String (str)
greeting = "Hello, world"
print("Greeting:", greeting)

# --- Integer (int)
year = 2025
print("Year:", year)

# --- Float (float)
pi = 3.14159
print("Pi:", pi)

# --- Boolean (bool)
is_logged_in = False
print("Logged In:", is_logged_in)

# --- NoneType (None)
value = None
print("Value is:", value)

# --- List (mutable sequence)
colors = ["red", "green", "blue"]
print("Colors:", colors)

# --- Tuple (immutable sequence)
dimensions = (1920, 1080)
print("Dimensions:", dimensions)

# --- Set (unordered unique items)
unique_numbers = {1, 2, 3, 2}
print("Unique Numbers:", unique_numbers)

# --- Dictionary (key-value pairs)
person = {"name": "Fahim", "age": 23}
print("Person Info:", person)

# 3. MULTIPLE VARIABLE ASSIGNMENT
x, y, z = 10, 20.5, "Python"
print("x:", x)
print("y:", y)
print("z:", z)

# 4. TYPE CHECKING
print("Type of x:", type(x))
print("Type of z:", type(z))

# 5. TYPE CASTING (CONVERSION)
a = "123"
b = int(a)  # converting string to integer
print("String to int:", b)

c = 456
d = str(c)  # converting int to string
print("Int to string:", d)

# 6. VARIABLE NAMING RULES
# Valid: my_var, _hidden, user2, first_name
# Invalid: 2user, user-name, class (reserved keyword)

# 7. CONSTANTS (by convention, use ALL CAPS)
PI = 3.1416
MAX_USERS = 100

# 8. CHECKING VARIABLE VALUE TYPES WITH isinstance()
print("Is age an int?", isinstance(age, int))
print("Is greeting a str?", isinstance(greeting, str))

# 9. MEMORY MANAGEMENT NOTE
# Python handles memory allocation and garbage collection automatically

# END OF TUTORIAL
print("\n--- VARIABLES & DATA TYPES TUTORIAL COMPLETE ---")