# student log in 
import csv

def students_list():

    students_data = [
        ["Student First Name", "Student Last Name", "Student Number"],
        ["John", "Mendez", "00001"],
        ["Joseph", "Carlos", "00002"],
        ["Bobby", "Makali", "00003"]
        ]

    file_path = r"C:\Users\admin\Desktop\Python\School Library Login System\students.csv"

    with open(file_path, "w", newline="") as students_file:
        csvwriter = csv.writer(students_file)
        csvwriter.writerows(students_data)
        print("Students list is created successfully.")


students_list()
