import datetime as dt

d = dt.datetime.now()

d2 = dt.datetime(1998, 5 ,14)

print(dt.timedelta.total_seconds(d - d2))
