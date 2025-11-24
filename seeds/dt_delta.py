import os
import datetime
import time

C1_Time = datetime.datetime.now()
print(f'curreent:{C1_Time}')

print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

c2_Time =os.path.getmtime('./test.txt')
c2_Time = datetime.datetime.fromtimestamp(c2_Time)
delta = C1_Time.__sub__(c2_Time)
print(f'delta.days:{delta.days}')
if delta.days > 100:
    print("hello")                  