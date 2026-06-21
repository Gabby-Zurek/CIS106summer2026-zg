# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 14:41:40 2026

@author: gabaz
"""

#Functions Pass By Value Questions 2 using a loop with a single to stop
#Allow user to input last name, number of hits, and bats at the keyboard
#Compute bating aveage (utalize Pass the hits and at bat average)
#Display last name, batting averages, and give count of number if players entered

#define function
def calculate_batting_average(hits, at_bats):
    if at_bats == 0:
        return 0.0
    return hits / at_bats

def main():
    player_count = 0 #Starts at 0 players
    
    #Check for player decision
    while True:
        choice = input("Do you want to enter a player? (Yes or No)")
        
        #Have code run loop as long as user enters 'yes'
        if choice != 'yes':
            break
        
        #section Input
        last_name = input("Enter last name of player: ")
        hits = int(input("Enter number of player hits: "))
        at_bats = int(input("Enter number of at bats: "))
    
        #Calculate using function above
        batting_avg = calculate_batting_average(hits, at_bats)
        player_count += 1
    
        #Display Results
        print(f"Player: {last_name}")
        print(f"Batting Average: {batting_avg:.3f}\n")
    
    #Output the total count after loop finishedyes
    print(f"Total players entered: {player_count}")

#insures main() is the one that runs in a given function
if __name__ == "__main__":
    main()