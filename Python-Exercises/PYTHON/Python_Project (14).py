import numpy
from numpy import *

x = int(input("Enter X: "))
y = int(input("Enter Y: "))
numbers_list = [number for number in range(x, y + 1)]
print(f"List: {numbers_list}")
print(f"Total Product: {numpy.prod(numbers_list)}")