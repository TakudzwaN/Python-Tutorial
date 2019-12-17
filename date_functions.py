# timedelta Allows You To Add or Remove Days, Weeks or Months From A Date
from datetime import datetime, timedelta

today = datetime.now()
print("Today is " + str(today))

# Subtracting 1 Day
oneDay = timedelta(days=1)
yesterday = today - oneDay
print("Yesterday was " + str(yesterday))

# Subtracting 1 Week
oneWeek = timedelta(weeks=1)
lastWeek = today - oneWeek
print("Last week was " + str(lastWeek))