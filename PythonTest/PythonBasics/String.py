# strings in python

str1 = "hello world"
str2 = "my world"
str3 = "world"
str4 = " w h i t e "
print(str1[1])  # same as c++ string

print(str1[0: 5])  # same as list for sub-string

str1 += str2  # concatenation of strings
print(str1)

print(str3 in str2)  # checks if substring exists in string

var = str2.split("o")  # splits the string based on character into a list
print(var)
print(var[0])

print(str4)
print(str4.strip())  # removes leading and back white spaces in string lstrin rstrip if i want left or right only
