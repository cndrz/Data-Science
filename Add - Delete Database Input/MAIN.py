import mysql.connector
from mysql.connector import Error

def insert_input(input_type, input_value):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='number_letter',
            user='root ',
            password='---'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            insert_query = """INSERT INTO user_inputs (input_type, input_value) VALUES (%s, %s)"""
            cursor.execute(insert_query, (input_type, input_value))
            connection.commit()
            print("Input successfully inserted into the database.")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def question():
    while True:
        print("A = Numerical Input")
        print("B = Alphabetical Input")

        choice = input("Please enter your choice (A or B): ").strip().upper()

        if choice == 'A':
            while True:
                try:
                    numerical = input("Enter The Numerical Value: ").strip()
                    if numerical == "":
                        raise ValueError
                    numerical = int(numerical)
                    print(f"You entered the numerical value: {numerical}")
                    insert_input('Numerical', numerical)
                    break
                except ValueError:
                    print("Only enter numerical values (e.g - 250, 1, 00). Whitespace is not allowed.")
        
        elif choice == 'B':
            while True:
                alphabetical = input("Enter the Alphabetical Value: ").strip()
                if alphabetical.isalpha() and alphabetical != "":
                    print(f"You entered the alphabetical value: {alphabetical}")
                    insert_input('Alphabetical', alphabetical)
                    break
                else:
                    print("Only enter alphabetical values (e.g - abc, XYZ). Whitespace is not allowed.")
        
        else:
            print("Invalid input. Please enter 'A' or 'B'.")
            continue

        while True:
            repeat = input("Do you want to enter another input? (yes or no): ").strip().lower()
            if repeat in ['yes', 'no']:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        if repeat == 'no':
            break

question()
