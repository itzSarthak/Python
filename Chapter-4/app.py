# ------------------------------------
# 📚 Python Tuples - Master Revision Note
# ------------------------------------

# ✅ Tuples store multiple items in a **single variable**, just like lists
# ❌ BUT: Tuples are **immutable** (cannot be changed after creation)

students = ("Sarthak", "Shubham", "Anurag", True, 'A')

# 🔹 Tuple with one item needs a comma!
age = (21,)
print(len(age))         # Output: 1

# ⚠️ Not a tuple (just a number)
# age = (21)  --> This is int, not a tuple

# 🔹 Type check
print(type(age))                # <class 'tuple'>
print(type(students[-1]))      # <class 'str'>

# ------------------------------------
# 📌 Accessing Tuple Items
# ------------------------------------

print(students)         # Entire tuple
print(students[0])      # First element
print(students[-2])     # Second last

# 🔹 Slicing (just like lists)
print(students[1:3])    # From index 1 to 2

# ------------------------------------
# ✏️ Modify Tuple (Indirectly)
# ------------------------------------

# ✅ Convert tuple → list → modify → convert back to tuple

temp = list(students)
temp.remove("Anurag")       # Remove item
temp.append("Sakshi")       # Add item

students = tuple(temp)
print(students)

# ------------------------------------
# 📦 Tuple Packing and Unpacking
# ------------------------------------

# ✅ Packing: Assign multiple values to one tuple
gender = ("Male", "Female", "Other")

# ✅ Unpacking: Break tuple into individual variables
(g1, g2, g3) = gender
print(g1)
print(g2)
print(g3)

# 🔹 Using `*` for flexible unpacking
(g1, *g2) = gender
print(g1)     # 'Male'
print(g2)     # ['Female', 'Other']

(*g1, g2) = gender
print(g1)     # ['Male', 'Female']
print(g2)     # 'Other'

# ------------------------------------
# 🔁 Looping Through Tuples
# ------------------------------------

# 🔹 Using for loop
for student in students:
    print(student)

# 🔹 Using while loop
i = 0
while i < len(students):
    print(students[i])
    i += 1

# ------------------------------------
# 🔗 Joining Tuples
# ------------------------------------

batch1 = ("Ravi", "Sumit")
batch2 = ("Rani", "Neha")

combined = batch1 + batch2
print(combined)     # ('Ravi', 'Sumit', 'Rani', 'Neha')

# ------------------------------------
# ♻️ Tuple Methods
# ------------------------------------

# Only 2 main built-in methods:
numbers = (1, 2, 3, 2, 2, 5)

print(numbers.count(2))   # 3 times
print(numbers.index(5))   # Index = 5

# ------------------------------------
# 🧠 Quick Summary:
# ------------------------------------
# ✅ Immutable
# ✅ Faster than lists
# ✅ Use when data shouldn't change
# ✅ Can be used as keys in dictionaries (if items are immutable)

