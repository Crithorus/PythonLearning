#   Try/catch method in python

#   Try block is where you place code that might generate an error
#   Catch block contains the code to handle that error
#   Catch block can be used to specify what actions to take when error occurs

#   This method prevents the programme from crashing when error occurs

#   in python, try catch is try EXCEPT
itemsInCart = 0
# 2 items will be added to cart

try:
    with open('input.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)
    print("File does not exist in the directory!")

#   The final block contains code that will always be executed even if exception occurs
#   This block can be used to clean up such as releasing resources and closing files

finally:
    print("Cleaning up resources")
