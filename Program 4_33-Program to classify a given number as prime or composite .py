# -*- coding: utf-8 -*-
"""
Created on Sun May 24 19:50:04 2020

@author: ak792
"""
# WAP to classify a given number as prime or composite.
print("Program to classify a given number as prime or composite.\n\n\n")
num = int(input("Enter any number : "))
flag = 0
for i in range (2,num//2):
    if num%i==0:
        flag = 1
        break
if flag==0:
    print("\nPrime number!")
else:
    print("Composite number!")
input()