# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 20:55:38 2026

@author: gabaz
"""

#More functions question 2
#Prompt reader to repeadidly do the program (yes initiates loop)
#Prompt user for make, model, electric vichicle code (Y/N), and MSRP of an automobile (Sticker price)
#Calculate door price, Determine: % , add 7% sales tax, and return to display the total
#Sum all MSRP's and sum of all sales price of the cars (MSRP-discount+tax)
#Utalize car list as givn in code

def calculate_door_price(make, model, is_electric, msrp):
    """
    Computes the discount percent, discount amount, tax, and out-the-door price.
    Returns a tuple: (discount_percent, discounted_msrp, tax, final_price)
    """
    #Normalize string for strong matching
    make_clean = make.strip().lower()
    model_clean = model.strip().lower()
    is_electric_clean = is_electric.strip().upper()
    
    #Determine percent off MSRP baised on requierments
    if make_clean == "honda" and model_clean == "accord":
        pct_off = 0.10
    elif make_clean == "toyota" and model_clean == "rav4":
        pct_off = 0.15
    elif is_electric_clean == "Y":
        pct_off = 0.30
    else:
        pct_off = 0.05
        
    #Calculations
    discount_amount = msrp * pct_off
    discounted_msrp = msrp - discount_amount
    sales_tax = discounted_msrp * 0.07
    final_price = discounted_msrp + sales_tax
    
    return pct_off, discounted_msrp, sales_tax, final_price


def main():
    #accumilate statistics summery
    total_msrp = 0.0
    total_sales_price = 0.0
    
    print("---Automobile Price Calculator ---")
    
    #Continue loop or no?
    while True:
        run_program = input("\nDo you want to run the program? (Yes/No): ").strip().lower()
        if run_program not in ['yes', 'y']:
            break
        
        #Collect user inputs for the vehicle
        make = input("Enter make (e.g., Honda): ")
        model = input("Enter model (e.g., Accord): ")
        is_electric = input("Is it an electric vehicle? (Y/N): ")
        
        try:
            msrp = float(input("Enter MSRP (sticker price): $"))
        except ValueError:
            print("Invalid price input. Skipping this entry.")
            continue
        
        #Process the details using the function
        pct_off, discounted_msrp, tax, final_price = calculate_door_price(
            make, model, is_electric, msrp
        )
        
        #Update runing totals
        total_msrp += msrp
        total_sales_price += final_price
        
        #Display info for current vehicle
        print(f"\n---Vehicle Details---")
        print(f"Vehicle: {make} {model}")
        print(f"Original MSRP: ${msrp:,.2f}")
        print(f"Discount Rate: {pct_off * 100:.0f}%")
        print(f"New MSRP (After Discount): ${discounted_msrp:,.2f}")
        print(f"7% Sales Tax: ${tax:,.2f}")
        print(f"Out the Door Price: ${final_price:,.2f}")
        
    #Display final after total loop ends
    print("\n=======================")
    print("      Final Summery      ")
    print("=========================")
    print(f"Sum of all MSRPs:    ${total_msrp:,.2f}")
    print("Sum of all Sales Prices: ${total_sales_prices:,.2f}")
    print("=========================")
            
    
#insures main() is the one that runs in a given function
if __name__ == "__main__":
    main()