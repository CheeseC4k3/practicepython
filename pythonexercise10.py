#!/bin/python3

import random
#generade two lists of random length containing random ints (cant be duplicates inside one list!)
a = random.sample(range(1, 50), random.randint(10, 40))
b = random.sample(range(1, 50), random.randint(10, 40))
#print lists and length of lists
print("list a contains ", len(a)," integers: ", a, "\nlist b contains ", len(b)," integers:", b, "\n")
#print ints that are in both lists
print("integers that are in both lists: ", [value for value in a if (value in b)])
