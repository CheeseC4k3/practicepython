#!/bin/python3
import random


a = []
b = []

n = random.randint(1,100)
m = random.randint(1,100)

for i in range(0, n):
    a.append(random.randint(0,100))

for i in range(0, m):
    b.append(random.randint(0,100))

print("length of list a: " + str(len(a)))
print("length of list b: " + str(len(b)))

print("common integers of a + b:")
for i in a:
    if i in b:
        print(i)
