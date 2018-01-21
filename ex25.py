# Guessing Game Two

import random

if __name__ == '__main__':
    print("Choose a number between 0 and 100, and let me find it.")
    print("I only accept Yes, Too low, Too high as response")

    guess, counter, maximum, minimum = random.randint(0, 100), 0, 100, 0

    while True:
        counter += 1
        response = input("Is your number equal to %d?" % guess)

        if response == "Yes":
            print("I found %d in %d trials." % (guess, counter))
            break
        elif response == "Too low":
            if minimum < guess:
                minimum = guess

            guess = ((maximum + minimum) / 2) + 1
        elif response == "Too high":
            if maximum > guess:
                maximum = guess

            guess = minimum + (maximum - minimum) / 2
        else:
            print("Please give a valid response.")


