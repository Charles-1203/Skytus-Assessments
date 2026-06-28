#  Tasks

# Create users table with:

# Primary key

# Unique email

# Not null password

# Add foreign key between orders and users

# Create index on email column

# Create view to display user order summary


import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

# 1. Create Tables
cursor.executescript("""
    CREATE TABLE users (
        user_id INTEGER PRIMARY KEY,
        email TEXT UNIQUE,
        password TEXT NOT NULL
    );
    CREATE TABLE orders (
        order_id INTEGER PRIMARY KEY,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    );
    CREATE TABLE accounts (
        account_id INTEGER PRIMARY KEY,
        account_name TEXT,
        balance REAL
    );
""")

# 2. Insert Data & Create Index/View
cursor.executescript("""
    INSERT INTO users VALUES (1, 'alice@test.com', 'pass123'), (2, 'bob@test.com', 'pass456');
    INSERT INTO orders VALUES (101, 1), (102, 1), (103, 2);
    CREATE INDEX idx_user_email ON users(email);
    
    CREATE VIEW user_order_summary AS
    SELECT u.user_id, u.email, COUNT(o.order_id) AS total_orders
    FROM users u LEFT JOIN orders o ON u.user_id = o.user_id GROUP BY u.user_id;
""")



print("\n1. User Order Summary (From View):")
cursor.execute("SELECT * FROM user_order_summary;")
for row in cursor.fetchall():
    print(f"  {row}")

# Transactions
print("\n2. Transactions (Rollback & Commit):")
cursor.execute("INSERT INTO accounts VALUES (1, 'Alice Acc', 5000), (2, 'Bob Acc', 3000);")
conn.commit()

# Rollback test
cursor.execute("INSERT INTO accounts VALUES (3, 'Test Acc', 1000);")
conn.rollback() # Undoes Account 3

# Money transfer test
cursor.execute("UPDATE accounts SET balance = balance - 500 WHERE account_id = 1;")
cursor.execute("UPDATE accounts SET balance = balance + 500 WHERE account_id = 2;")
conn.commit()

cursor.execute("SELECT * FROM accounts;")
for row in cursor.fetchall():
    print(f"  {row}")

conn.close()