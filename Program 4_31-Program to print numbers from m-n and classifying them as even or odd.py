# -*- coding: utf-8 -*-
"""
Created on Sun May 24 08:29:48 2020

@author: ak792
"""
# WAP using for loop to print all the numbers from m-n therby classifying them
# as even or odd.
print("Program to print numbers from m-n and classifying them as even or odd.\n\n\n")
m = int(input("Enter the value of m : "))
n = int(input("Enter the value of n : "))
for i in range(m,n+1):
    if i%2==0:
        print(i," - Even")
    else:
        print(i," - Odd")
input()
