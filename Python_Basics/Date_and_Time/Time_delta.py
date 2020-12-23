from datetime import datetime

t1 = datetime(year=2015, month=5, day=10, hour=13, tzinfo=-7)
t2 = datetime(year=2020, month=5, day=29, hour=4)
diff = t1 - t2
print(diff.total_seconds())
