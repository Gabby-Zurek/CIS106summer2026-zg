# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#This code allows an user to enter a quantity of an item to determine the price and tax amount
#quantity's over or equal to 1000 will be priced at $3.00 while those bellow will be $5.00
#Tax is calculated at 7%

 
# Identify item quantity 
quantity = int(input("Enter the quantity of your item: "))

# Determine unit price given the quantity
if quantity >= 1000:
    unit_price = 3.00
else:
    unit_price = 5.00
    
# calculate (extended price, tax, and total)
ext_price = quantity * unit_price
tax = ext_price * 0.07
total = ext_price + tax

# display results
print(f"Quantity: {quantity}")
print(f"Unit Price: ${unit_price:,.2f}")
print(f"Extended Price:  ${ext_price:,.2f}")
print(f"Tax (7%): ${tax:,.2f}")
print(f"Total: {total:,.2f}")