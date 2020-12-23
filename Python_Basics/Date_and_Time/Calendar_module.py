import calendar

weekday_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# print(calendar.TextCalendar(firstweekday=6).formatyear(2020))
month, day, year = list(map(int, input().split()))
position = calendar.weekday(year=year, month=month, day=day)
print(weekday_list[position].upper())
