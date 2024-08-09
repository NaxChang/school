from datetime import datetime

year, month, day = map(int, input().split())

try:
    date = datetime(year, month, day)
    day_of_year = date.timetuple().tm_yday
    print(day_of_year)
except ValueError:
    print("error")
