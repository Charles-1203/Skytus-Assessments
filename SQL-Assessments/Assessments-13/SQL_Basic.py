# students(
#     student_id INT,
#     name VARCHAR(50),
#     department VARCHAR(30),
#     year INT,
#     marks INT
# )

# Tasks

# Display all student records

# Display only name and department

# Find students with marks greater than 75

# Display students from CSE department

# Sort students by marks (descending)

# Display top 3 scorers


import sqlite3

conn=sqlite3.connect("students.db")
cursor=conn.cursor()


cursor.execute("DROP TABLE IF EXISTS STUDENTS")

cursor.execute("""CREATE TABLE IF NOT EXISTS students (
               student_id INTeger Primary key  AUTOINCREMENT,
               name VARCHAR(30),
               department VARCHAR(20),
               year INTeger,
               marks INTEger)""")


cursor.execute("INSERT INTO students VALUES (1,'Charles','IT',2005,60)")


cursor.execute("""INSERT INTO students (name,department,year,marks) VALUES
               ('Charles2','IT',2005,70),
               ('Charles3','CSE',2005,90),
               ('Charles4','IT',2005,80);
               """)

conn.commit()

print("\nALL STUDENTS Records :")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

print("\n All the names and Departments of students : ")
cursor.execute("SELECT name,department FROM students")
for row in cursor.fetchall():
    print(row)

print("\n All the names and marks of students whos marks are above 75 : ")
cursor.execute("SELECT name,marks FROM students WHERE marks>75")
for row in cursor.fetchall():
    print(row)


print("\n All the names of students from CSE department: ")
cursor.execute("SELECT name,department FROM students WHERE department='CSE'")
for row in cursor.fetchall():
    print(row)

print("\n All the names and marks of students in Descending order: ")
cursor.execute("SELECT name,marks FROM students ORDER BY marks DESC ")
for row in cursor.fetchall():
    print(row)

print("\n All the names and marks of students in Descending order: ")
cursor.execute("SELECT name,marks FROM students ORDER BY marks DESC LIMIT 3 ")
for row in cursor.fetchall():
    print(row)



