# -----------------------------------------------------
# 📥 1. INPUT / OUTPUT in Python
# -----------------------------------------------------

# ✅ input() always returns string type by default
name = input("Enter your name: ")
print("Hello,", name)

# ✅ Taking multiple inputs
a, b = input("Enter two numbers separated by space: ").split()
print("You entered:", a, "and", b)

# ✅ Converting input to integer
age = int(input("Enter your age: "))
print("You are", age, "years old.")

# ✅ Formatting output using f-string
print(f"{name} is {age} years old.")

# -----------------------------------------------------
# 🔣 2. DATA TYPES & TYPECASTING
# -----------------------------------------------------

# Basic Data Types
x = "Python"       # str
y = 7              # int
z = 3.14           # float
flag = True        # bool

# Check type of variable
print(type(x), type(y), type(z), type(flag))

# ✅ Type Casting
a = str(123)       # Converts to string → '123'
b = int("456")     # Converts to int → 456
c = float("3.5")   # Converts to float → 3.5

# ⚠️ Invalid casting will cause runtime error
# int("abc") ❌ → ValueError

# ✅ Casting during input
num1 = int(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Sum =", num1 + num2)

# -----------------------------------------------------
# ➕ 3. OPERATORS in Python
# -----------------------------------------------------

# ✅ Arithmetic Operators
a = 10
b = 3

print("Addition:", a + b)        # 13
print("Subtraction:", a - b)     # 7
print("Multiplication:", a * b)  # 30
print("Division:", a / b)        # 3.33
print("Floor Division:", a // b) # 3
print("Modulus:", a % b)         # 1
print("Exponent:", a ** b)       # 1000

# ✅ Assignment Operators
x = 5
x += 3   # Same as x = x + 3
x -= 2
x *= 2
x /= 3

# ✅ Comparison Operators (Result is boolean)
print(5 == 5)    # True
print(5 != 2)    # True
print(3 < 10)    # True
print(6 >= 7)    # False

# ✅ Logical Operators
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

# ✅ Identity Operators
a = [1, 2]
b = a
c = [1, 2]

print(a is b)     # True (same object)
print(a is c)     # False (same content but diff object)

# ✅ Membership Operators
print('P' in "Python")    # True
print(5 in [1, 2, 3])     # False

# ✅ Bitwise Operators (on integers only)
print(5 & 3)   # 1  (AND)
print(5 | 3)   # 7  (OR)
print(5 ^ 3)   # 6  (XOR)
print(~5)      # -6 (NOT)
print(5 << 1)  # 10 (left shift)
print(5 >> 1)  # 2  (right shift)

# -----------------------------------------------------
# ✅ Summary
# -----------------------------------------------------
# Input → input(), split(), int(), float()
# Output → print(), f-string
# Data Types → str, int, float, bool
# Typecasting → str(), int(), float(), bool()
# Operators → Arithmetic, Assignment, Comparison,
#             Logical, Identity, Membership, Bitwise

