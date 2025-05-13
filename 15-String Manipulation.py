"""
Python String Manipulation Complete Tutorial

Covers:
- String creation and basics
- String methods
- Formatting techniques
- String operations
- Advanced manipulation
- Regular expressions
- Practical applications
"""

print("\n=== Python String Manipulation Tutorial ===\n")

# Section 1: String Basics
print("\n--- Section 1: String Basics ---\n")
# Creation
s1 = 'Single quotes'
s2 = "Double quotes"
s3 = '''Multiline
string'''
s4 = r"Raw string\n"
print(s1)
print(s2)
print(s3)
print(s4)

# Accessing characters
text = "Python"
print("First character:", text[0])     # P
print("Last character:", text[-1])     # n

# Slicing
print("Slice 2-4:", text[2:4])        # th
print("Reverse:", text[::-1])         # nohtyP

# Section 2: String Methods
print("\n--- Section 2: String Methods ---\n")
# Case methods
print("UPPER:", text.upper())         # PYTHON
print("lower:", text.lower())         # python

# Stripping whitespace
messy = "   Hello World!   \n"
print(f"Original: '{messy}'")
print(f"Stripped: '{messy.strip()}'")

# Splitting and joining
csv = "apple,banana,cherry"
fruits = csv.split(",")
print("Split:", fruits)               # ['apple', 'banana', 'cherry']
joined = "-".join(fruits)
print("Joined:", joined)              # apple-banana-cherry

# Searching
print("Find 'th':", text.find("th"))  # 2
print("Count 't':", text.count("t"))  # 1

# Validation
print("Is digit?", "123".isdigit())   # True
print("Is alpha?", "abc".isalpha())   # True

# Section 3: String Formatting
print("\n--- Section 3: String Formatting ---\n")
# Old-style (%)
print("Hello %s!" % "World")          # Hello World!

# str.format()
print("{} + {} = {}".format(2, 3, 5)) # 2 + 3 = 5
print("{1} before {0}".format("A", "B")) # B before A

# f-strings (Python 3.6+)
name = "Alice"
age = 30
print(f"{name} is {age} years old")   # Alice is 30 years old

# Format specifications
price = 49.99
print(f"Price: ${price:.2f}")         # Price: $49.99

# Section 4: String Operations
print("\n--- Section 4: String Operations ---\n")
# Concatenation
print("Py" + "thon")                  # Python

# Repetition
print("Ha" * 3)                       # HaHaHa

# Membership
print("'yt' in text:", 'yt' in text)  # True

# Length
print("Length:", len(text))           # 6

# Section 5: Advanced Manipulation
print("\n--- Section 5: Advanced Techniques ---\n")
# Translation table
trans = str.maketrans('aeiou', '12345')
print("Translate:", "apple".translate(trans)) # 1ppl2

# Partitioning
print("Partition:", text.partition("th")) # ('Py', 'th', 'on')

# Zfill
print("Zfill:", "42".zfill(5))        # 00042

# Section 6: Regular Expressions
print("\n--- Section 6: Regular Expressions ---\n")
import re

# Search pattern
pattern = r"\d{3}-\d{3}-\d{4}"
phone = "Phone: 123-456-7890"
match = re.search(pattern, phone)
if match:
    print("Phone found:", match.group())  # 123-456-7890

# Find all
text = "10 apples, 5 bananas, 8 cherries"
numbers = re.findall(r'\d+', text)
print("Numbers:", numbers)            # ['10', '5', '8']

# Replacement
censored = re.sub(r'password=\S+', 'password=*****', 
                 "login: user password=secret")
print("Censored:", censored)

# Section 7: Encoding/Decoding
print("\n--- Section 7: Encoding ---\n")
# Encoding
text = "café"
encoded = text.encode('utf-8')
print("Encoded:", encoded)            # b'caf\xc3\xa9'

# Decoding
decoded = encoded.decode('utf-8')
print("Decoded:", decoded)            # café

# Section 8: Practical Examples
print("\n--- Section 8: Practical Examples ---\n")
# Palindrome check
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print("Is 'madam' palindrome?", is_palindrome("madam"))  # True

# Password validator
def valid_password(pwd):
    return (len(pwd) >= 8 and
            any(c.isupper() for c in pwd) and
            any(c.isdigit() for c in pwd))

print("Is 'Pass123' valid?", valid_password("Pass123"))  # False (length 7)
print("Is 'Password123' valid?", valid_password("Password123"))  # True

# String compression
def compress(text):
    from itertools import groupby
    return "".join(f"{char}{len(list(group))}" 
                  for char, group in groupby(text))

print("Compressed:", compress("aaaabbbccd"))  # a4b3c2d1

# Section 9: Performance Tips
print("\n--- Section 9: Performance Tips ---\n")
# Concatenation with join
parts = ["Python"] * 1000
# Bad: result = ""
# for p in parts: result += p
# Good:
result = "".join(parts)
print("Joined length:", len(result))

# f-strings vs format
import timeit
print("f-string:", timeit.timeit('f"Value: {42}"', number=100000))
print(".format:", timeit.timeit('"Value: {}".format(42)', number=100000))

# Section 10: Common Pitfalls
print("\n--- Section 10: Common Pitfalls ---\n")
# Immutability
try:
    text[0] = "J"
except TypeError as e:
    print("Error:", e)

# Encoding issues
try:
    "café".encode('ascii')
except UnicodeEncodeError as e:
    print("Encoding error:", e)

print("\n=== Tutorial Complete ===")