# -*- coding: utf-8 -*-
"""
Created on Thu May 28 22:10:19 2026

@author: gabaz
"""

#Gather last_name and exam scores
last_name = input("Enter students last name: ")
midterm = float(input("Enter students midterm score: "))
final_exam = float(input("Enter students final exam score:"))

#calculate total points
point_total = (midterm* 0.40) + (final_exam* 0.60)

#Display total points
print(f"Student: {last_name}")
print(f"Total exam points:{point_total:.2f}")
