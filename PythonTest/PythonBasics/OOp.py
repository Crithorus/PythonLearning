# Classes in python

class Calculator:
    # class variables
    num = 100

    def __init__(self, a, b):  # constructor
        self.a = a
        self.b = b
        print("class constructed")

    def getData(self):
        value = self.a + self.b
        print("execute getData method in class", value)
