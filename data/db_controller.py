import mysql.connector
import os
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import ast

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
        INSERT INTO Consumer (Name, Age, Location, UserName, Password)
        VALUES (%(Name)s, %(Age)s, %(Location)s, %(UserName)s, %(Password)s)
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
        INSERT INTO Farmer (Name, Location, SoilType, UserName, Password)
        VALUES (%(Name)s, %(Location)s, %(SoilType)s,  %(UserName)s,  %(Password)s)
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
def insert_preference(connection, selected_month_year, consumerID, products, selected_products):
    cursor = connection.cursor()
    # Insert data into the Preference table
    insert_preference_query = "INSERT INTO Preference (ConsumerID, Month) VALUES (%s, %s)"
    cursor.execute(insert_preference_query, (consumerID, selected_month_year))  # Replace 1 with the actual ConsumerID

    # Get the PreferenceID of the inserted preference
    preference_id = cursor.lastrowid
    print(preference_id,'Preference ID')

    # Insert data into the ProductPreference table for each selected product
    insert_product_preference_query = "INSERT INTO ProductPreference (ProductID, PreferenceID) VALUES (%s, %s)"
    for product in products:
        if product['ProductName'] in selected_products:
            # Replace 'get_product_id' with a function that retrieves the ProductID based on the product name
            product_id = get_product_id(cursor, product['ProductName'])
            print(product_id, 'PRODUCT ID')
            cursor.execute(insert_product_preference_query, (product_id, preference_id))

    # Commit the changes to the database
    connection.commit()

