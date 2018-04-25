#Matthew Siegel
#4/25/18
#displayDate.py- displays the current date

from datetime import date

today = date.today()
day = today.day
monthNum = today.month
yearNum = today.year
weekDayNum = today.weekday()

weekdays = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
months = ['January','February','March','April','May','June','July','August','September','October','November','December']
print('Today is',weekdays[weekDayNum+1],',',months[monthNum-1],day,yearNum)


