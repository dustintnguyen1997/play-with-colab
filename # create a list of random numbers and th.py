# create a list of random numbers and then sort them
import random

# create a list of random numbers
numbers = []
for i in range(10):
    numbers.append(random.randint(1, 100))
    
# sort the list
numbers.sort()

# print the list
print(numbers)
