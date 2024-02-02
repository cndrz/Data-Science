import os
import csv
class logbook:

    def __init__(x):

        x.name = None
        x.number = None
        x.time = None

    def Employee_log(x):
        global log_file
        with open("Employee Logbook.csv", "a", newline = "") as log_file:
            writer = csv.writer(log_file)
            writer.writerow([f"Employee Name: {x.name}"])
            writer.writerow([f"Employee Number: {x.number}"])
            writer.writerow([f"Time In: {x.time}"])


    def login(x):
        x.name = input("Enter Employee Name: ")
        if any(character.isdigit() for character in x.name):
            return "Your Name Should Not Contain Any Number. Try Again."

        x.number = input("Enter Employee Number: ")
        if any(num.isalpha() for num in x.number):
            return "Your Employee Number Should Not Contain Any Letter. Try Again."
        

log = logbook()
log.login()
log.Employee_log()
