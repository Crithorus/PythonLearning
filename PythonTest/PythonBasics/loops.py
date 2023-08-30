# Demo on loops in python

# Indentation is very important to python
greeting = "Good Morning"

# ':' is like open and close braces in c++/c/c#/java?
if greeting == "Morning":
    print("Matches!")
else:
    print("NO!")

print("no longer in if else loop")

# for-loops
obj = [1, 2, "s", 4.4, "test"]

# iterate through each item (for-each)
for items in obj:
    print(items)

print("===========================================")
# iterate through a certain range (start,end,increment)
# using range(1,100,2) 1-99 and increment by 2 each time
# having only parameter for range creates a max value 1 to input - 1
for j in obj[0: 5: 2]:  # pos 1 to 2
    print(j)

print("==================WHILE==========================")

# while loops

val = 0

while val < 6:
    print(val)
    if val == 3:
        print("exiting loop")
        break

    if val == 2:
        continue  # this keyword skips the code below it
    val += 1

print("while-loop execution is done")
