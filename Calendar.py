import calendar

print(calendar.weekheader(5))
print()

print(calendar.month(2019, 12))

print(calendar.calendar(2020))

is_leap_year = calendar.isleap(2020)
print("Is 2020 going to be leap year? --->> ", is_leap_year)
