#10. Write a program to generate ClassNotFoundException 
import nonexistentmodule
#1. Write a program to generate Arithmetic Exception without exception handling
print(10 / 0)
#2. Handle the Arithmetic exception using try-catch block 
try:
    print(10 / 0)
except ZeroDivisionError:
    print("division by 0")

#3. Write a method which throws exception, Call that method in main class without try block 
def risky_division():
    return 10 / 0  
risky_division()  

#4. Write a program with multiple catch blocks 
try:
    x = int("abc")
    print(10 / 0)
except ZeroDivisionError:
    print("Division by 0")
except ValueError:
    print("Invalid")

#5. Write a program to throw exception with your own message 
def check_positive(num):
    if num < 0:
        raise ValueError("Number must be positive")
    return num

check_positive(-5)

#6. Write a program to create your own exception 
class MyError(Exception):
    pass

def test():
    raise MyError("This is a custom error")

test()

#7. Write a program with finally block 
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Handled division by zero")
finally:
    print("Finally block executed")

#8. Write a program to generate Arithmetic Exception 
print(5 / 0)

#9. Write a program to generate FileNotFoundException 
open("nonexistent.txt")

#11. Write a program to generate IOException 
with open("/root/secret.txt") as f:
    data = f.read()

#12. Write a program to generate NoSuchFieldException
with open("/root/secret.txt") as f:
    data = f.read()
