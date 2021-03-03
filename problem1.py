"""
-------------------------------------------------------------------------------
Name:   problem1.py
Purpose:  determine which group a player is in based on wins
 
Author: Yao.T
 
Created:  03/03/2021
------------------------------------------------------------------------------
"""

#initalize var
wins = ""

#user instructions
print("Enter the wins and losses for your team:")

#loop, ask user for game result
for x in range(6):
  result = input("").lower()
  if result == "w":
    wins += result 

#check # of wins, output 
if len(wins) >= 5:
  print("Your team is in Group 1")
elif len(wins) >= 3 and len(wins) < 5:
  print("Your team is in Group 2")
elif len(wins) >= 1 and len(wins) < 3:
  print("Your team is in Group 3")
else: 
  print("Your team is eliminated from the tournament")
