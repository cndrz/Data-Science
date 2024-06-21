import mysql.connector

def mailing(conn):
    
    first_name = input("Enter Employee First Name: ")
    last_name = input("Enter Employee Last Name: ")
    emp_id = int(input("Enter Employee ID: "))

    cursor = conn.cursor()
    query = "SELECT * FROM employees WHERE first_name = %s AND last_name = %s AND id = %s"
    cursor.execute(query, (first_name, last_name, emp_id))
    result = cursor.fetchone()

    if result:
        print("Employee verified:", result)
    else:
        print("Employee not found.")
    cursor.close()

def delivery(conn):
    first_name = input("Enter Employee First Name: ")
    last_name = input("Enter Employee Last Name: ")
    emp_id = int(input("Enter Employee ID: "))

    cursor = conn.cursor()
    query = "SELECT * FROM employees WHERE first_name = %s AND last_name = %s AND id = %s"
    cursor.execute(query, (first_name, last_name, emp_id))
    result = cursor.fetchone()

    if result:
        print("Employee verified:", result)
    else:
        print("Employee not found.")
    cursor.close()

def css(conn):
    first_name = input("Enter Employee First Name: ")
    last_name = input("Enter Employee Last Name: ")
    emp_id = int(input("Enter Employee ID: "))

    cursor = conn.cursor()
    query = "SELECT * FROM employees WHERE first_name = %s AND last_name = %s AND id = %s"
    cursor.execute(query, (first_name, last_name, emp_id))
    result = cursor.fetchone()

    if result:
        print("Employee verified:", result)
    else:
        print("Employee not found.")
    cursor.close()
