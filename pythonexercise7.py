#!/bin/python3

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#List comprehension that gives out all even numbers of list a
print([number for number in a if number%2 == 0])

