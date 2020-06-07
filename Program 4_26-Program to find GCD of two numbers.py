# -*- coding: utf-8 -*-
"""
Created on Sat May 23 09:11:59 2020

@author: ak792
"""
# WAP to calculate GCD of two numbers.
print("Program to find GCD of two numbers.\n\n\n")
num1=int(input("Enter first number : "))
num2=int(input("Enter second number : "))
GCD=1
if num1>num2:
    for i in range (1,num2+1):
        if(num1%i==0 and num2%i==0):
            GCD=i
elif num2>num1:
    for i in range (1,num1+1):
        if(num1%i==0 and num2%i==0):
            GCD=i
else:
    GCD=num1
print("\nGCD = ",GCD)
input()
