"""
A, B and C are classes 
A is a super class. B is a sub class of A. C is a sub class of B.  
Create three methods in each class, 2 methods are specific to each class and third 
method (override method) should be in all three Classes A, B and C 
Create a class with main method. Create an object for each class A, B and C in main 
method and call every method of each class using its own object/instance. 
Call an overridden method with super class reference to B and C class’s objects 
Runtime Polymorphism with Data Members/Instance variables, Repeat the above 
process only for data members
    
"""


# Class A
class A:
    x = "Data A"

    def method1(self):
        print("A: method1")

    def method2(self):
        print("A: method2")

    def common(self):
        print("A: common (overridden)")

# Class B
class B(A):
    y = "Data B"

    def method3(self):
        print("B: method3")

    def method4(self):
        print("B: method4")

    def common(self):
        print("B: common (overridden)")

# Class C
class C(B):
    z = "Data C"

    def method5(self):
        print("C: method5")

    def method6(self):
        print("C: method6")

    def common(self):
        print("C: common (overridden)")

# Main method
def main():
    print("=== Object of A ===")
    a = A()
    a.method1()
    a.method2()
    a.common()
    print("Data from A:", a.x)

    print("\n=== Object of B ===")
    b = B()
    b.method1()  # inherited
    b.method2()  # inherited
    b.method3()
    b.method4()
    b.common()
    print("Data from B:", b.y)
    print("Accessing inherited data from A:", b.x)

    print("\n=== Object of C ===")
    c = C()
    c.method1()  # from A
    c.method2()  # from A
    c.method3()  # from B
    c.method4()  # from B
    c.method5()
    c.method6()
    c.common()
    print("Data from C:", c.z)
    print("Inherited from B:", c.y)
    print("Inherited from A:", c.x)

    print("\n=== Overridden method using superclass reference ===")
    refA: A

    refA = B()
    refA.common()  # Calls B's overridden method

    refA = C()
    refA.common()  # Calls C's overridden method

    print("\n=== Polymorphism with Data Members ===")
    refA = B()
    print("refA.x:", refA.x)  # A's variable
    print("refA.y (via cast):", refA.y)  # Only if accessed as B

    refA = C()
    print("refA.x:", refA.x)
    print("refA.y (via cast):", refA.y)
    print("refA.z (via cast):", refA.z)

