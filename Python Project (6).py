import random

a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 12)
print("List A: ", a)
print("List B: ", b)
result = [i for i in a if i in b]
print("A and B Common Integers: ", result)