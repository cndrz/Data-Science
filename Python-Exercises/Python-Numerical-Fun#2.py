x = int(input("Enter First Integer: "))
y = int(input("Enter Second Integer: "))
for number in reversed(range(x, y + 1)):
    if number % 3 == 0:
        print(number)
    else:
        continue
