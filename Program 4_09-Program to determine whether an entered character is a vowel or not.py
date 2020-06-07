# -*- coding: utf-8 -*-
"""
Created on Fri May 22 15:26:25 2020

@author: ak792
"""
# WAP to determine whether the character entered is a vowel or not.
print("Program to determine whether entered character is a vowel or not.\n\n\n")
character = str(input("Enter any charater (any alphabet) : "))
if character=='a' or character=='e' or character=='i' or character=='o' or character=='u':
    print("\nIt is a vowel!")
elif character=='A' or character=='E' or character=='I' or character=='O' or character=='U':
    print("\nIt is a vowel!")
else:
    print("\nIt is not a vowel!")
input()
