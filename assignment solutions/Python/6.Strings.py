#1. Different ways creating a string 

str1 = "double quotes"
str2 = 'single quotes'
str3 = """Multiline
String"""
str4 = str("Using str constructor")
print(str1)
print(str2)
print(str3)
print(str4)


#2. Concatenating two strings using + operator 
conc = str1 + str2
print("Concatenating two strings using + operator ")
print("String:",conc)

#3. Finding the length of the string 
print("Lenght of string of str4:",str4,len(str4))
#4. Extract a string using Substring 
s = "Hello World"
print("Substring:",s[0:5])
print("Substring2:",s[6:])

#5. Searching in strings using index() 
print("Searching in strings using index()")
print(s.index("World")) 

#6. Matching a String Against a Regular Expression With matches() 
import re

a = "abcd"
p = r"^abc"
if re.match(p,a):
    print("Starts with abc")
else:
    print("Does not start with abc")


#7. Comparing strings  
print("Comparing strings")
s1 = "apple"
s2 = "banana"
print("Given two strings are same:",s1==s2)
print("s1 < s2",s1<s2)
print("s1 > s2",s1 > s2)

#8. startsWith(), endsWith() and compareTo() 
s = "Hello World"
print(s.startswith("Hello"))
print(s.endswith("World"))
print((s > "abc") - (s < "abc"))

#9. Trimming strings with strip() 
s = "  Hello world  "
print(s.strip())     
print(s.lstrip())    
print(s.rstrip())    

#10. Replacing characters in strings with replace() 
s = "apple"
print(s.replace("p", "b"))  # Output: abble

#11. Splitting strings with split() 
s = "apple,banana,mango"
fruits = s.split(",")
print(fruits)  # Output: ['apple', 'banana', 'mango']

#12. Converting integer objects to Strings 
num = 123
str_num = str(num)
print(str_num, type(str_num))  # Output: '123' <class 'str'>


#13. Converting to uppercase and lowercase
s = "HeLLo"
print(s.upper())  # Output: HELLO
print(s.lower())  # Output: hello