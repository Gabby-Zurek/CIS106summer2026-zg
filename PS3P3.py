# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 21:08:27 2026

@author: gabaz
"""

#Determine the total cost baised on the quantity and part number
#Display part number, cost per part, and total
#parts price: 10 and 55 = $1.00, 99 = $2.00, 80 and 70 = $3.00, and the rest are $5.00


#Obtain part number and quantity
part_number = input("Enter the part number: ")
quantity = int(input("Enter quantity of parts: "))
 
#Determine cost of unit baised on part number
if part_number == "10" or part_number == "55":
    unit_cost = 1.00
elif part_number == "99":
    unit_cost = 2.00
elif part_number == "80" or part_number == "70":
    unit_cost = 3.00
else:
    unit_cost = 5.00

#Calculate total
total_cost = quantity * unit_cost

#Display results  (part number, cost for each, and total)
print(f"\nPart Number: {part_number}")   
print(f"Unit Cost: ${unit_cost:,.2f}")
print(f"Total Cost: ${total_cost:,.2f}")      