# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 14:53:57 2026

@author: gabaz
"""

#Create text file with item, quantity, and price
#Compute extended price and read through file one line at a time
#Have each line display text file atributes and extended price
#After loop Display the sum of extended prices, count of the number of orders, and average order

#TestFile
with open("orders.txt", "w") as file:
    file.write("Banana,6,2\n")
    file.write("Potatos,2,12\n")
    file.write("Soda,24,5\n")
    file.write("Chocolate,10,4\n")
    file.write("Noodles,20,8\n")

#Identify variables
total_extended_price = 0
order_count = 0

print(f"{'Item':<10} {'Qty':<5} {'Price':<10} {'Extended Price'}")
print("-" * 45)

#Read file and compute
with open("orders.txt", "r") as file:
    for line in file:
        data = line.strip().split(',')
        
        if len(data) == 3:
            item = data[0]
            quantity = int(data[1])
            price = float(data[2])
            
            extended_price = quantity * price
            
            #Update counter and Display
            total_extended_price += extended_price
            order_count += 1
            
            print(f"{item:<10} {quantity:<5} ${price:9.2f} ${extended_price:.2f}")
            
#Final Calculation Display
if order_count > 0:
    average_order = total_extended_price / order_count
    print("-" * 45)
    print(f"Total Extended Price: ${total_extended_price:.2f}")
    print(f"Total Number of orders: {order_count}")            
    print(f"Average Order Value: ${average_order:.2f}")    
    