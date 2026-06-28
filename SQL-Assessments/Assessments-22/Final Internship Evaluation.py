
# 🎯 Task

# Design database for Mess Management System

# Create:

# Tables

# Relationships

# Sample data

# Write 15 business queries

# Optimize at least 3 queries



import sqlite3
import random
from datetime import datetime, timedelta

# Connect to in-memory database
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Enable foreign keys
cursor.execute("PRAGMA foreign_keys = ON;")

print("=== SETTING UP MESS MANAGEMENT SYSTEM ===")

# ==========================================
# 1. CREATE TABLES & RELATIONSHIPS
# ==========================================
cursor.executescript("""
    CREATE TABLE students (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        room_number TEXT,
        balance REAL DEFAULT 0.00
    );

    CREATE TABLE menu (
        item_id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT,
        meal_type TEXT,
        price REAL,
        calories INTEGER
    );

    CREATE TABLE daily_meals (
        meal_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        item_id INTEGER,
        consumption_date DATE,
        quantity INTEGER,
        FOREIGN KEY (student_id) REFERENCES students(student_id),
        FOREIGN KEY (item_id) REFERENCES menu(item_id)
    );

    CREATE TABLE payments (
        payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        amount REAL,
        payment_date DATE,
        payment_method TEXT,
        FOREIGN KEY (student_id) REFERENCES students(student_id)
    );
""")

print("Tables and relationships created successfully.")

# ==========================================
# 2. GENERATE "BIG" SAMPLE DATA
# ==========================================
print("Generating bulk data (100 Students, 5000+ Meals, 200+ Payments)...")

# Insert Menu
menu_items = [
    ('Poha', 'Breakfast', 30.0, 250), ('Idli Sambar', 'Breakfast', 40.0, 300), 
    ('Aloo Paratha', 'Breakfast', 50.0, 400), ('Omelette', 'Breakfast', 35.0, 200),
    ('Veg Thali', 'Lunch', 80.0, 700), ('Chicken Thali', 'Lunch', 120.0, 900),
    ('Paneer Rice', 'Lunch', 90.0, 800), ('Dal Khichdi', 'Dinner', 60.0, 500),
    ('Roti Sabzi', 'Dinner', 70.0, 600), ('Egg Curry', 'Dinner', 90.0, 750)
]
cursor.executemany("INSERT INTO menu (item_name, meal_type, price, calories) VALUES (?, ?, ?, ?)", menu_items)

# Generate 100 Students
students_data = []
for i in range(1, 101):
    name = f"Student_{i}"
    room = f"Block_{random.choice(['A', 'B', 'C'])}-{random.randint(100, 400)}"
    balance = round(random.uniform(-500, 2000), 2) # Some owe money, some have surplus
    students_data.append((name, room, balance))
cursor.executemany("INSERT INTO students (name, room_number, balance) VALUES (?, ?, ?)", students_data)

# Generate 5,000+ Meal Records over the last 30 days
start_date = datetime.now() - timedelta(days=30)
meals_data = []
for _ in range(5500):
    student_id = random.randint(1, 100)
    item_id = random.randint(1, 10)
    days_offset = random.randint(0, 30)
    c_date = (start_date + timedelta(days=days_offset)).strftime('%Y-%m-%d')
    qty = random.randint(1, 2)
    meals_data.append((student_id, item_id, c_date, qty))
cursor.executemany("INSERT INTO daily_meals (student_id, item_id, consumption_date, quantity) VALUES (?, ?, ?, ?)", meals_data)

# Generate 250 Payments
payment_methods = ['UPI', 'Cash', 'Card', 'NetBanking']
payments_data = []
for _ in range(250):
    student_id = random.randint(1, 100)
    amount = round(random.uniform(500, 3000), 2)
    days_offset = random.randint(0, 30)
    p_date = (start_date + timedelta(days=days_offset)).strftime('%Y-%m-%d')
    method = random.choice(payment_methods)
    payments_data.append((student_id, amount, p_date, method))
cursor.executemany("INSERT INTO payments (student_id, amount, payment_date, payment_method) VALUES (?, ?, ?, ?)", payments_data)

conn.commit()
print("Data generation complete!\n")

# ==========================================
# 3. 15 BUSINESS QUERIES
# ==========================================
print("=== EXECUTING 15 BUSINESS QUERIES ===")

def run_query(title, query):
    print(f"\n{title}")
    cursor.execute(query)
    # Fetch first 5 to keep terminal clean
    rows = cursor.fetchall()
    for row in rows[:5]:
        print(f"  {row}")
    if len(rows) > 5:
        print(f"  ... ({len(rows) - 5} more rows)")

# Q1: Students with negative balance (Defaulters)
run_query("Q1: Top 5 Defaulters (Negative Balance)", 
          "SELECT name, balance FROM students WHERE balance < 0 ORDER BY balance ASC LIMIT 5;")

# Q2: Total revenue from payments
run_query("Q2: Total Revenue Collected", 
          "SELECT SUM(amount) AS total_revenue FROM payments;")

