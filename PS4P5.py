# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 14:54:03 2026

@author: gabaz
"""

#Create text file with student last name, district code, and credits taken
#Compute Tuition (credits x cost per credit), District code I=$250 per credit, District code O= $500 per credit
#Display student last name, credits taken, and tuition for each line
#after loop Display total sum of all tuitions and the number of students.

#TestFile
file_content = """Jim
O
15
Gaza
I
18
Tal
I
16
Newmen
0
14
Dale
I
20"""

#Create file
with open("students.txt","w") as file:
    file.write(file_content)
    
#Initially reading and processing file
total_tuition = 0.0
student_count = 0


with open("students.txt", "r") as file:
    lines = [line.strip() for line in file if line.strip()]
        
 #loop for each line of a student(3x)
for i in range(0, len(lines), 3):
    last_name = lines[i]
    district_code = lines[i+1].upper()
    credits_taken = int(lines[i+2])
        
        #Determine cost per credit
    if district_code == 'I':
        cost_per_credit = 250.00
    elif district_code =='O':
        cost_per_credit = 500.00
    else:
        cost_per_credit = 0.00
            
    #Calculation and Display student details
    tuition_owed = credits_taken * cost_per_credit
    print(f"Student: {last_name} | Credits: {credits_taken} | Tuition Owed: ${tuition_owed:,.2f}")
        
    #Toals Update
    total_tuition += tuition_owed
    student_count += 1
        
#End loop summary
print("-" * 50)
print(f"Total Number of Students: {student_count}")
print(f"Total Tuition Owed: ${total_tuition:,.2f}")
        