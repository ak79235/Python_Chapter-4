# -*- coding: utf-8 -*-
"""
Created on Sun May 24 08:34:48 2020

@author: ak792
"""
# WAP using for loop to calculate factorial of a number.
print("Program to calulate factorial of a number.\n\n\n")
num = int(input("Enter the number : "))
if num==0:
    fact = 1
    print("Factorial = ",fact)
else:
    fact = 1
    for i in range (1,num+1):
        fact*=i
    print("Factorial = ",fact)
input()

    
