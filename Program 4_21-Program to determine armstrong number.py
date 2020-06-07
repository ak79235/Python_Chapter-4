# -*- coding: utf-8 -*-
"""
Created on Fri May 22 20:03:14 2020

@author: ak792
"""
# WAP to find whether the given number is an Armstrong numer or not.
print("Program to determine whether a number is Armstrong number or not.\n\n\n")
num = int(input("Enter any number : "))
s = 0
n=num
while n>0:
    r = n%10
    s = s+(r**3)
    n = n//10
if s==num:
    print("\nArmstrong number!")
else:
    print("\nNot an Armstrong number!")
input()
