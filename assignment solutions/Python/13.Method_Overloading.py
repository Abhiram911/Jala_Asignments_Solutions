#1. Write two methods with the same name but different number of parameters of same type and call the methods  
class Demo:
    def show(self, a=None, b=None):
        if b is None:
            print("One param:", a)
        else:
            print("Two params:", a, b)

obj = Demo()
obj.show(5)
obj.show(5, 10)
#2. Write two methods with the same name but different number of parameters of different data type and call the methods  
class Demo:
    def show(self, a, b=None):
        if b is None and isinstance(a, str):
            print("String:", a)
        elif isinstance(a, int) and isinstance(b, int):
            print("Two ints:", a, b)
        else:
            print("Other case")

obj = Demo()
obj.show("Hi")
obj.show(3, 4)

#3. Write two methods with the same name and same number of parameters of same type 
class Demo:
    def show(self, a):
        print("Second method:", a)  # This will be used

obj = Demo()
obj.show(10)
