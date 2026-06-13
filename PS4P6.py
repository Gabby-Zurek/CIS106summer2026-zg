# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 14:54:05 2026

@author: gabaz
"""

#Just before while loop, prompt user if they want to use this program. 
#Yes=continue on (while loop)    ect.=stop
#in while loop: user is asked for last name and two exam scores
#Compute average exam score, Display last name and average.
#After loop Display number of students who entered data
#Last statments in while loop promt to try again

#Start Counter for all students
student_count = 0

#Prompt user prior to the while loop
user_choice = input("Do you want to run this program? (Enter 'yes' to continue): ")

#While loop evaluates choice and prompts students for details
while user_choice.lower() == "yes":
    last_name = input("\nEnter the student's last name: ")
    exam1 = float(input("Enter First Exam Score: "))
    exam2 = float(input("Enter Seccond Exam Score: "))
    
    #compute 
    average_score = (exam1 + exam2) / 2
    
    #Display results 
    print(f"Students: {last_name}")
    print(f"Average Exam Score : {average_score:.2f}")
    
    #update counter and provide user with seccond prompt
    student_count += 1
    print("-" * 30)
    user_choice = input("Do you want to enter data for another student? (Yes/No): ")
    
#End loop details
print("\nProgram stopped.")
print(f"Total number of students who entered data: {student_count}")