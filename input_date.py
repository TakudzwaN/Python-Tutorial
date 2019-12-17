# Import DateTime Library
from datetime import datetime, timedelta

# Get Date From User
birthday = input("When where you born (day/month/year)? ")
birthdayDate = datetime.strptime(birthday, "%d/%m/%Y")

# Print User Entered Birthday
print("Your birthday is " + str(birthdayDate))

oneDay = timedelta(days=1)
birthEve = birthdayDate - oneDay
print("Birth Eve is " + str(birthEve))