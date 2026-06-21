# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 21:02:59 2026

@author: gabaz
"""

#Advanced function question 1
#User input quantity, price, and discount rate
#Calculate the discount amount and price
#Display the values calculated with quantity and price

def calculate_discount_and_price(quantity, price, discount_rate):
    """computes discount amount and discount price."""
   
    #Calculate
    discount_amount = quantity * price * discount_rate
    
    #Calculate the total discounted price
    discounted_price = (quantity * price) - discount_amount
    
    return discount_amount, discounted_price

#main portion of program
def main():
    print("---Discount Calculator---")
    #User input
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter item price: $"))
    discount_rate = float(input("Enter discount rate (e.g., 0.15 for 15%): "))
    
    #Call the function
    disc_amount, disc_price = calculate_discount_and_price(quantity, price, discount_rate)
    
    #Dispay Requerments
    print(f"\nQuantity: {quantity}")
    print(f"Original Price per Item: ${price:.2f}")
    print(f"Discount Amount: ${disc_amount:.2f}")
    print(f"Total Discounted Price: ${disc_price:.2f}")
    

#insures main() is the one that runs in a given function
if __name__ == "__main__":
    main()