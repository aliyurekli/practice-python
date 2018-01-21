# Birthday Dictionaries


import csv


if __name__ == '__main__':
    birthday_holder = {}

    with open("data/birthdays.csv") as f:
        reader = csv.DictReader(f)
        for line in reader:
            key, value = line["name"], line["birthday"]
            birthday_holder[key] = value

    print("Welcome to the birthday dictionary. We know the birthdays of:")

    for k in birthday_holder.keys():
        print(k)

    person = input("Who's birthday do you want to look up?")

    if person in birthday_holder.keys():
        print("%s's birthday is %s." % (person, birthday_holder.get(person)))
    else:
        print("Sorry, we do not know %s's birthday." % person)




