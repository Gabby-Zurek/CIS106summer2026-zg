# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 16:48:20 2026

@author: gabaz
"""

#Load file with 10 player names and their batting averages into a dictionary
#Write function to print the dictionary contents in 2 colums with headers on each

#Start empty dictionary
player_dictionary = {}

#Transfer data into dictionary
with open("baseball_stats.txt", "r") as file:
    for line in file:
        cleaned_line = line.replace("\n","")
        parts = cleaned_line.split()
        if parts:
            player_name = parts[0]
            batting_avg = float(parts[1])
            player_dictionary[player_name] = batting_avg
          #display results  
def display_player_stats(stats_dict):
    print(f"{'Player Name':<15} {'Batting Average':<15}")
    print("-" * 30)
    
    for player, avg in stats_dict.items():
        print(f"{player:<15}  {avg:<15.3f}")
        
#Initialize function
display_player_stats(player_dictionary)
    
