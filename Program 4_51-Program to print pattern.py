# -*- coding: utf-8 -*-
"""
Created on Mon May 25 17:06:54 2020

@author: ak792
"""
# WAP to print the following pattern.
#     1
#    12
#   123
#  1234
# 12345
for i in range (6):
    print()
    for j in range (5,i,-1):
        print(" ",end=' ')
    for k in range (i):
        print(k+1,end=' ')
input()

