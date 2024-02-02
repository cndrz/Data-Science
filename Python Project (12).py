first_number = int(input("Enter First Integer: "))
second_number = int(input("Enter Second Integer: "))
for number in reversed(range(first_number, second_number + 1)):
    print(number)
