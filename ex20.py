# Element Search


import random


def search_list(a, value):
    for i in a:
        if i == value:
            return True
    return False


def print_message(condition, value, a):
    if condition:
        print("%d exists in this list %s" % (value, a))
    else:
        print("%d does not exist in this list %s" % (value, a))


if __name__ == '__main__':
    myList = [random.randint(0, 50) for i in range(20)]
    myList.sort()

    search_value = random.randint(0, 50)
    exists = search_list(myList, search_value)

    if exists:
        print("%d exists in this list %s" % (search_value, myList))
    else:
        print("%d does not exist in this list %s" % (search_value, myList))
