from datetime import time
from day_calculator import dayPass

def add_time(start, duration, day=""):
  restMin=0
  days=0
  timeStart,zone = start.split(" ")
  hourStart, minuteStart = timeStart.split(":")
  hourDuration, minuteDuration = duration.split(":")

  if zone == "PM":
    hourStart = str(int(hourStart)+12)

  newHour = int(hourStart) + int(hourDuration)
  newMinutes= int(minuteStart) + int(minuteDuration)

  if newMinutes > 60:
    restMin = newMinutes - 60
    newHour += 1
  else:
    restMin = newMinutes
  
  while newHour > 23:
    newHour = newHour-24
    days +=1
    days//7
  dayOfWeek = ((days/7)-(days//7))*7
  date_string = time(newHour,restMin)
  format = "%-I:%M %p"
  my_date = time.strftime(date_string, format)
  if day !="":
    dayToReturn = dayPass(day, dayOfWeek) 
  if day=="":
    if days==0:
      my_date = my_date
    elif days == 1:
      my_date = my_date +" (next day)"
    else:
      my_date = my_date + " (%s days later)"%(days)
  else:
    if days==0:
      my_date = my_date +", " +dayToReturn
    elif days == 1:
      my_date = my_date +", " +dayToReturn +" (next day)"
    else:
      my_date = my_date +", " +dayToReturn + " (%s days later)"%(days)

  return my_date

