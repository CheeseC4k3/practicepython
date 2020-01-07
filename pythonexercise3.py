#!/bin/python3

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
r = int(input("random number"))
for i in a:
    if i < r:
        b.append(i)

print(b)
