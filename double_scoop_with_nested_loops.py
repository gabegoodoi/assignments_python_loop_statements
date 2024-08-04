# Objective: The aim of this assignment is to 
# practice using nested loops in Python.

# Task 1: Your Mood Tracker 
# Simulate a mood tracker that records your mood at 
# three different times of the day (morning, afternoon, evening) 
# for each day of the week. Use nested loops to implement this: 
# the outer loop should iterate over the days, 
# and the inner loop should iterate over the times of the day. 
# For each time, randomly select a mood from a predefined list and print it. 
# Use the random module again to randomly select the mood.

import random

moods = ["Happy", "Sad", "Energetic", "Calm", "Tired"]
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
time_of_day = ["morning", "afternoon", "evening"]

for day in days_of_week:
    for time in time_of_day:
        print(f"Your {day} {time} mood was {random.choice(moods)}")