# -*- coding: utf-8 -*-
"""
Created on Mon May 25 17:27:41 2020

@author: ak792
"""
# Using a for loop, write a program that prints out the decimal equivalents of
# 1/1, 1/2,...,1/n
print("Program to calculate decimal equivalent of fractional values.\n\n\n")
n = int(input("Enter the value of n : "))
for i in range (1,n+1):
    print("1/"+str(i)+" = %f"%(1/i))
input()
