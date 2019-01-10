
# Using the random module and the range method, generate a list of 20 random numbers between 0 and 49.
import random

random_numbers = [random.randint(0, 49) for n in range(20)]
print(random_numbers)

# With the resulting list, use a list comprehension to build a new list that contains each number squared. For example, if the original list is [2, 5], the final list will be [4, 25].

random_squared = [n**2 for n in random_numbers]
print(random_squared)