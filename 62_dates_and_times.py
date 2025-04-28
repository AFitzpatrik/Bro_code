import datetime

date = datetime.date(2025, 1, 2)
today = datetime.date.today()

time = datetime.time(12, 30, 59)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %d-%m-%y") # format time


target_datetime = datetime.datetime(2025, 4, 28, 12, 30, 1)
current_daytime = datetime.datetime.now()

if target_datetime > current_daytime:
    print("You need to wait!")
elif target_datetime < current_daytime:
    print("You missed the date!")
else:
    print("its NOW!!")





print(date)
print(today)
print(time)
print(now)