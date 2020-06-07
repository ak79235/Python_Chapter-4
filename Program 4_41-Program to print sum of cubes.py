# -*- coding: utf-8 -*-
"""
Created on Mon May 25 15:21:27 2020

@author: ak792
"""
# WAP to calculate the sum of cubes of numbers from 1-n.
print("Program to print sum of cubes from 1 to n.\n\n\n")
n = int(input("Enter any number : "))
sum = 0.0
for i in range (1,n+1):
    sum = sum + pow(i,3)
print("\nSum = ",sum)
input()

