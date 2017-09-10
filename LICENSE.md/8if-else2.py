# this is 8th python programme.
# Created by me.


authUser = "rohan"
User = raw_input("\nWatt's ur name : ")
if User.upper() == authUser.upper():                             # case-sensitive #to get rid convert it to upper
    print("\nWelcome...!!You are authorized.")                     # at any/both side.

print("Thank you.")             # condition match, print both stmt. otherwise only last one.


# use of boolean value in if-else
freeToaster=False                               # initialization of boolean is necessary.
deposit = raw_input("\nHow much would u like to deposit :")
if float(deposit) > 100:
    print("You get a free toaster.")
    freeToaster = True                         # variable.Also called flag
if freeToaster:
    print("Enjoy your toaster.")
else:
    print("Enjoy mug")
