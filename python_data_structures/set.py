import random

random_numbers = [random.randint(1,10) for _ in range (15)]


print(random_numbers)

unique_numbers = set(random_numbers)

# Display the unique numbers
print("Unique numbers (duplicates removed):", unique_numbers)

