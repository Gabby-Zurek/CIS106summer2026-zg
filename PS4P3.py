# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 14:54:01 2026

@author: gabaz
"""

#Creat file with employee last name and salary and determine bonus rate
#100000>= has 20%, 50000 has 15%, and the rest have 10%
#compute bonus and dispay emploee's last name, salary and bonus on each line
# display all bonuses paid outafter the loop

#TextFile
with open("employees.txt", "w") as make_file:
    make_file.write("Smith 120000.00\n")
    make_file.write("Zurek 50000.00\n")
    make_file.write("Lee 65000.00\n")
    make_file.write("Giller 300000.00\n")
    make_file.write("Jones 20000.00\n")
    
#Initialize loop
bonus_total = 0

try:
    with open("employees.txt","r") as file:
        print(f"{'Name':<10}  |  {'Salary':<12}  |  {'Bonus':<10}")
        print("-" * 35)
        
        
        for line in file:
            data = line.split()
            if len(data) < 2: 
                continue
            last_name = data[0]
            salary = float(data[1])
            #Determining bonus rate
            if salary >= 100000:
                rate = 0.20
            elif salary >= 50000:
                rate = 0.15
            else:
                rate = 0.10
        
            #Calculate
            bonus = salary * rate
            bonus_total += bonus
        
        #Display
            print(f"{last_name:<10} | ${salary:>10.2f} | ${bonus:>9.2f}")
    print("-" * 30)
    print(f"Total of all bonuses paid: ${bonus_total:,.2f}")
    
except FileNotFoundError:
    print("Error: employees.txt not found.")