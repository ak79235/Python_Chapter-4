# -*- coding: utf-8 -*-
"""
Created on Sun May 31 07:45:19 2020

@author: ak792
"""
# WAP that prompts the user to enter a string. The program calculates and
# displays the length of the string untill the user enters "QUIT". 
print("Program to display length of the string.\n\n\n")
string = str(input("Enter any string : "))
while string!="QUIT" :
    print("Length of string = ",len(string))
    string = str(input("Enter any string (Enter QUIT to exit) : "))
    string = string.upper()
input()  

