# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 21:09:22 2026

@author: gabaz
"""

#Advanced functions question 2
#Enter student's last name and 3 exam scores
#Use a function to calculate the average of the total points
#Display last name, total points, and average score

def compute_scores(score1, score2, score3):
    """Computes total points and average score."""
    total_points = score1 + score2 + score3
    average_score = total_points / 3
    return total_points, average_score

#---Main program prtion---
def main():
    print("\n---Student Grade Calculator---")
    #User inputs
    last_name = input("Enter students last name: ")
    score1 = float(input("Enter exam score 1: "))
    score2 = float(input("Enter exam score 2: "))
    score3 = float(input("Enter exam score 3: "))
    
    #Call function
    total, average = compute_scores(score1, score2, score3)
    
    #Display Results
    
    print(f"\nStudents Last Name: {last_name}")
    print(f"Total Points: {total:.2f}")
    print(f"Average exam score: {average:.2f}")


#insures main() is the one that runs in a given function
if __name__ == "__main__":
    main()