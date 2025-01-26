#Exercise 1: Understanding the Importance of Testing

#Instruction:

#Write a small Python function (e.g., a function to calculate the square of a number)
#  and intentionally introduce a bug (e.g., incorrect calculation logic).


# The buggy function
def calculate_square(number):
    """Calculate the square of a number."""
    # Intentional bug: Incorrect calculation logic
    return number * 3  # This should be number * number
