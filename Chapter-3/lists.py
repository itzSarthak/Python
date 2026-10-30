# CHAPTER 3 — PYTHON LISTS
# DSA + FASTAPI REVISION


# Creating Lists
# A list stores multiple items in an ordered, mutable collection.
# Lists can contain duplicates and different data types.

fruits = ["banana", "apple", "guava", "banana"]
mixed = ["Python", 24, True, 10.5]
empty = []

print(fruits)
print(len(fruits))


# Indexing
# Indexing accesses an element using its position.
# Positive indexing starts at 0; negative indexing starts at -1.

numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[2])
print(numbers[-1])
print(numbers[-2])


# Slicing
# Syntax: list[start:stop:step]
# start is included, stop is excluded.
# Leaving start or stop empty uses the default boundary.

print(numbers[0:3])
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[:])
print(numbers[-3:-1])

# Step
# step controls how many positions to skip between elements.
# A negative step traverses the list backwards.

print(numbers[::2])
print(numbers[::-1])


# Length and Membership
# len() returns the number of elements.
# in checks whether an element exists in the list.
# Membership checking takes O(n) time in the worst case.

print(len(numbers))
print(30 in numbers)
print(99 not in numbers)


# Modifying Elements
# Lists are mutable, so elements can be changed after creation.
# Slice assignment can replace multiple elements at once.

numbers[0] = 100
print(numbers)

numbers[1:3] = [200, 300]
print(numbers)


# Adding Elements
# append() adds one item to the end of the list.
# Appending a list adds that entire list as one nested element.

numbers = [10, 20, 30]

numbers.append(40)
print(numbers)

numbers.append([50, 60])
print(numbers)


# extend()
# extend() adds each item from an iterable to the existing list.
# Unlike append(), it does not add the entire list as one item.

numbers = [10, 20, 30]
numbers.extend([40, 50])
print(numbers)


# insert()
# insert(index, value) adds an element at a specified position.
# Elements after that position shift to the right.

numbers.insert(1, 15)
print(numbers)


# Removing Elements
# remove(value) deletes the first matching value.
# It raises ValueError if the value does not exist.

fruits = ["banana", "apple", "banana", "guava"]

fruits.remove("banana")
print(fruits)


# pop()
# pop() removes and returns the last element by default.
# pop(index) removes and returns the element at that index.
# Popping from the end is O(1); popping from the front is O(n).

numbers = [10, 20, 30, 40]

removed = numbers.pop()
print(removed, numbers)

removed = numbers.pop(0)
print(removed, numbers)


# del
# del removes an element or slice using its index.
# Unlike pop(), it does not return the removed element.

numbers = [10, 20, 30, 40]

del numbers[1]
print(numbers)


# clear()
# clear() removes all elements from the existing list.

numbers.clear()
print(numbers)


# Iterating Through Lists
# Direct iteration is preferred when you only need the values.
numbers = [10, 20, 30, 40]
for number in numbers:
    print(number)


# Index-based iteration
# range(len(list)) is useful when you need to access by index.
for i in range(len(numbers)):
    print(i, numbers[i])


# enumerate()
# Provides both the index and value during iteration.
# start=1 changes the starting index if needed.
for i, number in enumerate(numbers):
    print(i, number)

for i, number in enumerate(numbers, start=1):
    print(i, number)


# while loop
# Useful when iteration depends on a condition.
# Update the index to avoid an infinite loop.

i = 0

while i < len(numbers):
    print(numbers[i])
    i += 1


# List Comprehension
# Creates a new list by applying an expression to each item.
# Syntax: [expression for item in iterable]

numbers = [1, 2, 3, 4, 5, 6]

squares = [x * x for x in numbers]
print(squares)


# Filtering
# The if condition includes only matching elements.

evens = [x for x in numbers if x % 2 == 0]
print(evens)


# Filtering and transforming
# The condition filters elements before the expression is applied.

even_squares = [x * x for x in numbers if x % 2 == 0]
print(even_squares)


