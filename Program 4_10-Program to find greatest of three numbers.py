# -*- coding: utf-8 -*-
"""
Created on Fri May 22 15:34:01 2020

@author: ak792
"""
# WAP to find greatest number of three numbers
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))
if num1>num2 and num1>num3:
    print("\nGreatest number is ",num1)
elif num2>num1 and num2>num3:
    print("\nGreatest number is ",num2)
else:
    print("Greatest number is ",num3)
input()
