# -*- coding: utf-8 -*-
"""
Created on Mon May 25 14:56:36 2020

@author: ak792
"""
# WAP to the sum the series - 1+ 1/2 +...+ 1/n.
print("Program to print the sum of the series = 1 + 1/2 +...+ 1/n.\n\n\n")
n = int(input("Enter any number : "))
sum = 0
for i in range (1,n+1):
    sum += (1/i)
print("Sum = ",sum)
input()
