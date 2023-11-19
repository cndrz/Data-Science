import random

random_number = random.randint(1, 100)
player_life = 5

print("Lives =", player_life)
player_input = int(input("Enter Guess Here: "))


while player_input != random_number:
    if player_input < random_number:
        print("Incorrect Guess. Try Higher.")
        player_life -= 1
        print("Tries Left =", player_life)
        player_input = int(input("Enter Guess Here: "))
    elif player_input > random_number:
        print("Incorrect Guess. Try Lower.")
        player_life -= 1
        print("Tries Left =", player_life)
        player_input = int(input("Enter Guess Here: "))
    else:
        break


print("Correct Answer!")

        