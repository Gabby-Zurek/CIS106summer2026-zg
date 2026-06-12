# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 14:53:38 2026

@author: gabaz
"""

#User is able to enter a start, stop, and increment value from Keyboard
#Display all numbers from start to stop values using the increment value as you proceed
#Use while loop structure

#Identify variables
start = int(input("Enter start value: "))
stop = int(input("Enter stop value: "))
increment = int(input("Enter inrement value: "))

#User input calculation and Display
current = start
while current <= stop:
    print(current)
    current += increment