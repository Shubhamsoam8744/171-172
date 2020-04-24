# Write a program that does the following actions:
#
# Ask the for a single integer as input. Set it as the random seed.
# Generate a random integer between 0 and 100
# Generate a random integer between 1 and 7
# Generate a random integer between 400 and 600
# Generate a random float between 9 and 10
# Generate a random float between 1 and 2
# Generate a random float between 100 and 200
# Randomly shuffle the list [2,4,6,8,10]


import random

lis = [2,4,6,8,10]
print("Enter Seed for Testing:")
seed = int(input())
random.seed(seed)
print("Random Integer 1:", random.randint(0, 100))
print("Random Integer 2:", random.randint(1, 7))
print("Random Integer 3:", random.randint(400, 600))
print("Random Float 1:", random.uniform(9, 10))
print("Random Float 2:", random.uniform(1, 2))
print("Random Float 3:", random.uniform(100, 200))
random.shuffle(lis)
print("Random Shuffle:", lis)