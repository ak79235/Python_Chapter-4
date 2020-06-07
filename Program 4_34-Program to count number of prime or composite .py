# -*- coding: utf-8 -*-
"""
Created on Mon May 25 09:29:07 2020

@author: ak792
"""
# WAP using a while loop to read the numbers untill -1 is encountered. Also,
# count hte numbers of prime and composite numbers entered by the user.
print("Program to print number of prime and compsite numbers entered by the user.\n\n\n")
num = int(input("Enter any number (>0) : "))
num_prime = 0
num_com = 0
while num!=-1:
    flag = 0
    for i in range (2,(num//2)+1):
        if num%i==0:
            flag = 1
            num_com += 1
            break
    if flag==0:
        num_prime += 1
    num = int(input("Enter any number (>0) (Enter -1 to exit) : "))
print("\nTotal prime numbers entered = ",num_prime)
print("\nTotal composite numbers entered = ",num_com)
input()