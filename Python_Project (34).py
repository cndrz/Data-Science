import csv
class account:

    
    def __init__(x):

        x.name = None
        x.email = None
        x.password = None
    
    def file(x):
        with open("Account Details.csv", "a", newline = "") as account_file:
            writer = csv.writer(account_file)
            writer.writerow([f"Account Name: {x.name}"])
            writer.writerow([f"Account Email: {x.email}"])
            writer.writerow([f"Account Password: {x.password}"])

    def sign_up(x):

        x.name = input("Enter Name: ")
        if any(character.isdigit() for character in x.name):
            return "Your Name Should Not Contain Any Number. Sign-up Failed."

        x.email = input("Enter Email: ")
        if "@" not in x.email or "." not in x.email:
            return "Invalid Email Format. Sign-up Failed."

        x.password = input("Enter Password: ")
        if len(x.password) < 10:
            return "Password should be at least 10 Characters. Sign-up Failed."
        
    def account_details(x):

        print(f"Name: {x.name}")
        print(f"Email: {x.email}")
        print(f"Password: {x.password}")
        print("Your Quote For Today - 'Be Like Water' ")

user_account = account()
user_account.sign_up()
user_account.account_details()
user_account.file()

         



