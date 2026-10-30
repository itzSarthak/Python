# ⚙️ 1. FUNCTIONS in Python
# Basic Function
def greet():
    print("Hello, welcome!")

greet()


# Function with Parameters
def add(a, b):
    return a + b

print("Sum:", add(5, 7))


# Type Hints ⭐ Important for FastAPI
def add_numbers(a: int, b: int) -> int:
    return a + b

print(add_numbers(10, 20))


# Default Parameter
def greet_user(name="Guest"):
    print(f"Hi {name}!")

greet_user()
greet_user("Sarthak")


# Keyword Arguments
def intro(name, age):
    print(f"{name} is {age} years old.")

intro(age=22, name="Sarthak")


# Variable Number of Arguments
# *args → tuple of positional arguments
def show_skills(*skills):
    print("Skills:")

    for skill in skills:
        print(skill)

show_skills("Python", "C++", "Java")


# **kwargs → dictionary of keyword arguments
def show_details(**info):
    for key, value in info.items():
        print(f"{key} → {value}")

show_details(name="Sarthak", age=22, lang="Python")


# Return multiple values
def calc(x, y):
    return x + y, x * y

s, m = calc(3, 4)

print(f"Sum = {s}, Product = {m}")


# None ⭐ Important in development
def find_user():
    return None

result = find_user()

if result is None:
    print("User not found")


# Lambda Function
square = lambda x: x * x

print("Square of 6:", square(6))


# 🔒 2. FUNCTION SCOPE
def demo():
    x = 10
    print(x)

demo()

# x cannot normally be accessed here
# because x is local to demo()


# 🔁 3. CONTROL FLOW
# IF, ELIF, ELSE

age = 18

if age < 13:
    print("Child")
elif age < 18:
    print("Teen")
else:
    print("Adult")


# 🔄 4. FOR LOOP
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


# range(start, stop)
# stop is NOT included

for i in range(1, 4):
    print(i)

# 1
# 2
# 3


# range(start, stop, step)

for i in range(0, 10, 2):
    print(i)

# 0 2 4 6 8


# Reverse loop

for i in range(10, 0, -1):
    print(i)


# 🔢 5. ENUMERATE ⭐
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

# 0 apple
# 1 banana
# 2 cherry


# 🔗 6. ZIP ⭐
names = ["Sarthak", "Rahul", "Aman"]
marks = [90, 80, 70]

for name, mark in zip(names, marks):
    print(name, mark)


# 🔁 7. WHILE LOOP
n = 1

while n <= 3:
    print(n)
    n += 1


# 🛑 8. BREAK
for ch in "Sarthak":

    if ch == "h":
        break

    print(ch)


# ⏭️ 9. CONTINUE

for ch in "Sarthak":

    if ch == "h":
        continue

    print(ch)


# 💤 10. PASS
for ch in "Code":

    if ch == "d":
        pass
    else:
        print(ch)


# 🔁 11. NESTED LOOPS
for i in range(3):

    for j in range(3):

        print(i, j)


# 🔄 12. RECURSION ⭐ DSA
def countdown(n):

    if n == 0:
        return

    print(n)

    countdown(n - 1)

countdown(5)
