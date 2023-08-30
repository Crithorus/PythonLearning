# parent-child inheritance in python

# adding functions/class from other files
from OOp import Calculator


# in c++ it is public derive : public base
# in python it is class derive(base)
class childIMP(Calculator):
    num2 = 200

    def getCompleteData(self):
        return self.num2 + self.num


obj1 = childIMP(10, 20)
print(obj1.getCompleteData())

obj1.getData()
