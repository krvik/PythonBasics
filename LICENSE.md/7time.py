# this is 7th python programme.
# Created by me.


import datetime

currentTime = datetime.datetime.now()
print(currentTime)
print(currentTime.hour)
print(currentTime.minute)
print(currentTime.second)

# H=hour(24hr), M=minute,I=hour(12hr),p=am/pm,s=sec
print(datetime\
      .datetime.strftime(currentTime,"%H:%M,%p"))