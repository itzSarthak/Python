
"""
PYTHON DICTIONARIES — MASTER REVISION NOTE

Dictionary = key-value pairs.

- Ordered by insertion order (guaranteed in Python 3.7+).
- Mutable: values can be added, changed, or removed.
- Keys must be unique and hashable.
- Values can be any type: int, str, list, dict, etc.
- Access values using keys, not positional indexes.

DSA connection:
A dictionary is Python's built-in hash map.
"""

# 1. CREATING A DICTIONARY
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"],
    24: "A"
}

print(type(thisdict))
# Output: <class 'dict'>

print(len(thisdict))
# Output: 5

print(thisdict["brand"])
# Output: Ford

print(thisdict["colors"])
# Output: ['red', 'white', 'blue']

# Empty dictionary
empty_dict = {}

print(empty_dict)
# Output: {}

# dict() constructor
person = dict(name="Sam", age=22)

print(person)
# Output: {'name': 'Sam', 'age': 22}


# 2. ACCESSING VALUES
"""
Square brackets:
- dict[key] returns the value.
- Raises KeyError if the key doesn't exist.

get():
- Returns the value if the key exists.
- Returns None by default if the key is missing.
- Can accept a custom default value.
"""

person = {"name": "Sam", "age": 22}

print(person["name"])
# Output: Sam

print(person.get("age"))
# Output: 22

print(person.get("city"))
# Output: None

print(person.get("city", "Unknown"))
# Output: Unknown

# Check whether a key exists
print("name" in person)
# Output: True

print("city" in person)
# Output: False

"""
Important:
- "name" in person checks whether "name" is a KEY.
- It does not check whether "name" appears among values.
"""

person = {"name": "Sam", "city": "Mumbai"}

print("Sam" in person)
# Output: False

print("Sam" in person.values())
# Output: True


# 3. ADDING AND UPDATING ITEMS
"""
- Assigning to a new key adds an item.
- Assigning to an existing key overwrites its value.
- update() adds or overwrites multiple items.
"""

person = {"name": "Sam", "age": 22}

person["city"] = "Mumbai"
print(person)
# Output: {'name': 'Sam', 'age': 22, 'city': 'Mumbai'}

person["age"] = 23

print(person)
# Output: {'name': 'Sam', 'age': 23, 'city': 'Mumbai'}

person.update({"age": 24, "job": "Developer"})

print(person)
# Output: {'name': 'Sam', 'age': 24, 'city': 'Mumbai', 'job': 'Developer'}


# 4. REMOVING ITEMS
"""
pop(key):
- Removes the given key and returns its value.
- Raises KeyError if missing, unless a default is provided.

popitem():
- Removes and returns the last inserted key-value pair.

del:
- Removes a specific key.

clear():
- Removes all items.
"""

person = {"name": "Sam", "age": 22, "city": "Mumbai"}

removed = person.pop("age")

print(removed)
# Output: 22

print(person)
# Output: {'name': 'Sam', 'city': 'Mumbai'}

removed = person.pop("country", "Not found")

print(removed)
# Output: Not found

last_item = person.popitem()

print(last_item)
# Output: ('city', 'Mumbai')

del person["name"]

print(person)
# Output: {}

person = {"a": 1, "b": 2}
person.clear()

print(person)
# Output: {}


# 5. LOOPING THROUGH A DICTIONARY

person = {"name": "Sam", "age": 22, "city": "Mumbai"}

"""
Loop over a dictionary directly:
- Iterates through keys by default.

items():
- Gives each key-value pair as a tuple.
"""

for key in person:
    print(key)
# Output, one line per iteration:
# name
# age
# city

for key, value in person.items():
    print(key, value)
# Output, one line per iteration:
# name  Sam
# age  22
# city Mumbai

for value in person.values():
    print(value)
# Output, one line per iteration:
# Sam
# 22
# Mumbai


# 6. DICTIONARY VIEWS

"""
keys(), values(), and items() return views, not ordinary lists.

Views reflect changes made to the dictionary.
Use list(...) if you need a separate list of the current contents.
"""

