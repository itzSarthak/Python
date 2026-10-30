# 1. Input / Output & Control Flow in Python

# input() always returns string type by default
name = input("Enter your name: ")
print("Hello,", name)

#   Taking multiple inputs
a, b = input("Enter two numbers separated by space: ").split()
print("You entered:", a, "and", b)

#  Converting input to integer
age = int(input("Enter your age: "))
print("You are", age, "years old.")

#  Formatting output using f-string
print(f"{name} is {age} years old.")

#  Taking multiple INTEGER inputs
# input().split() gives strings
# map(int, ...) converts each string to an integer
a, b = map(int, input("Enter two integers: ").split())
print("Sum =", a + b)

# Example:
# Input:
# 10 20
#
# input()           -> "10 20"
# .split()          -> ["10", "20"]
# map(int, ...)     -> 10, 20
# a, b              -> a = 10, b = 20


# 2. DATA TYPES & TYPECASTING
# Basic Data Types
x = "Python"       # str
y = 7              # int
z = 3.14           # float
flag = True        # bool

# Check type of variable
print(type(x), type(y), type(z), type(flag))

#  Type Casting
a = str(123)       # Converts to string → '123'
b = int("456")     # Converts to int → 456
c = float("3.5")   # Converts to float → 3.5

# ⚠️ Invalid casting will cause runtime error
# int("abc") ❌ → ValueError

#  Casting during input
num1 = int(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Sum =", num1 + num2)


#  3. OPERATORS in Python
#  Arithmetic Operators
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

#  Assignment Operators
x = 5
x += 3
x -= 2
x *= 2
x /= 3

#  Comparison Operators
print(5 == 5)
print(5 != 2)
print(3 < 10)
print(6 >= 7)

#  Logical Operators
print(True and False)
print(True or False)
print(not True)

#  Identity Operators
a = [1, 2]
b = a
c = [1, 2]

print(a is b)
print(a is c)

#  Membership Operators
print('P' in "Python")
print(5 in [1, 2, 3])

#  Bitwise Operators
print(5 & 3)
print(5 | 3)
print(5 ^ 3)
print(~5)
print(5 << 1)
print(5 >> 1)


#  DSA INPUT/OUTPUT PATTERNS
# One integer
n = int(input())

# Multiple integers
a, b, c = map(int, input().split())

# Multiple test cases
t = int(input())

for _ in range(t):
    # solve one test case
    pass


# -----------------------------------------------------
#  Summary
# -----------------------------------------------------
# Input → input(), split(), int(), float(), map()
# Output → print(), f-string
# Data Types → str, int, float, bool
# Typecasting → str(), int(), float(), bool()
# Operators → Arithmetic, Assignment, Comparison,
#             Logical, Identity, Membership, Bitwise
