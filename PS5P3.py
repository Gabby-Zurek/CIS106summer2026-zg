# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 14:49:04 2026

@author: gabaz
"""

#More functions question 1
#Promt user to repeadetly do the program input yes or no
#Input yes enters loop and ask's for last name, month, and sales
#Compute to find the next months forcast and determine % (next month sales = salesx(1+forcast%)
#return next month sales and display value
#jan-mar is 10%, apr-jun is 15%, jul-sep is 20%, and oct-dec is 25%''

def compute_next_month_forcast(month, sales):
    #Determine forcast % baised on month
    month = month.lower()
    if month in ["jan", "feb", "mar"]:
        percent = 0.10
    elif month in ["apr", "may", "jun"]:
        percent = 0.15
    elif month in ["jul", "aug", "sep"]:
        percent = 0.20
    elif month in ["oct", "nov", "dec"]:
        percent = 0.25
    else:
        return None #Handle invaled month
    
    #Compute next month's sales estamate
    next_sales = sales * (1 + percent)
    return next_sales

def main():
    while True:
        choice = input("Do you want to run the program? (Yes or No): ").strip().lower()
       
        if choice == "no":
            break
        elif choice == "yes":
            last_name = input("Enter last name: ")
            month = input("Enter month (e.g, Jan): ")
            try:
                sales = float(input("Enter current month's sales: "))
                
                next_month_sales = compute_next_month_forcast(month, sales)
                
                if next_month_sales is not None:
                    print(f"\nUser: {last_name}")
                    print(f"Forcasted sales for next month: ${next_month_sales:,.2f}\n")
                else:
                    print("Invalid month entered. Please try again.")
            except ValueError:
                print("Please enter a numeric value for sales")
        else:
            print("Please enter 'yes' or 'no'. ")
    
#insures main() is the one that runs in a given function
if __name__ == "__main__":
    main()