person = {"name": "Sam", "age": 22}

keys_view = person.keys()
values_view = person.values()
items_view = person.items()

print(list(keys_view))
# Output: ['name', 'age']

print(list(values_view))
# Output: ['Sam', 22]

print(list(items_view))
# Output: [('name', 'Sam'), ('age', 22)]

person["city"] = "Mumbai"

print(list(keys_view))
# Output: ['name', 'age', 'city']

print(list(items_view))
# Output: [('name', 'Sam'), ('age', 22), ('city', 'Mumbai')]


# 7. COPYING DICTIONARIES

"""
Assignment creates an alias:
Both variables refer to the same dictionary.

copy() creates a shallow copy:
The outer dictionary is new, but nested mutable values
are still shared.
"""

original = {"a": 1, "b": 2}

alias = original
alias["a"] = 100

print(original)
# Output: {'a': 100, 'b': 2}

original = {"a": 1, "b": 2}

copied = original.copy()
copied["a"] = 100

print(original)
# Output: {'a': 1, 'b': 2}

print(copied)
# Output: {'a': 100, 'b': 2}

# Shallow-copy example with a nested list
original = {"scores": [80, 90]}
copied = original.copy()

copied["scores"].append(100)

print(original)
# Output: {'scores': [80, 90, 100]}

"""
If you need a fully independent copy of nested structures,
look into the copy.deepcopy() function from the copy module.
"""


# 8. USEFUL DICTIONARY METHODS

"""
setdefault(key, default):
- If key exists, returns its current value.
- Otherwise inserts key with default and returns default.

fromkeys(keys, value):
- Creates a dictionary with each key assigned the same value.
"""

person = {"name": "Sam"}

result = person.setdefault("age", 22)

print(result)
# Output: 22

print(person)
# Output: {'name': 'Sam', 'age': 22}

defaults = dict.fromkeys(["math", "science", "english"], 0)

print(defaults)
# Output: {'math': 0, 'science': 0, 'english': 0}

"""
Warning:
If the shared default value is mutable, such as a list,
all keys will refer to that same list.
"""

bad_defaults = dict.fromkeys(["A", "B"], [])

bad_defaults["A"].append(1)

print(bad_defaults)
# Output: {'A': [1], 'B': [1]}

"""
For independent mutable values, use a dictionary comprehension
instead of dict.fromkeys(..., []).
"""

good_defaults = {key: [] for key in ["A", "B"]}
good_defaults["A"].append(1)

print(good_defaults)
# Output: {'A': [1], 'B': []}


# 9. NESTED DICTIONARIES

"""
A dictionary can contain another dictionary as a value.
Access nested values one key at a time.
"""

student = {
    "name": "Sam",
    "marks": {
        "math": 90,
        "science": 85
    }
}

print(student["marks"])
# Output: {'math': 90, 'science': 85}

print(student["marks"]["math"])
# Output: 90

student["marks"]["english"] = 88

print(student["marks"]["english"])
# Output: 88

"""
Nested dictionaries are common in API responses when an object
contains another object, such as a user with an address.
"""


# 10. LIST OF DICTIONARIES
"""
A list of dictionaries represents multiple records.
Common API shape:
[
    {"id": 1, "name": "Sam"},
    {"id": 2, "name": "Mia"}
]
"""

users = [
    {"id": 1, "name": "Sam", "age": 22},
    {"id": 2, "name": "Mia", "age": 25},
    {"id": 3, "name": "Raj", "age": 21}
]

print(users[0])
# Output: {'id': 1, 'name': 'Sam', 'age': 22}

print(users[1]["name"])
# Output: Mia

for user in users:
    print(user["name"])
# Output, one line per iteration:
# Sam
# Mia
# Raj

# Find one record by ID
for user in users:
    if user["id"] == 2:
        print(user)
        break
# Output: {'id': 2, 'name': 'Mia', 'age': 25}


# 11. DICTIONARY OF LISTS

