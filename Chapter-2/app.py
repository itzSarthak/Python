# -----------------------------------------------------
# ⚙️ 1. FUNCTIONS in Python
# -----------------------------------------------------

# ✅ Basic Function
def greet():
    print("Hello, welcome!")

greet()

# ✅ Function with Parameters
def add(a, b):
    return a + b

print("Sum:", add(5, 7))

# ✅ Default Parameter
def greet_user(name="Guest"):
    print(f"Hi {name}!")

greet_user()
greet_user("Sarthak")

# ✅ Keyword Arguments
def intro(name, age):
    print(f"{name} is {age} years old.")

intro(age=22, name="NoobCoder")

# ✅ Variable Number of Arguments

# *args → Tuple of positional arguments
def show_skills(*skills):
    print("Skills:")
    for skill in skills:
        print(skill)

show_skills("Python", "C++", "Java")

# **kwargs → Dictionary of keyword arguments
def show_details(**info):
    for key, value in info.items():
        print(f"{key} → {value}")

show_details(name="Sarthak", age=22, lang="Python")

# ✅ Return multiple values
def calc(x, y):
    return x + y, x * y

s, m = calc(3, 4)
print(f"Sum = {s}, Product = {m}")

# ✅ Lambda Function (anonymous, one-line function)
square = lambda x: x * x
print("Square of 6:", square(6))

# -----------------------------------------------------
# 🔁 2. CONTROL FLOW (if, for, while)
# -----------------------------------------------------

# ✅ IF, ELIF, ELSE
age = 18

if age < 13:
    print("Child")
elif age < 18:
    print("Teen")
else:
    print("Adult")

# ✅ FOR LOOP
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# ✅ Loop with Range
for i in range(1, 4):
    print(f"Count: {i}")

# ✅ WHILE LOOP
n = 1
while n <= 3:
    print(f"While Loop: {n}")
    n += 1

# ✅ BREAK statement
for ch in "Sarthak":
    if ch == 'h':
        break
    print(ch)

# ✅ CONTINUE statement
for ch in "Sarthak":
    if ch == 'h':
        continue
    print(ch)

# ✅ PASS statement (does nothing, used to avoid error)
for ch in "Code":
    if ch == 'd':
        pass  # placeholder for future logic
    else:
        print(ch)

# -----------------------------------------------------
# ✅ Summary
# -----------------------------------------------------
# Function Types: basic, with args, default args, *args, **kwargs, lambda
# Return types: single & multiple values
# Control Flow: if, elif, else, for, while, break, continue, pass
