# -*- coding: utf-8 -*-
"""
Created on Mon May 25 15:54:07 2020

@author: ak792
"""
# WAP to generate calendar of a month given the start_day and the number of
# days in that month.
print("Program to generate month of a calendar.\n\n\n")
flag = 0
num = int(input("Enter starting day of month : "))
if num>7:
    num = num-7
days = int(input("Enter no. of days in the month : "))
if days!=31 and days!=30 and days!=29 and days!=28:
    print("\nEnter valid no of days!!!")
    flag=1
if flag==0:
    print("\nMON   TUE     WED   THURS  FRI    SAT    SUN")
    print("---------------------------------------------")
    for i in range (num-1):
        print(end="       ")    
        j=num
    for i in range (1, days+1):
        if i<10:
            print("", i ,end="     ")
        else:
            print(i,end="     ")
        if 7-j==0:
            print("\n")
            j=0
        j+=1
input()   


