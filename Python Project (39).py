import csv

class student_sign_in:
    
    def __init__(x):
        x.student_name = None
        x.student_number = None
    
    def welcome(x):

        print(f"Welcome To Topaz University, {x.student_name}.")

    def sign_in(x):

        x.student_name = input("Enter Student Name: ")
        if any(character.isdigit() for character in x.student_name):
            return "Your Name Should Not Contain Any Number. Sign-in Failed."

        x.student_number= int(input("Enter Student Number: "))
        if any(character.isalpha() for character in x.student_name): 
            return "Your Student Number Should Not Contain Any Letter. Sign-in Failed."

    def file(x):
        with open("Student Logbook.csv", "a", newline="") as student_file:
            w = csv.writer(student_file)
            w.writerow(["Student Name:" + "".join(x.student_name)])
            w.writerow(["Student Number:" + "".join(str(x.student_number))])
            w.writerow([])
    

student = student_sign_in()

student.sign_in()
student.file()
student.welcome()



