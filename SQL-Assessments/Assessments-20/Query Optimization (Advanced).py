# 🔹 Tasks

# Add index to improve search on orders.customer_id

# Use EXPLAIN to analyze query

# Optimize a slow join query

# Explain when index should not be used

import sqlite3
import time

# Connect to an in-memory database
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# ==========================================
# 1. SETUP SCHEMA AND DATA
# ==========================================
cursor.executescript("""
    -- Table with no indexes on strings for the "slow" join demonstration
    CREATE TABLE customers(
        customer_id INTEGER PRIMARY KEY, 
        name TEXT, 
        city TEXT
    );
    
    CREATE TABLE orders(
        order_id INTEGER PRIMARY KEY, 
        customer_id INTEGER, 
        customer_name TEXT, -- Included just to demonstrate a bad join
        order_date DATE, 
        amount REAL,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    );
""")

# Insert dummy data
cursor.executescript("""
    INSERT INTO customers (customer_id, name, city) VALUES 
        (1, 'John Doe', 'Mumbai'), 
        (2, 'Jane Smith', 'Delhi'), 
        (105, 'Alice Johnson', 'Pune');

    INSERT INTO orders (order_id, customer_id, customer_name, order_date, amount) VALUES 
        (1001, 1, 'John Doe', '2023-10-01', 5000), 
        (1002, 105, 'Alice Johnson', '2023-10-15', 12000),
        (1003, 2, 'Jane Smith', '2023-11-05', 8000);
""")

print("=== ADVANCED QUERY OPTIMIZATION ===")

# ==========================================
# 2. OPTIMIZE A SLOW JOIN QUERY
# ==========================================
print("\n--- Demonstrating Joins ---")

# BAD JOIN: Joining on a text column (customer_name)
print("1. 'Slow' Join (Joining on Text Columns):")
cursor.execute("""
    SELECT c.name, o.amount 
    FROM customers c
    JOIN orders o ON c.name = o.customer_name;
""")
for row in cursor.fetchall():
    print(f"  {row}")

# GOOD JOIN: Joining on indexed integer Primary/Foreign Keys
print("\n2. 'Optimized' Join (Joining on Integer Keys):")
cursor.execute("""
    SELECT c.name, o.amount 
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id;
""")
for row in cursor.fetchall():
    print(f"  {row}")


# ==========================================
# 3. ADD INDEX & USE EXPLAIN TO ANALYZE
# ==========================================
print("\n--- Analyzing Search Strategies ---")

# Analyze BEFORE adding the index (SQLite uses EXPLAIN QUERY PLAN)
print("3. Query Plan BEFORE Index (Full Table Scan):")
cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM orders WHERE customer_id = 105;")
for row in cursor.fetchall():
    print(f"  {row}")

# Add the Index
print("\n4. Adding Index to orders.customer_id...")
cursor.execute("CREATE INDEX idx_orders_customer_id ON orders(customer_id);")
print("  Index created successfully.")

# Analyze AFTER adding the index
print("\n5. Query Plan AFTER Index (Index Search):")
cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM orders WHERE customer_id = 105;")
for row in cursor.fetchall():
    print(f"  {row}")


# ==========================================
# 4. WHEN NOT TO USE AN INDEX (Printout)
# ==========================================
print("\n--- When NOT to use an Index ---")
print("""1. On highly volatile tables (frequent INSERT/UPDATE/DELETEs) because 
   the database must rewrite the index tree on every change.
2. On small tables where a full table scan is faster than looking up the index.
3. On columns with low cardinality (e.g., gender, boolean flags) because 
   the index won't efficiently filter the data.""")

# Clean up
conn.close()
