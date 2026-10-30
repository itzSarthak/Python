
# PYTHON TUPLES - MASTER REVISION NOTES FOR DSA + FASTAPI

# A tuple is an ordered sequence that cannot be structurally
# modified after creation.
#
# Properties:
# 1. Ordered: maintains element order.
# 2. Indexed: supports positive and negative indexing.
# 3. Immutable: cannot replace, add, or remove elements.
# 4. Allows duplicates.
# 5. Can store different data types.
#
# Example:
students = ("Sarthak", "Shubham", "Anurag", True, "A")

print(students)
# Output: ('Sarthak', 'Shubham', 'Anurag', True, 'A')


# 1. CREATING TUPLES
empty_tuple = ()
numbers = (10, 20, 30)
mixed = (1, "Python", True)

# Parentheses are optional when the commas make a tuple.
another_tuple = 10, 20, 30

print(type(empty_tuple))
# Output: <class 'tuple'>

print(type(another_tuple))
# Output: <class 'tuple'>

# A single element requires a trailing comma.
age = (21,)
not_a_tuple = (21)

print(type(age))
# Output: <class 'tuple'>

print(type(not_a_tuple))
# Output: <class 'int'>

# An empty tuple is different from a one-item tuple.
print(len(empty_tuple), len(age))
# Output: 0 1


# 2. ACCESSING ELEMENTS AND SLICING
students = ("Sarthak", "Shubham", "Anurag", "Sakshi")

print(students[0])
# Output: Sarthak

print(students[-1])
# Output: Sakshi

print(students[1:3])
# Output: ('Shubham', 'Anurag')

print(students[:2])
# Output: ('Sarthak', 'Shubham')

print(students[::2])
# Output: ('Sarthak', 'Anurag')

print(students[::-1])
# Output: ('Sakshi', 'Anurag', 'Shubham', 'Sarthak')

# Invalid indexes raise IndexError.
# students[10]  # IndexError: tuple index out of range


# 3. IMMUTABILITY - WHAT CAN AND CANNOT CHANGE?
numbers = (10, 20, 30)

# These operations are NOT allowed:
# numbers[0] = 100      # TypeError
# numbers.append(40)    # AttributeError
# del numbers[0]        # TypeError

# However, the variable can reference a different tuple.
numbers = (100, 20, 30)

print(numbers)
# Output: (100, 20, 30)

# Important: reassignment is allowed; item mutation is not.


# 4. A SUBTLE CASE: MUTABLE OBJECTS INSIDE A TUPLE
data = (1, 2, [3, 4])

# The tuple's third element is a list.
# We cannot replace that list, but we can mutate the list itself.
data[2].append(5)

print(data)
# Output: (1, 2, [3, 4, 5])

# This would fail:
# data[2] = [3, 4, 5]  # TypeError

# Remember:
# Tuple immutability does not make nested mutable objects immutable.


# 5. TUPLE PACKING AND UNPACKING
# Packing: multiple values form a tuple.
user = "Sarthak", 22, "Developer"

print(user)
# Output: ('Sarthak', 22, 'Developer')

# Unpacking: assign tuple elements to separate variables.
name, age, role = user

print(name)
# Output: Sarthak
print(age)
# Output: 22
print(role)
# Output: Developer

# Number of variables must match the number of elements.
# name, age = user  # ValueError: too many values to unpack


# 6. EXTENDED UNPACKING USING *
gender = ("Male", "Female", "Other")

first, *remaining = gender

print(first)
# Output: Male
print(remaining)
# Output: ['Female', 'Other']

*initial, last = gender

print(initial)
# Output: ['Male', 'Female']
print(last)
# Output: Other

first, *middle, last = (10, 20, 30, 40, 50)

print(first, middle, last)
# Output: 10 [20, 30, 40] 50

# The starred variable receives a LIST, not a tuple.


# 7. SWAPPING VARIABLES - COMMON DSA/PYTHON IDIOM
a = 10
b = 20

a, b = b, a
# basically (b,a) is a tuple and we are unpcaking it

print(a, b)
# Output: 20 10

# Python evaluates the right side before assigning the variables.
# This is useful in sorting algorithms and array manipulation.


# 8. LOOPING THROUGH A TUPLE
numbers = (10, 20, 30)

# Usually the simplest and most readable approach.
for number in numbers:
    print(number)

# Output:
# 10
# 20
# 30

# Use enumerate() when both the index and value are needed.
for index, number in enumerate(numbers):
    print(index, number)

# Output:
# 0 10
# 1 20
# 2 30

# Index-based traversal is also possible.
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

# Output:
# 10
# 20
# 30


# 9. TUPLE METHODS AND MEMBERSHIP
numbers = (1, 2, 3, 2, 2, 5)

print(numbers.count(2))
# Output: 3

print(numbers.index(5))
# Output: 5

print(3 in numbers)
# Output: True

print(100 not in numbers)
# Output: True

# Tuples have only two tuple-specific methods:
# count(value) -> number of occurrences
# index(value) -> first matching index
#
# index() raises ValueError if the element is not found.
# numbers.index(100)  # ValueError


# 10. CONCATENATION AND REPETITION
batch1 = ("Ravi", "Sumit")
batch2 = ("Rani", "Neha")

combined = batch1 + batch2
print(combined)
# Output: ('Ravi', 'Sumit', 'Rani', 'Neha')

repeated = (1, 2) * 3
print(repeated)
# Output: (1, 2, 1, 2, 1, 2)