def get_product_id(cursor, product_name):
    query = "SELECT ProductID FROM Product WHERE ProductName = %s"
    cursor.execute(query, (product_name,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        # Handle the case where the product is not found (return None or raise an exception)
        return None

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
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Product")
        products = cursor.fetchall()

        for product in products:
            # Process or print each product if needed
            print(product)

        cursor.close()
        return products
    except Exception as e:
        print(f"Error: {str(e)}")
        return [{'ProductID':1, 'ProductName': "Rice"}, {'ProductID':2,'ProductName':"Wheat"}, {'ProductID':3,'ProductName':"Maize"}, {'ProductID':4,'ProductName':"Sugarcane"}, {'ProductID':5,'ProductName':"Cotton"}, {'ProductID':6,'ProductName':"Soybeans"}, {'ProductID':7,'ProductName':"Groundnuts"}, {'ProductID':8,'ProductName':"Tea"}, {'ProductID':9,'ProductName':"Jute"}, {'ProductID':10,'ProductName':"Rubber"}]

def get_product_preferences_count(connection):
    cursor = connection.cursor()

    # Query to get the product names and their preference count
    query = """
        SELECT Product.ProductName, COUNT(ProductPreference.PreferenceID) as PreferenceCount
        FROM Product
        LEFT JOIN ProductPreference ON Product.ProductID = ProductPreference.ProductID
        LEFT JOIN Preference ON ProductPreference.PreferenceID = Preference.PreferenceID
        GROUP BY Product.ProductID
    """

    try:
        cursor.execute(query)
        result = cursor.fetchall()

        # Convert the result to a list of dictionaries for easy access
        product_preferences = [{"ProductName": row[0], "PreferenceCount": row[1]} for row in result]
        print(product_preferences)
        return product_preferences

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
    
def get_top_product_preferences(connection, limit=5):
    cursor = connection.cursor()

    # Query to get the top 5 product names and their preference count
    query = """
        SELECT Product.ProductName, COUNT(ProductPreference.PreferenceID) as PreferenceCount
        FROM Product
        LEFT JOIN ProductPreference ON Product.ProductID = ProductPreference.ProductID
        LEFT JOIN Preference ON ProductPreference.PreferenceID = Preference.PreferenceID
        GROUP BY Product.ProductID
        ORDER BY PreferenceCount DESC
        LIMIT %s
    """

    try:
        cursor.execute(query, (limit,))
        result = cursor.fetchall()

        # Convert the result to a list of dictionaries for easy access
        product_preferences = [{"ProductName": row[0], "PreferenceCount": row[1]} for row in result]
        print(product_preferences)
        return product_preferences

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []

def get_preference_count_by_month(connection):
    cursor = connection.cursor(dictionary=True)

    # Query to get the preference count for each month
    query = """
        SELECT 
            Preference.Month,
            COUNT(ProductPreference.PreferenceID) as PreferenceCount
        FROM 
            Preference
        LEFT JOIN 
            ProductPreference ON Preference.PreferenceID = ProductPreference.PreferenceID
        GROUP BY 
            Preference.Month
        ORDER BY 
            PreferenceCount DESC
    """

    try:
        cursor.execute(query)
        result = cursor.fetchall()

        # Convert the result to a list of dictionaries for easy access
        monthly_preference_count = [{"Month": ast.literal_eval(row['Month'])[0], "PreferenceCount": row['PreferenceCount']} for row in result]
        print(monthly_preference_count)
        return monthly_preference_count

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
    

def generate_product_preference_report(connection):
    cursor = connection.cursor(dictionary=True)

    # Query to get product preferences along with other details
    query = """
                SELECT 
            Product.ProductName, 
            COUNT(ProductPreference.PreferenceID) as PreferenceCount,
            Consumer.Location,
            Preference.Month,
            Product.Season,
            Product.SoilType
        FROM Product
        LEFT JOIN ProductPreference ON Product.ProductID = ProductPreference.ProductID
        LEFT JOIN Preference ON ProductPreference.PreferenceID = Preference.PreferenceID
        LEFT JOIN Consumer ON Preference.ConsumerID = Consumer.ConsumerID
        GROUP BY Product.ProductID, Consumer.Location, Preference.Month, Product.Season, Product.SoilType;

    """

    try:
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        pdf_filename = "consumer_report.pdf" 
        document = SimpleDocTemplate(pdf_filename)

        # Creating the title
        title = Paragraph("Consumer Preference Report", getSampleStyleSheet()['Title'])
        
        # Extracting data for the table
        data = [['Product', 'Preference Count', 'Location', 'Month', 'Soil Type', 'Season']]
        for entry in result:
            data.append([
                entry['ProductName'],
                str(entry['PreferenceCount']),
                entry['Location'],
                entry['Month'],
                entry['SoilType'],
                entry['Season']
            ])

        # Creating the table
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))

        # Build the PDF document
        document.build([title, table])

        print(f"Report generated and saved as {pdf_filename}")
        


    except mysql.connector.Error as err:
        print(f"Error: {err}")
