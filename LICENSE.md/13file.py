# this is 13th python programme.
# Created by me.
# python3


inputFile = 'input.txt'
WRITE = 'w'
READ = 'r'
READWRITE = 'w+'
APPEND = 'a'

myFile = open(inputFile, mode=READWRITE)
myFile.write("Hey")                         # by default writing is done in single line.
myFile.write("How are u.?")                 # unless until not specified by \n, \t.
myFile.close()

print("File written successfully...1!")





