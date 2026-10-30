# CHAPTER 4 — PYTHON SETS
# DSA + FASTAPI REVISION

"""
Creating Sets

- A set stores unique elements.
- Sets are unordered, unindexed, and mutable.
- Elements must be hashable, such as integers, strings, or tuples.
- Lists and dictionaries cannot be elements of a set.
"""

thisset = {"apple", "banana", "cherry", 2, 5, "X"}

print(thisset)
print(len(thisset))


"""
Duplicate Values

- Sets automatically remove duplicate values.
- Equal values with equal hashes are treated as the same element.
"""

numbers = {1, 2, 2, 3, 3, 3}

print(numbers)


"""
Empty Set

- {} creates an empty dictionary, not a set.
- Use set() to create an empty set.
"""

empty_set = set()
empty_dict = {}

print(type(empty_set))
print(type(empty_dict))


"""
Creating a Set from an Iterable

- set() converts an iterable into a set.
- Duplicate elements are removed.
- The original iterable is not modified.
"""

numbers = [1, 2, 2, 3, 4, 4]

unique_numbers = set(numbers)

print(unique_numbers)


"""
True, False, 1 and 0

- True == 1 and False == 0 in Python.
- Sets treat these equal values as the same element.
"""

values = {True, 1, False, 0}

print(values)
print(len(values))


"""
Adding Elements with add()

- add() inserts one element into a set.
- Adding an existing element does not create a duplicate.
"""

fruits = {"apple", "banana"}

fruits.add("cherry")
fruits.add("apple")

print(fruits)


"""
Adding Multiple Elements with update()

- update() accepts iterables such as lists, tuples, and strings.
- It adds each element individually.
- A string contributes individual characters.
"""

fruits = {"apple", "banana"}

fruits.update(["mango", "orange"])
fruits.update(("grapes", "kiwi"))

print(fruits)

letters = {"a", "b"}
letters.update("cat")

print(letters)


"""
Removing Elements with remove()

- remove(value) removes the specified element.
- It raises KeyError if the element does not exist.
"""

fruits = {"apple", "banana", "cherry"}

fruits.remove("banana")

print(fruits)


"""
Removing Elements with discard()

- discard(value) removes the element if present.
- It does not raise an error if the element is missing.
"""

fruits = {"apple", "banana", "cherry"}

fruits.discard("apple")
fruits.discard("mango")

print(fruits)


"""
Removing Elements with pop()

- pop() removes and returns an arbitrary element.
- Sets have no positional indexing, so pop() accepts no index.
- Do not rely on which element will be removed.
"""

fruits = {"apple", "banana", "cherry"}

removed = fruits.pop()

print(removed)
print(fruits)


"""
Clearing a Set

- clear() removes all elements from the existing set.
"""

fruits = {"apple", "banana", "cherry"}

fruits.clear()

print(fruits)


"""
Membership Checking

- in checks whether an element exists in a set.
- Membership checking takes O(1) average time.
- This is one of the most useful set operations in DSA.
"""

numbers = {10, 20, 30, 40}

print(20 in numbers)
print(99 not in numbers)


"""
Looping Through a Set

- Sets support iteration but not positional indexing.
- Iteration order is not guaranteed.
"""

numbers = {10, 20, 30, 40}

for number in numbers:
    print(number)

# numbers[0]  # Invalid: sets do not support indexing


"""
Union

- Combines elements from multiple sets.
- Duplicate elements appear only once.
- The | operator is shorthand for union().
"""

set1 = {1, 4, 5, 7}
set2 = {4, 7, 11, 12}
set3 = {5, 7, 20}

result = set1.union(set2, set3)
print(result)  # Output: {1, 4, 5, 7, 11, 12, 20}

result = set1 | set2
print(result)  # Output: {1, 4, 5, 7, 11, 12}


"""
Intersection

- Returns elements common to the sets.
- The & operator is shorthand for intersection().
"""

