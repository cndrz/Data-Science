number_input = int(input("Enter a number: "))
number_list = list(range(1, number_input + 1))
divisor = []

for number in number_list:
    if number_input % number == 0:
        divisor.append(number)

print(divisor)