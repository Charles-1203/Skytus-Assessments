# 🔹 Tasks

# Find employees earning more than average salary

# Find department with highest total salary

# Display employee with second highest salary

# Display employees working in same department as "Amit"

import sqlite3

# Connect to in-memory database
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# 1. Create Tables
cursor.executescript("""
    CREATE TABLE departments(
        dept_id INTEGER PRIMARY KEY,
        dept_name TEXT
    );
    CREATE TABLE employees(
        emp_id INTEGER PRIMARY KEY,
        emp_name TEXT,
        dept_id INTEGER,
        salary INTEGER,
        FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
    );
""")

# 2. Insert Sample Data
cursor.executescript("""
    INSERT INTO departments VALUES (1, 'Engineering'), (2, 'HR'), (3, 'Marketing');
    INSERT INTO employees VALUES 
        (101, 'Amit', 1, 60000),
        (102, 'Rohan', 1, 45000),
        (103, 'Priya', 1, 75000),
        (104, 'Neha', 2, 55000),
        (105, 'Karan', NULL, 40000); -- No department
""")



# Task: Display employee name with department name
print("\n1. Employees with Department Name:")
cursor.execute("""
    SELECT e.emp_name, d.dept_name 
    FROM employees e LEFT JOIN departments d ON e.dept_id = d.dept_id;
""")
for row in cursor.fetchall():
    print(f"  {row}")

# Task: Display employees earning more than 50,000
print("\n2. Employees earning > 50,000:")
cursor.execute("SELECT emp_name, salary FROM employees WHERE salary > 50000;")
for row in cursor.fetchall():
    print(f"  {row}")

# Task: Display department-wise total salary
print("\n3. Department-wise total salary:")
cursor.execute("SELECT dept_id, SUM(salary) FROM employees GROUP BY dept_id;")
for row in cursor.fetchall():
    print(f"  {row}")

# Task: Display departments with more than 2 employees
print("\n4. Departments with > 2 employees:")
cursor.execute("SELECT dept_id, COUNT(emp_id) FROM employees GROUP BY dept_id HAVING COUNT(emp_id) > 2;")
for row in cursor.fetchall():
    print(f"  {row}")

# Task: Find employees earning more than average salary
print("\n5. Employees earning > Average Salary:")
cursor.execute("SELECT emp_name, salary FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);")
for row in cursor.fetchall():
    print(f"  {row}")

# Task: Display employee with second highest salary
print("\n6. Second Highest Salary:")
cursor.execute("SELECT emp_name, salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 1;")
for row in cursor.fetchall():
    print(f"  {row}")

# Task: Employees working in same department as "Amit"
print("\n7. Employees in Amit's department:")
cursor.execute("""
    SELECT emp_name FROM employees 
    WHERE dept_id = (SELECT dept_id FROM employees WHERE emp_name = 'Amit') AND emp_name != 'Amit';
""")
for row in cursor.fetchall():
    print(f"  {row}")

conn.close()