# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 14:24:04 2026

@author: gabaz
"""

#Calculate the intrest rate of a CD with the principle amount of a CD and year
#Display the principle, intrest rate, and intrest amount for the first year
#over $100000 for 5 years is 6%, $50000-$100000 for 10 years is 5% while 5 years is 4%, and the rest are 2%

 
#Obtain original principle amount and CD maturity
principle = float(input("Enter the principle amount of the CD: $"))
years = int(input("Enter the years of maturity of the CD: "))

#Determine intrest rate based on maturity and principle
if principle > 100000 and years == 5:
    intrest_rate = 0.06
elif 50000 <= principle <= 100000 and years == 10:
    intrest_rate = 0.05
elif 50000 <= principle <= 100000 and years == 5:
    intrest_rate = 0.04
else:
    intrest_rate = 0.02
    
#Calculate intrestfor the first year
first_yr_intrest = principle * intrest_rate

#Display results
print(f"Principle: ${principle:,.2f}")
print(f"Intrest Rate: {intrest_rate * 105}%")
print(f"First year intrest: ${first_yr_intrest:,.2f}")
