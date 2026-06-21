# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 14:29:33 2026

@author: gabaz
"""

#Functions Pass By Value Questions 1 using a loop with a single to stop
#Allow user to provide quantity and prices and compute the total  baised on items in the loop
#have loop show total after each piece of data and add a 10% discount when total exeede's $10,000.00 (assuming typo in ? is adding an extra 0 an not misplacing the comma)
#Display quantity, price, and total extended price

#Utalize IPO organization

def compute_extended_price(qty, unit_price):
    """Calculates price with a 10% discount if total exeeds $10,000."""
    total = qty * unit_price
    if total > 10000:
        total = total * 0.90
    return total

def main():
    total_ext_price = 0
    print("Enter item details (Enter '0' for quantity to stop) ")
   
    while True:
        qty = float(input("\nEnter quantity: "))
        if qty == 0: #signal's code to stop
            break
        
        price = float(input("Enter unit price: "))
        
        #Call Function/ Pass by value
        ext_price = compute_extended_price(qty, price)
        
        #Update running total
        total_ext_price += ext_price
        
        #Display current results of item input
        print(f"Quantity: {qty}")
        print(f"Price: ${price:,.2f}")
        print(f"Extended Price: ${ext_price:.2f}")
        
    #Final display to user
    print("-" *30)
    print(f"Total Extended Price for all items: ${total_ext_price:,.2f}")
    
#insures main() is the one that runs in a given function
if __name__ == "__main__":
    main()