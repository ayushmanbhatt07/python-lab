
# 1. Write a Pandas program to create
# a) Date time object for Jan 15 2012.
# b) Specific date and time of 9:20 pm.
# c) Local date and time.
# d) A date without time.
# e) Current date.
# t) Time from a date time.
# g) Current local time.
# a) Date time object for Jan 15 2012
import pandas as pd
from datetime import datetime
dt1 = pd.Timestamp('2012-01-15')
print("Date time object for Jan 15 2012:", dt1)

# b) Specific date and time of 9:20 pm
dt2 = pd.Timestamp('2012-01-15 21:20:00')
print("Specific date and time of 9:20 pm:", dt2)

# c) Local date and time
local_dt = pd.Timestamp.now()
print("Local date and time:", local_dt)

# d) A date without time
date_only = pd.Timestamp('2012-01-15').date()
print("A date without time:", date_only)

# e) Current date
current_date = pd.Timestamp.now().date()
print("Current date:", current_date)

# f) Time from a date time
time_only = pd.Timestamp('2012-01-15 21:20:00').time()
print("Time from a date time:", time_only)

# g) Current local time
current_time = pd.Timestamp.now().time()
print("Current local time:", current_time)