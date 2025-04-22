from datetime import datetime, date, time

#Create datetime object
dt = datetime(2024, 10, 27, 10, 30, 0)
print("DateTime Object: ",dt)

#Create date object
d = date(2024, 10, 27)
print("Date Object: ",d)

#Create time object
t = time(10, 30, 0)
print("Time Object: ",t)

#Get current date and time
now = datetime.now()
print("Current date and time: ",now)

#Get today's date
today = date.today()
print("Today is: ",today)

#Date formatting
now = datetime.now()
formatted = now.strftime("%m-%d-%Y %H:%M:%S")
print("Formatted date: ",formatted)