# -*- coding: utf-8 -*-
"""
Created on Fri May 22 16:33:01 2020

@author: ak792
"""
# WAP to calculate roots of a quadratic equation.
print("Program to find roots of a quadratic equation.\n\n\n")
a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))
c = int(input("Enter value of c : "))
D = (b**2)-(4*a*c)
if D>0:
    print("\nDistinct real roots : ")
    print("\nRoot 1 = ",(-b+D)/(2*a))
    print("\nRoot 2 = ",(-b-D)/(2*a))
elif D==0:
    print("\nEqual real roots : ")
    print("\nRoot = ",-b/(2*a))
else:
    print("\nImaginary roots!!")
input()