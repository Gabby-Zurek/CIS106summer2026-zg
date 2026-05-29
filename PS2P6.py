# -*- coding: utf-8 -*-
"""
Created on Thu May 28 22:25:26 2026

@author: gabaz
"""

#input share standings
purchase_price = float(input("Enter the price per share when bought: "))
current_price = float(input("Enter the current price per share: "))
quantity = int(input("Enter the quantity of stock: "))

#calculation
value_change = (current_price - purchase_price) * quantity

#gains/loss output
print(f"The change in value of the stock is: ${value_change:,.2f}")

if value_change < 0:
    print("This is an indicated loss.") 
else:
    print("This is an indicated gain.")