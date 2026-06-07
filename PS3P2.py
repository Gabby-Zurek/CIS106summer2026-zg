# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 21:08:26 2026

@author: gabaz
"""

#Obtain input of quantity
quantity = int(input("Enter quantity of widgets: "))

#Determine price baised on quantity orderd
if quantity > 10000:
    price = 10
elif quantity >= 5000:
    price = 20
else:
    price = 30
    
#Calculate
ext_price = quantity * price
tax_amount = ext_price * 0.07
total = ext_price + tax_amount

#Display price results
print(f"Extended Price: {ext_price:,.2f}")
print(f"Tax: {tax_amount:,.2f}")
print(f"Total: ${total:,.2f}")