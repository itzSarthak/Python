# 🚀 First-Class Functions:
# In Python, functions are treated like variables.
# - You can pass them as arguments.
# - You can return them from other functions.
# - You can assign them to variables.

# --------------------------
# Example 1
# --------------------------

def divide(dividend, divisor):
    """Divide two numbers, raising ZeroDivisionError if divisor is 0"""
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return dividend / divisor

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def calculate(*values, operator):
    """
    Accepts any number of positional arguments (*values)
    and a named argument 'operator' (which is a function).
    Calls operator with the unpacked *values.
    """
    return operator(*values)

# Using 'calculate' with divide function
result = calculate(10, 2, operator=divide)
print("Divide result:", result)  # 5.0

# Using 'calculate' with multiply function
result = calculate(10, 2, operator=multiply)
print("Multiply result:", result)  # 20

# --------------------------
# Example 2
# --------------------------

# List of dictionaries
friends = [
    {"name": "Bob Smith", "age": 24},
    {"name": "Alex Carey", "age": 32}
]

# Search function that takes:
# - a sequence (list)
# - an expected value to match
# - a finder function that extracts what to compare
def search(sequence, expected, finder):
    for item in sequence:
        # finder(item) extracts the value to compare
        if finder(item) == expected:
            return item
    # If not found, return None (or raise error if you prefer)
    return None

# Finder function to extract 'name' from a dict
def get_name(friend):
    return friend["name"]

# Searching for a friend by name
result = search(friends, "Alex Carey", get_name)
print("Search result:", result)

# Searching for a name that doesn't exist
result = search(friends, "Green Carey", get_name)
print("Search result:", result)
