# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 14:24:22 2026

@author: gabaz
"""
#Determine cost per ticket and total baised on the number of tickets purchased
#Display ticket quantity, price per ticket, and total cost
#25 or more = $50, 10-24 is $60, 5-9 is $70, and 5 or less = $75


#User input (number of tickets)
quantity = int(input("Enter the quantity of concert tickets: "))

#Use quantity input to find pricing for tickets
if quantity >= 25:
    ticket_price = 50
elif 10 <= quantity <= 24:
    ticket_price = 60
elif 5 <= quantity <= 9:
    ticket_price = 70
else:
    ticket_price = 75
#Calculate total cost
total_cost = quantity * ticket_price

#Display to user
print(f"\nNumber of tickets: {quantity}")
print(f"Price per ticket: ${ticket_price}")
print(f"Total cost: ${total_cost}")