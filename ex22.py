# Read From File


def count_names(filename):
    names = {}

    with open(filename, "r") as f:
        data = f.readlines()

        for line in data:
            line = line.strip()
            if line in names:
                names[line] = names[line] + 1
            else:
                names[line] = 1

    return names


if __name__ == '__main__':
    a = count_names("data/names.txt")

    print(a)
