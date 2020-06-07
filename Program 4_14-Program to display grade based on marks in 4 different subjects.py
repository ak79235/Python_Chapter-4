# -*- coding: utf-8 -*-
"""
Created on Fri May 22 16:18:26 2020

@author: ak792
"""
# WAP to enter the marks of a student in four subjects. Then calculate the
# total and aggregate, and display the grade obtained by the student. If the 
# student scores an aggregate greter than 75%, then the grade is Distinction.
# If aggregate is >=60 and <75, then the grade is First Division. If aggregate 
# is >=50 and <60, then the grade is Second Division. If the aggregate is >=40
# and <50, then the grade is third division. Else the grade is fail.
print("Program to display the result of a student with grade.\n\n\n")
marks1 = int(input("Enter your marks in Mathematics (Out of 100) : "))
marks2 = int(input("Enter your marks in Physics (Out of 100) : "))
marks3 = int(input("Enter your marks in Chemistry (Out of 100) : "))
marks4 = int(input("Enter your marks in Computer Science (Out of 100) : ")) 
aggregate = (marks1 + marks2 + marks3 + marks4)/4
print("\nAggregate marks = ",aggregate)
if aggregate>75:
    print("\nGrade = Distinction.")
elif aggregate>=60:
    print("\nGrade = First Division")
elif aggregate>=50:
    print("\nGrade = Second Division")
elif aggregate>=40:
    print("\nGrade = Third Division")
else:
    print("\nFAIL!")
input()