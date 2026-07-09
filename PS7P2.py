# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 11:32:10 2026

@author: gabaz
"""

#Create a student class (First name, last name, and district code [I/O])
#Create method to determine tuition owed 
#$250 per credit for 'I' district
#$500 per credit for 'O' district

class Student:#student info
    def __init__(self, first, last, district, class_credits):
        self.first = first
        self.last = last
        self.district = district
        self.class_credits = class_credits
        
    def compute_tuition(self):#tuition rates
        if self.district == 'I':
                rate_credit = 250.00
        else:
                rate_credit = 500.00
                
        return self.class_credits * rate_credit

    def display(self):
        print("Student Name:", self.first, self.last)
        print("District code:", self.district)
        print("Credits taken:", self.class_credits)
        print("Tuition: $", format(self.compute_tuition(), ".2f"))
        print("-" * 40)
        
#Creatin a test of 2 objects
student1 = Student("Gabriella", "Zurek", "I", 16)
student2 = Student("Hope", "Mill", "O", 12)

#Display
student1.display()
student2.display()
    