"""
A dictionary can group multiple values under each key.

Example:
{
    "python": ["Sam", "Mia"],
    "java": ["Raj"]
}
"""

groups = {
    "python": ["Sam", "Mia"],
    "java": ["Raj"]
}

print(groups["python"])
# Output: ['Sam', 'Mia']

groups["python"].append("Raj")

print(groups["python"])
# Output: ['Sam', 'Mia', 'Raj']

groups["javascript"] = ["Mia"]

print(groups)
# Output: {'python': ['Sam', 'Mia', 'Raj'], 'java': ['Raj'], 'javascript': ['Mia']}


# 12. DICTIONARY COMPREHENSIONS
"""
Syntax:
{key_expression: value_expression for item in iterable}

Can also include a condition:
{key: value for item in iterable if condition}
"""

nums = [1, 2, 3, 4, 5]

squares = {n: n * n for n in nums}

print(squares)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

even_squares = {n: n * n for n in nums if n % 2 == 0}

print(even_squares)
# Output: {2: 4, 4: 16}

names = ["sam", "mia", "raj"]

name_lengths = {name: len(name) for name in names}

print(name_lengths)
# Output: {'sam': 3, 'mia': 3, 'raj': 3}


# ====================================================
# 13. MERGING DICTIONARIES
# ====================================================

"""
update():
- Mutates the dictionary on the left.
- If a key exists in both dictionaries, the right-hand value wins.

The | operator creates a new merged dictionary in Python 3.9+.
"""

a = {"x": 1, "y": 2}
b = {"y": 99, "z": 3}

merged = a | b

print(merged)
# Output: {'x': 1, 'y': 99, 'z': 3}

print(a)
# Output: {'x': 1, 'y': 2}

a.update(b)

print(a)
# Output: {'x': 1, 'y': 99, 'z': 3}


# ====================================================
# 14. SORTING DICTIONARIES
# ====================================================

"""
Dictionaries preserve insertion order, but they aren't
automatically sorted by key or value.

sorted(dict) sorts the keys and returns a list.
"""

scores = {"Mia": 88, "Sam": 95, "Raj": 78}

print(sorted(scores))
# Output: ['Mia', 'Raj', 'Sam']

# Sort entries by key
by_key = dict(sorted(scores.items()))

print(by_key)
# Output: {'Mia': 88, 'Raj': 78, 'Sam': 95}

# Sort entries by value, ascending
by_score = dict(sorted(scores.items(), key=lambda item: item[1]))

print(by_score)
# Output: {'Raj': 78, 'Mia': 88, 'Sam': 95}

# Sort entries by value, descending
by_score_desc = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))

print(by_score_desc)
# Output: {'Sam': 95, 'Mia': 88, 'Raj': 78}


# ====================================================
# 15. DICTIONARY UNPACKING
# ====================================================

"""
**dictionary unpacks key-value pairs into a function call
or a new dictionary.

When merging dictionaries this way, later values override
earlier values for duplicate keys.
"""

defaults = {"theme": "light", "language": "en"}
settings = {"theme": "dark"}

combined = {**defaults, **settings}

print(combined)
# Output: {'theme': 'dark', 'language': 'en'}


# ====================================================
# 16. DSA — FREQUENCY COUNTING
# ====================================================

"""
Pattern:
Count how many times each value occurs.

dict.get(value, 0) gives the current count, or zero
if the value hasn't appeared yet.
"""

nums = [1, 2, 2, 3, 1, 2]

freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1

print(freq)
# Output: {1: 2, 2: 3, 3: 1}

"""
Alternative:
collections.Counter is built for frequency counting.
"""

from collections import Counter

freq = Counter(nums)

print(dict(freq))
# Output: {1: 2, 2: 3, 3: 1}


# ====================================================
# 17. DSA — TWO SUM USING A DICTIONARY
# ====================================================

"""
For each number x:
- The required complement is target - x.
- Check whether that complement has appeared before.
- Store each number with its index.

Average time: O(n)
Extra space: O(n)
"""

def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []

print(two_sum([2, 7, 11, 15], 9))
# Output: [0, 1]

