# Guess Letters


import random


def get_random_word():
    words = []
    with open("data/sowpods.txt") as f:
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

    while True:
        letter = input("Guess a letter").upper()
        user_choices.append(letter)

        current_word = simulate_word(my_word, user_choices)
        print(current_word)

        if my_word == current_word:
            print("Correct")
            break
        else:
            print("Incorrect")
