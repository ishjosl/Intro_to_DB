import mysql.connector

def create_database():
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'password12'

    )

    if connection.is_connected():
        cursor = connection.cursor

        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
        
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")

    else:
        print("Failed to connect to MySQL server.")

    create_database()