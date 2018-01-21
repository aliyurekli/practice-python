# Max of Three


import sys


def find_max(a, b, c):
    num_list, maximum = [a, b, c], sys.maxsize * -1

    for i in range(len(num_list)):
        if num_list[i] > maximum:
            maximum = num_list[i]

    return maximum


if __name__ == '__main__':
    numbers = []

    for i in range(3):
        a = int(input("Enter number %d: " % (i+1)))
        numbers.append(a)

    val = find_max(numbers[0], numbers[1], numbers[2])

    print("Maximum value is %d" % val)