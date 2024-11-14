import mysql.connector

def create_database():
    # Establish the connection to MySQL server
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='password12'
    )

    # Check if the connection is successful
    if connection.is_connected():
        cursor = connection.cursor()

        # Create the database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

        # Close the cursor and connection
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")
    else:
        print("Failed to connect to MySQL server.")

# Call the function to create the database
create_database()
