# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 21:08:32 2026

@author: gabaz
"""

#Utalize emploee last name, salary, and job level to determine bonus rate
#Display emploee last name and bonus amount
#Job level's 10 and up get 25%, level's 5-9 is 20%, and rest have 10% bonus


# Obtain user input
last_name = input("Enter last name of employee: ")
salary = float(input("Enter salary of employee: "))
job_level = int(input("Enter your job level: "))

# Determine bonus
if job_level >= 10:
    bonus_rate = 0.25
elif 5 <= job_level <= 9:
    bonus_rate = 0.20
else:
    bonus_rate = 0.10
    
# Calculate bonus
bonus = salary * bonus_rate

#Display
print(f"Employee: {last_name}")    
print(f"Bonus: {bonus:,.2f}")
