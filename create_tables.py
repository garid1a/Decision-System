import sqlite3

# Step 1: Connect to the SQLite database (or create one if it doesn't exist)
connection = sqlite3.connect("data/consumer_data.db")

# Step 2: Create a cursor object to execute SQL statements
cursor = connection.cursor()

# Step 3: Define SQL statements to create tables
create_consumer_table_sql = """
CREATE TABLE IF NOT EXISTS consumers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    product_preference TEXT,
    purchase_month TEXT
)
"""

create_farmer_table_sql = """
CREATE TABLE IF NOT EXISTS farmers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    recommendation TEXT,
    climate TEXT,
    soil_conditions TEXT
)
"""

# Step 4: Execute the SQL statements to create tables
cursor.execute(create_consumer_table_sql)
cursor.execute(create_farmer_table_sql)

# Step 5: Commit the changes to the database
connection.commit()

# Step 6: Close the database connection
connection.close()

print("Database tables created successfully.")
