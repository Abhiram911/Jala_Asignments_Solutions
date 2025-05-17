#1.Write a program to print your name.
n = input("Enter your name: ")
print(n)

#2.Write a program for a Single line comment and multi-line comments
#Single line Comment
"""
Multi-line
comments
"""

#3.Define variables for different Data Types int, Boolean, char, float, double and print on the Console.
Number = 1000
Boolean = True
Character = "V"
Float_value = 11.09
Double_value = 1.2345678987654

print("Int Data-type:",Number)
print("Boolean Data-type:",Boolean)
print("Character Data-type:",Character)
print("Float_value Data-type:",Float_value)
print("Double_value Data-type:",Double_value)

#4. Define the local and Global variables with the same name and print both variables and understand the scope of the variables 
x = 10  # Global variable
def my_function():
    x = 20  # Local variable
    print("Local x inside function:", x)

my_function()
print("Global x outside function:", x)
