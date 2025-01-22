#Exercise 3: Custom Exception

#Instructions:

#Create a custom exception class called ValueTooHighError that inherits from the Exception class.
#Write a program that takes a number as input and raises a ValueTooHighError exception if the number is greater than 100.

# Define the custom exception
class ValueTooHighError(Exception):
    def __init__(self, message="Value is too high!"):
        self.message = message
        super().__init__(self.message)

# Function to check the input value
def check_value(number):
    if number > 100:
        # Raise the custom exception if the number is greater than 100
        raise ValueTooHighError(f"ValueTooHighError: The number {number} is greater than 100.")
    else:
        print(f"The number {number} is within the  range.")

def main():
    try:
        # Prompt user to input a number
        num = int(input("Enter a number: "))
        check_value(num)
    except ValueTooHighError as e:
        # Handle the custom exception
        print(e)
    except ValueError:
        # Handle invalid input (e.g., non-integer values)
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
