# ------------------------------------
# 📚 Python Sets - Master Revision Note
# ------------------------------------

# ✅ Sets are:
# - Unordered
# - Unindexed
# - No duplicate items
# - Mutable (can add/remove), but elements themselves must be immutable

thisset = {"apple", "banana", "cherry", 2, 5, 'X'}
print(thisset)
print(len(thisset))   # Length of set

# ❗️Note:
# 0 == False, 1 == True → Sets treat them as same value!

# ------------------------------------
# ➕ Adding Items to a Set
# ------------------------------------

thisset.add("Male")     # Add single item

# Can update with any iterable (tuple, list, string, etc.)
temp = ('Q', 'R')
thisset.update(temp)

# ------------------------------------
# ➖ Removing Items from a Set
# ------------------------------------

# ✅ remove() - throws error if item not present
thisset.remove('X')

# ✅ discard() - does NOT throw error if item not found
thisset.discard(5)

# ✅ pop() - removes random item (since set is unordered)
thisset.pop()

print(len(thisset))

# ------------------------------------
# 🔁 Looping & Membership
# ------------------------------------

for st in thisset:
    print(st)

if 2 in thisset:
    print("2 is present in the set.")

# ------------------------------------
# 🔧 Set Operations (Powerful Stuff!)
# ------------------------------------

set1 = {1, 4, 5, 7}
set2 = {'A', 'B', 'C', 4, 11}
set3 = {"Sarthak", "Aarya", 'C', 4}

# 1️⃣ Union – Combines all elements, removes duplicates
result = set1.union(set2, set3)
print("Union:", result)

# 2️⃣ Intersection – Returns only elements common to all sets
result = set1.intersection(set2, set3)
print("Intersection:", result)

# 🔁 intersection_update() modifies original set:
# set1.intersection_update(set2, set3)

# 3️⃣ Difference – Items present in first set but not in others
result = set1.difference(set2, set3)
print("Difference:", result)

# 🔁 difference_update() modifies original set:
# set1.difference_update(set2)

# 4️⃣ Symmetric Difference – Items that are in either set, but not in both
result = set1.symmetric_difference(set2)
print("Symmetric Difference:", result)
print(f"Length of symmetric diff set is: {len(result)}")

# 🔁 symmetric_difference_update() modifies original set:
# set1.symmetric_difference_update(set2)

# ------------------------------------
# 🧰 Other Useful Set Methods
# ------------------------------------

# ✅ isdisjoint() → True if no common elements
print(set1.isdisjoint(set3))

# ✅ issubset() → True if all elements of set1 in set2
print({1, 4}.issubset(set1))

# ✅ issuperset() → True if set1 contains all elements of set2
print(set1.issuperset({4}))

# ✅ clear() – Empties the set
copy_set = set1.copy()
copy_set.clear()
print("Cleared Set:", copy_set)

# ✅ copy() – Returns shallow copy
new_copy = set1.copy()
print("Copied Set:", new_copy)
