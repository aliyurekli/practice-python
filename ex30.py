# Pick Word


import random


def get_random_word(d):
    rand_index = random.randint(0, len(d)-1)

    return d[rand_index]


if __name__ == '__main__':
    words = []
    with open("data/sowpods.txt") as f:
        word = f.readline()
        while word:
            words.append(word.strip())
            word = f.readline()

    for i in range(10):
        print(get_random_word(words))