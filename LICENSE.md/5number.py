# this is 5th python programme.
# Created by me.

l = 2          # if no code it store, it as number.otherwise string
b = 4.54564
area = l*b

print(area)
power = l**5
print(power)    # string and int are not concatenated together.

# Number formatting :
print("Area is : %d" % area)
print("Length is : %d" % l)
print("Length is : %3d" % l)
print("Length is : %03d" % l)        # formatted with width three digit and leading zero.
print("Area is : %f" % area)
print("Area is : %.2f" % area)       # print with two decimal places

# Alternate formatting :
print("\nArea is :{0:f}".format(area))
print("My fav number is:{0:d}".format(45))
print("""There are three numbers!
First is {0:d}.
Second is {1:4d} and third is {2:d}.!!""".format(7,8,9))    # triple quote used for line formatting.
                                                                        # 0,1,2 are indexes.4 is number of spaces

print("Backslash is used to tell python, that "\
      "we are continuing to next line. It "\
      "automatically Indentate, to understand to compiler.")

# By default python treated number as string.
salary = raw_input("\nHey, watt's ur salary :")
bonus = raw_input("Watt abt Bonus :")
payCheck = salary + bonus

print(payCheck)   # or
print(salary+bonus)

# to convey specify , it's type
payCheck = float(salary)+float(bonus)           # int, long, float, complex
print(payCheck)



