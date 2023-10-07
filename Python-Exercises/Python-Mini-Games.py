def Main_Menu():

    print("\n[Mga kalokohokan ko]\n")

    print("1. Number Guess")
    print("2. Questionnaire")
    print("3. Combine String")

    user_input = int(input("\nEnter Choice >>> "))

    if user_input == 1:
        Number_Guess()

    elif user_input == 2:
        Questionnaire()

    elif user_input == 3:
        Combine_String()
def Number_Guess():
    import random

    print("\n[Number Guess]\n")

    random_number = random.randint(1, 101)

    while True:
        user_input = int(input("Guess The Number >>> "))

        if user_input == random_number:
            print("You Guessed Correctly!")
            choice = input("Try Again? Y / N >>> ")
            
            if choice == "Y":
                random_number = random.randint(1, 101)

            elif choice == "N":
                break

        elif user_input > random_number:
            print("You Guessed Too High!")

        elif user_input < random_number:
            print("You Guessed Too Low")

Main_Menu()







