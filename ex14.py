# List Remove Duplicates


import random


def remove_duplicates(a):
    return set(a)


myList = [random.randint(0, 20) for i in range(30)]

myListWithoutDuplicates = list(remove_duplicates(myList))

print (myList)
print (myListWithoutDuplicates)
