
# Write query to find Nth highest salary

# Remove duplicate records

# Find records common in two tables

# Find employees hired in last 6 months

# Find continuous duplicate values


import sqlite3

# Connect to in-memory database
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# ==========================================
# 1. SETUP SCHEMA AND DATA
# ==========================================
cursor.executescript("""
    -- Table for Nth highest salary, duplicates, and recent hires
    CREATE TABLE employees(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        salary INTEGER,
        hire_date DATE
    );
    
    -- Tables for finding common records
    CREATE TABLE table_a(val TEXT);
    CREATE TABLE table_b(val TEXT);
    
    -- Table for finding continuous duplicates
    CREATE TABLE data_stream(
        id INTEGER PRIMARY KEY,
        value TEXT
    );
""")

cursor.executescript("""
    -- Insert employees 
    -- (Notice 'Amit' is duplicated exactly, 'Priya' and 'Neha' are hired recently)
    INSERT INTO employees (name, salary, hire_date) VALUES 
        ('Amit', 60000, date('now', '-10 months')),
        ('Amit', 60000, date('now', '-10 months')), -- Duplicate row
        ('Rohan', 45000, date('now', '-8 months')),
        ('Priya', 75000, date('now', '-2 months')), -- Hired 2 months ago
        ('Neha', 55000, date('now', '-1 months'));  -- Hired 1 month ago

    -- Insert into table_a and table_b
    INSERT INTO table_a VALUES ('Apple'), ('Banana'), ('Orange');
    INSERT INTO table_b VALUES ('Banana'), ('Grape'), ('Apple');

    -- Insert continuous data ('Y' and 'X' repeat consecutively)
    INSERT INTO data_stream VALUES 
        (1, 'A'), 
        (2, 'B'), 
        (3, 'B'), -- Continuous duplicate
        (4, 'C'), 
        (5, 'D'),
        (6, 'D'); -- Continuous duplicate
""")

print("=== SQL CODING TEST ===")

# ==========================================
# 2. EXECUTE QUERIES & PRINT OUTPUT
# ==========================================

# Task 1: Find Nth highest salary (Let's find the 2nd highest)
# Using LIMIT 1 OFFSET (N-1)
print("\n1. 2nd Highest Salary:")
cursor.execute("""
    SELECT DISTINCT salary 
    FROM employees 
    ORDER BY salary DESC 
    LIMIT 1 OFFSET 1;
""")
for row in cursor.fetchall():
    print(f"  {row}")

# Task 2: Remove duplicate records
# We keep the row with the minimum ID for each distinct group of data
print("\n2. Removing duplicate records (Amit)...")
cursor.execute("""
    DELETE FROM employees 
    WHERE id NOT IN (
        SELECT MIN(id) 
        FROM employees 
        GROUP BY name, salary, hire_date
    );
""")
conn.commit()
print("  Duplicates removed. Current employees table:")
cursor.execute("SELECT * FROM employees;")
for row in cursor.fetchall():
    print(f"  {row}")

# Task 3: Find records common in two tables
# Using the INTERSECT operator
print("\n3. Records common in Table A and Table B:")
cursor.execute("""
    SELECT val FROM table_a
    INTERSECT
    SELECT val FROM table_b;
""")
for row in cursor.fetchall():
    print(f"  {row}")

# Task 4: Find employees hired in last 6 months
# Using SQLite's built-in date modifiers
print("\n4. Employees hired in the last 6 months:")
cursor.execute("""
    SELECT name, hire_date 
    FROM employees 
    WHERE hire_date >= date('now', '-6 months');
""")
for row in cursor.fetchall():
    print(f"  {row}")

# Task 5: Find continuous duplicate values
# Using the LAG() window function to compare current row with the previous row
print("\n5. Continuous duplicate values in data stream:")
cursor.execute("""
    SELECT id, value 
    FROM (
        SELECT 
            id, 
            value, 
            LAG(value) OVER (ORDER BY id) AS prev_value 
        FROM data_stream
    ) subquery
    WHERE value = prev_value;
""")
for row in cursor.fetchall():
    print(f"  {row}")

# Clean up
conn.close()