set1 = {1, 4, 5, 7}
set2 = {4, 7, 11, 12}
set3 = {5, 7, 20}

result = set1.intersection(set2)
print(result)  # Output: {4, 7}

result = set1 & set2 & set3
print(result)  # Output: {7}


"""
intersection_update()

- Modifies the original set.
- Keeps only elements that exist in the other set or sets.
- Returns None, so print the set after calling the method.
"""

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}

set1.intersection_update(set2)
print(set1)  # Output: {3, 4}


"""
Difference

- Keeps elements in the first set that are absent from the other.
- The - operator is shorthand for difference().
- A - B is not necessarily equal to B - A.
"""

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}

result = set1.difference(set2)
print(result)  # Output: {1, 2}

result = set1 - set2
print(result)  # Output: {1, 2}

print(set2 - set1)  # Output: {5}


"""
difference_update()

- Removes elements from the original set if they exist
  in the other set or sets.
- Modifies the original set and returns None.
"""

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}

set1.difference_update(set2)
print(set1)  # Output: {1, 2}


"""
Symmetric Difference

- Returns elements belonging to either set, but not both.
- The ^ operator is shorthand for symmetric_difference().
"""

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.symmetric_difference(set2)
print(result)  # Output: {1, 2, 5, 6}

result = set1 ^ set2
print(result)  # Output: {1, 2, 5, 6}
print(len(result))  # Output: 4


"""
symmetric_difference_update()

- Updates the original set with the symmetric difference.
- Modifies the original set and returns None.
"""

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

set1.symmetric_difference_update(set2)
print(set1)  # Output: {1, 2, 5, 6}


"""
Subset and Superset

- A subset contains only elements found in another set.
- A superset contains every element of another set.
- <= checks subset; >= checks superset.
"""

set1 = {1, 2, 3, 4}
set2 = {2, 3}

print(set2.issubset(set1))     # Output: True
print(set1.issuperset(set2))   # Output: True

print(set2 <= set1)            # Output: True
print(set1 >= set2)            # Output: True





"""
Disjoint Sets

- Two sets are disjoint if they have no common elements.
- isdisjoint() returns True when their intersection is empty.
"""

set1 = {1, 2, 3}
set2 = {4, 5, 6}

print(set1.isdisjoint(set2))  # Output: True

set3 = {3, 4, 5}
print(set1.isdisjoint(set3))  # Output: False


"""
Copying and Aliasing

- Assignment creates another reference to the same set.
- Changes through either variable affect that same set.
"""

set1 = {1, 2, 3}
set2 = set1

set2.add(4)

print(set1)  # Output: {1, 2, 3, 4}
print(set2)  # Output: {1, 2, 3, 4}


"""
copy()

- copy() creates a shallow copy of a set.
- Adding or removing elements in the copy does not change
  the original set.
"""

original = {10, 20, 30}
copied = original.copy()

copied.add(40)

print(original)  # Output: {10, 20, 30}
print(copied)    # Output: {10, 20, 30, 40}


"""
Set Comprehension

- Creates a set using an expression and an iterable.
- Syntax: {expression for item in iterable}
- Duplicate results are automatically removed.
"""

numbers = [1, 2, 2, 3, 4, 4, 5]

squares = {number * number for number in numbers}

print(squares)  # Output: {1, 4, 9, 16, 25}


"""
Filtering with Set Comprehension

- The if condition includes only matching elements.
"""

evens = {number for number in numbers if number % 2 == 0}

print(evens)  # Output: {2, 4}


"""
Filtering and Transforming

- Filters the input before calculating each result.
- Duplicate results are automatically removed.
"""

even_squares = {
    number * number
    for number in numbers
    if number % 2 == 0
}

print(even_squares)  # Output: {4, 16}


"""
Sorting a Set

- A set has no guaranteed order.
- sorted() returns a new sorted list, not a set.
"""

numbers = {40, 10, 30, 20}

