from datetime import datetime

import pygame
pygame.init()

alarm = pygame.mixer.Sound("./mixkit-digital-clock-digital-alarm-buzzer-992.wav")

# Function to add activities and set reminders
def add_activity():
    # Empty container for each activity
    activity = []

    # New activity to be added and added to the activity container in str format
    new_activity = input("Enter an activity:")
    activity.append(new_activity)

    # Add time in the format hh:mm (24-hours format)
    add_time = input("Add time in the format hh:mm (24-hours format):")
    activity.append(add_time)

    # Add date in the format yyyy-mm-dd
    add_date = input("Add date in the format yyyy-mm-dd:")
    activity.append(add_date)

    # Converting user's date and time into real time and setting up a reminder
    today_time = datetime.today().time()
    today_date = datetime.today().date()
    activity_date = datetime.strptime(add_date, "%Y-%m-%d").date()
    activity_time = datetime.strptime(add_time, "%H:%M").time()
    activity_day = activity_date.strftime("%A")

    if int(add_time[:2]) <= 24 and int(add_time[3:]) <= 59:
        if int(add_date[5:7]) <= 12 and int(add_date[8:]) <= 31:
            if today_date < activity_date or (today_date == activity_date and today_time < activity_time):
                print("Reminder set for", activity_day, activity_date, activity_time)

            elif activity_date == today_date and activity_time== today_time:
                alarm.play()

            else:
                print("Invalid Parameters")
    else:
        print("Invalid Parameters")

    return activity

# Infinite loop to continuously add activities
while True:
    print(add_activity())