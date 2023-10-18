first_list = [int(x) for x in input("Enter Multiple Integers [Separated By Space] > ").split()]
second_list = [int(y) for y in input("Enter More Multiple Integers [Separated By Space] > ").split()]
combined_list = first_list + second_list
print(f"Result >>> {combined_list[::-1]}")


