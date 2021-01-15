#!/bin/python3
#Input
name = input("Please enter your name: ")
age = input("Please enter your age: ")
random = input("Please enter a random number: ")
i=0
#output and year calculation
for i in range(int(random)):
	print("Hello "+ name + ", You will be 100 years old in " + str(100 - int(age) +2019))
	i+1

