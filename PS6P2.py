# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 16:48:08 2026

@author: gabaz
"""

#Add onto last problem by containing exam score's for the respective students
#Parallel array:modify the display function to include exam and last name array's


#Modified function to display the 10 last names and their scores
def display_paralleldata(lastnames_list, scores_list):
    print("Student exam scores: ")
    for i in range(len(lastnames_list)):
        print(f"{lastnames_list[i]}: {scores_list[i]}")
    print()
    print()#printing blankes for spacing
    
#Second function for reverse order of last names and scores
def display_parallel_reverse(lastnames_list, scores_list):
    print("Student exam scores in reverse order:")
    for i in range(len(lastnames_list) -1, -1, -1):
        print(f"{lastnames_list[i]}: {scores_list[i]}")
    print()
    print()
           
#10 Last names in the list from the problem 1
last_names = [
    "Jackson", "Kim", "Lang", "Zurek", "Smith", "Danels", "Patel", "Michels","Buron","Mills"]
#Adiitional data of exam scores
exam_scores = [90, 68, 84, 78, 98, 90, 70, 88, 80, 100]
#Calling functions(modified)
display_paralleldata(last_names, exam_scores)
display_parallel_reverse(last_names, exam_scores)