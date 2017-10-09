import time, os
import datetime

while True:
    a = datetime.datetime.now()

    ampm = a.strftime("%p")
    hour = a.strftime("%H")
    minute = a.strftime("%M")
    second = a.strftime("%S")

    weekday = a.strftime("%A")

    os.system("cls")
    print("%2s:%2s:%2s %2s   %s\n" %(hour, minute, second, ampm.lower(), weekday))
    time.sleep(1)
