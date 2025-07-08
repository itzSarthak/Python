class Book:
    # 👇 Class-level attributes (shared across all instances)
    count = 0
    types = ('HardCover', 'Binding')

    # ✅ Instance Method
    def __init__(self, name, book_type, weight):
        # Instance attributes (unique per object)
        self.name = name
        self.book_type = book_type
        self.weight = weight

    # ✅ Instance Method (because it uses self)
    def __str__(self):
        return f"The Book '{self.name}' is a '{self.book_type}' and weighs {self.weight} grams."

    # ✅ Class Method: Used to create a book with 'HardCover' type
    @classmethod
    def hardcover(cls, book_name, weight):
        # Accessing class attribute `types` using `cls`
        return cls(book_name, cls.types[0], weight + 100)
        # Adds 100g extra weight for hardcover

    # ✅ Static Method: Does not need self or cls
    @staticmethod
    def is_heavy(weight):
        # Utility function — does not depend on any instance or class data
        return weight > 500

# ========================
# ✅ Using the class method to create a hardcover book
book = Book.hardcover("Harry Potter", 235)
print(book)  # Calls __str__

# ✅ Using static method
print("Is the book heavy?", Book.is_heavy(book.weight))  # False (335g)

# ✅ Modifying an instance attribute
book.count = 22   # Adds a new instance variable `count` (does NOT change class-level `count`)
print("Instance-level count:", book.count)

# ✅ Showing class-level attribute remains unchanged
print("Class-level count:", Book.count)
