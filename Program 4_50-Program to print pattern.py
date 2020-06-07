# -*- coding: utf-8 -*-
"""
Created on Mon May 25 17:05:11 2020

@author: ak792
"""
# WAP to print the following pattern.
# 0
# 12
# 345
# 6789
count = 0
for i in range (1,5):
    print()
    for j in range (i):
        print(count,end=' ')
        count+=1
input()

