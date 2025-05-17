# 1. Create dictionary with 5 student ID-name pairs
students = {
    101: "Alice",
    102: "Bob",
    103: "Charlie",
    104: "David",
    105: "Eva"
}

# 1.1 Adding values to dictionary
students[106] = "Frank"  # Add new key-value pair
print("After adding:", students)

# 1.2 Updating values in dictionary
students[103] = "Chuck"  # Update name for key 103
print("After updating:", students)

# 1.3 Accessing values in dictionary
print("Student with ID 102:", students[102])

# 1.4 Create a nested dictionary (student info inside each ID)
nested_students = {
    101: {"name": "Alice", "age": 20},
    102: {"name": "Bob", "age": 22},
    103: {"name": "Charlie", "age": 21}
}

# 1.5 Access values of nested dictionary
for sid, info in nested_students.items():
    print(f"ID: {sid}, Name: {info['name']}, Age: {info['age']}")

# 1.6 Print keys present in dictionary
print("Student IDs:", list(students.keys()))

# 1.7 Delete a value from dictionary
del students[106]
print("After deletion:", students)
