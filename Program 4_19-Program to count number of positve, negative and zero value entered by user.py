# -*- coding: utf-8 -*-
"""
Created on Fri May 22 19:42:31 2020

@author: ak792
"""
# WAP to read the numbers untill -1 is encountered. Also count the negative, 
# positives, and zeroes entered by the user.
print("Program to count negatives, positives and zeroes entered by the user.\n\n\n")
negatives = 0
positives = 0
zeroes = 0
num = int(input("Enter any number : "))
while num!=-1:
    if num>0:
        positives+=1
    elif num==0:
        zeroes+=1
    else:
        negatives+=1
    num = int(input("Enter any number (-1 to exit) : "))
print("\nNumber of times positive value was entered : ",positives)
print("\nNumber of times negative value was entered : ",negatives)
print("\nNumber of times zero was entered : ",zeroes)
input()