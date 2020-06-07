# -*- coding: utf-8 -*-
"""
Created on Thu May 21 22:18:06 2020

@author: ak792
"""
# WAP to determine the character entered by the user.
print("Program to determine the character entered by the user.\n\n\n")
char = input("Enter any key (Number, Alphabet, Space) : ")
if char.isalpha():
    print("\nEntered charcter is a alphabet.")
elif char.isdigit():
    print("\nEntered character is a digit.")
elif char.isspace():
    print("\nEntered character is a space.")
input()