# These operations create new tuples.
# They do not modify the original tuples.


# 11. CONVERTING BETWEEN LISTS AND TUPLES
students = ("Sarthak", "Shubham", "Anurag")

temp = list(students)
temp.remove("Anurag")
temp.append("Sakshi")

students = tuple(temp)

print(students)
# Output: ('Sarthak', 'Shubham', 'Sakshi')

# Use a list directly if frequent modifications are required.
# Conversion is useful when a final immutable sequence is desired.


# 12. TUPLES AS DICTIONARY KEYS AND SET ELEMENTS

# Tuples containing only hashable elements can be dictionary keys.
locations = {
    (19, 72): "Mumbai",
    (28, 77): "Delhi",
}

print(locations[(19, 72)])
# Output: Mumbai

# Useful for grid coordinates in DSA.
visited = set()
visited.add((2, 3))

print((2, 3) in visited)
# Output: True

# But a tuple containing a list is unhashable.
# invalid = {(1, [2, 3])}  # TypeError: unhashable type: 'list'

# A tuple is not automatically hashable just because it is immutable.
# All its elements must be hashable for the tuple to be hashable.


# 13. SORTING TUPLES
scores = (("Aman", 80), ("Riya", 95), ("Dev", 85))

# sorted() returns a LIST, not a tuple.
by_score = sorted(scores, key=lambda item: item[1])

print(by_score)
# Output:
# [('Aman', 80), ('Dev', 85), ('Riya', 95)]

# Descending order:
by_score_desc = sorted(scores, key=lambda item: item[1], reverse=True)

print(by_score_desc)
# Output:
# [('Riya', 95), ('Dev', 85), ('Aman', 80)]

# Convert the result to a tuple if required.
print(tuple(by_score))
# Output:
# (('Aman', 80), ('Dev', 85), ('Riya', 95))


# 14. MULTIPLE RETURN VALUES - PRACTICAL PYTHON
def get_user():
    return "Sarthak", 22

# Multiple returned values are packed into a tuple.
result = get_user()

print(result)
# Output: ('Sarthak', 22)

name, age = get_user()

print(name, age)
# Output: Sarthak 22

# This is useful when a function naturally produces a fixed
# group of results, such as quotient and remainder.


# 15. DSA EXAMPLE: QUOTIENT AND REMAINDER
def divide(a, b):
    return a // b, a % b

quotient, remainder = divide(17, 5)

print(quotient, remainder)
# Output: 3 2

# DSA note:
# Returning a pair is common in algorithms that need two results.


# 16. DSA EXAMPLE: GRID COORDINATES
# Represent a cell as (row, column).
position = (2, 3)

row, col = position

print(row, col)
# Output: 2 3

# Tuples are useful as stable coordinate keys in sets/dictionaries.
visited_cells = {(0, 0), (1, 2), (2, 3)}

print((2, 3) in visited_cells)
# Output: True


# 17. TUPLE COMPARISON
print((1, 2) == (1, 2))
# Output: True

print((1, 2) < (1, 3))
# Output: True

print((1, 9) < (2, 0))
# Output: True

# Comparisons are lexicographical:
# Compare the first unequal pair of elements.
# This behavior can be useful in sorting and priority-based logic.


# 18. TUPLE VS LIST - QUICK REVISION
# List:
mutable_list = [1, 2, 3]
mutable_list[0] = 100

# Tuple:
immutable_tuple = (1, 2, 3)
# immutable_tuple[0] = 100  # TypeError

# Prefer a list for a collection that changes frequently.
# Prefer a tuple for a fixed-size record or immutable sequence.
# Do not choose a tuple solely because it is assumed to be faster.


# 19. FASTAPI: USING TUPLES IN TYPE ANNOTATIONS
# This function can be used in a FastAPI service or any Python code.
# It returns a pair: (user_id, username).

def get_user_summary(user_id: int) -> tuple[int, str]:
    username = "Sarthak"
    return user_id, username

summary = get_user_summary(101)

print(summary)
# Output: (101, 'Sarthak')

# tuple[int, str] means a tuple containing exactly two elements:
# first an int, then a str.
#
# For a variable-length tuple containing integers:
# tuple[int, ...]
#
# For an empty tuple:
# tuple[()]
#
# A tuple return type is a Python typing feature. It does not
# automatically define a FastAPI response schema.


# 21. COMMON PITFALLS
# 1. A comma creates a tuple; parentheses alone do not.
x = (5)
y = (5,)

print(type(x).__name__, type(y).__name__)
# Output: int tuple

# 2. Tuple unpacking requires matching element counts unless * is used.

# 3. index() fails if an item is absent; count() returns zero.

# 4. A tuple containing a list is not necessarily hashable.

# 5. Concatenation and repetition create new tuples.

# 6. Tuples are not automatically the best choice for API response
# models, large mutable collections, or every pair of values.

# 7. Immutable does not mean deeply immutable:
# a nested list or dictionary may still be changed.


# FINAL REVISION
# Remember:
# - Ordered, indexed, immutable sequence.
# - Single-item tuple: (value,)
# - Unpacking: a, b = (10, 20)
# - Extended unpacking: first, *rest = values
# - Swap: a, b = b, a
# - Dictionary/set keys: use hashable tuples.
# - DSA: coordinates, state keys, pairs, algorithm results.
# - FastAPI: useful internally; JSON serializes tuples as arrays.
# - Use lists for changing collections.
# - Use Pydantic models for named API response contracts.
