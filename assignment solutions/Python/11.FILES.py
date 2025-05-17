import os
#1. Write a program to read text file 
f = open("file.txt", "r")
print(f.read())
f.close()

#2. Write a program to write text to .txt file using  InputStream 
f = open("output.txt", "w")
f.write(input("Enter text: "))
f.close()

#3. Write a program to read a file stream 
f = open("file.txt", "r")
for line in f:
    print(line.strip())
f.close()

#4. Write a program to read a file stream supports random access 
f = open("file.txt", "rb")
f.seek(5)
print(f.read(10).decode())
f.close()

#5. Write a program to read a file a just to a particular index using seek() 
f = open("file.txt", "r")
f.seek(10)
print(f.read(15))
f.close()

#6. Write a program to check whether a file is having read access and write access permissions

print("Readable:", os.access("file.txt", os.R_OK))
print("Writable:", os.access("file.txt", os.W_OK))
