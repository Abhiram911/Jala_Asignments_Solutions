#1. Write a function to add integer values of an array 
def add_array(num,lst):
    lst.append(num)
    return lst
num1 = 1
num2 = 2
lst = []
add_array(num1,lst)
add_array(num2,lst)
print("The added listed",lst)

#2. Write a function to calculate the average value of an array of integers 
def avg_arr(arr):
    su = sum(arr)
    return(su/len(arr))
arr = [1,2,3,4,5,6,7,8,9,10]
print("Array:",arr)
print("Average of arr :",avg_arr(arr))

#3. Write a program to find the index of an array element 
arr = [1,2,3,4,5,6,7,8,9]
ele = 5
for i in range(len(arr)):
    if(arr[i] == ele):
        print(" Index of an array element :",i)

#4. Write a function to test if array contains a specific value 
def find(arr,ele):
    if ele in arr:
        return("We found the element")
    return("We didnt found the element")
print(find(arr,ele))

#5. Write a function to remove a specific element from an array 
def remove(arr,ele):
    arr.remove(ele)
    print(arr)
remove(arr,ele)

#6. Write a function to copy an array to another array 
def copy(arr,arr2):
    for i in range(0,len(arr)):
        arr2.append(arr[i])
    print("Original:",arr)
    print("Copied:",arr2)
arr2 = []
copy(arr,arr2)

#7. Write a function to insert an element at a specific position in the array 
def insert(arr,ele,pos):
    arr.insert(pos,ele)
    print("Insert element:",arr)
pos = 4
insert(arr,ele,pos)

#8. Write a function to find the minimum and maximum value of an array 
def max_min(arr,minimum,maximum):
    for i in arr:
        if i < minimum :
            minimum = i
        if i > maximum :
            maximum = i
    print("Maximum value:",maximum)
    print("Minimum value:",minimum)
minimum = arr[0]
maximum = arr[0]
max_min(arr,minimum,maximum)

#9. Write a function to reverse an array of integer values 
def reverse(arr):
    rev_arr = arr[::-1]
    print("reversed",rev_arr)
reverse(arr)

#10. Write a function to find the duplicate values of an array 
def find_dup(arr):
    se = set()
    for i in arr:
        if i in se:
            print(i,end =" ")
        else:
            se.add(i)
    print("These are dublicate elements") 
arr = [1,1,3,4,5,5,7,8,9]
print(arr)
find_dup(arr)

#11. Write a program to find the common values between two arrays 
def comman_vals(arr1,arr2):
    arr = []
    for i in arr2:
        if i in arr1:
            arr.append(i) 
    print("Array1:",arr1)
    print("Array2:",arr2)
    print("Common elements are:",arr)
arr1 = [1,2,4,5,7,8,9]
arr2 = [2,3,4,6,8]
comman_vals(arr1,arr2)
#12. Write a method to remove duplicate elements from an array 
def rem_dup(arr):
    print("Initial Array:",arr)
    arr = set(arr)
    arr = list(arr)
    print("Duplicates Removed:",arr)
arr = [1,1,2,3,4,5,5,6,7,8,9]
rem_dup(arr)
#13. Write a method to find the second largest number in an array 
def second_high(arr):
    maximum = 0
    second_max = 0
    for i in range(len(arr)):
        if(arr[i] > arr[maximum]):
            maximum = i
    arr.pop(maximum)
    for i in range(len(arr)):
        if(arr[i]>arr[second_max]):
            second_max = arr[i]
    print("Second largest Number:",second_max)    
second_high(arr)    
#14. Write a method to find the second largest number in an array 
def second_high(arr):
    maximum = 0
    second_max = 0
    for i in range(len(arr)):
        if(arr[i] > arr[maximum]):
            maximum = i
    arr.pop(maximum)
    for i in range(len(arr)):
        if(arr[i]>arr[second_max]):
            second_max = arr[i]
    print("Second largest Number:",second_max)    
second_high(arr)  
#15. Write a method to find number of even number and odd numbers in an array 
def odd_even(arr):
    odd = []
    even = []
    for i in arr:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    print("Array:",arr)
    print("Odd Numbers",odd)
    print("Even Number",even)
odd_even(arr)

#16. Write a function to get the difference of largest and smallest value 
def small_high(arr):
    maximum = 0
    minimum = 0
    for i in range(len(arr)):
        if(arr[i] > arr[maximum]):
            maximum = i
        if(arr[i] < arr[minimum]):
            minimum = i
            
    print("Array:",arr)
    print("Difference of largest and smallest value",arr[maximum]-arr[minimum])
small_high(arr)    
    
#17. Write a method to verify if the array contains two specified elements(12,23) 
def find(a,b,arr):
    if a in arr:
        print("array consist 12")
    else:
        print("array doesnt consist 12")
    if b in arr:
        print("array consist 23")
    else:
        print("array doesnt consist 23")
a = 23
b = 12
arr = [12,8,9,7,4,5,1,2,3]
find(b,a,arr)
#18. Write a program to remove the duplicate elements and return the new array
def rm(arr):
    s = set()
    newarr = []
    for i in arr:
        if i not in s:
            newarr.append(i)
            s.add(i)

    print("Elements are removed",newarr)
arr = [1,1,2,3,4,4,5,6,7,7,7,7]
rm(arr)
    