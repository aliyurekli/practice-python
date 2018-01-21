# Cows and Bulls

import random


def generate_number():
    return random.randint(1000, 9999)


def get_input():
    while True:
        a = int(input("Guess my number between 1000 and 9999: "))

        if 1000 <= a <= 9999:
            break
        else:
            print("Please make your guess between 1000 and 9999")

    return a


def play_turn(random_num, user_num):
    str1, str2 = str(random_num), str(user_num)

    cow, bull = 0, 0

    for i in range(len(str1)):
        if str1[i] == str2[i]:
            cow += 1
        else:
            temp = str2.replace(str2[i], "")
            if str1[i] in temp:
                bull += 1

    print("cow %d, bull %d" % (cow, bull))

    return cow == len(str1)


if __name__ == '__main__':
    num = generate_number()

    trials = 0

    while True:
        trials += 1

        guess = get_input()

        if play_turn(num, guess):
            break

    print("You found %d in %d trials" % (num, trials))