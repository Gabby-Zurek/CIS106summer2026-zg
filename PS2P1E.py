# -*- coding: utf-8 -*-
"""
Created on Thu May 28 21:34:18 2026

@author: gabaz
"""

#q1 weighted exam score calculator

#get exam scores from user
e1 = float(input("Enter the first exam: "))
e2 = float(input("Enter the second exam: "))

#calculate the total weighted score
score_total = (e1*0.60)+(e2*0.40)

#Results
print("The weighted total score:", score_total)
