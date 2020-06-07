# -*- coding: utf-8 -*-
"""
Created on Mon May 25 16:43:08 2020

@author: ak792
"""
# WAP to print the following pattern.
# Pass 1 - 1 2 3 4 5
# Pass 2 - 1 2 3 4 5
# Pass 3 - 1 2 3 4 5
# Pass 4 - 1 2 3 4 5
# Pass 5 - 1 2 3 4 5
print("Program to print a pattern.\n\n\n")
for i in range(1,6):
    print("Pass", i ,"-",end=" ")
    for j in range(1,6):
        print(j, end = " ")
    print("\n")  
input()
