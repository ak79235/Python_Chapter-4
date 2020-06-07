# -*- coding: utf-8 -*-
"""
Created on Mon May 25 15:01:46 2020

@author: ak792
"""
# WAP to sum the series - 1/(1^2) + 1/(2^2) +...+ 1/(n^2).
print("Program to sum the series - 1/(1^2) + 1/(2^2) +...+ 1/(n^2).\n\n\n")
n = int(input("Enter any number : "))
sum = 0.0
for i in range (1,n+1):
    sum = sum + 1/(pow(i, 2))
print("\nSum = ",sum)
input()
