class Person:
    def __init__(self, name, age):
        """Initialize the Person instance with name and age."""
        self.name = name
        self.age = age
        print(f"Creating Person: {self.name}, Age: {self.age}")

    def __del__(self):
        """Destructor that prints a farewell message when the object is deleted."""
        print(f"Farewell, {self.name}! You were {self.age} years old.")

# Example usage
if __name__ == "__main__":
    person1 = Person("Alice", 30)  # Creating an instance of Person
    person2 = Person("Bob", 25)     # Creating another instance of Person

    # Deleting the instances to trigger the destructor
    del person1
    del person2



