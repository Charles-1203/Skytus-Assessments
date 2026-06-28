# # 📌 Database: company_db

# # Tables

# # employees(
# # emp_id INT,
# # emp_name VARCHAR(50),
# # dept_id INT,
# # salary INT
# # )

# # departments(
# # dept_id INT,
# # dept_name VARCHAR(50)
# # )

# 🔹 Tasks

# Display employee name with department name

# Display employees earning more than 50,000

# Display department-wise total salary

# Display departments with more than 2 employees

# Display employees without a department



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
    INSERT INTO departments (dept_id, dept_name) VALUES 
        (1, 'Engineering'), 
        (2, 'HR'), 
        (3, 'Marketing');

    INSERT INTO employees (emp_id, emp_name, dept_id, salary) VALUES 
        (101, 'Amit', 1, 60000),
        (102, 'Rohan', 1, 45000),
        (103, 'Priya', 1, 75000),
        (104, 'Neha', 2, 55000),
        (105, 'Karan', NULL, 40000); -- Employee with no department
""")

print("=== BASIC QUERIES & JOINS ===")

# Task 1: Display employee name with department name
print("\n1. Employees with Department Name:")
cursor.execute("""
    SELECT e.emp_name, d.dept_name 
    FROM employees e 
    LEFT JOIN departments d ON e.dept_id = d.dept_id;
""")
for row in cursor.fetchall():
    print(f"  {row}")

# Task 2: Display employees earning more than 50,000
print("\n2. Employees earning > 50,000:")
cursor.execute("""
    SELECT emp_name, salary 
    FROM employees 
    WHERE salary > 50000;
""")
for row in cursor.fetchall():
    print(f"  {row}")

# Task 3: Display department-wise total salary
print("\n3. Department-wise total salary:")
cursor.execute("""
    SELECT d.dept_name, SUM(e.salary) AS total_salary 
    FROM employees e
    JOIN departments d ON e.dept_id = d.dept_id
    GROUP BY d.dept_name;
""")
for row in cursor.fetchall():
    print(f"  {row}")

# Task 4: Display departments with more than 2 employees
print("\n4. Departments with > 2 employees:")
cursor.execute("""
    SELECT d.dept_name, COUNT(e.emp_id) AS employee_count 
    FROM employees e
    JOIN departments d ON e.dept_id = d.dept_id
    GROUP BY d.dept_name
    HAVING COUNT(e.emp_id) > 2;
""")
for row in cursor.fetchall():
    print(f"  {row}")

# Task 5: Display employees without a department
print("\n5. Employees without a department:")
cursor.execute("""
    SELECT emp_name 
    FROM employees 
    WHERE dept_id IS NULL;
""")
for row in cursor.fetchall():
    print(f"  {row}")

# Close connection
conn.close()