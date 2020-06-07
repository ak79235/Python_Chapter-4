# -*- coding: utf-8 -*-
"""
Created on Fri May 22 19:52:44 2020

@author: ak792
"""
# WAP to read the numbers untill -1 is encountered. Find the average of positive
# numbers and negative numbers entered by the user.
print("Program to calculate average of negative and positive numbers.\n\n\n")
neg_count = 0
pos_count = 0
pos_sum = 0
neg_sum = 0
num = int(input("Enter any number : "))
while num!=-1:
    if num>0:
        pos_count += 1
        pos_sum += num
    elif num<0:
        neg_count += 1
        neg_sum += num
    num = int(input("Enter any number (-1 to exit) : "))
print("\nAverage of positive numbers : ",pos_sum/pos_count)
print("\nAverage of negative numbers : ",neg_sum/neg_count)
input()
