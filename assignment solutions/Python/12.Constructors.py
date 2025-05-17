#1. Write a class with a default constructor, one argument constructor and two argument constructors. Instantiate the class to call all the constructors of that class from a main class 
class First:
    def __init__(self, *args):
        if len(args) == 0:
            print("Default")
        elif len(args) == 1:
            print("One argument constructor:", args[0])
        elif len(args) == 2:
            print("Two argument constructor:", args[0], args[1])

First()
First("Hello")
First("Hello", "World")

#2. Call the constructors(both default and argument constructors) of super class from a child class 
class Parent:
    def __init__(self):
        print("Parent default")

    def __init__(self, msg="Default from Parent"):
        print(msg)

class Child(Parent):
    def __init__(self):
        super().__init__("Calling Parent from Child")
        print("Child constructor")

c = Child()

#3. Apply private, public, protected and default access modifiers to the constructor 
class AccessDemo:
    def __init__(self):              # Public
        print("Public constructor")

    def _protected_constructor(self):  # Protected (convention)
        print("Protected constructor")

    def __private_constructor(self):   # Private (name mangling)
        print("Private constructor")


obj = AccessDemo()
obj._protected_constructor()
# obj.__private_constructor() # error 
# Access through name mangling:
obj._AccessDemo__private_constructor()

#4. Write a program which illustrates the concept of attributes of a constructor.
class Student:
    def __init__(self, name, age):
        self.name = name 
        self.age = age    

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


s = Student("Alice", 20)
s.display()
