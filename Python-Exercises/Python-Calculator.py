import random

# VARIABLE TO KEEP TRACK OF CORRECT ANSWERS
correct_answers = 0

# VARIABLE TO CHANGE AMOUNT OF QUESTIONS
question_amount = 5

print("1. Addition [+]\n2. Subtraction [-]\n3. Multiplication [*]\n4. Division [/]")
user_input = int(input("Choose operation --> "))

if user_input in [1, 2, 3, 4]:
    
    # LOOP TO ASK X AMOUNT OF QUESTIONS TO USER
    for x in range(question_amount):
        if user_input == 1:

            # GENERATE 2 RANDOM NUMBERS
            addition_first_num = random.randint(0, 1000)
            addition_second_num = random.randint(0, 1000)

            # FORMULA FOR THE 2 RANDOM NUMBERS
            addition_correct_answer = addition_first_num + addition_second_num

            # USER INPUT FOR ANSWERING THE QUESTION
            print(f"\n{addition_first_num} + {addition_second_num}")
            addition_user_answer = int(input("Enter answer here --> "))

            # LOGIC TO DETERMINE IF THE ANSWER IS CORRECT
            if addition_user_answer == addition_correct_answer:
                print(f"{addition_first_num} + {addition_second_num} = {addition_user_answer}")
                print("Correct!")
                correct_answers += 1
            else:
                print("Incorrect!")

        elif user_input == 2:

            # GENERATE 2 RANDOM NUMBERS
            subtraction_first_num = random.randint(0, 1000)
            subtraction_second_num = random.randint(0, 1000)

            # FORMULA FOR THE 2 RANDOM NUMBERS
            subtraction_correct_answer = subtraction_first_num - subtraction_second_num

            # USER INPUT FOR ANSWERING THE QUESTION
            print(f"\n{subtraction_first_num} - {subtraction_second_num}")
            subtraction_user_answer = int(input("Enter answer here --> "))

            # LOGIC TO DETERMINE IF THE ANSWER IS CORRECT
            if subtraction_user_answer == subtraction_correct_answer:
                print(f"{subtraction_first_num} - {subtraction_second_num} = {subtraction_user_answer}")
                print("Correct!")
                correct_answers += 1
            else:
                print("Incorrect!")

        elif user_input == 3:

            # GENERATE 2 RANDOM NUMBERS
            multiplication_first_num = random.randint(0, 1000)
            multiplication_second_num = random.randint(0, 1000)

            # FORMULA FOR THE 2 RANDOM NUMBERS
            multiplication_correct_answer = multiplication_first_num * multiplication_second_num

            # USER INPUT FOR ANSWERING THE QUESTION
            print(f"\n{multiplication_first_num} * {multiplication_second_num}")
            multiplication_user_answer = int(input("Enter answer here --> "))

            # LOGIC TO DETERMINE IF THE ANSWER IS CORRECT
            if multiplication_user_answer == multiplication_correct_answer:
                print(f"{multiplication_first_num} * {multiplication_second_num} = {multiplication_user_answer}")
                print("Correct!")
                correct_answers += 1
            else:
                print("Incorrect!")

        elif user_input == 4:

            # GENERATE 2 RANDOM NUMBERS
            division_first_num = random.randint(1, 1000)
            division_second_num = random.randint(1, 100)

            # FORMULA FOR THE 2 RANDOM NUMBERS
            division_correct_answer = division_first_num // division_second_num

            # USER INPUT FOR ANSWERING THE QUESTION
            print(f"\n{division_first_num} // {division_second_num}")
            division_user_answer = int(input("Enter answer here --> "))

            # LOGIC TO DETERMINE IF THE ANSWER IS CORRECT
            if division_user_answer == division_correct_answer:
                print(f"{division_first_num} // {division_second_num} = {division_user_answer}")
                print("Correct!")
                correct_answers += 1
            else:
                print("Incorrect!")

    # DISPLAY NUMBER OF CORRECT ANSWER
    print(f"You got {correct_answers} out of {question_amount} questions correct.")

else:
    print("Invalid input. Please choose a valid operation (1-4).")
