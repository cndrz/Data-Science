import random


def choice_1():

    print("RNG - 1 to 1,000,000")
    random_number = random.randint(0, 1_000_000)
    print(random_number)


def choice_2():

    print("Word Concatenator")
    word_1 = input("Enter first word: ")
    word_2 = input("Enter second word: ")
    print(word_1 + word_2)


def choice_3():

    print("Addition Calculator")
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))
    print(number_1 + number_2)


while True:
    try:
        choice = int(input("Choose 1, 2, or 3? "))
        match choice:
            case 1:
                choice_1()
                break
            case 2:
                choice_2()
                break
            case 3:
                choice_3()
                break
            case _:
                print("Invalid Choice. Try again.")

    except ValueError:
        print("Invalid input. Please enter a number.")
