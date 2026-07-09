# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 11:31:23 2026

@author: gabaz
"""

#Utalize video of making a simple class and add method that accepts employee bonus rate
#ratexsalary calculation display
#Utalizing at a bonus rate of user's choice

class Employee:
    
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
        
        #Code for bonus
    def bonus_calc(self, rate):
        return rate * self.pay
        
emp_1 = Employee("Corey Schafer", 50000)
print(f"Employee {emp_1.name}, Base pay: ${emp_1.pay:,.2f}")

#prompting for bonus
rate_bonus = float(input("Enter the employee bonus rate: "))
bonus = emp_1.bonus_calc(rate_bonus)
print(f"Bonus: ${bonus:,.2f}")
    