# Conditional expression
# The if-else expression chooses a value for every element.

fruits = ["banana", "guava", "banana"]

replaced = [
    "orange" if fruit == "banana" else fruit
    for fruit in fruits
]

print(replaced)


# Avoid using comprehensions just for side effects like printing.
# A normal for loop is clearer when you only want to perform an action.


# Sorting
# sort() sorts the original list in place.
# By default, sorting is in ascending order.
# sort() returns None.

numbers = [24, 12, 45, 80, 12]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)


# sorted()
# sorted() returns a new sorted list without changing the original.

numbers = [24, 12, 45, 80]
sorted_numbers = sorted(numbers)

print(numbers)
print(sorted_numbers)


# Custom sorting
# key specifies the value used to determine sorting order.
# str.lower makes string sorting case-insensitive.

words = ["banana", "Apple", "cherry"]
words.sort(key=str.lower)
print(words)


# Reversing
# reverse() reverses the original list in place.
# It does not sort the elements.
numbers = [10, 20, 30, 40]

numbers.reverse()
print(numbers)


# Reversed copy
# Slicing with [::-1] creates a new list in reverse order.

numbers = [10, 20, 30, 40]

reversed_numbers = numbers[::-1]
print(reversed_numbers)
print(numbers)


# Copying and Aliasing

# Assignment creates another reference to the same list.
# Changes through either reference affect the same list.

a = [1, 2, 3]
b = a

b.append(4)

print(a)
print(b)


# copy()
# Creates a shallow copy of the list.
# For a flat list of immutable values, this is usually sufficient.

original = [10, 20, 30]
copied = original.copy()

copied.append(40)

print(original)
print(copied)


# A shallow copy does not recursively copy nested lists.
# Nested mutable objects may still be shared between copies.


# Useful Built-in Functions and Methods
# len() counts elements; sum() adds numeric elements.
# min() and max() return the smallest and largest values.

numbers = [10, 20, 30, 20]

print(len(numbers))
print(sum(numbers))
print(min(numbers))
print(max(numbers))


# count() returns the number of occurrences of a value.
# index() returns the first matching index.
# index() raises ValueError if the value is missing.

print(numbers.count(20))
print(numbers.index(30))


# Unpacking
# Unpacking assigns elements to variables in order.
# The number of variables must match the number of elements here.

coordinates = [10, 20]
x, y = coordinates

print(x, y)


# Nested Lists
# A list can contain other lists.
# This structure is commonly used to represent a matrix.
# Access elements with matrix[row][column].

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])
print(matrix[1][2])


# Iterate through rows and then their elements.

for row in matrix:
    for value in row:
        print(value)


# Row sums
# Each row is itself a list, so sum() can process each row.
row_sums = [sum(row) for row in matrix]
print(row_sums)


# Functions and Type Hints
# Lists can be passed into functions and returned from them.
# list[int] describes a list of integers for type checking
# and framework tooling; Python does not enforce it by itself.

def find_max(numbers: list[int]) -> int:
    return max(numbers)


print(find_max([4, 9, 2, 7]))


# Returning a list
# -> list[int] indicates that the function returns integer values
# inside a list.

def get_even_numbers(numbers: list[int]) -> list[int]:
    return [number for number in numbers if number % 2 == 0]


print(get_even_numbers([1, 2, 3, 4, 5, 6]))


# DSA Example — Linear Search

# Check each element until the target is found.
# Return its index, or -1 if it does not exist.
# Time complexity: O(n); extra space: O(1).

def linear_search(numbers: list[int], target: int) -> int:
    for i, number in enumerate(numbers):
        if number == target:
            return i

    return -1


print(linear_search([5, 8, 2, 9, 7], 9))
print(linear_search([5, 8, 2, 9, 7], 100))


# DSA — List Operation Complexity

# Index access: O(1)
# Append at end: O(1) amortized
# Insert/delete near the front: O(n)
# Membership search: O(n)
# Linear search: O(n)
# Sorting: O(n log n)
