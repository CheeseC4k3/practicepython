#!/bin/python3

import random
a = random.sample(range(1, 50), random.randint(10, 40))
b = random.sample(range(1, 50), random.randint(10, 40))

print(len(a), a, "\n", len(b), b, "\n")
print([value for value in a if (value in b)])
