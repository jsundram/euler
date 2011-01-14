# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
#
# A leap year occurs on any year evenly divisible by 4,
# but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century
# (1 Jan 1901 to 31 Dec 2000)?

import math
leap_years = 100 / 4
total_days = 365 * 100 + leap_years
days_per_month = 365.25 / 12.0 #365.25 days / year, 12 months / year
print math.floor(total_days / days_per_month / 7) # 1/7 of days are Sundays

# Alternatively:
import datetime
count = 0
for y in range(1901,2001):
    for m in range(1,13):
        if datetime.datetime(y,m,1).weekday() == 6:
            count += 1
print count
