# -*- coding: utf-8 -*-
"""
Created on Sun May 31 08:13:17 2020

@author: ak792
"""
# WAP that determines whether a student is eligible for PG course or not. To 
# be eligible, the student must have obtained more than 80% in X and XII
# examination, and 70% marks in graduation. If the student changes his stream 
# (Science, Commerce or Arts), then deduct 5% from his graduation score.
print("Program to check eligibility for PG course.\n\n\n")
X = int(input("Enter percentage obtained in class 10th : ")) 
XII_stream = str(input("Enter your stream in 12th(Science,Commerce,Arts)"))
XII_stream = XII_stream.lower()
XII = int(input("Enter percentage obtained in class 12th : "))
GRAD_stream = str(input("Enter your stream in Graduation(Science,Commerce,Arts) : "))
GRAD_stream = GRAD_stream.lower()
GRAD = int(input("Enter percentage obtained in class Graduation : "))
if XII_stream!=GRAD_stream:
    GRAD = GRAD-5
if X>80 and XII>80 and GRAD>70:
    print("\nYou are eligible for PG course.")
else:
    print("\nYou are not eligible for PG course.")
input()