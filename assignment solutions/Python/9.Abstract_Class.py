#1. Create an abstract class with abstract and non-abstract methods. 
from abc import ABC, abstractmethod

class Animal(ABC):  # abstract class
    @abstractmethod
    def sound(self):  # abstract method
        pass

    def eat(self):  # non-abstract method
        print("This animal eats food.")

#2. Create a sub class for an abstract class. Create an object in the child class for the  abstract class and access the non-abstract methods 
class Dog(Animal):
    def sound(self):  # implementing abstract method
        print("Dog barks.")

# Creating object of Dog (child class)
dog = Dog()
dog.eat()    # Accessing non-abstract method from abstract class


#3. Create an instance for the child class in child class and call abstract methods 
class Dog(Animal):
    def sound(self):
        print("Dog barks.")

    def call_sound(self):
        d = Dog()
        d.sound()   # calling abstract method from inside child class

dog = Dog()
dog.call_sound()


#4. Create an instance for the child class in child class and call non-abstract method
class Dog(Animal):
    def sound(self):
        print("Dog barks.")

    def call_eat(self):
        d = Dog()
        d.eat()  # calling non-abstract method from inside child class

dog = Dog()
dog.call_eat()
