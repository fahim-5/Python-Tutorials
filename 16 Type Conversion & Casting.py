"""
Type Conversion & Casting in Python - Complete Tutorial

This Python file covers all aspects of type conversion and type casting in Python
with practical examples and explanations.
"""

# =============================================
# Section 1: Introduction to Type Conversion
# =============================================
print("\n=== Section 1: Introduction to Type Conversion ===\n")

"""
Type conversion refers to converting one data type to another. In Python, there are two types:
1. Implicit Conversion (automatically done by Python)
2. Explicit Conversion (manually done by the programmer, also called casting)
"""

# =============================================
# Section 2: Implicit Type Conversion
# =============================================
print("\n=== Section 2: Implicit Type Conversion ===\n")

# Example 1: int + float = float
num_int = 10
num_float = 5.5
result = num_int + num_float  # Python automatically converts int to float
print(f"int + float: {num_int} + {num_float} = {result} (type: {type(result)})")

# Example 2: int + bool
# True is treated as 1, False as 0
bool_val = True
result = num_int + bool_val
print(f"int + bool: {num_int} + {bool_val} = {result} (type: {type(result)})")

# Example 3: Limitations - cannot implicitly convert incompatible types
try:
    result = "Hello" + 123  # Will raise TypeError
except TypeError as e:
    print(f"Error: {e} (Cannot implicitly convert string and int)")

# =============================================
# Section 3: Explicit Type Conversion (Casting)
# =============================================
print("\n=== Section 3: Explicit Type Conversion (Casting) ===\n")

"""
Python provides built-in functions for explicit type conversion:
- int(): converts to integer
- float(): converts to float
- str(): converts to string
- bool(): converts to boolean
- list(): converts to list
- tuple(): converts to tuple
- set(): converts to set
- dict(): converts to dictionary
"""

# Example 1: Converting to integer
print("\n--- Converting to Integer (int()) ---")
num_str = "123"
num_float = 12.7
num_bool = True
num_str_float = "456.7"  # Note: This can't be directly converted to int

converted_int = int(num_str)
print(f"string '123' to int: {converted_int} (type: {type(converted_int)})")

converted_int_from_float = int(num_float)  # Truncates decimal part
print(f"float 12.7 to int: {converted_int_from_float} (type: {type(converted_int)})")

converted_int_from_bool = int(num_bool)
print(f"bool True to int: {converted_int_from_bool} (type: {type(converted_int_from_bool)})")

try:
    invalid_conversion = int(num_str_float)  # Will raise ValueError
except ValueError as e:
    print(f"Error converting '456.7' to int: {e}")

# Example 2: Converting to float
print("\n--- Converting to Float (float()) ---")
num_str1 = "123"
num_str2 = "123.45"
num_int = 100
num_bool = False

converted_float1 = float(num_str1)
print(f"string '123' to float: {converted_float1} (type: {type(converted_float1)})")

converted_float2 = float(num_str2)
print(f"string '123.45' to float: {converted_float2} (type: {type(converted_float2)})")

converted_float3 = float(num_int)
print(f"int 100 to float: {converted_float3} (type: {type(converted_float3)})")

converted_float4 = float(num_bool)
print(f"bool False to float: {converted_float4} (type: {type(converted_float4)})")

# Example 3: Converting to string
print("\n--- Converting to String (str()) ---")
num_int = 42
num_float = 3.14
num_bool = True
num_list = [1, 2, 3]

converted_str1 = str(num_int)
print(f"int 42 to string: '{converted_str1}' (type: {type(converted_str1)})")

converted_str2 = str(num_float)
print(f"float 3.14 to string: '{converted_str2}' (type: {type(converted_str2)})")

converted_str3 = str(num_bool)
print(f"bool True to string: '{converted_str3}' (type: {type(converted_str3)})")

converted_str4 = str(num_list)
print(f"list [1, 2, 3] to string: '{converted_str4}' (type: {type(converted_str4)})")

