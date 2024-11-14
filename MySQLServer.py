import mysql.connector

def create_database():
    try:
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
    
    except mysql.connector.Error as e:
        # Handle any errors related to MySQL connection or query execution
        print(f"Error: {e}")
    
    except Exception as e:
        # Handle any other unforeseen errors
        print(f"An unexpected error occurred: {e}")
    create_database()