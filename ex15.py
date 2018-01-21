# Reverse Word Order


def reverse_sentence(sentence):
    s = sentence.split()

    return " ".join(s[::-1])


mySentence = input("Enter a sentence: ")

print(reverse_sentence(mySentence))