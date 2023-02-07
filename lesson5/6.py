import datetime as dt

d = dt.datetime.now()

format = "%A %B"
print(d.strftime(format))

#8:09:34 PM
format = "%I:%M%S %p"
print(d.strftime(format))

