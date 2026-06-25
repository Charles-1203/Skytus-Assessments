# ```text
# Tasks

# Count total number of students


import sqlite3

conn=sqlite3.connect("students.db")
cursor=conn.cursor()

cursor.execute("SELECT count(*) FROM students")

print("Total number of students in the table are:")
for row in cursor.fetchall():
    print(row)


# Find average marks of students

print("Average marks of students are:")
cursor.execute("SELECT AVG(marks) FROM students")
for row in cursor.fetchall():
    print(row)


# Find highest and lowest marks

print("Highest and Lowest  marks of students are:")
cursor.execute("SELECT MAX(marks), MIN(MARKS) FROM students")
for row in cursor.fetchall():
    print(row)



# Find department-wise average marks


print("Average marks of students WITH RESPECT TO THIER DEPARTMENT are:")
cursor.execute("SELECT AVG(marks) AS AVERAGE_MARKS,department FROM students GROUP BY department")

for row in cursor.fetchall():
    print(row)



# Display departments where average marks > 70

print("Departments with average marks greater than 70 are :")
cursor.execute("SELECT department,marks FROM students WHERE marks>70")

for row in cursor.fetchall():
    print(row)



