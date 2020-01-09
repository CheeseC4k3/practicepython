#!/bin/python3

num = int(input("enter random number"))

#show divisors of num
for i in range(2, num):
    if num%i ==0:
        print(i)
