# -*- coding: utf-8 -*-
"""
Created on Mon May 25 15:42:06 2020

@author: ak792
"""
# WAP using for loop to calculate the value of an investment. Input an initial
# value of investment and annual interest, and calculate the value of investment
# over time.
print("Program to calculate value of an investment.\n\n\n")
initial = int(input("Enter initial value of investment : "))
interest =  int(input("Enter interest rate (in %) : "))
years = int(input("Enter the number of years for which investment has to be done : "))
futureval = initial
for i in range (1,years+1):
    futureval = futureval + (futureval * (interest/100))
print("\nVALUE = ",futureval)
input()