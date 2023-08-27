print("Welcome to my quiz!")
answer = input("Are you ready to play? (yes/no) : ")
score = 0
questions = 5

if answer.lower == "yes":
    answer = input("Question 1: Who is the first founder of Our Lady of Fatima University? ")
    if answer.lower() == "Jose C. Olivares":
        score += 1
        print("Correct!")
    else:
        print("Wrong Answer...")
