# Birthday Json


import json


if __name__ == '__main__':
    birthday_holder = {}

    with open("data/birthdays.json") as f:
        birthday_holder = json.load(f)

    print("Welcome to the birthday dictionary. We know the birthdays of:")

    for k in birthday_holder.keys():
        print(k)

    person = input("Who's birthday do you want to look up?")

    if person in birthday_holder.keys():
        print("%s's birthday is %s." % (person, birthday_holder[person]))
    else:
        print("Sorry, we do not know %s's birthday." % person)

