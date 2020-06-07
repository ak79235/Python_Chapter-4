# -*- coding: utf-8 -*-
"""
Created on Sat May 23 09:48:31 2020

@author: ak792
"""
# WAP using a while loop that ask the user for a number, and prints a countdown
# from that number to zero.
print("Program to show countdown.\n\n\n")
num = int(input("Enter any number : "))
while num>=0:
    print(num)
    num-=1
input()
