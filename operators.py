# 🔥 All Python Operators 🔥

# 1️⃣ Arithmetic Operators
# ------------------------
# +   Addition
# -   Subtraction
# *   Multiplication
# /   Division
# //  Floor Division
# %   Modulus
# **  Exponent (Power)
a = 10
b = 3
print(a + b) # 13
print(a - b) # 7
print(a * b) # 30 
print(a / b) # 3.3333333333333335
print(a // b) # 3
print(a % b)  # 1
print(a ** b) # 1000
print(" ")


# 2️⃣ Comparison (Relational) Operators
# -------------------------------------
# ==  Equal to
# !=  Not equal to
# >   Greater than
# <   Less than
# >=  Greater than or equal to
# <=  Less than or equal to
print(a == b)  # False
print(a != b)  # True
print( a > b)  # True
print(a < b)   # False
print(a >= b)  # True
print(a <= b)  # False
print(" ")

# 3️⃣ Logical Operators
# ---------------------
# and   Returns True if both are True
# or    Returns True if at least one is True
# not   Reverses the result
x = True
y = False
print(x and y)  # False
print(x or y)  # False
print(not x)  # True
print(" ")

# 4️⃣ Assignment Operators
# ------------------------
# =   Assign
# +=  Add and assign
# -=  Subtract and assign
# *=  Multiply and assign
# /=  Divide and assign
# %=  Modulus and assign
# //= Floor divide and assign
# **= Exponent and assign
num = 5
num += 3
print(num) # 8
num *= 2
print(num) # 16
print(" ")

# 5️⃣ Bitwise Operators
# ---------------------
# &   AND
# |   OR
# ^   XOR
# ~   NOT
# <<  Left shift
# >>  Right shift
p = 5   # 0101
q = 3   # 0011
print(p & q)  # 1
print(p | q)  # 7
print(p ^ q)  # 6
print(~p)     # -6
print(p << 1) # 10 
print(p >> 1) # 2
print(" ")    

# 6️⃣ Membership Operators
# ------------------------
# in       Returns True if a value is in the sequence
# not in   Returns True if a value is not in the sequence
txt = "python"
print('p' in txt) #True
print('z' not in txt) #True
print(" ")
# 7️⃣ Identity Operators
# ----------------------
# is       True if both variables point to the same object
# is not   True if they don’t
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)       # True
print(a is not c)   # True
