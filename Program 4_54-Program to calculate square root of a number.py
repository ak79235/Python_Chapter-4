# -*- coding: utf-8 -*-
"""
Created on Mon May 25 17:19:59 2020

@author: ak792
"""
# WAP to calculate square root of a number. Demonstrate the use of break and 
# continue statement.
print("Program to calculate square root of a number.\n\n\n")
import math
while 1:
    num = int(input("Enter any number (Enter 0 to exit) : "))
    if num==0:
        break
    elif num<0:
        print("Square root of negative number cannot be calculated.")
        continue
    print("Square root = ",math.sqrt(num))
input()
