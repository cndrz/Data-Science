number = int(input("Enter number of weeks: "))

for number_of_weeks in range (1, number + 1):
    print(f"Week #{number_of_weeks}")
    for number_of_days in range (1, 7 + 1):
        print(" ", f"Day {number_of_days}")
    print()