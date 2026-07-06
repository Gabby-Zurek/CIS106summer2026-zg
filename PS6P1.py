# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 16:48:05 2026

@author: gabaz
"""

#Write function Not using Built in method
#Assign 10 last names to an array and write a function to display them
#write another function to display in reverse order

#Develop function to display original order of 10 names
def display_lastnames(lastnames_list):
    print("Last Names in original order: ")
    for i in range(len(lastnames_list)):
        print(lastnames_list[i])
    print()
    print()#printing blankes for spacing
    
#Second function for reverse order
def display_lastnames_reverse(lastnames_list):
    print("Lats Names in reverse order:")
    for i in range(len(lastnames_list) -1, -1, -1):
        print(lastnames_list[i])
    print()
    print()
           
#10 Last names in the list for the problem
last_names = [
    "Jackson", "Kim", "Lang", "Zurek", "Smith", "Danels", "Patel", "Michels","Buron","Mills"]

#Calling functions
display_lastnames(last_names)
display_lastnames_reverse(last_names)