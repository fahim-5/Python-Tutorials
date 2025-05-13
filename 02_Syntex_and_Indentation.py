# python_syntax_and_indentation_tutorial.py

# -------------------------------
# PYTHON SYNTAX & INDENTATION 101
# -------------------------------

# Python uses indentation to define code blocks.
# Unlike other languages, indentation is NOT optional.

# 1. PRINTING OUTPUT
print("Hello, Python world!")  # This is a single-line comment

# 2. VARIABLES AND DATA TYPES
name = "Fahim"
age = 23
is_student = True

print("Name:", name)
print("Age:", age)
print("Student Status:", is_student)

# 3. CONDITIONAL STATEMENTS (Indentation is required!)
if is_student:
    print("You are a student.")
else:
    print("You are not a student.")

# 4. LOOPS (Indented code runs inside the loop)
for i in range(3):
    print("Loop iteration:", i)
    print("Still inside loop")
print("Now outside the loop")

# 5. FUNCTIONS (Indented blocks are essential)
def greet(person):
    print("Hello,", person)
    print("Welcome to the Python world!")

greet("Fahim")

# 6. ERROR DUE TO WRONG INDENTATION
# Uncomment the below lines to see what happens

# def broken_function():
# print("This will cause an IndentationError")  # Missing indentation!

# 7. MULTI-LINE STATEMENTS
total = (1 + 2 +
         3 + 4)
print("Total:", total)

# 8. WHITESPACE BEST PRACTICES
# Always use 4 spaces (not tabs!) for indentation
# Use an editor like VS Code or PyCharm to format automatically

# END OF TUTORIAL
print("Syntax & Indentation tutorial complete!")