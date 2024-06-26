import mysql.connector
from mysql.connector import Error

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='fullname',
            user='root',
            password='---'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def insert_name(connection, first_name, last_name):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO fullname (first_name, last_name) VALUES (%s, %s)"
        cursor.execute(query, (first_name, last_name))
        connection.commit()
        print("Name successfully inserted into the database.")
    except Error as e:
        print(f"Failed to insert name into database: {e}")

def fullname():
    connection = connect_to_database()
    if not connection:
        print("Failed to connect to the database.")
        return

    while True:
        while True:
            first_name = input("Enter First Name: ").strip()
            if first_name and all(part.isalpha() for part in first_name.split()):
                first_name = ' '.join(part.capitalize() for part in first_name.split())
                break
            else:
                print("Invalid input. Please enter alphabetic characters only and ensure it is not empty or just spaces.")

        while True:
            last_name = input("Enter Last Name: ").strip()
            if last_name and all(part.isalpha() for part in last_name.split()):
                last_name = ' '.join(part.capitalize() for part in last_name.split())
                break
            else:
                print("Invalid input. Please enter alphabetic characters only and ensure it is not empty or just spaces.")

        print(f"Full Name: {first_name} {last_name}")

        insert_name(connection, first_name, last_name)

        while True:
            again = input("Do you want to enter another name? (yes/no): ").strip().lower()
            if again == 'yes' or again == 'no':
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        if again != 'yes':
            break

    connection.close()

fullname()
