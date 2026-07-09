# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 11:32:13 2026

@author: gabaz
"""

#Modify PS7P2 to utalize a dictionary
#Expand district typers to include international students who pay $800 per credit in district 'X'

class Student:#student info
    #Dictionary for tuition rates
    tuition_rates = {
        "I": 250.00, #In-district
        "O": 500.00, #Out-district
        "X": 800.00, #International
        "G": 250.00  #Reciprocity/ same as in district
    }

    def __init__(self, first, last, district, class_credits):
        self.first = first
        self.last = last
        self.district = district
        self.class_credits = class_credits
        
    def compute_tuition(self):#tuition rates using dictionary
        rate = Student.tuition_rates.get(self.district, 500.00)
                     
        return self.class_credits * rate

    def display(self):
        print("Student Name:", self.first, self.last)
        print("District code:", self.district)
        print("Credits taken:", self.class_credits)
        print("Tuition: $", format(self.compute_tuition(), ".2f"))
        print("-" * 40)
        
#Creatin a test of 2 objects
student1 = Student("Gabriella", "Zurek", "I", 16)
student2 = Student("Hope", "Mill", "O", 12)
student3 = Student("Kim", "Flit", "X", 10)
student4 = Student("Lia","Park", "G", 14)

#Display
student1.display()
student2.display()
student3.display()
student4.display()