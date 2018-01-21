# List Overlap

import random

sizeA, sizeB = random.randint(1, 20), random.randint(1, 20)

a = [random.randint(0, 100) for i in range(sizeA)]
b = [random.randint(0, 100) for j in range(sizeB)]

test, main, commons = b, a, []

if sizeA < sizeB:
    test = a
    main = b

for x in test:
    if x in main:
        commons.append(x)

print("First list: %s" % a)
print("Second list: %s" % b)
print("Common items: %s" % commons)
