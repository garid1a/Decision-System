import mysql.connector

def create_db_connection():
    try:
        # Replace the following with your actual database credentials
        conn = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='password',
            database='FarmData'
        )
        print("Database connection established successfully.")
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
