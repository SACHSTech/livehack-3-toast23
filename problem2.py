"""
-------------------------------------------------------------------------------
Name:   problem2.py
Purpose: compute # of days it took to pass 100km and average distance per day
 
Author: Yao.T
 
Created:  03/03/2021
------------------------------------------------------------------------------
"""

#program title
print("***** Welcome to the DoorDash Distance Tracker *****\n")

#initalize var 
totalDistance = 0
days = 0

#loop, get distance per day until total distance == 100km
print("** Travel Log **")
while totalDistance <= 100:
  distance = float(input("Enter the distance travelled for the day: "))
  totalDistance += distance
  days += 1
  
#calculate average distance per day 
averageDistance = round(totalDistance / days) 

#output
print("\n** Summary **")
print(f"It took {days} days to surpass 100km driven.")
print(f"The average distance driven per day is {averageDistance} km.")