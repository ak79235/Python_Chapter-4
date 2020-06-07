# -*- coding: utf-8 -*-
"""
Created on Fri May 22 14:48:33 2020

@author: ak792
"""
# WAP to enter any character. If the entered character is in lowercase then
# convert it into uppercase and if it is an uppercase character, then covert
# it into lowercase.
print("Program to print lowercase in uppercase and vice-versa.\n\n\n")
char = input("Enter any alphabet (lowercase or Uppercase) : ")
if char.isalpha():
    if char.islower():
        char = char.upper()
    else:
        char = char.lower()
    print(char)
else:
    print("Enter valid alphabet!!")
input()

