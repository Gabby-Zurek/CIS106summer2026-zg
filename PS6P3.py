# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 16:48:11 2026

@author: gabaz
"""

#Load last name and score(previous problem)
#Add function to display last name, highest, and lowest score


#Simulate File
import io
file_data = """Jackson,90
Kim,68
Lang,84
Zurek,78
Smith,98
Daniels,90
Patel,70
Michels,88
Buron,80
Mills,100"""

#Data input from text file
def load_data_from_file(file_string):
    """Load parallel arrays from a text file"""
    names = []
    scores = []
    
    #Load data from file scores.txt
    with io.StringIO(file_string) as file:
        for line in file:
            #split the formatting
           if line.strip():
               parts = line.strip().split(',')
               names.append(parts[0])
               scores.append(int(parts[1]))
    return names, scores

def find_highest_and_lowest(names_array, scores_array):
    """Find and display highest and lowest scores of students"""
                    
    #Checks list/ "array" length
    length = 0
    for _ in scores_array:
        length += 1
        
    if length == 0:
        print("No data available")
        return
    
    #Manipulate hint guidlines for Find Highest Score Logic
    high_var = 0
    high_index = 0
    low_var = 999
    low_index = 0
    
    for i in range(length):
        if scores_array[i] > high_var:
            high_var = scores_array[i]
            high_index = i
         
        if scores_array[i] < low_var:
            low_var = scores_array[i]
            low_index = i
#Display results to user
    print("---- Performance Analysis Results ----")
    print(f"Highest Score: {high_var} by {names_array[high_index]}")
    print(f"Lowest Score: {low_var} by {names_array[low_index]}")

#Exicution of function
names_from_file, scores_from_file = load_data_from_file(file_data)
find_highest_and_lowest(names_from_file, scores_from_file)        