# List Ends

import random


def make_sublist(a):
    return [a[0], a[-1]]


listSize = random.randint(1, 20)
randomList = [random.randint(0, 100) for i in range(listSize)]

b = make_sublist(randomList)

print("Original list: %s" % randomList)
print("New list: %s" % b)
