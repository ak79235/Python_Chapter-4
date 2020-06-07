# -*- coding: utf-8 -*-
"""
Created on Fri May 22 14:57:32 2020

@author: ak792
"""
# A company decides to give bonus to all it's employees on Diwali. A 5% bonus
# on salary is given to the male workers and 10% bonus on salary to the female
# workers. WAP to enter the salary of an employee and sex of the employee. If 
# the salary of the employee is less than ₹ 10,000 then the employee gets an 
# extra 2% bonus on salary. Calculate the bonus that has to be given to the
# employee and display the salary that the employee will get.
print("Program to display salary of employee with bonus.\n\n\n")
salary = int(input("Enter your salary : "))
gender = str(input("Enter your gender (M/F) : "))
if gender == 'm' or gender == 'M':
    if salary<10000:
        bonus = 0.07 * salary
    else:
        bonus = 0.05 * salary
elif gender == 'f' or gender == 'F':
    if salary<10000:
        bonus = 0.12 * salary
    else:
        bonus = 0.10 * salary      
print("\nSalary = ",salary+bonus)
input()