import random 
list = []

for a in range (0, 10):
     random_number = random.randint(1, 100)
     list.append(random_number)

even_num_list = [number for number in list if number % 2 == 0]

print("List of numbers: " + str(list))
print("Even numbers in list above: " + str(even_num_list))
     