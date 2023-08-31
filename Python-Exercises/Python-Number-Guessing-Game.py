import random 
random_num = random.randint(1,500)
num_input = 0 
repetition = 0 

while num_input != random_num and num_input != "exit":
    num_input =input("Guess a number between 1 to 500: ")

    if num_input == "exit":
        break

    num_input = int(num_input)
    repetition += 1 

    if num_input < random_num:
        print("Higher!")
    elif num_input > random_num:
        print("Lower!")
    else:
        print("You are Correct!!!")
        print("You Took", repetition, "Tries!")


