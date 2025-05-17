#1. Write a function for arithmetic operators(+,-,*,/)
def arithmetic_operations(a,b):
    print("Addition + ",a+b)
    print("Subtraction - ",a-b)
    print("multiplication * ",a*b)
    print("division / ",a/b)

a = 10
b = 2
arithmetic_operations(a,b)

#2. Write a method for increment and decrement operators(++, --) 
def increment(a):
    a += 1
    print("increment",a)
def decrement(a):
    a -= 1
    print("decrement",a)
a = 10
increment(a)
decrement(a)
#3. Write a program to find the two numbers equal or not. 
num1 = 100
num2 = 110
num3 = 100
if (num1 == num2):
    print("num1 and num2 Equal")
else:
    print("num1 and num2 Not Equal")
if (num1 == num3):
    print("num1 and num3 Equal")
else:
    print("num1 and num3 Not Equal")
#4. Program for relational operators (<,<==, >, >==) 
if num1 > num2:
    print("Num1 > Num2")
else:
    print("Num1 < Num2")
if num1 < num2:
    print("Num1 < Num2")
else:
    print("Num1 > Num2")   

if num1 <= num3:
    print("Num1 <= Num3 ") 
if num1 >= num3:
    print("Num1 >= Num3 ") 
    
#5. Print the smaller and larger number 
if(num1 < num2):
    print("num1 is smaller")
    print("num2 is larger")
else:
    print("num2 is smaller")
    print("num1 is larger")  
     