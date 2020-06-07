# -*- coding: utf-8 -*-
"""
Created on Mon May 25 17:17:51 2020

@author: ak792
"""
# WAP to print the following pattern.
#     1
#    2 2
#   3 3 3
#  4 4 4 4 
# 5 5 5 5 5 
for i in range (1,6):
    print()
    for j in range (5,i,-1):
        print(" ",end=' ')
    for k in range (i):
        print(i," ",end=' ')
input()

