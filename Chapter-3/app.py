# ------------------------------------
# 📚 Python List - Master Revision Note
# ------------------------------------

# ✅ List can store multiple items of any data type
fruits = ["banana", "apple", "guava", "banana", 24, True, 'A']

# 🔹 Printing entire list
print(fruits)

# 🔹 Length of list
print(len(fruits))

# ------------------------------------
# 📌 Indexing
# ------------------------------------

# 🔹 Access using positive and negative index
print(fruits[1])    # apple
print(fruits[-2])   # True

# 🔹 Access a slice (range of items)
print(fruits[0:2])     # ['banana', 'apple']
print(fruits[-3:-2])   # [24]
print(fruits[2:])      # ['guava', 'banana', 24, True, 'A']

# ------------------------------------
# ✅ Check existence
# ------------------------------------
print("guava" in fruits)   # True

# ------------------------------------
# ✏️ Modify elements
# ------------------------------------

# 🔹 Replace a slice with new items
fruits[1:3] = ["orange", "grapes"]
print(fruits)

# 🔹 Insert item at specific index
fruits.insert(3, "coconut")
print(fruits)

# 🔹 Append item at end
fruits.append("pineapple")
print(fruits)

# 🔹 Extend list with another list
more_fruits = ["kiwi", "papaya"]
fruits.extend(more_fruits)
print(fruits)

# You could also use:
# fruits = fruits + more_fruits
# or loop:
# for f in more_fruits:
#     fruits.append(f)

# ------------------------------------
# ❌ Remove items
# ------------------------------------

# 🔹 Remove first occurrence of "banana"
fruits.remove("banana")
print(fruits)

# 🔹 Remove element by index
fruits.pop(5)    # Removes 6th element
print(fruits)

# 🔹 Remove last element
fruits.pop()
print(fruits)

# 🔹 Delete specific index
del fruits[3]
print(fruits)

# 🔹 Clear entire list
# fruits.clear()
# print(fruits)

# ------------------------------------
# 🔁 Loop through list
# ------------------------------------

# 🔹 Direct element iteration
for fruit in fruits:
    print(fruit)

# 🔹 Index-based iteration
for i in range(len(fruits)):
    print(fruits[i])

# 🔹 While loop iteration
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

# ------------------------------------
# 🔄 List Comprehension
# ------------------------------------

# 🔹 Print using list comprehension
[print(x) for x in fruits]

# 🔹 Filtering items containing 'a'
newlist = ["ajay", "binod", "anurag", "sarthak", "shubham"]
sublist = [n for n in newlist if "a" in n]
print(sublist)

# 🔹 Uppercase those filtered items
uppersublist = [n.upper() for n in newlist if "a" in n]
print(uppersublist)

# 🔹 Replace "banana" with "orange"
fruits = ["banana", "guava", "banana"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

# ------------------------------------
# 🔢 Sorting and Copying
# ------------------------------------

age = [24, 12, 45, 80]

# 🔹 Reverse list
age.reverse()
print(age)

# 🔹 Sort ascending
age.sort()
print(age)

# 🔹 Sort descending
age.sort(reverse=True)
print(age)

# 🔹 Case-insensitive sort (on strings)
# fruits.sort(key=str.lower)

# 🔹 Copy list
num = age.copy()
print(num)
