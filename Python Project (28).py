import os

def append_letters(letter):
    global file_1
    file_1 = open(os.path.join("letters_folder", "letter.txt"), "a")
    file_1.write(letter)
    file_1.close()

def append_numbers(number):
    global file_2
    file_2 = open(os.path.join("numbers_folder", "number.txt"), "a")
    file_2.write(number)
    file_2.close()

def letter_file():
    folder_path = "letters_folder"
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, "letter.txt")
    return open(file_path, "a")

def number_file():
    folder_path = "numbers_folder"
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, "number.txt")
    return open(file_path, "a")

def character():
    while True:
        user_input = input("Enter a character: ")
        if user_input.isalpha():
            file_1 = letter_file()
            append_letters(user_input + "\n")
            file_1.close()
        elif user_input.isdigit():
            file_2 = number_file()
            append_numbers(user_input + "\n")
            file_2.close()
        else:
            quit()

character()
