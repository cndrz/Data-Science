import mysql.connector

def mailing(conn):
    
    first_name = input("Enter Employee First Name: ")
    last_name = input("Enter Employee Last Name: ")
    emp_id = int(input("Enter Employee ID: "))

    cursor = conn.cursor()
    query = "SELECT * FROM mailing_emp WHERE emp_firstname = %s AND emp_lastname = %s AND emp_id = %s"
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
    query = "SELECT * FROM delivery_emp WHERE emp_firstname = %s AND emp_lastname = %s AND emp_id = %s"
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
    query = "SELECT * FROM css_emp WHERE emp_firstname = %s AND emp_lastname = %s AND emp_id = %s"
    cursor.execute(query, (first_name, last_name, emp_id))
    result = cursor.fetchone()

    if result:
        print("Employee verified:", result)
    else:
        print("Employee not found.")
    cursor.close()
