# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 16:48:14 2026

@author: gabaz
"""

#Expand dictionary to lisk three grade values and another function to fid the average
#print names, averages, and the class average of each grade

#Example dictionare for problem
student_report = {
    "Ben": [70, 90, 68], 
    "Lia": [80, 96, 59],
    "Dian": [97, 96, 87],
    "Gale": [87, 49, 99],
    "Grant": [97, 80, 90],
}

def analyze_performance(data):
    #Print names and each indifidual avg's
    print(f"{'Student Name':<15}    {'Average Grade':<15}")
    print("-" * 35)
    
    #Start Tracker for the three assignment sums
    sum_grade1 = 0
    sum_grade2 = 0
    sum_grade3 = 0
    student_count = 0
   
    
    #find class averages
    for name, grade in data.items():
        #calculate
        individual_sum = 0
        individual_count = 0
        for g in grade:
            individual_sum += g
            individual_count += 1
        individual_avg = individual_sum / individual_count
        print(f"{name:<15}    {individual_avg:.2f}")
        
        #Column tracking
        sum_grade1 += grade[0]
        sum_grade2 += grade[1]
        sum_grade3 += grade[2]
        student_count += 1
        
    #Display results
    print("=" * 35)
    print("Class averages by exam category: ")
    print(f"Exam 1 Average: {sum_grade1 / student_count:.2f}")
    print(f"Exam 2 Average: {sum_grade2 / student_count:.2f}")
    print(f"Exam 3 Average: {sum_grade3 / student_count:.2f}")

#Exicute function
analyze_performance(student_report)