# -*- coding: utf-8 -*-
"""
Created on Sun May 31 07:37:06 2020

@author: ak792
"""
# WAP that prompts the user to enter a number. If the number is equla to 99,
# print "Congratulations". If the number is less than 99, print - enter again 
# and aim higher - else print enter again a lower number. The program should
# run untill the user guesses the correct number that is 99.
print("Program to guess the right number.\n\n\n")
num = int(input("Enter any number : "))
while num!=99:
    if num<99:
        num = int(input("Enter again and aim higher : "))
    else:
        num = int(input("Enter again and aim lower : "))
print("\nCongratulations! You have guessed the number.")
input()
