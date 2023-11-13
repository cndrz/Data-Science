import random

def list_logic():

    blank_list = [random.randrange(1, 100, 1) for x in range(10)]
    print(str(blank_list))
    filtered_list= [blank_list[0], blank_list[9]]
    print(f"Filtered List: {filtered_list}")

list_logic()