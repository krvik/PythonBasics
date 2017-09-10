# this is 8th python programme.
# Created by me.


country = "canada"                  # one can also take input from user

if country == "canada":
    print("Hello")
elif country == "india":
    print("Namaskar...!!")
elif country == "china":
    print("Greeting in chinese.")
else:
    print("Oppps....!!!")


# checking multiple condition
wonLottery = True
bigWin = False

if wonLottery and bigWin :            # both condition should be true
    print("\nYou can retrive amount")
else:
    print ("\nyou have to wait.")


# using or
day = 'saturday'
if day == 'saturday' or 'sunday':
    print("\nGood sleep")
else:
    print("\nRun to work")

# and is having high priority than or.
team = raw_input("Enter ur fav team :").upper()
opening = raw_input("Enter opening batsman :").upper()
Light = 'sunny'.upper()

if team == 'INDIA' and Light == 'RAINY' \
        or opening == 'GAMBHIR':
    print("India will win")
else:
    print("Un-predictable")

