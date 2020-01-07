#!/bin/python3

num = int(input("enter a random number"))
check = int(input("enter a divisor"))

if num%check == 0:
    print("num divides evenly by check")
else:
    print("num is not divided evenly by check")
