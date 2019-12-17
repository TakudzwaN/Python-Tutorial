# Import DateTime Library
from datetime import datetime

today = datetime.now()

# Returns Only The Day Portion Of The Date
print("Day " + str(today.day))

# Returns Only The Month Portion Of The Date
print("Month " + str(today.month))

# Returns Only The Year Portion Of The Date
print("Year " + str(today.year))
# Can Return Upto Seconds