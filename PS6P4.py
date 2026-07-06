# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 16:48:16 2026

@author: gabaz
"""

#Create dictionarty using student name as key and grades as value
#Print each students names and grades in a two colum display with headers

def calc_and_print_grades(student_data):
    #Print the headers
    print(f"{'Student Name':<15}  |  {'Grade':<5}")
    print("-" * 30)
    total_grade = 0
    
    #print each student and their grades
    for name, grade in student_data.items():
        print(f"{name:<15}  |  {grade:<5}")
        total_grade += grade
        
    print("-" * 30)
    
    #Calc class avg
    class_avg = total_grade  /  len(student_data)
    print(f"{'Class Average':<15}  |  {class_avg:5.2f}")
#Example dictionare for problem
student_grades = {
    "Ben": 98,
    "Lia": 85,
    "Dian": 79,
    "Gale": 88,
    "Grant": 97
}

#Run function
calc_and_print_grades(student_grades)