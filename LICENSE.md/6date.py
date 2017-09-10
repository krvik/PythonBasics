# this is 6th python programme.
# Created by me.

import datetime

currentDate = datetime.date.today()
print(currentDate)
print(currentDate.year)
print(currentDate.month)
print(currentDate.day)

# strftime allows us to specify date format
print(currentDate.strftime('%d %b,%Y'))
print(currentDate.strftime('%d/%m/%y'))
print(currentDate.strftime('%d-%m-%Y'))
print(currentDate.strftime('%m %B,%Y'))
print(currentDate.strftime('%A,%a'))

print(currentDate.strftime('Hey, vikash..!! Your bday is on %A, %d %B.'))

userInput = raw_input("\nwhat's ur bday(mm/dd/YYYY) :")
Bday = datetime.datetime.strptime(userInput,'%m/%d/%Y')     # datetime module>datetime class>strpline method(p=parsing)
print(Bday)                                                 # accept userInput only in %m/%d/%Y format

# operation on date
nextBday = datetime.datetime.strptime("10/25/2018",'%m/%d/%Y')\
    .date()
difference = nextBday - currentDate
print(difference.days)              # for more google dateutil



