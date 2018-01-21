# Character input

import datetime

now = datetime.datetime.now()

name = input("Hello, what is your name?")
age = int(input("And, your age?"))

year100 = now.year - age + 100

print("Dear %s, you will be 100 years old in %d" % (name, year100))