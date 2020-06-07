# -*- coding: utf-8 -*-
"""
Created on Sat May 23 08:20:06 2020

@author: ak792
"""
# WAP to enter a binary number and convert it into decimal number.
print("Program to convert bianry to decimal.\n\n\n")
num = int(input("Enter a binary number : "))
number=0
i=0
while num!=0:
    number = number + ((num%10)*(2**i))
    num = num//10
    i+=1
print("\nDecimal equivalent = ", number)
input()
