from datetime import date

today = date.today()
days=["Sun", "Mon", "Tues", "Wed", "Thur", "Fri", "Sat"]
print("Tommorrow will be "+days[(today.weekday()+1)%7])

from datetime import datetime
now=datetime.now()
print(now.strftime("%d-%b-%Y %H:%M:%S"))
