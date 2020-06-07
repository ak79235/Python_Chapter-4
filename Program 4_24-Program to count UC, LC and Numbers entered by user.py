# -*- coding: utf-8 -*-
"""
Created on Sat May 23 08:29:55 2020

@author: ak792
"""
# WAP to read a character untill a * is encountered. Also count the number of
# uppercase, lowercase, and numbers entered by the user.
print("Program to count differnt entries made by user.\n")
c = input("Press any key (alphabet or number) : ")
uc = 0
lc = 0
number =0
while c!='*':
    if c.isalpha():
        if c.islower():
            lc+=1
        else:
            uc+=1
    elif c.isdigit():
        number+=1
    else:
        print("\nInvalid input!!")
    c = input("Press any key (alphabet or number) (Press * to exit) : ")
print("\n No. of Uppercase alphabets = ",uc)
print("\n No. of Lowercase alphabets = ",lc)
print("\n No. of Numbers = ",number)
input()
