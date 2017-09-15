
# method read, read all file content
# readline, read it line by line.
myFile = open("13file2.csv",mode='r+')
line1 = myFile.readline()
print(line1)
line2 = myFile.readline()
print(line2)

print("\n")


LinesAll = myFile.read()
print(LinesAll)

myFile.close()
