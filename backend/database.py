import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("data/consumer_data.db")
        self.cursor = self.conn.cursor()

    def execute_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()
