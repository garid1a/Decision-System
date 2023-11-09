import mysql.connector
 
# Insert a new Consumer into the database
def insert_consumer(connection, consumer):
    """
    Insert a new consumer into the database.

    Args:
    - db_connection: The database connection.
    - consumer: A dictionary containing the consumer's data.

    Returns:
    - consumer_id: The ID of the newly inserted consumer, or None if the insertion fails.
    """
    try:
        cursor = connection.cursor(dictionary=True)
        insert_query = """
        INSERT INTO Consumer (Name, Age, Location)
        VALUES (%(Name)s, %(Age)s, %(Location)s)
        """
        cursor.execute(insert_query, consumer)
        connection.commit()
        consumer_id = cursor.lastrowid
        cursor.close()
        return consumer_id
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Select a Consumer by Username and Password
def login_consumer(connection, username, password):
    cursor = connection.cursor()
    select_query = "SELECT ConsumerID, Name, Age, Location FROM Consumer WHERE UserName = %s AND Password = %s"
    login_data = (username, password)
    
    try:
        cursor.execute(select_query, login_data)
        consumer = cursor.fetchone()
        if consumer:
            print("Login successful")
            consumer_id, name, age, location = consumer
            return {"ConsumerID": consumer_id, "Name": name, "Age": age, "Location": location}
        else:
            print("Login failed: Invalid username or password")
            return None
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Insert a new Farmer into the database
def insert_farmer(connection, farmer): 
    try:
        cursor = connection.cursor(dictionary=True)
        insert_query = """
        INSERT INTO Farmer (Name, Location, SoilType)
        VALUES (%(Name)s, %(Location)s, %(SoilType)s)
        """
        cursor.execute(insert_query, farmer)
        connection.commit()
        print("Farmer inserted successfully")
        farmer_id = cursor.lastrowid
        cursor.close()
        return farmer_id
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def login_farmer(connection, username, password):
    cursor = connection.cursor()
    select_query = "SELECT FarmerID, Name, Location FROM Farmer WHERE UserName = %s AND Password = %s"
    login_data = (username, password)
    
    try:
        cursor.execute(select_query, login_data)
        farmer = cursor.fetchone()
        if farmer:
            print("Login successful")
            farmer_id, name, location = farmer
            return {"FarmerID": farmer_id, "Name": name, "Location": location}
        else:
            print("Login failed: Invalid username or password")
            return None
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Insert a new Preference into the database
def insert_preference(connection, preference):
    cursor = connection.cursor()
    insert_query = "INSERT INTO Preference (ConsumerID, ProductID, Month) VALUES (%s, %s, %s)"
    preference_data = (preference.consumer_id, preference.product_id, preference.month)
    
    try:
        cursor.execute(insert_query, preference_data)
        connection.commit()
        print("Preference inserted successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Insert a new Product into the database
def insert_product(connection, product):
    cursor = connection.cursor()
    insert_query = "INSERT INTO Product (ProductName, Season, SoilType) VALUES (%s, %s, %s)"
    product_data = (product.product_name, product.season, product.soil_type)
    
    try:
        cursor.execute(insert_query, product_data)
        connection.commit()
        print("Product inserted successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def select_consumer_by_id(connection, consumer_id):
    cursor = connection.cursor(dictionary=True)
    select_query = "SELECT * FROM Consumer WHERE ConsumerID = %s"
    data = (consumer_id,)

    try:
        cursor.execute(select_query, data)
        consumer = cursor.fetchone()
        return consumer
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        cursor.close()

def update_consumer(connection, consumer_id, new_name, new_age, new_location):
    cursor = connection.cursor()
    update_query = "UPDATE Consumer SET Name = %s, Age = %s, Location = %s WHERE ConsumerID = %s"
    data = (new_name, new_age, new_location, consumer_id)

    try:
        cursor.execute(update_query, data)
        connection.commit()
        print("Consumer updated successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def delete_consumer(connection, consumer_id):
    cursor = connection.cursor()
    delete_query = "DELETE FROM Consumer WHERE ConsumerID = %s"
    data = (consumer_id,)

    try:
        cursor.execute(delete_query, data)
        connection.commit()
        print("Consumer deleted successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def get_preferences_by_location(connection, location):
    cursor = connection.cursor()
    select_query = "SELECT * FROM Preference p JOIN Consumer c ON p.ConsumerID = c.ConsumerID WHERE c.Location = %s"
    
    try:
        cursor.execute(select_query, (location,))
        preferences = cursor.fetchall()
        return preferences
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []

def get_preferences_by_age(connection, age):
    cursor = connection.cursor()
    select_query = "SELECT * FROM Preference p JOIN Consumer c ON p.ConsumerID = c.ConsumerID WHERE c.Age = %s"
    
    try:
        cursor.execute(select_query, (age,))
        preferences = cursor.fetchall()
        return preferences
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []

def get_preferences_by_month(connection, month):
    cursor = connection.cursor()
    select_query = "SELECT * FROM Preference WHERE Month = %s"
    
    try:
        cursor.execute(select_query, (month,))
        preferences = cursor.fetchall()
        return preferences
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
    
def get_preferences_by_consumer(connection, consumer_id):
    cursor = connection.cursor()
    select_query = "SELECT * FROM Preference WHERE ConsumerID = %s"
    
    try:
        cursor.execute(select_query, (consumer_id,))
        preferences = cursor.fetchall()
        return preferences
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
    
def add_product(connection, product):
    cursor = connection.cursor()
    insert_query = "INSERT INTO Product (ProductName, Season, SoilType) VALUES (%s, %s, %s)"
    product_data = (product.product_name, product.season, product.soil_type)
    
    try:
        cursor.execute(insert_query, product_data)
        connection.commit()
        print("Product added successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def delete_product(connection, product_id):
    cursor = connection.cursor()
    delete_query = "DELETE FROM Product WHERE ProductID = %s"
    
    try:
        cursor.execute(delete_query, (product_id,))
        connection.commit()
        print("Product deleted successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def update_product(connection, product):
    cursor = connection.cursor()
    update_query = "UPDATE Product SET ProductName = %s, Season = %s, SoilType = %s WHERE ProductID = %s"
    product_data = (product.product_name, product.season, product.soil_type, product.product_id)
    
    try:
        cursor.execute(update_query, product_data)
        connection.commit()
        print("Product updated successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def get_all_products(connection):
    try:
        cursor = connection.cursor(dictionary=True)  # Use a dictionary cursor for easier data access
        cursor.execute("SELECT * FROM Product")
        products = cursor.fetchall()
        cursor.close()  # Close the cursor

        return products
    except Exception as e:
        print(f"Error: {str(e)}")
        return []