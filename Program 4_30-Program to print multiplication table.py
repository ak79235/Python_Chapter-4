# -*- coding: utf-8 -*-
"""
Created on Sun May 24 08:25:53 2020

@author: ak792
"""
# WAP to print the multiplication table of n, where n is entered by the user.
print("Program to print multiplication table of n.\n\n\n")
n = int(input("Enter the value of n : "))
for i in range (1,11):
    print(n," * ",i," = ",n*i)
input()  