sorted_numbers = sorted(numbers)

print(sorted_numbers)  # Output: [10, 20, 30, 40]
print(type(sorted_numbers))  # Output: <class 'list'>


"""
Converting Between Lists and Sets

- set(list) removes duplicate elements.
- list(set) converts the set into a list.
- The original order is not guaranteed after conversion.
"""

items = [3, 1, 3, 2, 1]

unique_items = set(items)
items_again = list(unique_items)

print(unique_items)  # Output: {1, 2, 3} (order may vary)
print(items_again)   # Output: [1, 2, 3] (order may vary)


"""
DSA — Remove Duplicates

- Convert a list to a set for a simple uniqueness operation.
- This does not preserve the original list order.
"""

numbers = [1, 2, 2, 3, 1, 4, 3]

unique_numbers = set(numbers)

print(unique_numbers)  # Output: {1, 2, 3, 4} (order may vary)


"""
DSA — Remove Duplicates While Preserving Order

- Use a set to track values already seen.
- Use a list to store unique values in their original order.
- Set membership is O(1) on average.
"""

numbers = [1, 2, 2, 3, 1, 4, 3]

seen = set()
unique_numbers = []

for number in numbers:
    if number not in seen:
        seen.add(number)
        unique_numbers.append(number)

print(unique_numbers)  # Output: [1, 2, 3, 4]


"""
DSA — Detect Duplicates

- A list containing duplicates has fewer unique set elements.
- Compare the lengths to detect whether duplicates exist.
"""

numbers = [1, 2, 3, 2, 4]

has_duplicates = len(numbers) != len(set(numbers))

print(has_duplicates)  # Output: True


"""
DSA — Find Common Elements

- Convert lists to sets when unique common values are needed.
- Intersection returns values found in both collections.
- Duplicate counts and original order are not preserved.
"""

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common = set(list1) & set(list2)

print(common)  # Output: {3, 4} (order may vary)


"""
DSA — Track Previously Seen Values

- Check whether an element is already in the set.
- If it is, a duplicate has been found.
- Otherwise, add it to the set for future checks.
"""

numbers = [4, 7, 2, 7, 9]

seen = set()

for number in numbers:
    if number in seen:
        print("Duplicate found:", number)
        # Output: Duplicate found: 7
        break

    seen.add(number)

"""
DSA — Two Sum Using a Set

- For each number, calculate its complement.
- Check whether that complement has already been seen.
- Add the current number only after checking.
- Average time complexity: O(n).
"""

def has_two_sum(numbers: list[int], target: int) -> bool:
    seen = set()

    for number in numbers:
        complement = target - number

        if complement in seen:
            return True

        seen.add(number)

    return False


print(has_two_sum([2, 7, 11, 15], 9))
print(has_two_sum([1, 2, 3], 10))


"""
Set Operation Complexity

- Add: O(1) average.
- Remove / discard: O(1) average.
- Membership (in): O(1) average.
- Copy: O(n).
- Union of two sets: O(len(A) + len(B)).
- Sorting with sorted(): O(n log n).
- Hash-table operations can take O(n) in the worst case.
"""


"""
FastAPI — Removing Duplicate Tags

- JSON arrays can contain duplicate values.
- A Python set can remove duplicates during processing.
- Return a list because JSON responses use arrays, not sets.
- Sorting gives the response a predictable order.
"""




# Example request body:
# {
#     "tags": ["python", "dsa", "python", "fastapi"]
# }

# Example response:
# ["dsa", "fastapi", "python"]


"""
FastAPI — Checking Uniqueness

- Compare the list length with the set length.
- If the lengths differ, at least one duplicate exists.
- This helper can be used in backend validation logic.
"""

def contains_only_unique_values(values: list[str]) -> bool:
    return len(values) == len(set(values))


print(contains_only_unique_values(["python", "dsa", "fastapi"]))
print(contains_only_unique_values(["python", "dsa", "python"]))
