# -*- coding: utf-8 -*-
"""
Created on Fri May 22 06:50:24 2020

@author: ak792
"""
# WAP to determine whether a person is eligible to vote or not. If he is not 
# eligible, display how many years are left to be eligible.
print('''Program to determine eligibilty of a person to vote.\n\n\n''')
age = int(input("Enter your age : "))
if(age>=18):
    print("\nYou are eligible to vote!")
else:
    print("\nYou have to wait " + str(18-age) + " years to vote.")
input()