# Q3: Most popular food item overall
run_query("Q3: Most Popular Menu Item", 
          """SELECT m.item_name, SUM(d.quantity) AS total_ordered 
             FROM menu m JOIN daily_meals d ON m.item_id = d.item_id 
             GROUP BY m.item_id ORDER BY total_ordered DESC LIMIT 1;""")

# Q4: Most popular breakfast item
run_query("Q4: Most Popular Breakfast Item", 
          """SELECT m.item_name, SUM(d.quantity) AS total 
             FROM menu m JOIN daily_meals d ON m.item_id = d.item_id 
             WHERE m.meal_type = 'Breakfast' 
             GROUP BY m.item_id ORDER BY total DESC LIMIT 1;""")

# Q5: Total meals consumed by Student 1
run_query("Q5: Total Meals consumed by Student 1", 
          "SELECT SUM(quantity) FROM daily_meals WHERE student_id = 1;")

# Q6: Average price of meals by meal type
run_query("Q6: Average Price by Meal Type", 
          "SELECT meal_type, ROUND(AVG(price), 2) FROM menu GROUP BY meal_type;")

# Q7: Students who ate Veg Thali today (simulated as the most recent day)
run_query("Q7: Students who ordered 'Veg Thali'", 
          """SELECT DISTINCT s.name FROM students s 
             JOIN daily_meals d ON s.student_id = d.student_id 
             JOIN menu m ON d.item_id = m.item_id 
             WHERE m.item_name = 'Veg Thali';""")

# Q8: Revenue breakdown by payment method
run_query("Q8: Revenue by Payment Method", 
          "SELECT payment_method, ROUND(SUM(amount), 2) FROM payments GROUP BY payment_method;")

# Q9: Busiest day in the mess (Highest meals served)
run_query("Q9: Busiest Day in the Mess", 
          """SELECT consumption_date, SUM(quantity) AS meals_served 
             FROM daily_meals GROUP BY consumption_date ORDER BY meals_served DESC LIMIT 1;""")

# Q10: Highest single payment made
run_query("Q10: Highest Single Payment", 
          "SELECT s.name, p.amount, p.payment_date FROM payments p JOIN students s ON p.student_id = s.student_id ORDER BY p.amount DESC LIMIT 1;")

# Q11: Total calories consumed by Student 5 overall
run_query("Q11: Total Calories Consumed by Student 5", 
          """SELECT s.name, SUM(m.calories * d.quantity) AS total_calories 
             FROM daily_meals d 
             JOIN menu m ON d.item_id = m.item_id 
             JOIN students s ON d.student_id = s.student_id
             WHERE s.student_id = 5;""")

# Q12: Number of students in Block A
run_query("Q12: Number of Students in Block A", 
          "SELECT COUNT(*) FROM students WHERE room_number LIKE 'Block_A%';")

# Q13: Total amount spent by all students on 'Chicken Thali'
run_query("Q13: Total Revenue from Chicken Thali", 
          """SELECT SUM(m.price * d.quantity) 
             FROM daily_meals d JOIN menu m ON d.item_id = m.item_id 
             WHERE m.item_name = 'Chicken Thali';""")

# Q14: Average payment amount
run_query("Q14: Average Payment Amount", 
          "SELECT ROUND(AVG(amount), 2) FROM payments;")

# Q15: Top 3 Students with highest total consumption value (The biggest eaters)
run_query("Q15: Top 3 Biggest Eaters (By Value)", 
          """SELECT s.name, SUM(m.price * d.quantity) AS total_value_eaten 
             FROM daily_meals d 
             JOIN menu m ON d.item_id = m.item_id 
             JOIN students s ON d.student_id = s.student_id 
             GROUP BY s.student_id ORDER BY total_value_eaten DESC LIMIT 3;""")


# ==========================================
# 4. OPTIMIZE 3 QUERIES
# ==========================================
print("\n=== QUERY OPTIMIZATION ===")

# Explain a query BEFORE optimization (Full table scan on dates)
print("\n[Before Optimization] Searching for meals on a specific date:")
cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM daily_meals WHERE consumption_date = '2023-11-01';")
for row in cursor.fetchall(): print(f"  {row}")

# Applying Optimizations (Indexes)
print("\nApplying 3 Optimizations (Creating Indexes)...")
cursor.executescript("""
    -- Optimization 1: Index on consumption dates (Heavily queried for reports)
    CREATE INDEX idx_daily_meals_date ON daily_meals(consumption_date);
    
    -- Optimization 2: Index on menu meal types (Breakfast, Lunch, Dinner filtering)
    CREATE INDEX idx_menu_type ON menu(meal_type);
    
    -- Optimization 3: Composite index on payments for student lookups ordered by date
    CREATE INDEX idx_payments_student_date ON payments(student_id, payment_date);
""")
print("Indexes created successfully.")

# Explain the SAME query AFTER optimization (Uses the index)
print("\n[After Optimization] Searching for meals on a specific date:")
cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM daily_meals WHERE consumption_date = '2023-11-01';")
for row in cursor.fetchall(): print(f"  {row}")

conn.close()