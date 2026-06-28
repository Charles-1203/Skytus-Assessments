	
# 🔹 Tasks

# Start a transaction

# Insert record into accounts

# Rollback changes

# Commit valid transactions

# Demonstrate transfer of money using transaction	
# 🔹 Tasks

# Start a transaction

# Insert record into accounts

# Rollback changes

# Commit valid transactions

# Demonstrate transfer of money using transaction


import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# 1. Create Tables
cursor.executescript("""
    CREATE TABLE customers(customer_id INTEGER PRIMARY KEY, name TEXT, city TEXT);
    CREATE TABLE products(product_id INTEGER PRIMARY KEY, product_name TEXT, price REAL);
    CREATE TABLE orders(order_id INTEGER PRIMARY KEY, customer_id INTEGER, order_date DATE, amount REAL);
    CREATE TABLE order_items(order_id INTEGER, product_id INTEGER, quantity INTEGER);
""")

# 2. Insert Sample Data
cursor.executescript("""
    INSERT INTO customers VALUES (1, 'John', 'Mumbai'), (2, 'Sara', 'Delhi'), (3, 'Mike', 'Pune');
    INSERT INTO products VALUES (1, 'Laptop', 60000), (2, 'Mouse', 1000);
    INSERT INTO orders VALUES 
        (101, 1, '2023-10-01', 61000), 
        (102, 1, '2023-10-15', 2000),
        (103, 2, '2023-11-05', 60000);
    INSERT INTO order_items VALUES (101, 1, 1), (101, 2, 1), (102, 2, 2), (103, 1, 1);
""")

print("=== ASSESSMENTS 7-8 ===")

print("\n1. Total orders per customer:")
cursor.execute("""
    SELECT c.name, COUNT(o.order_id) 
    FROM customers c LEFT JOIN orders o ON c.customer_id = o.customer_id GROUP BY c.name;
""")
for row in cursor.fetchall():
    print(f"  {row}")

print("\n2. Customers who never placed an order:")
cursor.execute("SELECT name FROM customers WHERE customer_id NOT IN (SELECT customer_id FROM orders);")
for row in cursor.fetchall():
    print(f"  {row}")

print("\n3. Highest selling product (by quantity):")
cursor.execute("""
    SELECT p.product_name, SUM(oi.quantity) as tq 
    FROM products p JOIN order_items oi ON p.product_id = oi.product_id 
    GROUP BY p.product_id ORDER BY tq DESC LIMIT 1;
""")
for row in cursor.fetchall():
    print(f"  {row}")

print("\n4. Monthly sales report:")
cursor.execute("SELECT strftime('%Y-%m', order_date), SUM(amount) FROM orders GROUP BY 1;")
for row in cursor.fetchall():
    print(f"  {row}")

print("\n5. Customers with total purchase > ₹50,000:")
cursor.execute("""
    SELECT c.name, SUM(o.amount) FROM customers c JOIN orders o ON c.customer_id = o.customer_id 
    GROUP BY c.name HAVING SUM(o.amount) > 50000;
""")
for row in cursor.fetchall():
    print(f"  {row}")

print("\n6. EXPLAIN QUERY PLAN (Optimized Search):")
cursor.execute("CREATE INDEX idx_order_cust ON orders(customer_id);")
cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM orders WHERE customer_id = 1;")
for row in cursor.fetchall():
    print(f"  {row}")

conn.close()