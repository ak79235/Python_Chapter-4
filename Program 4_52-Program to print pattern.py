# -*- coding: utf-8 -*-
"""
Created on Mon May 25 17:12:36 2020

@author: ak792
"""
# WAP to print the following pattern.
#     1
#    121
#   12321
#  1234321
# 123454321
for i in range (1,6):
    print()
    for j in range (5,i,-1):
        print(" ",end=' ')
    for k in range (i):
        print(k+1,end=' ')
    for l in range (i,1,-1):
        print(l,end=' ')
input()

