#1. Define a static variable and access that through a class  
class First:
    var = 1204
print("Static variable and access that through a class:",First.var)

#2. Define a static variable and access that through a instance 
obj = First()
print("Access that through an instance:",obj.var)

#3. Define a static variable and change within the instance 
obj.var = 1220
print()
print("Instance variable",obj.var)
print("Unchanged",First.var)

#4. Define a static variable and change within the class
class Second:
    var = 111
    
    @classmethod
    def change(cls,val):
        cls.var = val
Second.change(222)
print(" A static variable and change it within the class")
print("Second.var",Second.var)
obj1 = Second()
print("obj1.var",obj1.var)