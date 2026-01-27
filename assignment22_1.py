import gc

class Demo:
    value=10
    def __init__(self,No1,No2):
       
        self.value1=No1
        self.value2=No2

    def fun(self):
        print("Inside instance method",self.value1,self.value2)

    
    def gun(self):
         print("Inside instance method",self.value1,self.value2)

#allocate
obj1 = Demo(11,21)
obj2 = Demo(51,101)

obj1.fun()
obj2.fun()
obj1.gun()
obj2.gun()

print("End of application")
