# this is 12th python programme.
# Created by me.
# python3

guests = ['rohan','abc','xyz','vikash','mike','rocky','sam']
score = [41,45,25,63,48,96]


print(guests)
print(score)
print(score[2])
print(score[-1])        # [-1]last,[-2]second last

# updating list value
guests[0]='sachin'
print(guests)

# appending new value
guests.append('sam')
print(guests)

# removing value
guests.remove("vikash")
print(guests)

# alternate way of removing is delete
del guests[2]
print(guests)

# finding indices of values. It find value, then stop searching
print(guests.index('sam'))    # if searching for value not in list. it shows error, handled later.


# sorting of lists, alphabetically
guests.sort()
print(guests)
score.sort()
print(score)


# using for loop with list
for steps in range(5):
    print(guests[steps])

guestsNumber = len(guests)
print(guestsNumber)



