from datetime import datetime, timedelta
from time import time
from timeit import timeit

timestamp = time()
print(timestamp)

dt1 = datetime(2025, 1, 1)
print(dt1)
# for more info search on google strptime
dt = datetime.strptime("2026/04/16", "%Y/%m/%d")
print(dt)
dt2 = datetime.now()
print(dt2)
print(f"{dt2.year}-{dt2.month}")
print(dt2.strftime("%Y/%m/%d"))
dt = datetime.fromtimestamp(time())
print(dt)

dif = dt2 - dt1
print("dif:", dif)
print("dif.days:", dif.days)
print("dif.seconds:", dif.seconds)
print("dif.microseconds:", dif.microseconds)
print("dif.total_seconds()", dif.total_seconds())
