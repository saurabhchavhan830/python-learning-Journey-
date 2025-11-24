# ⚙️ Type Conversion
"""
It means changing one data type into another — like turning a string into an integer or a float into a string.
"""

# 🧩 Types of Conversion
'''
# 1. Implicit Type Conversion (Automatic)

Python does it on its own when safe — no manual effort.

Example:
'''

x = 10       # int
y = 3.5      # float
z = x + y    # int + float → float
print(z)     # Output: 13.5
print(type(z))  # float


# 👉 Python automatically converted x (int) to float. 

"""
# 2. Explicit Type Conversion (Manual)

You do it yourself using built-in functions.

Example:
"""

a = "100"
b = int(a)    # string → int
print(b)      # Output: 100
print(type(b))  # int