# -*- coding: utf-8 -*-
"""
Created on Mon May 25 15:26:56 2020

@author: ak792
"""
# WAP to sum of squares of even numbers.
print("Program to display sum of squares of even numbers.\n\n\n")
n = int(input("Enter any number : "))
sum = 0
for i in range (2,n+1,2):
    sum = sum + pow(i, 2)
print("\nThe Sum of squares of even numbers less than 10 is ",sum)
input()
