# this is 13th python programme.
# Created by me.
# python3

fileName = '13file2.csv'
WRITE = 'w'                             # w+/r+ for readwrite
APPEND = 'a'                            # b for binary files(images)
numberStudent = int(input("Enter no of student added :"))

for data in range(numberStudent):
    data = input("Enter Roll,Name,Div :")
    file = open(fileName, mode=APPEND)
    file.write(data+'\n')
    file.close()

print("file successfully written.")