print(two_sum([3, 2, 4], 6))
# Output: [1, 2]

print(two_sum([1, 2, 3], 10))
# Output: []


# ====================================================
# 18. DSA — GROUPING VALUES
# ====================================================

"""
Use a dictionary of lists when several values share one key.

Example: group numbers by whether they are even or odd.
"""

nums = [1, 2, 3, 4, 5, 6]

groups = {}

for num in nums:
    key = "even" if num % 2 == 0 else "odd"
    groups.setdefault(key, []).append(num)

print(groups)
# Output: {'odd': [1, 3, 5], 'even': [2, 4, 6]}


# ====================================================
# 19. DSA — FIRST NON-REPEATING CHARACTER
# ====================================================

"""
Use a frequency dictionary, then scan the string again
to find the first character with frequency 1.
"""

def first_unique_char(text: str) -> str | None:
    freq = {}

    for char in text:
        freq[char] = freq.get(char, 0) + 1

    for char in text:
        if freq[char] == 1:
            return char

    return None

print(first_unique_char("aabbcddee"))
# Output: c

print(first_unique_char("aabb"))
# Output: None


# ====================================================
# 20. DSA — INVERT A DICTIONARY
# ====================================================

"""
Swap keys and values.

This is appropriate when values are unique.
If multiple keys share a value, a simple inversion
will overwrite earlier keys.
"""

original = {"a": 1, "b": 2, "c": 3}

inverted = {value: key for key, value in original.items()}

print(inverted)
# Output: {1: 'a', 2: 'b', 3: 'c'}


# ====================================================
# 21. DSA — COUNT DISTINCT VALUES
# ====================================================

nums = [1, 2, 2, 3, 3, 3]

freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1

print(len(freq))
# Output: 3

print(list(freq.keys()))
# Output: [1, 2, 3]


# ====================================================
# 22. FASTAPI — DICTIONARY AS A JSON RESPONSE
# ====================================================

"""
A Python dictionary returned by a FastAPI endpoint is
serialized into a JSON object.

Example response:
{
    "message": "Hello",
    "count": 3
}

JSON object keys are strings.
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/summary")
def get_summary() -> dict[str, str | int]:
    return {
        "message": "Hello",
        "count": 3
    }

"""
GET /summary response body:
{
    "message": "Hello",
    "count": 3
}
"""


# ====================================================
# 23. FASTAPI — LIST OF DICTIONARIES
# ====================================================

@app.get("/users")
def get_users() -> list[dict[str, str | int]]:
    return [
        {"id": 1, "name": "Sam"},
        {"id": 2, "name": "Mia"}
    ]

"""
GET /users response body:
[
    {"id": 1, "name": "Sam"},
    {"id": 2, "name": "Mia"}
]
"""


# ====================================================
# 24. FASTAPI — REQUEST BODY WITH PYDANTIC
# ====================================================

"""
For structured request bodies, use a Pydantic model rather
than accepting an unvalidated arbitrary dictionary.

FastAPI uses the model for parsing, validation, and API docs.
"""

from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    age: int
    skills: list[str]

@app.post("/users")
def create_user(user: UserCreate) -> dict:
    return {
        "message": "User created",
        "user": user.model_dump()
    }

"""
Example request body:
{
    "name": "Sam",
    "age": 22,
    "skills": ["Python", "FastAPI"]
}

Example response body:
{
    "message": "User created",
    "user": {
        "name": "Sam",
        "age": 22,
        "skills": ["Python", "FastAPI"]
    }
}
"""


# ====================================================
# 25. DICTIONARY COMPLEXITY — DSA QUICK REVISION
# ====================================================

"""
Average-case complexity:

Lookup by key:       O(1)
Insert/update:       O(1)
Delete by key:       O(1)
Loop over entries:   O(n)
Copy dictionary:     O(n)

Worst-case hash-table operations can be O(n).

Use dictionaries when you need:
- Fast lookup by key.
- Frequency counts.
- Mapping values to indexes.
- Grouping items.
- Caching computed results.
"""
