# -*- coding: utf-8 -*-
"""
Created on Sat May 23 09:23:58 2020

@author: ak792
"""
# WAP to print the reverse of a number.
print("Program to reverse a number.\n\n\n")
num = int(input("Enter any number : "))
number = 0 
while num!=0:
    number = (number*(10)) + (num%10)
    num = num//10
print("\nReversed number = ",number)
input()
