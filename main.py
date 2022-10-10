from fileinput import filename
import os
import time
import datetime
from tracemalloc import start

scriptDir = os.getcwd()
whPath = os.path.expanduser("~/working-hours")

currTime = int(time.time())-(3*24*60*60)
currDate = datetime.date.fromtimestamp(currTime)
currWeekday = int(time.strftime("%w", time.gmtime(currTime)))

workDayTimeSec = int(8*60*60)
overtime = 0

# prerequisites
if not os.path.exists(whPath):
    os.mkdir(whPath, mode=0o755)

os.chdir(whPath)
count = currWeekday
for i in range(1, 6):
    if count > 0:
        currFile = str(currDate - datetime.timedelta(days=i-1))
        timestamp = []
        with open(currFile, "r") as f:
            timestamp = [line.rstrip() for line in f]
        if not len(timestamp) == 2:
            count -= 1
            continue
        realWorkTimeSec = int(timestamp[1])-int(timestamp[0])
        timeDelta = workDayTimeSec - realWorkTimeSec
        overtime -= timeDelta
        count -= 1
    else:
        break

if overtime > 0:
    print(f"You got {int(overtime/60)} min of overtime this week")
elif overtime < 0:
    print(f"You are {int(overtime/60)} min short of work schedule this week!")
else:
    print("This is just perfect! Not even a minute of overtime.")
