# -*- coding: utf-8 -*-
"""
Created on Fri May 22 16:10:49 2020

@author: ak792
"""
# WAP to take input from the user and then check whether it is a number or a 
# character. If it is a character, determine whether it is in uppercase or
# lowercase.
print("Program to determine digit or alphabet.\n\n\n")
ch = input("Enter any character (alphabet or number) : ")
if ch.isalpha():
    if ch.islower():
        print("\nIt is a lowercase alphabet.")
    else:
        print("\nIt is a uppercase alphabet.")
elif ch.isdigit():
    print("\nIt is a number.")
else:
    print("\nInvalid entry!!")
input()