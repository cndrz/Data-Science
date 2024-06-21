import importlib
import mysql.connector

def create_db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="02200000329_DelaCruz",
            database="XXX"
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def handle_section(function_name, conn):
    try:
        module = importlib.import_module("FUNCTIONS")
        function = getattr(module, function_name)
        function(conn)
    except ImportError:
        print("Error: The FUNCTIONS.py file could not be found.")
    except AttributeError:
        print(f"Error: The FUNCTIONS.py file does not contain a function named '{function_name}'.")

def display_menu():
    print("Welcome To XXX Mailing Company")
    print("Select Your Designated Section")
    print("A. Mail Sorting Sect.")
    print("B. Delivery Sect.")
    print("C. Customer Service Sect.")

def select_section():
    display_menu()
    conn = create_db_connection()
    if conn is None:
        print("Failed to connect to the database. Exiting...")
        return

    while True:
        user_input = input("--> ").upper()
        if user_input in ['A', 'B', 'C']:
            break
        else:
            print("Invalid selection. Please choose A, B, or C.")

    if user_input == "A":
        handle_section("mailing", conn)
    elif user_input == "B":
        handle_section("delivery", conn)
    elif user_input == "C":
        handle_section("css", conn)
    
    conn.close()

if __name__ == "__main__":
    select_section()
