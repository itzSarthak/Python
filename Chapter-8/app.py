# Example function to divide two numbers
def divide(dividend, divisor):
    # Raise a built-in error if divisor is 0
    if divisor == 0:
        raise ZeroDivisionError("Divisor can't be zero!")

    # Raise a built-in error if dividend is not a number
    if not isinstance(dividend, (int, float)):
        raise TypeError("Dividend must be a number!")

    return dividend / divisor


# Custom Error Class (inherits from Exception)
class GradeCalculationError(Exception):
    """Raised when grades list is empty or invalid"""
    pass


grades = []

try:
    # Check if grades list is empty
    if len(grades) == 0:
        raise GradeCalculationError("No grades to calculate average!")

    # Try dividing
    average = divide(sum(grades), len(grades))
    print(f"Average Grade: {average}")

# Catch ZeroDivisionError specifically
except ZeroDivisionError as ex:
    print(f"ZeroDivisionError occurred: {ex}")

# Catch TypeError specifically
except TypeError as ex:
    print(f"TypeError occurred: {ex}")

# Catch custom GradeCalculationError
except GradeCalculationError as ex:
    print(f"Custom Error: {ex}")

# Catch ANY other Exception (must be last)
except Exception as ex:
    print(f"Other Exception occurred: {ex}")

# Else block runs if no exception occurs
else:
    print("Calculation completed successfully!")

# Finally block always runs
finally:
    print("Finished calculating grades.\n")
