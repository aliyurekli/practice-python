# Password Generator

import random
import string


def generate(n):
    return "".join(random.choices(string.digits + string.ascii_letters + string.punctuation, k=n))


length = random.randint(8, 12)
password = generate(length)

print("Password of length %d is generated: %s" % (length, password))