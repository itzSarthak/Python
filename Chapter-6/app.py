# ----------------------------------------
# 📚 Python Dictionaries - Master Revision Note
# ----------------------------------------

# ✅ Dictionary = { key: value } pair
# - Ordered (Python 3.7+)
# - Mutable (changeable)
# - Keys must be unique & immutable

thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"],
    24: 'A'
}

print(type(thisdict))     # <class 'dict'>
print(len(thisdict))      # Total key-value pairs
print(thisdict)

# ----------------------------------------
# ➕ Adding & Updating Items
# ----------------------------------------

# ✅ Add new key-value
thisdict["Price"] = 123.22

# ✅ Update existing key or add new ones (if not present)
thisdict.update({"model": "Mustang"})

# ⚠️ update() can add multiple items at once
thisdict.update({"brand": "Tata", "year": 2020})  # Overwrites 'brand' & 'year'

# ----------------------------------------
# ➖ Removing Items
# ----------------------------------------

thisdict.pop(24)          # Removes key 24
thisdict.popitem()        # Removes last inserted pair (like stack)
# del thisdict["year"]    # Removes specific key
# thisdict.clear()        # Clears all items

# ----------------------------------------
# 🔁 Looping through Dictionary
# ----------------------------------------

# ✅ Loop through keys and values
for k, v in thisdict.items():
    print(k, ":", v)

# ✅ Loop through keys only
for k in thisdict:
    print("Key:", k, "→", thisdict[k])

# ✅ Loop through values
for val in thisdict.values():
    print("Value:", val)

# ----------------------------------------
# 🧾 Dictionary Views
# ----------------------------------------

# Get keys
keylist = thisdict.keys()
print("Keys:", keylist)

# Get values
valuelist = thisdict.values()
print("Values:", valuelist)

# Get all items as (key, value) tuple
itemlist = thisdict.items()
print("Items:", itemlist)

# ➕ New key affects views
thisdict[22] = "Sarthak"
print("Updated Items:", itemlist)  # Updates automatically because it's a view

# ----------------------------------------
# 📋 Copying Dictionaries
# ----------------------------------------

copy_dict = thisdict.copy()
print("Copied Dictionary:", copy_dict)

# or use dict constructor
copy2 = dict(thisdict)
print("Another Copy:", copy2)

# ----------------------------------------
# 🧠 Extra Useful Dictionary Methods
# ----------------------------------------

# ✅ fromkeys() → create new dict with default value
defaults = dict.fromkeys(["math", "science", "english"], 0)
print("Subject Scores:", defaults)

# ✅ get() → safe way to access key (returns None if not found)
print(thisdict.get("brand"))      # Output: Tata
print(thisdict.get("unknown"))    # Output: None

# ✅ setdefault() → return value if key exists, else add it
x = thisdict.setdefault("engine", "Diesel")
print(x)
print(thisdict)

# ----------------------------------------
# 🧠 Summary Table
# ----------------------------------------

# | Feature             | Dictionary                   |
# |---------------------|------------------------------|
# | Ordered             | ✅ (since Python 3.7+)        |
# | Mutable             | ✅                            |
# | Duplicates allowed  | ❌ (keys must be unique)      |
# | Indexed by          | Key (not position)           |

