# -*- coding: utf-8 -*-
"""
Created on Fri May 22 06:58:10 2020

@author: ak792
"""
# WAP to find larger of two numbers.
print("Program to find the larger of the two numbers.\n\n\n")
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
if num1==num2:
    print("\nBoth numbers are equal!")
elif num1>num2:
    print("\n",num1," is greater than ",num2)
else:
    print("\n",num2," is greater than ",num1)
input()
