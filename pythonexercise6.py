#!/bin/python3

string = input("please enter a word")
string_bwd = string[::-1]

print("backward your word means: " + string_bwd)

if string_bwd == string:
    print("that means your word is a palindrome")
else:
    print("that means your word is NOT a palindrome")