def generate_product_report(connection):
    cursor = connection.cursor(dictionary=True)

    # Query to get product preferences along with other details
    query = """
                SELECT 
                    Product.ProductName, 
                    COUNT(ProductPreference.PreferenceID) as PreferenceCount
                FROM Product
                LEFT JOIN ProductPreference ON Product.ProductID = ProductPreference.ProductID
                GROUP BY Product.ProductID;
            """

    try:
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        pdf_filename = "product_report.pdf" 
        document = SimpleDocTemplate(pdf_filename)

        # Extracting data for the table
        data = [['Product', 'Preference Count']]
        for entry in result:
            data.append([
                entry['ProductName'],
                str(entry['PreferenceCount']),
            ])

        # Creating the title
        title = Paragraph("Product Report", getSampleStyleSheet()['Title'])

        # Creating the table
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))

        # Build the PDF document
        document.build([title, table])

        print(f"Product report generated and saved as {pdf_filename}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
def generate_product_preference_report_by_location(connection):
    cursor = connection.cursor(dictionary=True)

    # Query to get product preferences along with other details
    query = """
        SELECT 
            Product.ProductName, 
            COUNT(ProductPreference.PreferenceID) as PreferenceCount,
            Consumer.Location,
            Preference.Month
        FROM Product
        LEFT JOIN ProductPreference ON Product.ProductID = ProductPreference.ProductID
        LEFT JOIN Preference ON ProductPreference.PreferenceID = Preference.PreferenceID
        LEFT JOIN Consumer ON Preference.ConsumerID = Consumer.ConsumerID
        GROUP BY Product.ProductID, Consumer.Location, Preference.Month;
    """

    try:
        cursor.execute(query)
        result = cursor.fetchall()

        pdf_filename = "Location_preference_report.pdf" 
        document = SimpleDocTemplate(pdf_filename)

        # Creating the title
        title = Paragraph("Product Preference Report for Farmers - Location", getSampleStyleSheet()['Title'])
        
        # Extracting data for the table
        data = [['Product', 'Preference Count', 'Location', 'Month']]
        current_location = None  # To track the current location while iterating through result
        for entry in result:
            if entry['Location'] != current_location:
                data.append(['', '', entry['Location'], ''])  # Add a row for the location
                current_location = entry['Location']
            data.append([
                entry['ProductName'],
                str(entry['PreferenceCount']),
                '',
                entry['Month']
            ])

        # Creating the table
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))

        # Build the PDF document
        document.build([title, table])

        print(f"Report generated and saved as {pdf_filename}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
def generate_product_preference_report_by_product(connection):
    cursor = connection.cursor(dictionary=True)

    # Query to get product preferences along with other details
    query = """
        SELECT 
            Product.ProductName, 
            Preference.Month,
            COUNT(ProductPreference.PreferenceID) as PreferenceCount
        FROM Product
        LEFT JOIN ProductPreference ON Product.ProductID = ProductPreference.ProductID
        LEFT JOIN Preference ON ProductPreference.PreferenceID = Preference.PreferenceID
        GROUP BY Product.ProductID, Preference.Month;
    """

    try:
        cursor.execute(query)
        result = cursor.fetchall()

        pdf_filename = "product_preference_report_by_product.pdf" 
        document = SimpleDocTemplate(pdf_filename)

        # Creating the title
        title = Paragraph("Product Preference Report for Farmers - Crop", getSampleStyleSheet()['Title'])
        
        # Extracting data for the table
        data = [['Product', 'Month', 'Preference Count']]
        current_product = None  # To track the current product while iterating through result
        for entry in result:
            if entry['ProductName'] != current_product:
                data.append([entry['ProductName'], '', ''])  # Add a row for the product
                current_product = entry['ProductName']
            data.append([
                '',
                entry['Month'],
                str(entry['PreferenceCount'])
            ])

        # Creating the table
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))

        # Build the PDF document
        document.build([title, table])

        print(f"Report generated and saved as {pdf_filename}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
def generate_product_preference_report_by_month(connection):
    cursor = connection.cursor(dictionary=True)

        # Query to get product preferences along with other details
    query = """
            SELECT 
                Product.ProductName, 
                COUNT(ProductPreference.PreferenceID) as PreferenceCount,
                Preference.Month
            FROM Product
            LEFT JOIN ProductPreference ON Product.ProductID = ProductPreference.ProductID
            LEFT JOIN Preference ON ProductPreference.PreferenceID = Preference.PreferenceID
            GROUP BY Product.ProductID, Preference.Month;
        """

    try:
        cursor.execute(query)
        result = cursor.fetchall()

        pdf_filename = "Monthly_product_preference_report.pdf" 
        document = SimpleDocTemplate(pdf_filename)

        # Creating the title
        title = Paragraph("Product Preference Report for Farmers - Monthly", getSampleStyleSheet()['Title'])
        
        # Extracting data for the table
        data = [['Product', 'Preference Count']]

        # Creating a dictionary to store preference count for each month
        month_preference_count = {}

        for entry in result:
            month = entry['Month']
            if month not in month_preference_count:
                month_preference_count[month] = []
            month_preference_count[month].append([entry['ProductName'], str(entry['PreferenceCount'])])

        # Adding the data to the table
        for month, preferences in month_preference_count.items():
            data.append([month, ''])  # Add a row for the month
            data.extend(preferences)

        # Creating the table
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))

        # Build the PDF document
        document.build([title, table])

        print(f"Report generated and saved as {pdf_filename}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")