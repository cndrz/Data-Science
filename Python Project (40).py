import random

def open_file(numbers):
    with open("number_list.txt", "w") as file:
        for number in numbers:
            file.write(f"{str(number)}\n")


number_list = [random.randint(1, 50) for _ in range(5)]


open_file(number_list)
