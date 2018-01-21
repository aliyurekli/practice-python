# Hangman

import random


def get_random_word():
    words = []
    with open("data/turkish.txt", encoding="utf-8") as f:
        word = f.readline()
        while word:
            words.append(word.strip())
            word = f.readline()

    return words[random.randint(0, len(words)-1)]


def simulate_word(w, letters):
    output = []

    for c in w:
        if c in letters:
            output.append(c)
        else:
            output.append("_ ")

    return "".join(output).rstrip()


if __name__ == '__main__':
    my_word = get_random_word()
    user_choices = []

    print("Welcome to Hangman")
    print(simulate_word(my_word, user_choices))

    counter = 6
    found = False

    while counter > 0:
        letter = input("You have %d chances, guess a letter " % counter).upper()

        if letter not in user_choices:
            user_choices.append(letter)

            current_word = simulate_word(my_word, user_choices)
            print(current_word)

            if letter not in my_word:
                counter -= 1

            if my_word == current_word:
                print("Correct, the word is %s" % my_word)
                found = True
                break
        else:
            print("You have already guessed that letter")

    if not found:
        print("Sorry, the word is %s" % my_word)