# Example 4: Converting to boolean
print("\n--- Converting to Boolean (bool()) ---")
"""
In Python, the following are considered False:
- None
- False
- Zero of any numeric type: 0, 0.0, 0j
- Empty sequences: '', (), []
- Empty mappings: {}
"""

num_zero = 0
num_non_zero = 10
empty_str = ""
non_empty_str = "Hello"
empty_list = []
non_empty_list = [1, 2, 3]

print(f"int 0 to bool: {bool(num_zero)}")
print(f"int 10 to bool: {bool(num_non_zero)}")
print(f"empty string to bool: {bool(empty_str)}")
print(f"non-empty string to bool: {bool(non_empty_str)}")
print(f"empty list to bool: {bool(empty_list)}")
print(f"non-empty list to bool: {bool(non_empty_list)}")

# =============================================
# Section 4: Advanced Type Conversion Examples
# =============================================
print("\n=== Section 4: Advanced Type Conversion Examples ===\n")

# Example 1: Converting between sequence types
print("\n--- Converting Between Sequence Types ---")
my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
my_set = {7, 8, 9}
my_str = "hello"

# Tuple to list
converted_list = list(my_tuple)
print(f"tuple (1,2,3) to list: {converted_list} (type: {type(converted_list)})")

# List to tuple
converted_tuple = tuple(my_list)
print(f"list [4,5,6] to tuple: {converted_tuple} (type: {type(converted_tuple)})")

# String to list (splits into characters)
converted_str_list = list(my_str)
print(f"string 'hello' to list: {converted_str_list} (type: {type(converted_str_list)})")

# Set to list
converted_set_list = list(my_set)
print(f"set {{7,8,9}} to list: {converted_set_list} (type: {type(converted_set_list)})")

# Example 2: Converting to dictionary
print("\n--- Converting to Dictionary ---")
"""
To convert to dictionary, the original data must be in a format that can be 
interpreted as key-value pairs, like a list of tuples.
"""

list_of_tuples = [('a', 1), ('b', 2), ('c', 3)]
converted_dict = dict(list_of_tuples)
print(f"list of tuples to dict: {converted_dict} (type: {type(converted_dict)})")

# Example 3: Converting numbers between different bases
print("\n--- Converting Numbers Between Bases ---")
binary_str = "1010"
hex_str = "1a"

# Convert binary string to int
binary_to_int = int(binary_str, 2)
print(f"binary '1010' to int: {binary_to_int}")

# Convert hex string to int
hex_to_int = int(hex_str, 16)
print(f"hex '1a' to int: {hex_to_int}")

# Convert int back to binary and hex strings
int_num = 26
int_to_binary = bin(int_num)
int_to_hex = hex(int_num)
print(f"int 26 to binary string: {int_to_binary}")
print(f"int 26 to hex string: {int_to_hex}")

# =============================================
# Section 5: Type Conversion with Collections
# =============================================
print("\n=== Section 5: Type Conversion with Collections ===\n")

# Example 1: Converting between list, set, and tuple
original_list = [1, 2, 2, 3, 4, 4, 5]

# List to set (removes duplicates)
list_to_set = set(original_list)
print(f"list [1,2,2,3,4,4,5] to set: {list_to_set} (type: {type(list_to_set)})")

# Set back to list
set_to_list = list(list_to_set)
print(f"set {{1,2,3,4,5}} back to list: {set_to_list} (type: {type(set_to_list)})")

# List to tuple
list_to_tuple = tuple(original_list)
print(f"original list to tuple: {list_to_tuple} (type: {type(list_to_tuple)})")

# Example 2: Converting dictionary to other types
original_dict = {'a': 1, 'b': 2, 'c': 3}

# Dictionary to list of keys
dict_to_keys_list = list(original_dict)
print(f"dict to list (keys only): {dict_to_keys_list}")

# Dictionary to list of values
dict_to_values_list = list(original_dict.values())
print(f"dict to list of values: {dict_to_values_list}")

