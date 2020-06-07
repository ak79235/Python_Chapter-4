# -*- coding: utf-8 -*-
"""
Created on Fri May 22 15:46:49 2020

@author: ak792
"""
# Wap to calculate tax given the following conditions :
# If income is less than 1,50,000 then no tax.
# If taxable income is 1,50,001-3,00,000 then charge 10 % tax
# If taxable income is 3,00,001-5,00,000 then charge 20 % tax
# If taxable income is above 5,00,001 then charge 30 % tax
print("Progam to display tax based on different conditions.\n\n\n")
salary = int(input("Enter annulal income : "))
min1 = 150000
if salary<min1:
    tax = 0
elif salary<300001:
    tax = 0.1 * (salary-min1)
elif salary<500001:
    tax = 0.2 * (salary-min1)
else:
    tax = 0.3 * (salary-min1)
print("TAX = ",tax)
input()