# Python Tutorial

print("hello")

# comment block
s = 42
# print multiple variable types
print("value s=", s, 4.5)

# ==============================LIST======================================
# array = list in python. Can hold multiple variable type
myArray = [1.2, 3, "hello"]

# direct access to last index of the array
print(myArray[-1])

# access mid-array (start index to specified index -1
print(myArray[1:3])

# insert mid array/list (position and value
myArray.insert(2, "Insert")
print(myArray)

# append list (adds new value at the back of the list)
myArray.append("append")
print(myArray)

# update list
myArray[2] = "Hello"

# delete item in list
del myArray[0]

# ==============================TUPLE======================================

# Main difference between list and tuple is that tuple is 'constant' upon creation
# [] vs ()
val = (1, 2, 3, "tim")

print(val[3])

# ==============================DICTIONARY======================================

# basically a map with key-pair value
# Key and value can be of any data type ex = {key:value}
dic = {"a": 2, 3: "b", "c": "d", 2.3: 1.2}

print(dic["a"])

# create dictionary at run time

runDic = {} # empty dic

runDic["test"] = 12

runDic[1] = "test1"

print(runDic)


