import datetime as dt

d = dt.datetime.now()

print(d)
print(d.month)

d = dt.datetime(2004,7,14)

print(d.strftime("%a"))
print(d.strftime("%A"))

print(d.strftime("%Z"))