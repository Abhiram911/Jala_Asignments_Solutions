#1. Write a program to print  “Bright IT Career”  ten times using for loop 
for i in range(10):
    print("Bright IT Career")

#2. Write a python program to print 1 to 20 numbers using the while loop. 
n = 1
while n < 21:
    print(n)
    n += 1
#3. Program to equal operator and not equal operators 
a = 10
b = 20

if a == b:
    print("a is equal to b")
else:
    print("a is not equal to b")

if a != b:
    print("a is not equal to b")
else:
    print("a is equal to b")

#4. Write a program to print the odd and even numbers. 
n = 20
print("Odd numbers:")
for i in range(1,n+1):
    if i%2 != 0 :
        print(i)
print("Even numbers:")
for j in range(1,n+1):
    if j%2 == 0 :
        print(j)

#5. Write a program to print largest number among three numbers. 
num1 = 100
num2 = 200
num3 = 300
if num1 > num2 and num2 > num3:
    print("Num1 is largest number among three numbers")
elif num2 > num1 and num1 > num3:
    print("Num2 is largest number among three numbers")
else:
    print("Num3 is largest number among three numbers")

#6. Write a  program to print even number between 10 and 20 using while 
num1 = 10
num2 = 20
while num1 <= num2:
    if(num1%2 == 0):
        print("Even Number:",num1)
    num1 += 1
#7. Write a program to print 1 to 10 using the do-while loop statement. 
# python doesnt have any do-while loop
i = 1
print("Mimic of Do-while loop Python doesnt have any do-while loop")
while True:
    print("Value of i:", i)
    i += 1
    if i > 10:
        break


#8. Write a program to find Armstrong number or not 
n = 153
d = 3
k = n
su = 0
while k > 0:
    a = k%10
    su += a**d
    k = k//10
if su == n :
    print("Given number is a Armstrong Number")
else:
    print("It is not a armstrong number")

#9. Write a program to find the prime or not. 
n = 7
k = 0
for i in range(2,n//2):
    if(n%i == 0):
        k += 1
        print(i)   
        print("Not a prime Number")
        break
if k == 0:
    print("It is a prime Number")
#10. Write a program to palindrome or not. 
n = 121
k = n
org = 0
while k > 0:
    a = k%10
    org = org*10 + a
    k = k//10
if(n == org):
    print("Palindrome")
else:
    print("Not Palindrome")
    
#11. Program to check whether a number is EVEN or ODD using switch 
"""
    Python doesn't contain Switch case
"""

#12. Print gender (Male/Female) program according to given M/F using switch 
"""
    Python doesn't contain Switch case
"""