# -*- coding: utf-8 -*-
"""
Created on Sun May 31 07:54:58 2020

@author: ak792
"""
# WAP that prompts the user to enter five words. If the length of any word is
# less than 6 characters, then it asks the user to enter it again. However if 
# a word is of 6 or more characters, then it displays it on the screen.
print("Program to display 5 words.\n\n\n")
i = 0
while i<5:
    word = str(input("Enter any word : "))
    if len(word)>=6:
        print("You entered : ",word)
        i+=1
    else :
        print("Enter another word with 6 or more letters!")
input()   

