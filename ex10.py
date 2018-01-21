# List Overlap Comprehensions

import random

sizeA, sizeB = random.randint(1, 20), random.randint(1, 20)

a = [random.randint(0, 100) for i in range(sizeA)]
b = [random.randint(0, 100) for j in range(sizeB)]

commons = [i for i in a for j in b if i == j]

print("First list: %s" % a)
print("Second list: %s" % b)
print("Common items: %s" % set(commons))
