# -*- coding: utf-8 -*-
"""
Created on Sat May 23 09:07:18 2020

@author: ak792
"""
# WAP to enter a number and then calculate the sum of it's digits.
print("Program to calculate sum of digits of a number.\n\n\n")
num = int(input("Enter any number : "))
sum = 0 
while num!=0:
    sum += num%10
    num = num//10
print("Sum = ",sum)
input()
