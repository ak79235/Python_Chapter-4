# -*- coding: utf-8 -*-
"""
Created on Sun May 24 08:21:50 2020

@author: ak792
"""
# WAP using for loop to calculate the avera of first n natural numbers.
print("Program to calculate average of first n natural numbers.\n\n\n")
num = int(input("Enter the value of n : "))
s = 0
for i in range (1,num+1):
    s += i
print("\nAverage of numbers : ",s/num)
input()