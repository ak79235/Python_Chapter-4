# -*- coding: utf-8 -*-
"""
Created on Fri May 22 15:11:39 2020

@author: ak792
"""
# WAP to find whether a given year is leap year or not.
print("Program to find whether a year is a leap year or not.\n\n\n")
year = int(input("Enter any year : "))
if (year%4==0 and year%100!=0)or(year%400==0):
    print("\nIt is a leap year!!")
else:
    print("\nIt is not a leap year!!")
input()
