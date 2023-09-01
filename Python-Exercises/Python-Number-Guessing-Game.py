import random 

random_num = random.randint(1,500)
num_input = 0 
repetition = 0 

while num_input != random_num and num_input != "exit":
    num_input = input("Guess a number between 1 to 500: ")
    if num_input == "exit":
        print("ByeBye!!")
        break
    
    num_input = int(num_input)
    repetition += 1 

    if num_input > 500:
        print("It's 1 to 500, your guess is too high...")    
    elif num_input <= 0:
        print("It's 1 to 500, your guess is too low...")
    elif num_input < random_num:
        print("Higher!")
    elif num_input > random_num:
        print("Lower!")
    else:
        print("You are correct!!!")
        print("You took", repetition, "tries!")


