number_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for x in number_list:
    if x < 50: print(x)

print( [ x for x in number_list if x < 5 ] )
