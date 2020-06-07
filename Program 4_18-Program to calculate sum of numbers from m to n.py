# -*- coding: utf-8 -*-
"""
Created on Fri May 22 19:37:42 2020

@author: ak792
"""
# WAP to calculate sum of numbers from m to n.
print("Program to print sum of numbers from m to n.\n\n\n")
m = int(input("Enter first number : "))
n = int(input("Enter second number : "))
sum = 0
while m<=n:
    sum+=m
    m+=1
print("\nSum = ",sum)
input()
