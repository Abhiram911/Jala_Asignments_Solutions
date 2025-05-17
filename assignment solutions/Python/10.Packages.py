#1. Create a program to create two class. 
#1.1. Create a constructor and a method for each class 
#1.2. Create a __init__.py for adding all packages 
#1.3. Import the respective packages 
#1.4. Call each class by creating an object to it  
#1.5. Create a program by all the above 
#ClassOne
class ClassOne:
    def __init__(self):
        print("ClassOne constructor called")

    def greet(self):
        print("Hello from ClassOne")

#ClassTwo
class ClassTwo:
    def __init__(self):
        print("ClassTwo constructor called")

    def greet(self):
        print("Hello from ClassTwo")

#Main part of the program
def main():
    obj1 = ClassOne()
    obj1.greet()

    obj2 = ClassTwo()
    obj2.greet()

#Call main
if __name__ == "__main__":
    main()
