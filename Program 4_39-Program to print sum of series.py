# -*- coding: utf-8 -*-
"""
Created on Mon May 25 15:10:04 2020

@author: ak792
"""
# WAP to sum the series - 1/2 + 2/3 +...+ n/(n+1).
print("Prpgram to sum the series - 1/2 + 2/3 +...+ n/(n+1).\n\n\n")
n = int(input("Enter any number : "))
sum = 0.0
for i in range (1,n+1):
    sum = sum + (i/(i+1))
print("\nSum = ",sum)
input()
