import os
import csv
from datetime import datetime
class logbook:

    def __init__(x):
    
        x.name = None
        x.number = None
        x.time = datetime.now().strftime("%H:%M:%S")
        x.date = datetime.now().strftime("%m-%d-%Y")

    def Employee_log(x):
        global log_file
        with open("Employee Logbook.csv", "a", newline = "") as log_file:
            writer = csv.writer(log_file)
            writer.writerow([f"Employee Name: {x.name}"])
            writer.writerow([f"Employee Number: {x.number}"])
            writer.writerow([f"Date: {x.date}"])
            writer.writerow([f"Time In: {x.time}"])
            writer.writerow(" ")


    def login(x):
        while True:
            try:
                x.name = input("Enter Employee Name: ")
                if any(character.isdigit() for character in x.name):
                    raise ValueError("Your Name Should Not Contain Any Number. Try Again.")

                x.number = input("Enter Employee Number: ")
                if any(num.isalpha() for num in x.number):
                    raise ValueError("Your Employee Number Should Not Contain Any Letter. Try Again.")

                break

            except ValueError as error:
                print(error)
        

log = logbook()
log.login()
log.Employee_log()
