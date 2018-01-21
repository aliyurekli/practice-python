# Guessing Game One

import random

value = random.randint(1, 9)

while True:
    user = int(input("Guess the number:"))

    if user == value:
        print("Your guess %d is correct" % user)
        break
    elif user > value:
        print("Your guess %d is too high" % user)
    else:
        print("Your guess %d is too low" % user)
