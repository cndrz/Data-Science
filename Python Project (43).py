import csv
from datetime import datetime

class student:

    def __init__(x):

        x.student_name = None
        x.student_number = None
        x.time = datetime.now().strftime("%H:%M:%S")
        x.date = datetime.now().strftime("%m-%d-%Y")

    def student_log(x):

        global log_file
        with open("Student_Logbook.csv", "a", newline="") as log_file:
            writer = csv.writer(log_file)
            writer.writerow([f"Student Name: {x.name}"])
            writer.writerow([f"Student Number: {x.number}"])
            writer.writerow([f"Date: {x.date}"])
            writer.writerow([f"Time In: {x.time}"])
            writer.writerow(" ")

    def student_login(x):
        while True:
            try:
                x.name = input("Enter Your Full Name: ")
                if any(character.isdigit() for character in x.name):
                    raise ValueError(
                        "Your Name Should Not Contain Any Number. Try Again."
                    )

                x.number = input("Enter Student Number: ")
                if any(num.isalpha() for num in x.number):
                    raise ValueError(
                        "Your Student Number Should Not Contain Any Letter. Try Again."
                    )

                break

            except ValueError as error:
                print(error)

class teacher:

    def __init__(x):

        x.teacher_name = None
        x.teacher_number = None
        x.time = datetime.now().strftime("%H:%M:%S")
        x.date = datetime.now().strftime("%m-%d-%Y")

    def teacher_log(x):

        global log_file
        with open("Teacher_Logbook.csv", "a", newline="") as log_file:
            writer = csv.writer(log_file)
            writer.writerow([f"Teacher Name: {x.name}"])
            writer.writerow([f"Teacher Number: {x.number}"])
            writer.writerow([f"Date: {x.date}"])
            writer.writerow([f"Time In: {x.time}"])
            writer.writerow(" ")

    def teacher_login(x):
        while True:
            try:
                x.name = input("Enter Your Full Name: ")
                if any(character.isdigit() for character in x.name):
                    raise ValueError(
                        "Your Name Should Not Contain Any Number. Try Again."
                    )

                x.number = input("Enter Teacher Number: ")
                if any(num.isalpha() for num in x.number):
                    raise ValueError(
                        "Your Teacher Number Should Not Contain Any Letter. Try Again."
                    )

                break

            except ValueError as error:
                print(error)

def logging():

    while True:

        print("1 - Student")
        print("2 - Teacher")
        answer = input("Select an option: ")

        try:
            match answer:
                case "1":
                    student_log = student()
                    student_log.student_login()
                    student_log.student_log()
                    break

                case "2":
                    teacher_log = teacher()
                    teacher_log.teacher_login()
                    teacher_log.teacher_log()
                    break

                case _:
                    raise ValueError
        except ValueError:
            print("Invalid option. Try again")

logging()
