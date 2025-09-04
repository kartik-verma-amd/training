# A school wants to maintain student records using a text file.
 
# You are required to write a Python program that performs the following file handling operations step by step:
 
# Write Operation:
# - Create a file named students.txt.
# - Write details of students (Name, Roll Number, Marks) into the file.
 
# Read Operation:
# - Read the content of students.txt and display it on the screen.
 
# Rename Operation:
# - Rename the file from students.txt to student_records.txt.
 
# Directory Operations:
# - Create a directory called SchoolData.
# - Move the renamed file student_records.txt into this directory.
# - List all files present in SchoolData to confirm the file is inside.
 
# Delete Operation:
# - Delete the file student_records.txt from inside the directory.
 
# Finally, delete the SchoolData directory.

import os
import shutil

file = open("students.txt", "w+")
file.write("Alice, 101, 89\n")
file.write("Bob, 102, 76\n")
file.write("Charlie, 103, 92\n")

file.seek(0)
content = file.read()
print(content)
file.close()

os.rename("students.txt", "student_records.txt")

os.mkdir("SchoolData")
shutil.move("student_records.txt", "SchoolData/student_records.txt")
files = os.listdir("SchoolData")
for f in files:
    print(f)

os.remove("SchoolData/student_records.txt")

os.rmdir("SchoolData")
