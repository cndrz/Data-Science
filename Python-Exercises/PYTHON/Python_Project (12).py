x = int(input("Enter First Integer: "))
y = int(input("Enter Second Integer: "))
numbers_list = [number for number in reversed(range(x*3, y*3 + 1)) if number % 2 == 0] # Change the number of divisibility to be printed to user's desire
print(numbers_list)