# Dictionary to list of tuples (items)
dict_to_items_list = list(original_dict.items())
print(f"dict to list of items (key-value pairs): {dict_to_items_list}")

# =============================================
# Section 6: Special Cases and Caveats
# =============================================
print("\n=== Section 6: Special Cases and Caveats ===\n")

# Example 1: Converting strings with commas to float
num_with_comma = "1,234.56"
try:
    # This will raise a ValueError
    float(num_with_comma)
except ValueError:
    print(f"Can't directly convert '{num_with_comma}' to float due to comma")
    # Solution: Remove commas first
    cleaned_num = num_with_comma.replace(",", "")
    converted_float = float(cleaned_num)
    print(f"After cleaning: {converted_float}")

# Example 2: Converting non-numeric strings
non_numeric_str = "abc123"
try:
    int(non_numeric_str)
except ValueError as e:
    print(f"Error converting '{non_numeric_str}' to int: {e}")

# Example 3: Loss of precision when converting float to int
large_float = 1.9999999999999999
converted_int = int(large_float)
print(f"Converting large float {large_float} to int: {converted_int} (precision lost)")

# Example 4: Boolean conversion of strings
print("\nBoolean conversion of strings:")
print(f"bool('False'): {bool('False')}")  # Any non-empty string is True
print(f"bool(''): {bool('')}")  # Empty string is False

# =============================================
# Section 7: Practical Applications
# =============================================
print("\n=== Section 7: Practical Applications ===\n")

# Example 1: User input processing
print("\n--- Processing User Input ---")
# Simulate user input (in real code, use input())
user_input = "25.5"  # Normally: user_input = input("Enter a number: ")

# Convert to float for calculations
try:
    number = float(user_input)
    print(f"User input '{user_input}' converted to float: {number}")
    print(f"Calculating {number} * 2 = {number * 2}")
except ValueError:
    print("Please enter a valid number!")

# Example 2: Data cleaning in a list
print("\n--- Data Cleaning ---")
mixed_data = ["10", "20.5", "thirty", "40", "50.2", "60"]

clean_numbers = []
for item in mixed_data:
    try:
        # Try to convert to float first (to handle both int and float strings)
        num = float(item)
        clean_numbers.append(num)
    except ValueError:
        print(f"Skipping invalid value: '{item}'")

print(f"Cleaned numbers: {clean_numbers}")

# Example 3: Configuring settings from environment variables
print("\n--- Configuring Settings ---")
import os

# Simulate environment variables
os.environ['MAX_CONNECTIONS'] = "100"
os.environ['DEBUG_MODE'] = "True"
os.environ['TIMEOUT'] = "5.5"

# Convert environment variables to appropriate types
config = {
    'max_connections': int(os.environ.get('MAX_CONNECTIONS', '10')),
    'debug_mode': os.environ.get('DEBUG_MODE', 'False').lower() in ('true', '1', 't'),
    'timeout': float(os.environ.get('TIMEOUT', '1.0'))
}

print("Application configuration:")
for key, value in config.items():
    print(f"{key}: {value} (type: {type(value).__name__})")

# =============================================
# Section 8: Conclusion
# =============================================
print("\n=== Section 8: Conclusion ===\n")

print("""
Key Takeaways:
1. Python performs implicit conversion for compatible types (int to float, etc.)
2. Use explicit conversion (casting) when you need to control the conversion
3. Common conversion functions: int(), float(), str(), bool(), list(), tuple(), set(), dict()
4. Always handle potential ValueError exceptions when converting user input or unreliable data
5. Be aware of precision loss when converting between numeric types
6. Boolean conversion follows specific truthy/falsy rules in Python

Remember: Not all conversions are possible or meaningful. Always consider:
- What happens if the conversion fails?
- Is any data or precision lost in the conversion?
- Does the conversion make logical sense for your use case?
""")

print("End of Type Conversion & Casting Tutorial")