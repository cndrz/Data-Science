number = int(input("Enter n: "))
blank_list = [*range(0, number + 1, 1)]
print(" ", *blank_list)
for rows in range (0, number + 1):
    print(rows, end = " ")
    for columns in range (0, number + 1):
        print(columns + rows, end = " ")
    print()