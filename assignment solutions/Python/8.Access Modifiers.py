"""
1. Create a class with PRIVATE fields, private method and a main method. Print the fields 
in main method. Call the private method in main method. 
Create a sub class and try to access the private fields and methods from sub class. 
"""
class A:
    def __init__(self):
        self.__x = 10  # private variable

    def __show(self):  # private method
        print("Private:", self.__x)

    def access(self):
        self.__show()

obj = A()
print("Only way to access:",obj.access())
#print(A.__show()) error
"""
2. Create a class with PROTECTED fields and methods. Access these fields and methods 
from any other class in the same package.  
Also, Access the PROTECTED fields and methods from child class located in a different 
package 
Access the PROTECTED fields and methods from any class in different package 
"""
class B:
    def __init__(self):
        self._y = 20  # protected variable

    def _show(self):  # protected method
        print("Protected:", self._y)

class SubB(B):
    def access(self):
        print("Child accessing:", self._y)
        self._show()

child = SubB()
child.access()  


"""
3. Create a class with PUBLIC fields and methods.  
Access the public methods and fields from any class in the same package or different 
package.
"""
class C:
    def __init__(self):
        self.z = 30  # public variable

    def show(self):
        print("Public:", self.z)

obj = C()
print(obj.z)     
obj.show()       

