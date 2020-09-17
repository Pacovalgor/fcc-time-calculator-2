
def dayPass(day,dayOfWeek):
  newDay =""
  if day.lower() == "monday":
    if dayOfWeek==0:
      newDay = "Monday"
    elif dayOfWeek==1:
      newDay = "Tuesday"
    elif dayOfWeek==2:
      newDay = "Wednesday"
    elif dayOfWeek==3:
      newDay = "Thursday"
    elif dayOfWeek==4:
      newDay = "Friday"
    elif dayOfWeek==5:
      newDay = "Saturday"
    elif dayOfWeek==6:
      newDay = "Sunday"
  elif day.lower() == "tuesday":
    if dayOfWeek==0:
      newDay = "Tuesday"
    elif dayOfWeek==1:
      newDay = "Wednesday"
    elif dayOfWeek==2:
      newDay = "Thursday"
    elif dayOfWeek==3:
      newDay = "Friday"
    elif dayOfWeek==4:
      newDay = "Saturday"
    elif dayOfWeek==5:
      newDay = "Sunday"
    elif dayOfWeek==6:
      newDay = "Monday"
  elif day.lower() == "wednesday":
    if dayOfWeek==0:
      newDay = "Wednesday"
    elif dayOfWeek==1:
      newDay = "Thursday"
    elif dayOfWeek==2:
      newDay = "Friday"
    elif dayOfWeek==3:
      newDay = "Saturday"
    elif dayOfWeek==4:
      newDay = "Sunday"
    elif dayOfWeek==5:
      newDay = "Monday"
    elif dayOfWeek==6:
      newDay = "Tuesday"
  elif day.lower() == "thursday":
    if dayOfWeek==0:
      newDay = "Thursday"
    elif dayOfWeek==1:
      newDay = "Friday"
    elif dayOfWeek==2:
      newDay = "Saturday"
    elif dayOfWeek==3:
      newDay = "Sunday"
    elif dayOfWeek==4:
      newDay = "Monday"
    elif dayOfWeek==5:
      newDay = "Tuesday"
    elif dayOfWeek==6:
      newDay = "Wednesday"
  elif day.lower() == "friday":
    if dayOfWeek==0:
      newDay = "Friday"
    elif dayOfWeek==1:
      newDay = "Saturday"
    elif dayOfWeek==2:
      newDay = "Sunday"
    elif dayOfWeek==3:
      newDay = "Monday"
    elif dayOfWeek==4:
      newDay = "Tuesday"
    elif dayOfWeek==5:
      newDay = "Wednesday"
    elif dayOfWeek==6:
      newDay = "Thursday"
  elif day.lower() == "saturday":
    if dayOfWeek==0:
      newDay = "Saturday"
    elif dayOfWeek==1:
      newDay = "Sunday"
    elif dayOfWeek==2:
      newDay = "Monday"
    elif dayOfWeek==3:
      newDay = "Tuesday"
    elif dayOfWeek==4:
      newDay = "Wednesday"
    elif dayOfWeek==5:
      newDay = "Thursday"
    elif dayOfWeek==6:
      newDay = "Friday"
  elif day.lower() == "sunday":
    if dayOfWeek==0:
      newDay = "Sunday"
    elif dayOfWeek==1:
      newDay = "Monday"
    elif dayOfWeek==2:
      newDay = "Tuesday"
    elif dayOfWeek==3:
      newDay = "Wednesday"
    elif dayOfWeek==4:
      newDay = "Thursday"
    elif dayOfWeek==5:
      newDay = "Friday"
    elif dayOfWeek==6:
      newDay = "Saturday"
  return newDay
  