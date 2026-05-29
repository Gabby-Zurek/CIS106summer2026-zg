# -*- coding: utf-8 -*-
"""
Created on Thu May 28 22:25:29 2026

@author: gabaz
"""

#Money recieved total
total_money = float(input("Enter the total amount of money earned:"))

#divide total between the three people
per_person = total_money / 3

#Display amount each person gets
print(f"Each person receives: ${per_person:.2f}")
