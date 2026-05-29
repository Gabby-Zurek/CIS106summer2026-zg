# -*- coding: utf-8 -*-
"""
Created on Thu May 28 21:55:26 2026

@author: gabaz
"""

# search for stoch ticker symbol and details
ticker = input("Enter stock ticker symbol:")
shares_amount = float(input("Enter number of shares:"))
share_cost = float(input("Enter cost per share:"))

#invested
investment_total = shares_amount*share_cost

#display results ($0.00)
print(f"\nStock: {ticker}")
print(f"Amount invested: ${investment_total:.2f}")