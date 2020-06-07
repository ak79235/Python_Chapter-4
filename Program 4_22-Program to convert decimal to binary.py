# -*- coding: utf-8 -*-
"""
Created on Sat May 23 07:59:44 2020

@author: ak792
"""
# WAP to enter a decimal number. Calculate and display the binary equivalent
# of this number.
print("Converting decimal value to binary.\n\n\n")
number = 0
i = 0
num = int(input("Enter any decimal value : "))
n = num
while n!=0:
    number = number + ((n%2)*(10**i))
    n = n//2
    i+=1
print("\nBinary equivalent = ",number)
i = 0
number = 0
n = num 
while n!=0:
    number = number + ((n%8)*(10**i))
    n = n//8
    i+=1
print("\nOctal equivalent = ",number)
i = 0
number = ''
n = num 
while n!=0:
    r = n%16
    if r==10:
        r = 'A'
    elif r==11:
        r = 'B'
    elif r==12:
        r = 'C'
    elif r==13:
        r = 'D'
    elif r==14:
        r = 'E'
    elif r==15:
        r = 'F'        
    number = str(number) + str(r)
    n = n//16
    i+=1
def my_function(x):
  return x[::-1]
mytext = my_function(number)
print("\nHexadecimal equivalent = ",mytext)
input()
