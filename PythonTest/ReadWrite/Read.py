# How to open file in python

# Same as C++, remember to close files
file = open('input.txt')

# Read all contents of file
# print(file.read())
# print(file.read(5))  # prints input amount of characters
# print(file.readline())  # take not of previous read commands
# print(file.readline())  # additional read line will read next line

# line = file.readline()  # assign line to a variable

# This reads line by line until EOF
# while line != "":
#     print(line)
#     line = file.readline()

# Store line by line into a list
for line in file.readlines():
    print(line)
file.close()
