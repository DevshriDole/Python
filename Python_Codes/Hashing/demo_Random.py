import random


# Generate a random float between 0 and 1
random_float = random.random()
print(f"Random float: {random_float}")

# Generate a random integer between 1 and 10
random_int = random.randint(1, 10)
print(f"Random integer: {random_int}")

# Generate a random even number between 0 and 20
random_even = random.randrange(0, 21, 2)
print(f"Random even number: {random_even}")

# Choose a random element from a list
my_list = ["apple", "banana", "cherry", "date"]
random_item = random.choice(my_list)
print(f"Random item from list: {random_item}")


