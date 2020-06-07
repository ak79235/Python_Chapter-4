# -*- coding: utf-8 -*-
"""
Created on Fri May 22 15:38:49 2020

@author: ak792
"""
# WAP that prompts the user to enter a number between 1-7 and then display the
# corresponding day of the week.
print("Program to display day of the week based on input.\n\n\n")
num = int(input("Enter any number (1-7) : "))
if num==1:
    print("\nMonday")
elif num==2:
    print("\nTuesday")
elif num==3:
    print("\nWednesday")
elif num==4:
    print("\nThursday")
elif num==5:
    print("\nFriday")
elif num==6:
    print("\nSaturday")
elif num==7:
    print("\nSunday")
else:
    print("\nWrong input!!!")
input()
