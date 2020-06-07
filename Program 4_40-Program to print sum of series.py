# -*- coding: utf-8 -*-
"""
Created on Mon May 25 15:15:43 2020

@author: ak792
"""
# WAP to sum the series - 1/1 + (2^2)/2 +...+ (n^n)/n.
print("Prpgram to sum the series - 1/1 + (2^2)/2 +...+ (n^n)/n.\n\n\n")
n = int(input("Enter any number : "))
sum = 0.0
for i in range (1,n+1):
    sum = sum + (pow(i,i)/i)
print("\nSum = ",sum)
input()

