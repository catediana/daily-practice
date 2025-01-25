#creating person class with 2 urguments
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age  # This will call the setter

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative.")
        self._age = age

    @classmethod
    def create_child(cls, name):
        # Create and return a new instance of Person with age set to 0
        return cls(name, 0)

# Example usage
person1 = Person("Cate", 25)  
print(f"Before setting child's age: {person1.name}, Age: {person1.age}")  # Output: Cate, Age: 25

# Creating a child using the factory method
child = Person.create_child("Bob")
print(f"Child created: Name: {child.name}, Age: {child.age}")  # Output: Child created: Name: Bob, Age: 0

# Setting age for person1
person1.age = 30  # Valid update
print(f"Updated person1's age: {person1.name}, Age: {person1.age}")  # Output: Cate, Age: 30

# Trying to set a negative age (this will raise an error)
try:
    person1.age = -5
except ValueError as e:
    print(e)  # Output: Age cannot be negative.
