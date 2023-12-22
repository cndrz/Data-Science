number = 5

while number != 0:
    print(f"number {number}", end = " ")
    if number % 2 == 0:
        print("[Even Number]", end = " ")
    print()
    number -= 1
