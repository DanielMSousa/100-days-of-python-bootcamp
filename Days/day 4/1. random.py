# Python uses Mersenne twister to randomize
# there's a Khan academy video about it

import random

#random.randint(a, b) -> generates a random number between a and b (both included)
random_integer = random.randint(1, 10)

print(random_integer)

#random.random(a, b) -> generates a random number between 0 and 1 (1 not included)
random_float = random.random() * 5

print(random_float)